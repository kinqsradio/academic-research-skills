"""Opt-in, read-only public-template checks; Python 3.10+, Git required.

This structural check is deliberately separate from private-project validation.
It examines working-tree content at Git-index paths, not history or untracked files.
"""

import argparse
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


RESEARCH_ROOTS = (
    "docs/planning/", "docs/literature/", "docs/methods/", "docs/decisions/",
    "submissions/",
)
REGISTERS = ("papers/DOWNLOADS.md", "papers/REFERENCES.md", "submissions/VERSION.md")
SOURCE_ID = re.compile(r"\bP\d{3,}\b")
NUMBERED_REFERENCE = re.compile(r"^\s*\[\d+\]\s+\S", re.MULTILINE)
PDF_LINK = re.compile(r"\]\([^\n)]*\.pdf(?:[?#][^\n)]*)?\)", re.IGNORECASE)
TABLE_SEPARATOR = re.compile(r"^:?-{3,}:?$")


def prose_without_code(content):
    """Ignore code examples, so register documentation can show a source-ID schema."""
    lines = []
    fence = None
    for line in content.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(re.sub(r"(`+).*?\1", "", line))
    return "\n".join(lines)


def has_table_records(content):
    """Permit arbitrary Markdown table headers/separators, reject populated rows."""
    previous_table_line = False
    in_body = False
    for line in content.splitlines():
        stripped = line.strip()
        if "|" not in stripped:
            previous_table_line = False
            in_body = False
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        separator = bool(cells) and all(TABLE_SEPARATOR.fullmatch(cell) for cell in cells)
        if separator and previous_table_line:
            in_body = True
        elif in_body and any(cells):
            return True
        previous_table_line = True
    return False


def check_public_template(root):
    """Return violations; fail closed when Git/index or required registers are absent."""
    root = Path(root).resolve()
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--cached", "-z"],
            check=True, capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        return [f"Cannot inspect Git index (Git and repository metadata required): {error}"]
    paths = sorted(set(result.stdout.decode("utf-8", errors="surrogateescape").split("\0")) - {""})
    errors = []
    for register in REGISTERS:
        if register not in paths:
            errors.append(f"{register}: required empty template register is not tracked")
    for name in paths:
        path = PurePosixPath(name)
        if path.suffix.lower() == ".pdf":
            errors.append(f"{name}: tracked PDFs are forbidden in the public template")
        in_research = name.startswith(RESEARCH_ROOTS)
        if in_research and path.name != "GUIDELINES.md" and name != "submissions/VERSION.md":
            errors.append(f"{name}: research scaffolding permits only folder GUIDELINES.md and empty submissions/VERSION.md")
        if name not in REGISTERS:
            continue
        local = root / name
        if local.is_symlink() or not local.is_file():
            errors.append(f"{name}: register must be a regular local file")
            continue
        try:
            content = local.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{name}: cannot read UTF-8 register: {error}")
            continue
        # Check table rows before removing code: a record is still populated when
        # its ID or filename happens to be wrapped in Markdown code formatting.
        if has_table_records(content):
            errors.append(f"{name}: populated register table; retain headers and separators only")
        prose = prose_without_code(content)
        if name.startswith("papers/") and (
            SOURCE_ID.search(prose) or NUMBERED_REFERENCE.search(prose) or PDF_LINK.search(prose)
        ):
            errors.append(f"{name}: source record detected; keep source IDs, references and paper links on a private research branch")
        if name == "submissions/VERSION.md" and re.search(r"^#{1,6}\s+v\d{3,}\b", prose, re.MULTILINE | re.IGNORECASE):
            errors.append(f"{name}: submission version record detected")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="repository root (defaults to this script's repository)")
    args = parser.parse_args()
    errors = check_public_template(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Public-template structural checks passed (tracked paths; working-tree register content).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
