#!/usr/bin/env python3
"""Regenerate the repo structure block in README.md from tracked files."""
import json
import re
import subprocess
import sys
from pathlib import Path

README = Path("README.md")
COMMENTS_FILE = Path(".github/tree-comments.json")
START, END = "<!-- TREE:START -->", "<!-- TREE:END -->"

# Top-level entries to hide from the tree
EXCLUDE = {".github", ".gitignore", ".gitattributes", "scripts"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def tracked_files():
    out = subprocess.check_output(["git", "ls-files", "-z"], text=True)
    files = [f for f in out.split("\0") if f]
    return [f for f in files if f.split("/")[0] not in EXCLUDE]


def build_tree(files):
    root = {}
    for f in files:
        *dirs, name = f.split("/")
        node = root
        for d in dirs:
            node = node.setdefault(d, {})
        node[name] = None  # None = file, dict = directory
    return root


def render(node, comments, seen, prefix="", path=""):
    rows = []
    # directories first, then files, each alphabetical
    items = sorted(node.items(), key=lambda kv: (kv[1] is None, kv[0].lower()))
    for i, (name, child) in enumerate(items):
        last = i == len(items) - 1
        is_dir = child is not None
        rel = f"{path}{name}{'/' if is_dir else ''}"
        seen.add(rel)
        if is_dir:
            icon = "📁"
        elif Path(name).suffix.lower() in IMAGE_EXT:
            icon = "🖼️"
        else:
            icon = "📄"
        label = f"{prefix}{'└── ' if last else '├── '}{icon} {name}{'/' if is_dir else ''}"
        rows.append((label, comments.get(rel, "")))
        if is_dir:
            rows += render(child, comments, seen, prefix + ("    " if last else "│   "), rel)
    return rows


def display_width(s):
    """Emoji count as 2 columns; variation selectors as 0."""
    w = 0
    for ch in s:
        o = ord(ch)
        if o == 0xFE0F:
            continue
        w += 2 if o >= 0x1F000 else 1
    return w


def format_rows(rows):
    col = max(display_width(label) for label, _ in rows) + 1
    lines = []
    for label, comment in rows:
        if comment:
            lines.append(f"{label}{' ' * (col - display_width(label))}# {comment}")
        else:
            lines.append(label)
    return "\n".join(lines)


def main():
    comments = {}
    if COMMENTS_FILE.exists():
        comments = json.loads(COMMENTS_FILE.read_text(encoding="utf-8"))

    files = tracked_files()
    if not files:
        sys.exit("No tracked files found; is this a git repository?")

    seen = set()
    tree = format_rows(render(build_tree(files), comments, seen))

    stale = sorted(set(comments) - seen)
    if stale:
        print("Warning: comments for paths that no longer exist:", file=sys.stderr)
        for key in stale:
            print(f"  - {key}", file=sys.stderr)

    block = f"{START}\n```text\n{tree}\n```\n{END}"
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(f"Markers {START} / {END} not found in README.md")

    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, text, flags=re.S)
    if new != text:
        README.write_text(new, encoding="utf-8")
        print("README.md structure updated.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    main()
