#!/usr/bin/env python3
"""Check the portable research library without executing research workflows.

Run from any directory: python3 /path/to/repository/scripts/validate_repository.py
Checks local Markdown links (not remote URLs or heading anchors), skill metadata,
and accidental dependencies on a developer's checkout. PDFs must stay out of the
Git index. Registered paper PDFs may be absent in portable clones; use
--require-local-papers when research needs those local files. Uses the standard
library and the Git CLI when Git metadata is present.
"""

from pathlib import Path
import argparse
import ast
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = tuple(sorted(p.name for p in (ROOT / "skills").iterdir()
                      if p.is_dir() and not p.name.startswith(".")))

EXCLUDED = {".git", "__pycache__", ".venv", "venv", ".pytest_cache", "node_modules"}


def local_pdf_links(contents, base):
    """Resolve local PDF links, preserving filename case and decoding URL paths."""
    for target in re.findall(r"\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", contents):
        parsed = urlsplit(target.strip("<>"))
        if not parsed.scheme and not parsed.netloc and parsed.path:
            destination = (base / unquote(parsed.path)).resolve()
            if destination.suffix.lower() == ".pdf":
                yield destination


def paper_records(errors):
    """Match each paper filename to the same stable IDs in both registers."""
    paper_dir = ROOT / "papers"
    downloads = paper_dir / "DOWNLOADS.md"
    references = paper_dir / "REFERENCES.md"
    records = [{}, {}]
    if downloads.is_file():
        for row in downloads.read_text(encoding="utf-8").splitlines():
            match = re.match(r"\|\s*\[(P[0-9]+)\]", row)
            if match:
                for pdf in local_pdf_links(row, paper_dir):
                    records[0].setdefault(pdf, set()).add(match[1])
    if references.is_file():
        catalog = references.read_text(encoding="utf-8")
        headings = list(re.finditer(r"^##\s+(.+?)\s*$", catalog, re.MULTILINE))
        reference_ids = []
        for index, heading in enumerate(headings):
            source_id = heading[1]
            if not re.fullmatch(r"P[0-9]+", source_id):
                continue
            reference_ids.append(source_id)
            end = headings[index + 1].start() if index + 1 < len(headings) else len(catalog)
            for pdf in local_pdf_links(catalog[heading.end():end], paper_dir):
                records[1].setdefault(pdf, set()).add(source_id)
        if len(reference_ids) != len(set(reference_ids)):
            errors.append("Duplicate source IDs in reference catalog")
    registered = set()
    local_pdfs = {p.resolve() for p in paper_dir.rglob("*")
                  if p.is_file() and p.suffix.lower() == ".pdf"}
    for pdf in sorted(local_pdfs | records[0].keys() | records[1].keys()):
        if not pdf.is_relative_to(paper_dir.resolve()):
            label = str(pdf.relative_to(ROOT)) if pdf.is_relative_to(ROOT) else "outside repository"
            errors.append(f"Paper register PDF link leaves papers/: {label}")
            continue
        label = pdf.relative_to(ROOT)
        for name, record in zip(("DOWNLOADS.md", "REFERENCES.md"), records):
            if pdf not in record:
                errors.append(f"{label}: missing stable-ID file record in {name}")
        if pdf in records[0] and pdf in records[1]:
            if records[0][pdf] != records[1][pdf]:
                errors.append(f"{label}: source IDs do not match between paper registers")
            else:
                registered.add(pdf)
    return registered, local_pdfs


