# QuantEcon Style Audit — May 2026

Style-guide compliance audit of the QuantEcon lecture series, scored against the conventions in [`QuantEcon.manual`](https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide) using the rule registry from [`QuantEcon/action-style-guide`](https://github.com/QuantEcon/action-style-guide).

## 📊 Read the report

**Published site:** https://quantecon.github.io/audit.2026-05.style-guide/

The site is a Jupyter Book with the full cross-series synthesis, charts, scoring spec, and a drill-down report for every one of the 299 audited lectures.

## Scope

- **299 lectures** across 5 series: `lecture-python-intro`, `lecture-python-programming`, `lecture-python.myst`, `lecture-python-advanced.myst`, `lecture-dp`
- **7 in-scope rule categories**: Writing, Math, Code, Figures, References, Links, Admonitions (JAX out of scope)
- **Audit dates:** 2026-05-27 (v1, writing + math) / 2026-05-28 (v2, full extension)

## Scoreboard

| Series | Lectures | Overall | HIGH | weakest category |
|--------|---------:|--------:|-----:|------------------|
| lecture-python-advanced.myst | 62 | 7.0 | 6 | Math (5.6) |
| lecture-dp | 50 | 7.5 | 17 | Figures (6.9) |
| lecture-python-intro | 51 | 7.6 | 1 | Figures (6.4) |
| lecture-python-programming | 26 | 8.0 | 3 | Figures (6.5) |
| lecture-python.myst | 110 | 9.0 | 2 | Writing (8.0) |
| **Corpus** | **299** | **8.0** | **29** | Figures (7.4) |

## Repository layout

```
.
├── README.md                  ← this file
├── ROADMAP.md                 ← project direction, open decisions, phased plan
├── UPDATE.md                  ← runbook: how to re-run the audit & refresh this report
├── requirements.txt           ← Jupyter Book build dependencies
├── contributions/             ← source behind the action-style-guide issues (#18–#21)
├── .github/workflows/         ← build + deploy to GitHub Pages
└── lectures/                  ← Jupyter Book source
    ├── _config.yml, _toc.yml
    ├── intro.md               ← front-page triage (where to focus)
    ├── details.md             ← full findings & remediation plan
    ├── spec.md                ← scoring rubric + report template (the audit spec)
    ├── charts.md              ← visual summary (built from audit data)
    ├── appendix.md            ← feedback to the style guide & action-style-guide
    └── lecture-<series>/      ← per-series "Summary" + per-lecture reports
```

**This repository is the source of truth for the audit report.** To reproduce the audit or refresh the documents, follow [`UPDATE.md`](UPDATE.md).

## About the `audit.YYYY-MM.{topic}` convention

This repo was created under QuantEcon's date-stamped audit convention. As noted in [`ROADMAP.md`](ROADMAP.md), the project is moving toward a **durable, regularly-updated** model — the naming and migration are open decisions pending feedback on the related [`action-style-guide` issues](https://github.com/QuantEcon/action-style-guide/issues) (#18–#21).

## Related

- Contribution issues opened against `action-style-guide`: [#18](https://github.com/QuantEcon/action-style-guide/issues/18) (new rules), [#19](https://github.com/QuantEcon/action-style-guide/issues/19) (Phase 4.3 acceleration), [#20](https://github.com/QuantEcon/action-style-guide/issues/20) (bulk audit mode), [#21](https://github.com/QuantEcon/action-style-guide/issues/21) (corpus offer)
- Style guide source: https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide
