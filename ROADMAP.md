# Roadmap

Living document for the QuantEcon lecture style-audit project. Tracks strategic
direction, open design decisions, and pending work.

**Last updated:** 2026-08-25

> **Program coordination has moved.** Program-level direction — the style-guide
> consolidation (rules database, linter, AI review agent), repo naming, cadence, and
> tooling decisions — now lives in the planning hub **`QuantEcon/project-style-guide`**
> (private), the program's home of record. This file records this audit's own context and
> follow-ups; where its phases overlap program planning, **the hub supersedes**.

---

## Where we are today

- **The audit is reproducible.** A pass is now a pipeline (`tools/qestyle_*.py`) over a
  **pinned corpus snapshot**, not a reading exercise: 41 of the 49 rules are checked by
  program, scores and priority buckets are derived arithmetically from the rubric, and
  `tools/qestyle_check.py` gates the result. Same commits in, same numbers out.
- **Corpus refreshed to 348 lectures** across the 5 series (from 300 at the previous
  snapshot). 49 lectures were added and 1 report was retired.
- **First real time series.** The same checks were run over both the previous and the
  current snapshot, so `lectures/data/rule_reach_history.csv` holds a like-for-like
  comparison and `charts.md` plots it. This is the thing the project has been aiming at
  since the shift to a durable model — and the first evidence that any rule is
  *improving* rather than just being counted.
- **Tier 2 dashboard live** — Jupyter Book on GitHub Pages at
  **https://quantecon.github.io/audit.2026-05.style-guide/**, with the synthesis, 5
  charts (now including the cross-pass trend), the spec, and a report per lecture. Chart
  data is no longer inline: it is read from `lectures/data/` at build time.
