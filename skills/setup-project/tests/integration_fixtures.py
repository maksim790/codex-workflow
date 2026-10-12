"""Create isolated Git fixtures for manual Codex skill integration runs."""

import argparse
import shutil
import subprocess
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]


def write(root, relative, content):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def git(root, *args):
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


def create(root, mode):
    root.mkdir(parents=True)
    git(root, "init", "--quiet")
    shutil.copytree(SKILL, root / ".agents" / "skills" / "setup-project",
                    ignore=shutil.ignore_patterns("tests", "__pycache__"))
    write(root, "README.md", "# Tiny Catalog\n\nA Python standard-library HTTP catalog. Run `python -B -m unittest discover -s tests`.\n")
    write(root, "src/catalog.py", """ITEMS = ['pen', 'notebook']


def list_items():
    return list(ITEMS)
""")
    write(root, "app.py", """from http.server import BaseHTTPRequestHandler, HTTPServer
from src.catalog import list_items


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/items':
            self.send_error(404)
            return
        body = ('\\n'.join(list_items()) + '\\n').encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    HTTPServer(('127.0.0.1', 8000), Handler).serve_forever()
""")
    write(root, "tests/test_catalog.py", """import unittest
from src.catalog import list_items


class CatalogTests(unittest.TestCase):
    def test_items(self):
        self.assertEqual(list_items(), ['pen', 'notebook'])
""")
    if mode != "init":
        write(root, "AGENTS.md", """# Tiny Catalog instructions

Read [knowledge base](docs/Home.md) before relevant changes. Verified test command: `python -B -m unittest discover -s tests`. Preserve existing ADRs and personal notes.
""")
        write(root, "docs/Home.md", """# Tiny Catalog knowledge base

- [Architecture](02-Architecture/Overview.md)
- [HTTP interface](05-Interfaces/HTTP.md)
- [Decision record](11-Decisions/ADR-0001-Python.md)
""")
        write(root, "docs/02-Architecture/Overview.md", """# Architecture

The standard-library HTTP server in `app.py` serves a catalog in memory through `src/catalog.py`.

## Sources
- [Server](../../app.py)
- [Catalog](../../src/catalog.py)
""")
        write(root, "docs/05-Interfaces/HTTP.md", """# HTTP interface

`GET /items` returns the in-memory item names as plain text. No write endpoint is documented.

## Sources
- [Server](../../app.py)
""")
        write(root, "docs/11-Decisions/ADR-0001-Python.md", """# ADR-0001: Python standard library

- Status: Accepted
- Date: 2025-01-01

Use Python's standard library for this test fixture.
""")
        write(root, "docs/Personal-Notes.md", "# Personal notes\n\nKeep my local examples and wording intact.\n")
        write(root, "docs/12-Development/Verification.md", "# Verification\n\nRun `python -B -m unittest discover -s tests`.\n")
    if mode in ("update", "audit"):
        # A new HTTP write path and event journal are the architecture change.
        write(root, "src/events.py", """EVENTS = []


def record_item_added(name):
    EVENTS.append({'type': 'item_added', 'name': name})
""")
        write(root, "src/catalog.py", """from src.events import record_item_added

ITEMS = ['pen', 'notebook']


def list_items():
    return list(ITEMS)


def add_item(name):
    ITEMS.append(name)
    record_item_added(name)
""")
        app = (root / "app.py").read_text(encoding="utf-8")
        app = app.replace("from src.catalog import list_items", "from src.catalog import list_items, add_item")
        app = app.replace("\n\nif __name__ == '__main__':", """
    def do_POST(self):
        if self.path != '/items':
            self.send_error(404)
            return
        name = self.rfile.read(int(self.headers.get('Content-Length', '0'))).decode().strip()
        if not name:
            self.send_error(400)
            return
        add_item(name)
        self.send_response(201)
        self.end_headers()


if __name__ == '__main__':""")
        write(root, "app.py", app)
    if mode == "audit":
        write(root, "docs/02-Architecture/Overview.md", """# Architecture

The catalog persists in SQLite and has no event journal.

## Sources
- [Server](../../app.py)
""")
        write(root, "docs/05-Interfaces/HTTP.md", """# HTTP interface

The server supports only `GET /items`.
[Removed API details](Missing.md)

## Sources
- [Server](../../app.py)
""")
        write(root, "docs/12-Development/Verification.md", "# Verification\n\nRun `python old-test-runner.py`.\n")
    git(root, "add", ".")
    subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                    "commit", "--quiet", "-m", "fixture"], cwd=root, check=True, capture_output=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    args = parser.parse_args()
    for name in ("init", "update", "audit"):
        create(args.base / name, name)
    print(args.base)
