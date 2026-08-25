#!/usr/bin/env python3
"""Consistency gate for the audit — run before pushing.

Each check here corresponds to something that silently broke in a previous pass:
lectures that were never audited, a report describing a lecture that does not
exist, a header whose score does not match its own table, a reviewer quietly
editing a measured count, a proposed rule cited without its tag.

    python3 tools/qestyle_check.py --root lectures --data lectures/data --corpus ../quantecon

Exits non-zero if any check fails.
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from qestyle_rules import PROPOSED                     # noqa: E402
from qestyle_scan import SERIES                        # noqa: E402
from qestyle_score import compute, parse_report        # noqa: E402

RULE_RE = re.compile(r"\bqe-(?:writing|math|code|jax|fig|ref|link|admon)-\d{3}\b")
LEGACY_RE = re.compile(r"\bqe-(?:math|writing)-A\d\b|\[(?:W[1-8]|M(?:1[0-4]|[1-9]))\]")


class Checker:
    def __init__(self):
        self.failures = []
        self.notes = []

    def fail(self, check, detail):
        self.failures.append((check, detail))

    def note(self, msg):
        self.notes.append(msg)

    def report(self):
        by_check = {}
        for check, detail in self.failures:
            by_check.setdefault(check, []).append(detail)
        for msg in self.notes:
            print(f"  {msg}")
        if not self.failures:
            print("\nAll checks passed.")
            return 0
        print()
        for check, details in by_check.items():
            print(f"FAIL {check} ({len(details)})")
            for d in details[:12]:
                print(f"     {d}")
            if len(details) > 12:
                print(f"     ... {len(details) - 12} more")
        return 1


def check_coverage(ck, root, corpus):
    """Every corpus lecture has a report, and every report has a lecture."""
    for series in SERIES:
        src = os.path.join(corpus, series, "lectures")
        rep = os.path.join(root, series)
        if not os.path.isdir(src):
            ck.note(f"{series}: corpus not present, coverage not checked")
            continue
        lectures = {f[:-3] for f in os.listdir(src) if f.endswith(".md")}
        reports = {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(rep, "*.md"))
                   if os.path.basename(p) != "index.md"}
        for miss in sorted(lectures - reports):
            ck.fail("coverage", f"{series}/{miss}: lecture has no report")
        for extra in sorted(reports - lectures):
            ck.fail("coverage", f"{series}/{extra}: report has no lecture in the corpus")
        ck.note(f"{series}: {len(lectures)} lectures, {len(reports)} reports")


def check_scores(ck, root):
    """Header overall score and priority must follow from the score table."""
    n = 0
    for path in sorted(glob.glob(os.path.join(root, "lecture-*", "*.md"))):
        if os.path.basename(path) == "index.md":
            continue
        n += 1
        scores, declared, priority, _ = parse_report(path)
        overall, prio = compute(scores)
        if overall is None:
            ck.fail("score-arithmetic", f"{path}: no parsable category scores")
            continue
        if declared != f"{overall:.1f} / 10":
            ck.fail("score-arithmetic",
                    f"{path}: header {declared!r} vs categories {overall:.1f}")
        if priority != prio:
            ck.fail("priority-bucket", f"{path}: header {priority!r} vs rule {prio!r}")
    ck.note(f"score arithmetic checked on {n} reports")


def check_agreement(ck, root, data):
    """A report may not cite a count the evidence layer did not measure."""
    path = os.path.join(data, "violations.csv")
    if not os.path.exists(path):
        ck.note("violations.csv absent, report/CSV agreement not checked")
        return
    measured = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            measured[(r["series"], r["lecture"], r["rule"])] = int(r["count"])
    n = 0
    for rp in sorted(glob.glob(os.path.join(root, "lecture-*", "*.md"))):
        if os.path.basename(rp) == "index.md":
            continue
        series = os.path.basename(os.path.dirname(rp))
        stem = os.path.basename(rp)[:-3]
        with open(rp, encoding="utf-8") as fh:
            text = fh.read()
        for m in re.finditer(
            r"\*\*\[(qe-[a-z]+-\d{3})(?: \(proposed\))?\]\*\* —[^\n]*?"
            r"\*Count:\* (\d+)", text
        ):
            rule, cited = m.group(1), int(m.group(2))
            want = measured.get((series, stem, rule))
            n += 1
            if want is None:
                ck.fail("report-csv-agreement",
                        f"{rp}: cites {rule} which violations.csv does not record")
            elif want != cited:
                ck.fail("report-csv-agreement",
                        f"{rp}: {rule} cited as {cited}, measured {want}")
    ck.note(f"{n} cited counts cross-checked against violations.csv")


def check_conventions(ck, root):
    """The conventions that were deliberately applied and are easy to regress."""
    n_prop = 0
    for path in sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True)):
        # Skip build output: jupyter-book copies the sources into _build/html/_sources,
        # and the runbook has people build before re-running this gate.
        if "_build" in path.split(os.sep):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        base = os.path.basename(path)
        for m in LEGACY_RE.finditer(text):
            ck.fail("conventions", f"{path}: legacy/placeholder rule id {m.group(0)!r}")
        if re.search(r"^# Style Audit —", text, re.M):
            ck.fail("conventions", f"{path}: '# Style Audit —' title prefix")
        if "Spec version" in text:
            ck.fail("conventions", f"{path}: 'Spec version' metadata line")
        for m in re.finditer(r"(?i)carry-forward|carries forward|carried forward", text):
            ck.fail("conventions", f"{path}: two-pass wording {m.group(0)!r}")
        if path.startswith(os.path.join(root, "lecture-")):
            if base == "index.md":
                if not re.match(r"^# Summary\s*$", text.split("\n")[0]):
                    ck.fail("conventions", f"{path}: series index H1 must be '# Summary'")
            else:
                want = f"# {base[:-3]}"
                if text.split("\n")[0].strip() != want:
                    ck.fail("conventions",
                            f"{path}: H1 must be the bare lecture stem ({want!r})")
        # Proposed rules must carry the tag wherever they are cited.
        if base == "spec.md":
            continue
        for m in RULE_RE.finditer(text):
            rule = m.group(0)
            if rule not in PROPOSED:
                continue
            tail = text[m.end():m.end() + 26]
            if "(proposed)" in tail:
                n_prop += 1
                continue
            # A section that is itself about the proposed rules does not need to
            # repeat the tag on every row.
            line_start = text.rfind("\n", 0, m.start()) + 1
            line = text[line_start:text.find("\n", m.end())]
            heads = re.findall(r"^#{1,6} .*$", text[:m.start()], re.M)
            context = (heads[-1] if heads else "") + " " + line
            if "proposed" in context.lower():
                n_prop += 1
                continue
            ck.fail("conventions", f"{path}: {rule} cited without a (proposed) tag")
    ck.note(f"{n_prop} tagged citations of proposed rules")


def check_snapshot(ck, root, data):
    """Report headers must name the snapshot the evidence came from."""
    path = os.path.join(data, "snapshot.json")
    if not os.path.exists(path):
        ck.note("snapshot.json absent, snapshot pinning not checked")
        return
    with open(path, encoding="utf-8") as fh:
        snap = json.load(fh)["snapshot"]
    for rp in sorted(glob.glob(os.path.join(root, "lecture-*", "*.md"))):
        if os.path.basename(rp) == "index.md":
            continue
        series = os.path.basename(os.path.dirname(rp))
        want = snap.get(series, {}).get("commit", "")[:10]
        with open(rp, encoding="utf-8") as fh:
            head = fh.read(1200)
        m = re.search(r"\*\*Corpus snapshot:\*\*\s*`([0-9a-f]+)`", head)
        if not m:
            ck.fail("snapshot", f"{rp}: no corpus-snapshot line")
        elif want and m.group(1) != want:
            ck.fail("snapshot", f"{rp}: snapshot {m.group(1)} != {want}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default="lectures")
    ap.add_argument("--data", default="lectures/data")
    ap.add_argument("--corpus", default="")
    args = ap.parse_args()

    ck = Checker()
    if args.corpus:
        check_coverage(ck, args.root, args.corpus)
    check_scores(ck, args.root)
    check_agreement(ck, args.root, args.data)
    check_conventions(ck, args.root)
    check_snapshot(ck, args.root, args.data)
    return ck.report()


if __name__ == "__main__":
    sys.exit(main())