def check_git_index(errors):
    """The Git index includes tracked files and newly staged additions."""
    if not (ROOT / ".git").exists():
        print("Git index PDF check skipped: this copy has no Git metadata.")
        return
    try:
        result = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z"],
                                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (OSError, subprocess.CalledProcessError):
        errors.append("Unable to inspect Git index for prohibited PDFs")
        return
    for filename in result.stdout.decode("utf-8", errors="surrogateescape").split("\0"):
        if filename.lower().endswith(".pdf"):
            errors.append(f"{filename}: PDF is tracked/staged in Git; PDFs must remain local")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-local-papers", action="store_true",
                        help="also require registered paper PDFs to be present for research use")
    args = parser.parse_args()
    errors = []
    check_git_index(errors)
    registered_pdfs, local_pdfs = paper_records(errors)
    absent_pdfs = {p for p in registered_pdfs if not p.is_file()}
    if args.require_local_papers:
        for pdf in sorted(absent_pdfs):
            errors.append(f"{pdf.relative_to(ROOT)}: registered PDF required locally for research use")
    folders = [ROOT] + [p for p in ROOT.rglob("*") if p.is_dir()
                       and not EXCLUDED.intersection(p.relative_to(ROOT).parts)]
    for folder in folders:
        if not (folder / "GUIDELINES.md").is_file():
            errors.append(f"{folder.relative_to(ROOT)}: missing GUIDELINES.md")
    markdown = sorted(p for p in ROOT.rglob("*.md")
                      if not EXCLUDED.intersection(p.relative_to(ROOT).parts))
    links_checked = 0
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if re.search(r"(?:/Users/[^/\s]+/|/home/[^/\s]+/|[A-Z]:\\Users\\)", text):
            errors.append(f"{rel}: contains a machine-specific home path")
        # Fenced code contains illustrative Markdown, not document navigation.
        prose = re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", text,
                       flags=re.MULTILINE | re.DOTALL)
        prose = re.sub(r"(`+)[^`\n]*?\1", "", prose)
        targets = re.findall(r"\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", prose)
        targets += re.findall(r"^\s*\[(?!\^)[^\]]+\]:\s*(<[^>]+>|\S+)", prose, re.MULTILINE)
        for target in targets:
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith(("#", "//")):
                continue
            dest = unquote(parsed.path)
            if not dest or any(c in dest for c in ("*", "{", "}", "$")):
                continue
            candidate = (path.parent / dest).resolve()
            if not candidate.is_relative_to(ROOT):
                errors.append(f"{rel}: link leaves repository: {target}")
            elif not candidate.exists():
                if candidate not in registered_pdfs:
                    errors.append(f"{rel}: missing link: {target}")
            links_checked += 1
    for name in SKILLS:
        path = ROOT / "skills" / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"Missing skill: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---" not in text[4:]:
            errors.append(f"{name}: missing YAML frontmatter")
            continue
        metadata = text.split("---", 2)[1]
        if not re.search(rf"^name:\s*['\"]?{re.escape(name)}['\"]?\s*$", metadata, re.MULTILINE):
            errors.append(f"{name}: frontmatter name does not match directory")
        if not re.search(r"^description:\s*\S", metadata, re.MULTILINE):
            errors.append(f"{name}: missing description")
    for path in (ROOT / "skills").rglob("*"):
        if path.name == ".git":
            errors.append(f"Nested Git metadata: {path.relative_to(ROOT)}")
        if path.is_symlink() and (not path.exists() or not path.resolve().is_relative_to(ROOT)):
            errors.append(f"Nonportable symlink: {path.relative_to(ROOT)}")
    python_files = sorted(p for p in ROOT.rglob("*.py") if not EXCLUDED.intersection(p.relative_to(ROOT).parts))
    json_files = sorted(p for p in ROOT.rglob("*.json") if not EXCLUDED.intersection(p.relative_to(ROOT).parts))
    for path in python_files:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: Python parse error: {exc}")
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: JSON parse error: {exc}")
    print(f"Checked {len(folders)} folder guides, {len(markdown)} Markdown files, {links_checked} local links, and {len(SKILLS)} skills.")
    print(f"Parsed {len(python_files)} Python files and {len(json_files)} JSON files without executing research workflows.")
    print(f"Paper files: {len(local_pdfs)} local PDFs; {len(absent_pdfs)} registered PDFs absent locally."
          + (" Local presence required." if args.require_local_papers else
             " Registered absent PDFs are allowed for portable clones."))
    if errors:
        print("\n".join(errors))
        return 1
    print("Repository structure and local Markdown links passed. Runtime workflows and external links were not tested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
