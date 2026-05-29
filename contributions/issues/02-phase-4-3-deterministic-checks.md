## Summary

Phase 4.3 in the [roadmap](https://github.com/QuantEcon/action-style-guide/blob/main/docs/developer/roadmap.md) (and section 2.C of [IMPROVEMENTS.md](https://github.com/QuantEcon/action-style-guide/blob/main/IMPROVEMENTS.md)) targets **~13 mechanical rules via regex** to remove hallucination risk and reduce per-rule LLM cost.

The recent [May 2026 lecture audit](https://github.com/QuantEcon/audit.2026-05.style-guide) (299 lectures across 5 series, 7 in-scope rule categories) generated rule-by-rule violation data that supports a more aggressive Phase 4.3 scope:

- **22 rules** can be fully or near-fully deterministic (vs ~13 currently estimated)
- The audit corpus provides **labelled regression test data** for every one of them
- Concrete prioritisation order is now possible, driven by corpus violation frequency
- **Six rules each have 60+ corpus violations** — extending Phase 4.3 to cover them would touch the majority of lectures in the corpus

This issue extends — not replaces — the existing Phase 4.3 plan.

## Comparison with current Phase 4.3 candidate list

The IMPROVEMENTS.md §2.C "high confidence" list:

- `qe-math-002` (transpose) — `^T` → `^\top`
- `qe-math-003` (matrix brackets) — `pmatrix` → `bmatrix`
- `qe-math-004` (no bold vectors) — `\mathbf` removal
- `qe-math-006` (aligned vs align) inside `$$`
- `qe-math-007` (no `\tag`)
- `qe-writing-008` (multiple spaces)
- `qe-fig-003` (`ax.set_title`/`suptitle`)

That's 7 explicit candidates plus an "approximately 15–20" estimate.

The audit-extended list adds eight more deterministic candidates (validated against the corpus), most with substantial violation counts:

| Rule | Corpus violations | Detection |
|------|-------------------|-----------|
| **`qe-code-002`** — Greek spelled out | **~150 / 299** | regex on identifiers in code cells |
| **`qe-fig-001`** — unnecessary `figsize=` | **~125 / 299** | regex on `figsize=` in `plt.subplots`/`plt.figure` |
| **`qe-fig-005`** — figures missing `:name:` field | **~120 / 299** | parse figure / image directive metadata |
| **`qe-link-002`** — raw `*.quantecon.org` URLs | **~60 / 299** | regex on hard-coded intersphinx URLs |
| **`qe-fig-006`** — Title Case axis labels | **~50 / 299** | regex on `set_xlabel`/`set_ylabel` case |
| `qe-fig-007` — removed matplotlib spines | ~30 / 299 | regex on `spines[*].set_visible(False)` |
| `qe-fig-008` — `lw=2` for line charts | low count, easy detection | AST on `plot()` calls |
| `qe-fig-010` — Plotly without `{only} latex` | low count, easy detection | detect plotly + check for directive |
| `qe-admon-003` — tick-count mismatch | **build-risk** | parse fence tick counts |
| `qe-admon-004` — missing `prf:` prefix | low count, easy detection | regex on proof-family directives |
| `qe-code-004` / `qe-code-005` — `time.time()`/`%timeit` | ~15 lectures combined | regex on timing patterns |

### Net-new rules from [#18 — Proposal: 7 new style rules](https://github.com/QuantEcon/action-style-guide/issues/18) (if accepted)

| Rule | Detection | Audit evidence |
|------|-----------|---------------|
| `qe-writing-009` (IID) | case-sensitive regex `\bi\.i\.d\.\b\|\biid\b` | ~30 lectures |
| `qe-math-010` (`\mathbb{P/E/V}`) | regex on bare `E[`, `E_t`, `\mathbb E` (no braces), `\Pr(`, `\Var(` | **~60 lectures** |
| `qe-math-011` (distribution naming) | regex on `\mathcal{N}`, `\{\cal N\}` for distributions | ~30 lectures |
| `qe-math-012` (`\cdot` not `*` in math) | regex `\*` inside `$…$` / `$$…$$` | small but clear |

## Full deterministic candidate list (22)

In priority order — based on audit-measured violation frequency × ease of implementation × build-risk severity:

### Tier 1 — Build-risk (1 occurrence is enough)

1. **`qe-math-006`** — `\begin{align}` inside `$$` (would break PDF builds). Found in [`lecture-python.myst/divergence_measures.md:134`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/divergence_measures.md#L134) during the audit.
2. **`qe-admon-003`** — Tick-count mismatch in nested directives (build-breaking).

### Tier 2 — Highest corpus impact (>100 lectures affected)

3. **`qe-writing-006`** — Title Case in H2+ headings (partial: needs proper-noun list). Affects **~170 / 299 lectures**. Single biggest corpus pattern. Could ship as Tier-2 partial-deterministic (curated proper-noun list maintained in the repo) with LLM fallback for unknown words.
4. **`qe-code-002`** — Greek letters spelled out (`alpha`, `beta`) in code instead of unicode. **~150 lectures**, mostly mixed within-file (would benefit from per-lecture normalisation).
5. **`qe-fig-001`** — Unnecessary `figsize=` overrides. **~125 lectures**, heavy in `lecture-python.myst` (75/110).
6. **`qe-fig-005`** — Figures missing `:name:` field for `numref` cross-referencing. **~120 lectures**.

### Tier 3 — Strong corpus impact (40–100 lectures)

7. **`qe-fig-003`** — Embedded matplotlib titles. ~90 lectures.
8. **`qe-link-002`** — Raw `*.quantecon.org` URLs instead of `{doc}` links. ~60 lectures.
9. **`qe-math-010`** (new rule) — Bare `E_t` for expectation. ~60 lectures.
10. **`qe-fig-006`** — Title Case axis labels. ~50 lectures.
11. **`qe-math-002`** — Prime / `^T` for transpose. ~46 lectures. Care needed: preserve derivative-prime (`u'`, `f'`) and next-period notation (`x'`).

### Tier 4 — Moderate (15–40 lectures)

12. **`qe-math-011`** (new rule) — `\mathcal{N}` for normal distribution. ~30 lectures.
13. **`qe-writing-009`** (new rule) — IID. ~30 lectures.
14. **`qe-fig-007`** — Removed matplotlib spines. ~30 lectures.
15. **`qe-ref-001`** — `{cite}` vs `{cite:t}` for author-name narrative citations. ~37 lectures plus **zero-`{cite:t}`-usage in 2 entire series**.
16. **`qe-code-003`** — Mid-lecture pip install. ~15 lectures.
17. **`qe-code-004`** / **`qe-code-005`** — `time.time()` / `%timeit`. ~15 lectures combined.

### Tier 5 — Pure regex, lower frequency

18. `qe-math-003` — pmatrix/matrix → bmatrix
19. `qe-math-004` — `\mathbf`/`\boldsymbol` removal on vectors
20. `qe-math-007` — `\tag{` detection
21. `qe-writing-008` — Multiple spaces between words
22. **`qe-math-012`** (new rule) — `*` in math

## Test data offer

The audit corpus contains **labelled violations per rule per lecture across 7 categories**. Per-series READMEs in the audit repo list which lectures violate which rules. For example, from [lecture-dp/README.md](https://quantecon.github.io/audit.2026-05.style-guide/lecture-dp/index.html):

> **`qe-fig-001`** — Unnecessary `figsize=` declarations. Heavy in `odu` (7×), `calvo` (5×), `career` (5×), `chang_ramsey` (5×), `lqcontrol` (5×), `mccall_q` (5×), `mccall_fitted_vfi` (5×)…

That gives a concrete labelled set: 7+ specific lectures known to violate `qe-fig-001` with occurrence counts. A deterministic regex for `qe-fig-001` can be validated against these exact files.

This can serve as:

- **Regression test corpus** — for each candidate regex, run on the lecture files of the audit repos and validate the regex flags the same lectures the audit flagged (and not others).
- **False-positive validation** — lectures *not* flagged by the audit should not trigger the regex.
- **Coverage target** — count of audit-flagged lectures the regex catches gives a precision/recall measurement.

A small companion can be added to action-style-guide's test suite that ingests the audit's per-series rankings as expected violations.

## What's being asked

1. Should Phase 4.3 scope be extended from ~13 to 22 rules, using the prioritisation above?
2. Is the team open to ingesting the audit corpus as a test-data dependency? Two possible shapes:
   - Reference the audit repo by commit SHA from tests
   - Vendor the audit's series-README data into `tests/fixtures/audits/2026-05/`
3. Should Tier 1 (build-risk) ship first as a one-off PR, separate from the larger Phase 4.3 effort?

## References

- **Audit data:** https://github.com/QuantEcon/audit.2026-05.style-guide
- **Cross-series synthesis (with corpus counts per rule):** https://quantecon.github.io/audit.2026-05.style-guide/intro.html
- **Audit spec § 9 (deterministic-check candidates):** https://quantecon.github.io/audit.2026-05.style-guide/spec.html
- **Existing Phase 4.3:** [`docs/developer/roadmap.md`](https://github.com/QuantEcon/action-style-guide/blob/main/docs/developer/roadmap.md), [`IMPROVEMENTS.md § 2.C`](https://github.com/QuantEcon/action-style-guide/blob/main/IMPROVEMENTS.md)
