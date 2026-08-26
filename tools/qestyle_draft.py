#!/usr/bin/env python3
"""Draft a per-lecture audit report from measured evidence.

The audit spec makes most of a report derivable. Severity (spec §5) is a function
of occurrence count and the rule's audit weight; the overall score and priority
(spec §4) are arithmetic. So this tool writes the mechanical part of every report
— header, score table, severity-bucketed issue list — and leaves the judgment
part (the rules spec §9 marks LLM-only, plus Strengths and Recommended actions)
for the review pass to fill in.

    python3 tools/qestyle_draft.py --corpus /path/to/quantecon --out lectures
    python3 tools/qestyle_draft.py --corpus ... --calibrate     # print the score distribution

Category scores come from a weighted violation load. The constants below were
calibrated so that applying this function to the May-2026 corpus snapshot
reproduces that pass's published corpus average and HIGH share — which is what
makes scores comparable across passes.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from qestyle_lex import lex                                     # noqa: E402
from qestyle_rules import (                                     # noqa: E402
    BUILD_RISK, CATEGORY, PROPOSED, count_citations, load_rule_titles, run_all,
)
from qestyle_scan import SERIES, applicability                   # noqa: E402

# Audit weight per rule — spec §2 (registry rules) and §3 (proposed rules).
WEIGHT = {
    "qe-writing-001": "high", "qe-writing-002": "medium", "qe-writing-003": "medium",
    "qe-writing-004": "high", "qe-writing-005": "medium", "qe-writing-006": "very-high",
    "qe-writing-007": "low", "qe-writing-008": "low", "qe-writing-009": "medium",
    "qe-math-001": "high", "qe-math-002": "very-high", "qe-math-003": "high",
    "qe-math-004": "high", "qe-math-005": "medium", "qe-math-006": "very-high",
    "qe-math-007": "high", "qe-math-008": "medium", "qe-math-009": "low",
    "qe-math-010": "very-high", "qe-math-011": "high", "qe-math-012": "medium",
    "qe-math-013": "medium", "qe-math-014": "low", "qe-math-015": "low",
    "qe-code-001": "medium", "qe-code-002": "medium", "qe-code-003": "high",
    "qe-code-004": "low", "qe-code-005": "low", "qe-code-006": "medium",
    "qe-fig-001": "low", "qe-fig-002": "low", "qe-fig-003": "high",
    "qe-fig-004": "medium", "qe-fig-005": "medium", "qe-fig-006": "medium",
    "qe-fig-007": "medium", "qe-fig-008": "low", "qe-fig-009": "low",
    "qe-fig-010": "high", "qe-fig-011": "medium",
    "qe-ref-001": "medium",
    "qe-link-001": "medium", "qe-link-002": "high",
    "qe-admon-001": "high", "qe-admon-002": "low", "qe-admon-003": "very-high",
    "qe-admon-004": "high", "qe-admon-005": "medium",
}

# --- scoring constants ----------------------------------------------------
# One violated rule costs WEIGHT_POINTS × REPEAT_FACTOR. The constants are set so
# the resulting score lands where the §4 rubric's own words put it: an isolated
# low-weight deviation near 9.5, one rule violated throughout near 6.5, several
# such rules near 4–5.
WEIGHT_POINTS = {"very-high": 1.60, "high": 1.15, "medium": 1.00, "low": 0.40}


def repeat_factor(n: int) -> float:
    """Saturating factor: repetition matters, but a 60th instance does not."""
    if n <= 1:
        return 1.0
    if n <= 4:
        return 1.7
    if n <= 9:
        return 2.3
    if n <= 24:
        return 2.8
    return 3.2


def rule_penalty(rule: str, count: int) -> float:
    return WEIGHT_POINTS[WEIGHT[rule]] * repeat_factor(count)


# Penalties within a category are combined with a decay, so a category is scored
# on its worst problems rather than on a raw sum. Without this, a category with
# eleven rules (Figures) would be punished for breadth in a way one with five
# (Writing) never could be.
DECAY = (1.0, 0.75, 0.6, 0.45, 0.35, 0.3, 0.25, 0.2, 0.18, 0.15, 0.12)

CATEGORY_CAP = 7.0          # most a single category can lose

# The judgment-only rules belong to their categories too, so a reviewer finding
# scores exactly like a measured one.
JUDGMENT_CATEGORY = {
    "qe-writing-002": "writing", "qe-writing-003": "writing",
    "qe-writing-005": "writing", "qe-writing-007": "writing",
    "qe-math-009": "math", "qe-math-014": "math", "qe-math-015": "math",
    "qe-code-001": "code",
}
CAT_LABEL = {"writing": "Writing", "math": "Math", "code": "Code", "jax": "JAX",
             "figures": "Figures", "references": "References", "links": "Links",
             "admonitions": "Admonitions"}
CAT_ORDER = ["writing", "math", "code", "jax", "figures", "references", "links",
             "admonitions"]


def category_score(cat, violations):
    """0–10 for one category, from its rules' weighted violation load."""
    members = list(CATEGORY.get(cat, [])) + [r for r, c in JUDGMENT_CATEGORY.items()
                                             if c == cat]
    parts = sorted(
        (rule_penalty(rule, violations[rule]["count"])
         for rule in members if rule in violations),
        reverse=True)
    penalty = sum(p * (DECAY[i] if i < len(DECAY) else DECAY[-1])
                  for i, p in enumerate(parts))
    penalty = min(penalty, CATEGORY_CAP)
    return max(1.0, round((10.0 - penalty) * 2) / 2)


