# QuantEcon Style Audit — May 2026

> [!IMPORTANT]
> **This repository is the frozen record of the May 2026 style audit.** No further passes run here.
>
> The living successor is **[`QuantEcon/compliance-lecture-style`](https://github.com/QuantEcon/compliance-lecture-style)** — the standing conformance ledger. It carries this audit forward as the `2026-05` period of its cross-period history, alongside a completed `2026-08` pass over 348 lectures, together with the rubric, the runbook, the measurement tooling and a findings report for every lecture in the corpus.
>
> **Nothing here moves and nothing here breaks.** This report stays published at its original address, this repository keeps its name, and every link into it keeps working. An audit is an event; the record the audits update is the ledger. See [#2](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/2) for the decision and [#7](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/7) for the migration.

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

## About the naming, and where this went

This repo was created under QuantEcon's date-stamped audit convention, on the assumption that an audit is a one-off snapshot. Style conformance turned out to be a persistent concern with a time series attached, which is a different shape — so the project needed a durable home.

It did **not** get one by renaming this repository. Under [QEP-3](https://github.com/QuantEcon/qeps/pull/7) — the org's repository-naming standard, still an open proposal under review — renames fix names but never transmute types: a repository that has outgrown its type is *succeeded* by a new repository of the right type and archived, rather than renamed into it. A rename here would also have broken the published Pages URL and the audit links inside the live `action-style-guide` issues, for no reader benefit.

So the standing record was assembled as a new repository of a new type — `compliance-lecture-style`, QEP-3's proposed `compliance-{domain}` type: a conformance **ledger**, re-measured in place each pass, seeded from this audit. This repository keeps its name for life and is archived once absorbed, with its report still published and its issues still readable.

The dated `audit-*` convention is not retired; it remains right for a genuinely episodic audit — a security review of a release, a one-time deep dive. Under QEP-3's proposed grammar new dated audit repositories take the dash form (`audit-YYYY-MM-topic`); the dotted names that already exist, including this one, are grandfathered.

Open questions this audit raised have moved to [the ledger's tracker](https://github.com/QuantEcon/compliance-lecture-style/issues), because archiving locks issues here: the `{doc}` link form for same-series references ([#1](https://github.com/QuantEcon/compliance-lecture-style/issues/1), from #1 here), the near-empty MEDIUM priority band ([#2](https://github.com/QuantEcon/compliance-lecture-style/issues/2), from #3), how lectures shared between `lecture-dp` and `lecture-python.myst` are counted ([#3](https://github.com/QuantEcon/compliance-lecture-style/issues/3), from #4), and the audit weights now that rule reach is measured ([#4](https://github.com/QuantEcon/compliance-lecture-style/issues/4), from #6).

## Related

- Contribution issues opened against `action-style-guide`: [#18](https://github.com/QuantEcon/action-style-guide/issues/18) (new rules), [#19](https://github.com/QuantEcon/action-style-guide/issues/19) (Phase 4.3 acceleration), [#20](https://github.com/QuantEcon/action-style-guide/issues/20) (bulk audit mode), [#21](https://github.com/QuantEcon/action-style-guide/issues/21) (corpus offer)
- Style guide source: https://github.com/QuantEcon/QuantEcon.manual/tree/main/manual/styleguide
