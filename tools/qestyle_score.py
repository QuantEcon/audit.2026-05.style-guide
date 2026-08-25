#!/usr/bin/env python3
"""Derive overall scores and priority buckets from the per-lecture score tables.

The rubric in ``lectures/spec.md`` §4 defines the overall score as the mean of the
in-scope category scores, and the priority bucket as a function of that mean and
the weakest category. Both are therefore arithmetic, not judgment — so this tool
computes them from each report's own score table rather than trusting a written
header. (In the previous pass 94 of 299 reports carried an overall that did not
match their own categories, and 35 carried a priority bucket the rule does not
give.)

    python3 tools/qestyle_score.py --check          # report drift, change nothing
    python3 tools/qestyle_score.py --fix            # rewrite headers to match
    python3 tools/qestyle_score.py --csv lectures/data/scores.csv

Run ``--fix`` after any agent pass, then ``--check`` in CI.
"""

from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import sys

CATEGORIES = ["Writing", "Math", "Code", "JAX", "Figures",
              "References", "Links", "Admonitions"]
ROW_RE = re.compile(
    r"^\|\s*(" + "|".join(CATEGORIES) + r")\s*\|\s*([^|]+?)\s*\|", re.M)
OVERALL_RE = re.compile(r"^(- \*\*Overall score:\*\*\s*)(.+)$", re.M)
PRIORITY_RE = re.compile(r"^(- \*\*Priority:\*\*\s*)(.+)$", re.M)
SCORE_CELL_RE = re.compile(r"^([\d]+(?:\.\d)?)\s*/\s*10$")


def parse_report(path):
    """Return (category scores dict, declared overall, declared priority, text)."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    scores = {}
    for m in ROW_RE.finditer(text):
        cat, cell = m.group(1), m.group(2).strip()
        sm = SCORE_CELL_RE.match(cell)
        if sm:
            scores[cat] = float(sm.group(1))
        else:
            scores[cat] = cell            # N/A or "out of scope"
    dm = OVERALL_RE.search(text)
    pm = PRIORITY_RE.search(text)
    declared = dm.group(2).strip() if dm else None
    priority = pm.group(2).strip() if pm else None
    return scores, declared, priority, text


def compute(scores):
    """Overall = mean of in-scope categories; priority per spec §4."""
    nums = [v for k, v in scores.items() if isinstance(v, float)]
    if not nums:
        return None, None
    overall = round(sum(nums) / len(nums), 1)
    if overall <= 5.0 or min(nums) <= 4:
        prio = "HIGH"
    elif overall <= 7.0:
        prio = "MEDIUM"
    elif overall <= 8.5:
        prio = "LOW"
    else:
        prio = "NONE"
    return overall, prio


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default="lectures", help="book source root")
    ap.add_argument("--check", action="store_true", help="report drift only")
    ap.add_argument("--fix", action="store_true", help="rewrite headers to match")
    ap.add_argument("--csv", default="", help="write per-lecture scores CSV here")
    ap.add_argument("--declared", action="store_true",
                    help="record the header's own overall/priority instead of the "
                         "recomputed ones (used to capture a past pass as published)")
    args = ap.parse_args()

    paths = sorted(p for p in glob.glob(os.path.join(args.root, "lecture-*", "*.md"))
                   if os.path.basename(p) != "index.md")
    rows, drift = [], []
    for path in paths:
        scores, declared, priority, text = parse_report(path)
        overall, prio = compute(scores)
        if overall is None:
            drift.append((path, "no parsable category scores"))
            continue
        series = os.path.basename(os.path.dirname(path))
        stem = os.path.basename(path)[:-3]
        if args.declared:
            dnum = re.match(r"([\d.]+)", declared or "")
            overall_out = float(dnum.group(1)) if dnum else overall
            prio_out = priority or prio
        else:
            overall_out, prio_out = overall, prio
        rows.append({
            "series": series, "lecture": stem,
            "overall": overall_out, "priority": prio_out,
            **{c.lower(): (scores.get(c) if isinstance(scores.get(c), float) else
                           ("out-of-scope" if str(scores.get(c, "")).lower().startswith("out")
                            else "N/A"))
               for c in CATEGORIES},
        })
        want_o = f"{overall:.1f} / 10"
        if declared != want_o or priority != prio:
            drift.append((path, f"header says {declared!r}/{priority!r}, "
                                f"categories give {want_o!r}/{prio!r}"))
            if args.fix:
                text = OVERALL_RE.sub(lambda m: m.group(1) + want_o, text, count=1)
                text = PRIORITY_RE.sub(lambda m: m.group(1) + prio, text, count=1)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(text)

    if args.csv:
        os.makedirs(os.path.dirname(args.csv) or ".", exist_ok=True)
        with open(args.csv, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=[
                "series", "lecture", "writing", "math", "code", "jax", "figures",
                "references", "links", "admonitions", "overall", "priority"])
            w.writeheader()
            for r in rows:
                w.writerow(r)

    print(f"reports: {len(rows)}")
    print(f"{'fixed' if args.fix else 'drifting'}: {len(drift)}")
    for p, why in drift[:20]:
        print(f"  {p}: {why}")
    if len(drift) > 20:
        print(f"  ... {len(drift) - 20} more")

    if args.check and drift:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