BREAKS_BUILD = ("inside $$", "never closed", "ticks) inside")


def severity(rule, count, details=()):
    """Spec §5: Critical / High / Medium / Low for one finding.

    A build-risk rule is only Critical when the occurrence really is the
    breaking shape. ``qe-math-006`` also reports bare amsmath blocks, which are
    a convention deviation rather than a build failure.
    """
    if rule in BUILD_RISK:
        if any(marker in d for d in details for marker in BREAKS_BUILD):
            return "Critical"
        return "High"
    w = WEIGHT[rule]
    if count >= 5 or w == "very-high":
        return "High"
    if count >= 2 or w == "high":
        return "Medium"
    return "Low"


def priority_bucket(overall, cat_scores):
    nums = [v for v in cat_scores.values() if isinstance(v, float)]
    if overall <= 5.0 or (nums and min(nums) <= 4):
        return "HIGH"
    if overall <= 7.0:
        return "MEDIUM"
    if overall <= 8.5:
        return "LOW"
    return "NONE"


def rule_label(rule, titles):
    tag = " (proposed)" if rule in PROPOSED else ""
    return f"qe-{rule.split('qe-')[1]}{tag}"


def one_line_note(cat, violations, titles):
    """A short cell for the score table, naming the rules that cost the most."""
    scored = []
    members = list(CATEGORY.get(cat, [])) + [r for r, c in JUDGMENT_CATEGORY.items()
                                             if c == cat]
    for rule in members:
        v = violations.get(rule)
        if v:
            scored.append((rule_penalty(rule, v["count"]), rule, v["count"]))
    if not scored:
        return "no mechanical violations detected."
    scored.sort(reverse=True)
    parts = [f"`{rule}`{' (proposed)' if rule in PROPOSED else ''} ×{n}"
             for _, rule, n in scored[:3]]
    extra = "" if len(scored) <= 3 else f", +{len(scored) - 3} more"
    return "; ".join(parts) + extra + "."


def fmt_lines(v, limit=10):
    ls = v["lines"][:limit]
    more = "" if len(v["lines"]) <= limit else ", …"
    return ", ".join(str(x) for x in ls) + more


def summarise_hits(hits_by_rule):
    """{rule: [Hit]} -> {rule: {count, lines, samples}}, the shape the report uses."""
    return {
        rule: {
            "count": len(hs),
            "lines": sorted({h.line for h in hs}),
            "samples": [escape_roles(h.detail) for h in hs[:4]],
        }
        for rule, hs in hits_by_rule.items()
    }


