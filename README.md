# QuantEcon Style Audit

Style-guide compliance audit of the QuantEcon lecture corpus, scored against the
conventions in
[`QuantEcon.manual`](https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide)
using the rule registry from
[`QuantEcon/action-style-guide`](https://github.com/QuantEcon/action-style-guide).

## 📊 Read the report

**Published site:** https://quantecon.github.io/audit.2026-05.style-guide/

A Jupyter Book with the cross-series synthesis, charts, the scoring spec, and a
drill-down report for every audited lecture.

## Scope

- **348 lectures** across 5 series: `lecture-python-intro`,
  `lecture-python-programming`, `lecture-python.myst`, `lecture-python-advanced.myst`,
  `lecture-dp`
- **7 in-scope rule categories**: Writing, Math, Code, Figures, References, Links,
  Admonitions (the 7 `qe-jax-*` rules are out of scope — they target `lecture-jax`)
- **41 of the 49 rules are checked by program** — 36 of the 42 in-scope registry rules
  plus 5 of the 7 proposed in [issue #18](https://github.com/QuantEcon/action-style-guide/issues/18);
  the remaining 8 are genuine judgment calls and are reviewed by reading
- **Corpus snapshot pinned per series** — see
  [`lectures/data/snapshot.json`](lectures/data/snapshot.json)

## Scoreboard

<!-- qe:readme-scoreboard -->
| Series | Lectures | Overall | HIGH | weakest category |
|--------|---------:|--------:|-----:|------------------|
| lecture-python-advanced.myst | 68 | 7.5 | 44 | Writing (4.6) |
| lecture-python.myst | 145 | 7.9 | 78 | Writing (4.9) |
| lecture-dp | 52 | 8.0 | 28 | Writing (5.6) |
| lecture-python-programming | 27 | 8.1 | 19 | Writing (4.1) |
| lecture-python-intro | 56 | 8.4 | 14 | Writing (6.2) |
| **Corpus** | **348** | **7.9** | **183** | Writing (5.1) |
<!-- /qe:readme-scoreboard -->

Every HIGH-priority lecture in this pass is HIGH because of a single weak category
rather than a low overall score, so the triage question is *which category* rather than
*which lecture*. Math is the binding constraint on most of them.

## How it works

```
corpus snapshot ──► tools/qestyle_scan.py ──► lectures/data/*.csv
                                                    │
                          tools/qestyle_draft.py ◄───┤   per-lecture reports
                                                    │
                          tools/qestyle_score.py ◄───┤   scores + priority
                                                    │
                          tools/qestyle_report.py ◄──┘   aggregate tables
```

The numbers live in `lectures/data/`. The per-lecture reports, the scoreboard, the
triage page and the charts are all derived from them, so they cannot disagree.
`tools/qestyle_check.py` is the gate that asserts it.

Reproduce or refresh a pass with [`UPDATE.md`](UPDATE.md), or invoke the `/audit-pass`
skill; the methodology is [`lectures/spec.md`](lectures/spec.md) §8–§10.

## Repository layout

```
.
├── README.md                  ← this file
├── ROADMAP.md                 ← project direction, open decisions, phased plan
├── UPDATE.md                  ← runbook: how to run a pass and refresh this report
├── CLAUDE.md                  ← read-me-first orientation for agents
├── requirements.txt           ← Jupyter Book build dependencies (needs Python 3.12+)
├── tools/                     ← the audit pipeline (lexer, rule checks, scoring, reports)
├── .claude/skills/audit-pass/ ← skill that drives a full pass end to end
├── contributions/             ← source behind the action-style-guide issues (#18–#21)
├── .github/workflows/         ← build + deploy to GitHub Pages
└── lectures/                  ← Jupyter Book source
    ├── _config.yml, _toc.yml
    ├── data/                  ← the numbers; everything else is derived from these
    ├── intro.md               ← front-page triage (where to focus)
    ├── details.md             ← full findings & remediation plan
    ├── spec.md                ← rubric, methodology, deterministic coverage
    ├── charts.md              ← visual summary, built from data/ at build time
    ├── appendix.md            ← feedback to the style guide & action-style-guide
    └── lecture-<series>/      ← per-series "Summary" + per-lecture reports
```

**This repository is the source of truth for the audit report.**

## About the `audit.YYYY-MM.{topic}` convention

This repo was created under QuantEcon's date-stamped audit convention, on the
assumption that each audit is a one-off snapshot. `lectures/data/` now carries a
cross-period time series, which is the thing a dated-and-archived repo cannot
accumulate — so the repo is being renamed to **`audit-lectures-style-guide`**, tracked in
[#2](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/2). The dated
convention stays right for genuinely episodic audits. See [`ROADMAP.md`](ROADMAP.md) §1.

## Related

- Contribution issues opened against `action-style-guide`:
  [#18](https://github.com/QuantEcon/action-style-guide/issues/18) (new rules),
  [#19](https://github.com/QuantEcon/action-style-guide/issues/19) (deterministic-checker
  scope), [#20](https://github.com/QuantEcon/action-style-guide/issues/20) (bulk audit
  mode), [#21](https://github.com/QuantEcon/action-style-guide/issues/21) (corpus offer)
- Style guide source:
  https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide
