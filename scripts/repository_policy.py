"""Check repository hygiene only; this is not an application build or secret scanner."""

from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
required = (
    "README.md", "CONTRIBUTING.md", "AGENTS.md", ".editorconfig",
    ".gitattributes", ".gitignore", ".github/CODEOWNERS",
    ".github/pull_request_template.md", ".github/workflows/repository-policy.yml",
    ".github/branch-protection.json",
)
errors = []
for name in required:
    path = root / name
    if not path.is_file() or not path.read_bytes().strip():
        errors.append(f"missing or empty collaboration file: {name}")

tracked = subprocess.check_output(
    ["git", "ls-files", "-z"], cwd=root
).decode("utf-8").split("\0")
conflict = re.compile(r"^(?:<{7} .+|={7}|>{7} .+)$", re.MULTILINE)
blocked_dirs = {"node_modules", "target", "dist", "coverage", ".idea", ".vscode", "__pycache__"}
blocked_suffixes = {".pem", ".key", ".p12", ".pfx", ".jks", ".log", ".pyc"}
for name in filter(None, tracked):
    rel = PurePosixPath(name)
    sensitive_env = (rel.name == ".env" or rel.name.startswith(".env.")) and rel.name != ".env.example"
    if sensitive_env or rel.suffix.lower() in blocked_suffixes or blocked_dirs.intersection(rel.parts):
        errors.append(f"unexpected local, credential, or generated file: {name}")
    path = root / name
    if path.is_file():
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if conflict.search(content):
            errors.append(f"unresolved merge conflict marker: {name}")

if errors:
    print("Repository policy failed:", file=sys.stderr)
    print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
    sys.exit(1)
print("Repository policy passed. Application build and tests are not part of this check.")
