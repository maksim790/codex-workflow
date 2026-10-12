"""Record content hashes and Git status for a fixture without changing it."""

import hashlib
import json
import subprocess
import sys
from pathlib import Path


root = Path(sys.argv[1]).resolve()
output = Path(sys.argv[2]).resolve()
files = {}
for path in root.rglob("*"):
    if path.is_file() and ".git" not in path.relative_to(root).parts:
        files[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
status = subprocess.run(["git", "status", "--porcelain=v1"], cwd=root,
                        check=True, capture_output=True, text=True).stdout
output.write_text(json.dumps({"files": files, "git_status": status},
                             ensure_ascii=False, indent=2), encoding="utf-8")
