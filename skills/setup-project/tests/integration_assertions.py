"""Check the three disposable repositories after applying the skill workflows."""

import json
import subprocess
import sys
from pathlib import Path


base = Path(sys.argv[1]).resolve()


def run(root, *argv):
    return subprocess.run(argv, cwd=root, capture_output=True, text=True, check=True).stdout


init = base / "init"
expected_new = {
    "AGENTS.md", "docs/Home.md", "docs/01-Project/Overview.md",
    "docs/02-Architecture/Overview.md", "docs/05-Interfaces/HTTP.md",
    "docs/12-Development/Verification.md",
}
actual_new = {line[3:] for line in run(init, "git", "status", "--porcelain=v1", "--untracked-files=all").splitlines()}
assert actual_new == expected_new, (actual_new, expected_new)
docs = init / "docs"
assert {p.name for p in docs.iterdir() if p.is_dir()} == {
    "01-Project", "02-Architecture", "05-Interfaces", "12-Development"
}
assert all(any(path.iterdir()) for path in docs.iterdir() if path.is_dir())
assert "Status: proposed" in (docs / "12-Development/Verification.md").read_text(encoding="utf-8")
assert "SQLite" not in "\n".join(p.read_text(encoding="utf-8") for p in docs.rglob("*.md"))
assert "do_GET" in (init / "app.py").read_text(encoding="utf-8")
assert "GET /items" in (docs / "05-Interfaces/HTTP.md").read_text(encoding="utf-8")

update = base / "update"
assert set(run(update, "git", "diff", "--name-only").splitlines()) == {
    "docs/02-Architecture/Overview.md", "docs/05-Interfaces/HTTP.md"
}
assert "POST /items" in (update / "docs/05-Interfaces/HTTP.md").read_text(encoding="utf-8")
assert "src/events.py" in (update / "docs/02-Architecture/Overview.md").read_text(encoding="utf-8")
for path in ("docs/11-Decisions/ADR-0001-Python.md", "docs/Personal-Notes.md"):
    original = subprocess.run(["git", "show", "HEAD:" + path], cwd=update,
                              capture_output=True, check=True).stdout
    assert (update / path).read_bytes() == original, path
run(update, "git", "diff", "--check")

before = json.loads((base / "audit-before.json").read_text(encoding="utf-8"))
after = json.loads((base / "audit-after.json").read_text(encoding="utf-8"))
assert before == after
assert before["git_status"] == ""
assert len(before["files"]) >= 10
print("INIT, UPDATE, AUDIT assertions passed; audit preserved", len(before["files"]), "files")