JUDGMENT_RULES = {
    "qe-writing-002", "qe-writing-003", "qe-writing-005", "qe-writing-007",
    "qe-math-009", "qe-code-001", "qe-math-014", "qe-math-015",
}


# A MyST role quoted in prose — ``{cite}`Hall1978```, ``{doc}`ifp_egm``` — is *sample text*
# here, not a live cross-reference, and the cited work is not in this book. Left bare, Sphinx
# tries to resolve every one: 615 of them across the reports, and 478 of the build's warnings.
# Wrapped in a space-padded double-backtick span they render literally and resolve nothing.
# The padding matters: ``` ``{doc}`x``` ``` closes on a run of three and does not parse.
ROLE_RE = re.compile(
    r"(?<!`)(\{(?:cite|cite:t|eq|doc|numref|ref|term|abbr|prf:ref)\}(?:`[^`\n]*`)?)")


def escape_roles(text: str) -> str:
    """Render a MyST role in prose as literal text rather than a cross-reference."""
    return ROLE_RE.sub(r"`` \1 ``", text)


def tag_proposed(text: str) -> str:
    """Add the (proposed) tag to a bare proposed-rule citation in reviewer prose.

    Reviewers write Strengths and Actions freehand, so they cite rules without the
    tag the conventions require. Normalising here keeps the convention without
    asking a reviewer to remember it.
    """
    for rule in sorted(PROPOSED, reverse=True):
        text = re.sub(
            re.escape(rule) + r"`?(?! ?\(proposed\))(?!`? ?\*\(proposed\)\*)",
            lambda m: m.group(0) + " (proposed)", text)
    return text


def load_review(series, stem):
    """Read one review overlay, if the review pass has produced it.

    The overlay carries only what a program cannot measure: findings for the
    judgment-only rules, plus the Strengths and Recommended actions prose. It is
    kept separate from the drafts so that fixing a check and re-running the
    evidence layer never discards reviewer work.
    """
    if not ARGS or not ARGS.reviews:
        return {}
    path = os.path.join(ARGS.reviews, series, stem + ".json")
    if not os.path.exists(path):
        return {}
    import json
    with open(path, encoding="utf-8") as fh:
        try:
            return json.load(fh)
        except ValueError:
            return {}


