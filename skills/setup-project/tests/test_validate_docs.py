"""Behavioral tests against disposable project vaults."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate-docs.py"


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def run_validator(self, *extra):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--root", str(self.root),
             "--vault", "docs", "--format", "json", *extra],
            capture_output=True, text=True, check=False,
        )
        return result, json.loads(result.stdout)

    def test_valid_links_and_code_are_ignored(self):
        self.write("docs/Home.md", "# Home\n[Page](Page.md#section)\n`[No](missing.md)`\n~~~md\n[No](missing.md)\n~~~\n")
        self.write("docs/Page.md", "# Section\n")
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(data["findings"], [])
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(after, before)

    def test_line_numbers_survive_fenced_code(self):
        self.write("docs/Home.md", "# Home\n```md\n[ignored](x.md)\n```\n[bad](missing.md)\n")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 1)
        self.assertIn("Line 5:", data["findings"][0]["message"])

    def test_directory_is_not_a_valid_document_link(self):
        self.write("docs/Home.md", "# Home\n[Folder](subdir)\n")
        (self.root / "docs" / "subdir").mkdir()
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 1)
        self.assertIn("link_not_file", [item["code"] for item in data["findings"]])

    def test_parenthesized_filename_and_url_encoding(self):
        self.write("docs/Home.md", "# Home\n[Page](Page_(v2).md)\n[Spaces](<Space Name.md>)\n[Encoded](Space%20Name.md)\n")
        self.write("docs/Page_(v2).md", "# Page\n")
        self.write("docs/Space Name.md", "# Space\n")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 0, data)

    def test_fence_marker_inside_longer_fence_does_not_close_it(self):
        self.write("docs/Home.md", "# Home\n````md\n```\n[ignored](missing.md)\n````\n")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 0, data)

    def test_missing_home_and_missing_vault(self):
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 1)
        self.assertIn("home_missing", [item["code"] for item in data["findings"]])
        result, data = self.run_validator("--vault", "absent")
        self.assertEqual(result.returncode, 1)
        self.assertIn("vault_missing", [item["code"] for item in data["findings"]])

    def test_custom_vault_path(self):
        self.write("knowledge/Home.md", "# Home\n")
        result, data = self.run_validator("--vault", "knowledge")
        self.assertEqual(result.returncode, 0, data)

    def test_home_with_invalid_links_has_no_valid_navigation(self):
        self.write("docs/Home.md", "# Home\n[Lost](missing.md)\n")
        self.write("docs/Page.md", "# Page\n")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 1)
        self.assertIn("home_no_valid_links", [item["code"] for item in data["findings"]])

    def test_symlink_outside_root_is_not_read(self):
        outside = self.root.parent / (self.root.name + "-outside.md")
        outside.write_text("[secret](missing.md)\n", encoding="utf-8")
        self.addCleanup(outside.unlink)
        self.write("docs/Home.md", "# Home\n[Outside](Outside.md)\n")
        try:
            (self.root / "docs" / "Outside.md").symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 1)
        codes = [item["code"] for item in data["findings"]]
        self.assertIn("outside_root", codes)
        self.assertNotIn("link_missing", codes)

    @unittest.skipUnless(sys.platform == "win32", "NTFS junctions are Windows-only")
    def test_junction_outside_root_is_not_read(self):
        outside = self.root.parent / (self.root.name + "-junction-target")
        outside.mkdir()
        self.addCleanup(outside.rmdir)
        secret = outside / "secret.md"
        secret.write_text("[secret](missing.md)\n", encoding="utf-8")
        self.addCleanup(secret.unlink)
        self.write("docs/Home.md", "# Home\n[Outside](out/secret.md#secret)\n")
        junction = self.root / "docs" / "out"
        quoted_junction = str(junction).replace("'", "''")
        quoted_outside = str(outside).replace("'", "''")
        created = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command",
             f"New-Item -ItemType Junction -Path '{quoted_junction}' -Target '{quoted_outside}'"],
            capture_output=True, text=True, check=False,
        )
        if created.returncode != 0:
            self.skipTest("junctions unavailable")
        self.addCleanup(os.rmdir, junction)
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 1)
        codes = [item["code"] for item in data["findings"]]
        self.assertIn("outside_root", codes)
        self.assertNotIn("link_missing", codes)

    def test_outside_root_link_is_reported_without_reading(self):
        self.write("docs/Home.md", "# Home\n[Outside](../../private.md#secret)\n")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 0)
        self.assertIn("outside_root", [item["code"] for item in data["findings"]])

    def test_invalid_utf8_target_is_reported_instead_of_crashing(self):
        self.write("docs/Home.md", "# Home\n[Bad](Bad.md#heading)\n")
        (self.root / "docs" / "Bad.md").write_bytes(b"\xff")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 1)
        self.assertIn("read_failure", [item["code"] for item in data["findings"]])

    def test_malformed_url_does_not_crash(self):
        self.write("docs/Home.md", "# Home\n[Bad](http://[invalid)\n")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 1)
        self.assertIn("link_invalid", [item["code"] for item in data["findings"]])

    def test_duplicate_headings_and_same_page_anchors(self):
        self.write("docs/Home.md", "# Home\n## Section\n## Section\n[Second](#section-1)\n[Missing](#section-2)\n")
        result, data = self.run_validator()
        self.assertEqual(result.returncode, 0)
        self.assertEqual([item["code"] for item in data["findings"]], ["anchor_missing"])


if __name__ == "__main__":
    unittest.main()