- **4 issues open** against `action-style-guide`
  ([#18](https://github.com/QuantEcon/action-style-guide/issues/18) new rules,
  [#19](https://github.com/QuantEcon/action-style-guide/issues/19) deterministic-checker
  scope, [#20](https://github.com/QuantEcon/action-style-guide/issues/20) bulk audit
  mode, [#21](https://github.com/QuantEcon/action-style-guide/issues/21) corpus offer).
  #19 now has an answer from implementation — see §4.1.

---

## 1. Naming: decided

> **Decision (2026-08).** Rename this repo to **`QuantEcon/audit-lectures-style-guide`** —
> the date comes out of the name, the scope and the topic stay in it. Tracked in
> [#2](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/2), with the
> migration checklist and the Pages-URL consequences.

The earlier decision (2026-05) was to keep `audit.YYYY-MM.{topic}` and publish a new dated
repo per period, archiving the prior one — a rename was avoided because it would break the
published Pages URL and the posted issue cross-links.

What changed is that `lectures/data/` began accumulating across passes.
`history.csv` and `rule_reach_history.csv` now hold one row per period, and the trend chart
is built from them: the same checks over two pinned snapshots, so the comparison measures
the lectures rather than the method. A new dated repo per period either loses that series
or requires copying it forward by hand at every pass. The dated convention and a
cross-period time series pull in opposite directions, and the series is worth more.

The immediate prompt was that this pass left the repo named for 2026-05 while carrying a
2026-08 snapshot — not a stable end state either way.

Of the migration options in §2.3, **α (rename in place)** is what was chosen: the
accumulated `lectures/data/` history is the asset, and a rename keeps it where it is.
GitHub redirects `github.com` links, so the four posted `action-style-guide` issue
cross-links survive; the Pages URL does not redirect and the 16 in-repo references to it
need editing.

**The dated convention is not retired.** It remains the right fit for genuinely episodic
audits — a security review of a release, a one-time deep dive. Style-guide compliance
turned out to be a persistent concern with a time series attached, which is a different
shape.

---

## 2. Open design decisions

### 2.1 Repo name

| Name | Pros | Cons |
|------|------|------|
| `QuantEcon/style-audits` (plural) | Implies recurring snapshots; matches the `lecture-*` naming family | Slightly verbose |
| `QuantEcon/lecture-style-audit` | Clear scope; "lecture" anchors it to the corpus | Singular implies one-shot |
| `QuantEcon/lecture-quality` | Broader umbrella; could expand beyond style | Vague — what does "quality" mean operationally? |
| `QuantEcon/style-compliance` | Direct, professional | Less discoverable; "compliance" reads as regulatory |
| Keep `audit.YYYY-MM.style-guide` | No migration; preserves the Pages URL and issue cross-links | The name goes stale the moment a pass refreshes it, as it has now |

**Resolved:** `QuantEcon/audit-lectures-style-guide` — see §1. It reads as
"an audit, of the lectures, against the style guide", and leaves room for a
sibling (`audit-lectures-accessibility`) without implying a one-off or needing a
date. `style-audits` was the earlier leaning; the chosen name keeps the `audit-`
prefix that already signals what kind of repo this is.

### 2.2 Time-series storage

Largely settled in practice: `lectures/data/*.csv` holds the current pass, and
`history.csv` / `rule_reach_history.csv` hold one row per period. That is the hybrid
(option D) the earlier analysis preferred — markdown for humans, CSV for charts. The
remaining question is only whether per-pass markdown snapshots are worth keeping
alongside, or whether git history is enough. **Leaning:** git history is enough.

### 2.3 Migration

- **α** — rename this repo. Preserves history and the 4 issue cross-links; breaks the
  Pages URL.
- **β** — archive this repo as the baseline; create the durable repo and carry
  `lectures/data/` forward. Cleaner conceptually; loses the per-lecture git history.
- **γ** — keep both: this repo as the 2026-05 reference, the new one going forward.

**Resolved: α.** The accumulated `lectures/data/` history is the asset and a rename keeps
it in place. Losing the old Pages URL costs less than re-establishing the series.

### 2.4 Cadence + automation

The manual cost of a pass has dropped sharply — the evidence and scoring layers are
code, so a pass is a scripted run plus a review of the 8 judgment-only rules. That makes
a scheduled pass genuinely cheap:

- **Scheduled GitHub Action / Routine**: run `tools/qestyle_scan.py` and
  `tools/qestyle_draft.py` on a cron, open a PR with the diff. Now the obvious next step.
- **Triggered**: run before each lecture-series release, as a quality gate.

**Leaning:** wire the scripted part to a schedule; keep the review pass human-triggered.
`action-style-guide` [#20](https://github.com/QuantEcon/action-style-guide/issues/20) is
no longer a blocker for cadence, though it would still be the better long-term home for
the checks.

---

## 3. Dashboard

Tier 2 (Jupyter Book + charts) is live and now reads from `lectures/data/`, which is what
Tier 3 would have needed anyway. Remaining Tier 3 ideas, in order of likely value:

1. **Sortable / filterable lecture table** — the HIGH list is long enough that scanning
   it in markdown is work.
2. **Per-rule drill-down page** — one page per rule, listing every lecture and line. The
   data is already in `violations.csv`.
3. **Score-delta chart** — which lectures improved or regressed between passes. Needs
   `scores.csv` from two passes; available from the next pass onward.
4. **Category floor view** — since every HIGH lecture is triggered by a single weak
   category, a view grouped by *which* category would match how the work actually gets
   done.

Build these only if the Tier 2 pages are being used.

---

## 4. Pending external work

### 4.1 `action-style-guide` issues

| Issue | Status |
|-------|--------|
| [#18](https://github.com/QuantEcon/action-style-guide/issues/18) — 7 new style rules | Open. 5 of the 7 are now implemented as checks here and carry measured corpus evidence; `qe-math-014` and `qe-math-015` remain judgment-only and weak-evidence, and are still the two candidates to defer. |
| [#19](https://github.com/QuantEcon/action-style-guide/issues/19) — deterministic-checker scope | **Answered by implementation.** The issue argued the planned "~13" rules should be 22. Building them showed **41 of 49** are mechanically checkable — 36 of the 42 in-scope registry rules plus 5 proposed. The 8 that are not are listed in [spec §9](lectures/spec.md). The issue body should be updated with this result. |
| [#20](https://github.com/QuantEcon/action-style-guide/issues/20) — bulk audit mode | Open. Still the right long-term home for the checks: `tools/qestyle_rules.py` is a working reference implementation that could be contributed rather than maintained here. |
| [#21](https://github.com/QuantEcon/action-style-guide/issues/21) — corpus as test fixtures | Open, no action required. `lectures/data/violations.csv` is now a labelled fixture set with line numbers, which is more useful than the offer as originally framed. |

### 4.2 Findings to file against lecture repos

Small and structural; worth an issue each regardless of audit cadence.

- `lecture-python-programming/lectures/python_by_example.md:499` and `:549` — two
  `{exercise-start}` fences never closed, so each swallows the rest of its exercise
  including a nested `{hint}` at the same tick count (`qe-admon-003`). The only two
  malformed gated directives in ~690 across the corpus.
- `lecture-python.myst/lectures/cross_product_trick.md:133` — malformed
  `` {eq}`eq:Kalman102} `` reference. `lecture-dp` carries a synced copy with the same
  defect; fixing upstream fixes both.
- `lecture-python.myst/lectures/ifp_advanced.md:158` — raw `\label{a:y0}` inside `$$`,
  which MyST does not resolve (`qe-math-007`). Same synced-copy situation.

> **Withdrawn.** The previous report's headline build-risk finding —
> `divergence_measures.md:134` as `\begin{align}` inside `$$`, "breaks the PDF build" —
> does not hold. There is no `align` inside `$$` anywhere in the corpus. That line is a
> bare top-level `\begin{align}`, which MyST's amsmath extension handles. It remains a
> convention outlier (17 bare alignment blocks against 6,094 `$$` blocks) and is reported
> as one, but no issue should be filed calling it a build break.

---

## 5. Phased plan

### Phase 0 — Stabilise findings ✅
Audit published, spec published, 4 contribution issues opened.

### Phase 1 — Tier 2 dashboard ✅
Jupyter Book with `quantecon-book-theme`, per-lecture reports committed, charts, sidebar
TOC, GitHub Pages deploy. Chart data externalised to `lectures/data/` (was a Phase 1
follow-up; done).

### Phase 2 — Repo naming ✅ decided, migration pending
Rename to `audit-lectures-style-guide`, tracked in
[#2](https://github.com/QuantEcon/audit.2026-05.style-guide/issues/2). See §1 for the
reasoning and §2.3 for why the rename is in place rather than a fresh repo.

### Phase 3 — Cadence ◐ in progress
A second pass has run, on a pinned snapshot, with a like-for-like comparison to the
first. The procedure is documented in `UPDATE.md` and gated by
`tools/qestyle_check.py`. What remains is agreeing an interval and putting the scripted
part on a schedule.

### Phase 4 — Tier 3 dashboard (conditional)
See §3. Only if the Tier 2 pages are being used.

### Phase 5 — Automation ◐ partly delivered
The evidence and scoring layers are scripts, so most of what Phase 5 anticipated exists.
What is left is scheduling them and opening the PR automatically — and, longer term,
moving the checks into `action-style-guide` per #20 rather than maintaining them here.

---

## 6. Risks + known concerns

- **Judgment drift — largely mitigated.** The previous pass showed the failure mode
  clearly: 94 of 299 reports carried an overall score that did not match their own
  categories, 35 carried a priority bucket the rubric does not give, one report described
  a lecture that does not exist, and the largest series was scored noticeably more
  leniently than the others. Scores are now arithmetic and evidence is measured, so this
  class of error cannot recur silently. It remains possible in the 8 judgment-only rules.
- **Heuristic checks need maintenance.** `qe-writing-004` and `qe-writing-006` depend on
  curated proper-noun and common-noun lists; `qe-math-002` has to tell a transpose
  apostrophe from a derivative and a `^T` transpose from a terminal date. All three were
  tightened against adversarial review of real hits, and all three will need extending as
  lectures are added. They are the most likely source of a wrong count.
- **The MEDIUM band barely populates.** Applied consistently, spec §4's "any single
  in-scope category ≤ 4 → HIGH" catches nearly every lecture before its *overall* falls
  into the 5.1–7.0 MEDIUM range — every HIGH lecture in this pass was triggered by the
  category floor, and only one lecture in the corpus has an overall at or below 5.0. The
  4-bucket scheme is effectively 3 buckets. Worth revisiting §4 in the spec: either widen
  MEDIUM, or replace the flat floor with something graduated.
- **Audit cost.** The mechanical layer runs the whole corpus in seconds at no token cost.
  The remaining cost is the review pass over the judgment-only rules, which scales with
  corpus size.
- **Lecture content evolves.** Counts go stale immediately after each pass. Pinning the
  snapshot means a stale number is at least an *honest* number about a known commit.
- **Duplicated lectures inflate counts.** `lecture-dp` syncs several lectures verbatim
  from `lecture-python.myst`, so their findings appear twice in the corpus totals. This is
  disclosed in `details.md` but not corrected for; deciding whether to de-duplicate is a
  scoping question for the next pass.

---

## 7. Design notes worth preserving

- **Why the evidence layer came first.** Every defect found in the previous pass was a
  bookkeeping failure, not a taste failure — arithmetic, coverage, a hallucinated file.
  Those are exactly the failures a program does not make, and they were consuming the
  credibility that the judgment calls needed.
- **Why scores are derived rather than asserted.** The rubric already defines the overall
  score as a mean and the priority bucket as a threshold rule. Anything that *defines* a
  number should compute it; asking a reviewer to also arrive at it by hand only creates a
  second opinion to reconcile.
- **Why the trend is reported on rule reach, not on scores.** Reach is a count of
  lectures matching a fixed program, so it is comparable across passes by construction.
  Score levels depend on the scoring function, so a change to that function would show up
  as a spurious trend. Both are recorded, but reach is the honest headline.
- **Why bare `align` is reported differently from `align` inside `$$`.** They fail
  differently — one is a nested math environment that breaks a PDF build, the other is a
  supported MyST form that merely departs from the corpus convention. Collapsing them is
  what produced a headline finding that did not survive checking.
- **Why Tier 3 waits on Tier 2 being used.** Dashboards become maintenance burdens.
  Prove the use case on the familiar stack first.