def draft_report(series, stem, path, titles):
    doc = lex(path, series)
    violations = summarise_hits(run_all(doc))
    review = load_review(series, stem)
    # Reviewer findings on the judgment-only rules enter the same scoring
    # function as measured ones, with the same audit weights.
    reviewed = {}
    for f in review.get("judgment", []):
        rule = f.get("rule")
        if rule not in JUDGMENT_RULES or not f.get("count"):
            continue
        reviewed[rule] = {
            "count": int(f["count"]),
            "lines": [int(x) for x in (f.get("lines") or [])][:24],
            # Reviewers cite other rules inside a finding's prose too, not just in
            # Strengths and Actions — so the tag has to be normalised here as well.
            "samples": [escape_roles(tag_proposed(f.get("detail", "")))],
        }
    violations.update(reviewed)
    applies = applicability(doc)
    cites, cites_t = count_citations(doc)

    cat_scores = {}
    for cat in CAT_ORDER:
        a = applies[cat]
        if a == "out of scope":
            cat_scores[cat] = "out of scope"
        elif not a:
            cat_scores[cat] = "N/A"
        else:
            cat_scores[cat] = category_score(cat, violations)

    nums = [v for v in cat_scores.values() if isinstance(v, float)]
    overall = round(sum(nums) / len(nums), 1) if nums else 0.0
    prio = priority_bucket(overall, cat_scores)

    # --- header -----------------------------------------------------------
    audited = [CAT_LABEL[c].lower() for c in CAT_ORDER
               if isinstance(cat_scores[c], float)]
    out = [f"# {stem}", ""]
    out += [
        f"- **Series:** {series}",
        f"- **File:** `lectures/{stem}.md`",
        f"- **Audit date:** {ARGS.date}",
        f"- **Corpus snapshot:** `{ARGS.snapshot.get(series, '')[:10]}`",
        f"- **Categories audited:** {', '.join(audited)}"
        + ("  *(JAX out of scope)*" if cat_scores["jax"] == "out of scope" else ""),
        f"- **Overall score:** {overall:.1f} / 10",
        f"- **Priority:** {prio}",
        "",
        "## Score breakdown",
        "",
        "| Category     | Score | One-line note |",
        "|--------------|-------|---------------|",
    ]
    for cat in CAT_ORDER:
        v = cat_scores[cat]
        if isinstance(v, float):
            cell = f"{v:g}/10"
            note = one_line_note(cat, violations, titles)
        elif v == "out of scope":
            cell, note = "out of scope", "JAX rules target `lecture-jax`."
        else:
            cell, note = "N/A", NA_REASON[cat]
        out.append(f"| {CAT_LABEL[cat]:<12} | {cell:<5} | {note} |")

    # --- issues -----------------------------------------------------------
    buckets = {"Critical": [], "High": [], "Medium": [], "Low": []}
    for rule, v in sorted(violations.items()):
        cat = next((c for c, rs in CATEGORY.items() if rule in rs),
                   JUDGMENT_CATEGORY.get(rule))
        if cat and not isinstance(cat_scores.get(cat), float):
            continue        # rule sits in a category this lecture does not score
        sev = severity(rule, v["count"], v["samples"])
        title = titles.get(rule, "")
        tag = " (proposed)" if rule in PROPOSED else ""
        sample = v["samples"][0] if v["samples"] else ""
        src = " *(reviewer)*" if rule in JUDGMENT_RULES else ""
        buckets[sev].append(
            f"- **[{rule}{tag}]**{src} — {title}. *Count:* {v['count']}. "
            + (f"*Lines:* {fmt_lines(v)}. " if v["lines"] else "")
            + (f"*Example:* {sample}." if sample else "")
        )

    out += ["", "## Issues", ""]
    for sev in ("Critical", "High", "Medium", "Low"):
        head = {"Critical": "### Critical", "High": "### High severity",
                "Medium": "### Medium severity", "Low": "### Low severity"}[sev]
        out += [head]
        out += buckets[sev] if buckets[sev] else ["_None found._"]
        out += [""]

    # --- reviewer prose, with a measured fallback -------------------------
    out += ["", "## Strengths", ""]
    strengths = [escape_roles(tag_proposed(s)) for s in review.get("strengths", []) if s.strip()]
    if strengths:
        out += [f"- {s.rstrip('.')}." for s in strengths]
    else:
        clean = [CAT_LABEL[c] for c in CAT_ORDER
                 if isinstance(cat_scores[c], float) and cat_scores[c] >= 9]
        if clean:
            out.append(f"- {', '.join(clean)} score 9 or above — no material "
                       f"violations measured in those categories.")
        for rule in ("qe-math-006", "qe-admon-003", "qe-math-007", "qe-admon-004"):
            if rule not in violations:
                out.append(f"- No `{rule}` violations — {titles.get(rule, '')}.")
        if cites_t and "qe-ref-001" not in violations:
            out.append(f"- Citations distinguish `{{cite}}` from `{{cite:t}}` correctly "
                       f"({cites} parenthetical, {cites_t} in-text).")
        if not out[-1].startswith("- "):
            out.append("- No mechanical violations of note.")

    out += ["", "## Recommended actions", ""]
    actions = [escape_roles(tag_proposed(a)) for a in review.get("actions", []) if a.strip()]
    if actions:
        out += [f"{i}. {a.rstrip('.')}." for i, a in enumerate(actions, 1)]
    else:
        ranked = sorted(
            ((rule_penalty(r, v["count"]), r, v)
             for r, v in violations.items()
             if isinstance(cat_scores.get(
                 next((c for c, rs in CATEGORY.items() if r in rs),
                      JUDGMENT_CATEGORY.get(r, "writing"))), float)),
            reverse=True)
        if ranked:
            for i, (_, rule, v) in enumerate(ranked[:7], 1):
                tag = " (proposed)" if rule in PROPOSED else ""
                out.append(f"{i}. `{rule}`{tag} — {titles.get(rule, '')} "
                           f"({v['count']} occurrence"
                           f"{'s' if v['count'] != 1 else ''}).")
        else:
            out.append("1. No remediation required; keep the current conventions.")
    out.append("")
    return "\n".join(out), overall, prio, cat_scores, violations, reviewed


