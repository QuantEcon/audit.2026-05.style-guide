#!/usr/bin/env python3
"""Regenerate ``lectures/_toc.yml`` from what is actually on disk.

Run after a pass that added or removed lectures. Keeping this in a script rather
than a heredoc in the runbook means the sidebar cannot drift from the reports.

    python3 tools/qestyle_toc.py --root lectures
"""

from __future__ import annotations

import argparse
import os
import sys

SERIES_ORDER = [
    "lecture-python-intro",
    "lecture-python-programming",
    "lecture-python.myst",
    "lecture-python-advanced.myst",
    "lecture-dp",
]
OVERVIEW = ["charts", "details", "spec", "appendix"]


def build(root: str) -> str:
    lines = ["format: jb-book", "root: intro", "parts:",
             "  - caption: Overview", "    chapters:"]
    lines += [f"      - file: {name}" for name in OVERVIEW]
    for series in SERIES_ORDER:
        folder = os.path.join(root, series)
        if not os.path.isdir(folder):
            continue
        stems = sorted(f[:-3] for f in os.listdir(folder)
                       if f.endswith(".md") and f != "index.md")
        lines += [f'  - caption: "{series} ({len(stems)} lectures)"',
                  "    chapters:",
                  f"      - file: {series}/index",
                  "        sections:"]
        lines += [f"          - file: {series}/{s}" for s in stems]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default="lectures")
    ap.add_argument("--check", action="store_true",
                    help="fail if the on-disk TOC differs, rather than rewriting it")
    args = ap.parse_args()

    text = build(args.root)
    path = os.path.join(args.root, "_toc.yml")
    if args.check:
        current = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if current != text:
            print(f"{path} is out of date")
            return 1
        print(f"{path} is up to date")
        return 0
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {path} ({text.count('- file:')} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