NA_REASON = {
    "writing": "no narrative text.",
    "math": "no mathematical content.",
    "code": "no executable code cells.",
    "jax": "not a JAX lecture.",
    "figures": "no figures or plotting code.",
    "references": "no citations in this lecture.",
    "links": "no links.",
    "admonitions": "no admonitions, exercises or solutions.",
}

ARGS = None


def main():
    global ARGS
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--out", default="", help="book root to write reports into")
    ap.add_argument("--date", default="2026-08-25")
    ap.add_argument("--rules", default="")
    ap.add_argument("--reviews", default="",
                    help="directory of review overlays (see load_review)")
    ap.add_argument("--judgment-csv", default="",
                    help="write the merged reviewer findings here")
    ap.add_argument("--calibrate", action="store_true",
                    help="print the resulting score distribution and write nothing")
    ARGS = ap.parse_args()

    rules_dir = ARGS.rules or os.path.join(
        ARGS.corpus, "action-style-guide", "style_checker", "rules")
    # A rule title can itself quote a role — qe-math-013 is "Reference equations via
    # ``{eq}`label```" — so titles are escaped once, at load.
    titles = {k: escape_roles(v) for k, v in load_rule_titles(rules_dir).items()}

    import subprocess
    ARGS.snapshot = {}
    for s in SERIES:
        try:
            ARGS.snapshot[s] = subprocess.run(
                ["git", "-C", os.path.join(ARGS.corpus, s), "rev-parse", "HEAD"],
                capture_output=True, text=True, check=True).stdout.strip()
        except Exception:
            ARGS.snapshot[s] = ""

    stats, judgment = [], []
    for series in SERIES:
        root = os.path.join(ARGS.corpus, series, "lectures")
        if not os.path.isdir(root):
            continue
        dest = os.path.join(ARGS.out, series) if ARGS.out else ""
        if dest:
            os.makedirs(dest, exist_ok=True)
        for fn in sorted(f for f in os.listdir(root) if f.endswith(".md")):
            stem = fn[:-3]
            text, overall, prio, cats, viol, reviewed = draft_report(
                series, stem, os.path.join(root, fn), titles)
            stats.append((series, stem, overall, prio))
            for rule, v in reviewed.items():
                judgment.append((series, stem, rule, v["count"]))
            if dest:
                with open(os.path.join(dest, fn), "w", encoding="utf-8") as fh:
                    fh.write(text)

    if ARGS.judgment_csv and judgment:
        import csv
        os.makedirs(os.path.dirname(ARGS.judgment_csv) or ".", exist_ok=True)
        with open(ARGS.judgment_csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["series", "lecture", "rule", "count"])
            w.writerows(judgment)
        print(f"wrote {ARGS.judgment_csv} ({len(judgment)} reviewer findings)")

    n = len(stats)
    by_prio = {p: sum(1 for s in stats if s[3] == p)
               for p in ("HIGH", "MEDIUM", "LOW", "NONE")}
    mean = sum(s[2] for s in stats) / n if n else 0
    print(f"lectures: {n}   corpus mean: {mean:.2f}")
    for p in ("HIGH", "MEDIUM", "LOW", "NONE"):
        print(f"  {p:7s} {by_prio[p]:4d}  ({by_prio[p]/n*100:.1f}%)")
    if ARGS.calibrate:
        for series in SERIES:
            rows = [s for s in stats if s[0] == series]
            if rows:
                print(f"  {series:32s} n={len(rows):4d} "
                      f"mean={sum(r[2] for r in rows)/len(rows):.2f} "
                      f"HIGH={sum(1 for r in rows if r[3]=='HIGH')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
