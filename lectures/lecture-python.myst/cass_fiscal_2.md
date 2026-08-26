# cass_fiscal_2

- **Series:** lecture-python.myst
- **File:** `lectures/cass_fiscal_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×2; `qe-writing-003` ×3; `qe-writing-002` ×3, +3 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×4; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×6; `qe-fig-005` ×3; `qe-fig-008` ×2, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 351, 358, 364, 374, 380, 387. *Example:* .set_title.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 44, 79. *Example:* H2 Title Case: 'A Two-Country Cass-Koopmans Model' (Two-Country, Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 8. *Lines:* 18, 22, 65, 394, 588. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 142, 335, 348, 519. *Example:* 35 code lines carry trailing whitespace (142, 145, 147, 149, 157, 158, 192, 216, 284, 289-302, 309, 322, 333, 353, 360, 366, 368, 370, 372, 376, 383, 401, 512, 520, 526, 527, 570); every axes index omits the space after the comma - `axes[0,0]`, `axes[1,2]` and so on across 33 lines (348-388, 574-580); line 335-336 continues an expression with a backslash and then starts the continuation with `*(1+τc[:-1])` at the same indent as the assignment, where parentheses and a leading space would be PEP8; and the continuation lines at 368-373 and 520-522 are indented to a column that does not match their opening bracket, with `init_glob, tol=1e-12` at 522 lined up under the lambda's arguments rather than under `root(`'s.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['mpmath'].
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 441, 503, 569. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 577, 578. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 83. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 18, 127, 482. *Example:* line 18 is a 45-word sentence that uses the phrase "this QuantEcon lecture" twice and chains two cross-references, a model class and a shock type into one span; lines 121-127 make the same point twice ("We can set holdings of foreign capital equal to zero in each country if we allow $B_t^f$ to be nonzero" at 123, then "Therefore, we set holdings of foreign capital equal to zero in both countries while allowing international lending" at 127); line 482 is a 42-word sentence carrying the timing of the opening, the no-arbitrage link, the direction of the saving response and its effect on the foreign return.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 225, 401, 497. *Example:* the H4 at line 497 reads "Experiment 2: A foreseen increase in $g$ from 0.2 to 0.4 at t=10", which is a verbatim copy of the Experiment 1 heading at 433 - the experiment is actually a capital-tax increase, as the prose at 499 and the `'τ_k'` shock at 508 both say. The production function `f` and its derivative `f_prime` are not defined until 401-411, after the five functions that call them (`Bf_path` at 150, `Bf_ss` at 159, `compute_euler` at 221, `compute_residuals_global` at 305, `plot_global_results` indirectly), so the reader meets $f(k_t)$ in code four times before learning it is Cobb-Douglas. And the three-line H3 at 225-229 is followed immediately by an H3 at 231 on the same subject.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 51, 348. *Example:* the model's structure - two countries, goods and claims traded but not labour, one bilateral IOU $B^f_t$, capital taxed at the rate of the jurisdiction where it sits (51-53, 81-87) - is exactly the kind of thing a two-box-and-arrows diagram settles in one glance, and there is none. Separately the three figures cannot be read on their own: `plot_global_results` (322-391) passes no `label=` to any of its eighteen `plot` calls and never calls `ax.legend()`, so the domestic/foreign distinction lives only in the prose at 439 ("blue lines represent the domestic economy and orange dotted lines represent the foreign economy"), which is stated once and never repeated for the figures at 503-531 and 569-584.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 329. *Example:* figsize=.


## Strengths

- The Euler equation is implemented once and reused for both countries (216-222), with the prose at 213 saying explicitly why that works - "they have the same form but use different variables" - rather than duplicating the function with starred arguments.
- Every steady-state condition gets its own equation label and is then cited by name: `` {eq}`eq:steady_k_bar` ``, `` {eq}`eq:steady_k_star` ``, `` {eq}`eq:steady_c_k_bar` `` and `` {eq}`eq:steady_c_kB` `` are all defined at 237-253 and 255 reads two of them back as "feasibility" and "trade balance".
- The economics of Experiment 1 is narrated as a causal chain in eight short paragraphs (476-494) - announcement, consumption smoothing, extra saving, the open-economy alternative to domestic capital, no-arbitrage synchronisation, capital build-up, drawdown, current-account deficit - one step per paragraph.
- The portfolio-indeterminacy problem is not swept aside: 121-127 states that domestic capital, foreign capital and loans bear the same return, that portfolios are therefore indeterminate, and that setting foreign capital holdings to zero is a *choice* made to reduce the number of initial conditions.
- The exercise at 556-562 asks the reader to swap one panel of an existing figure and reproduce a published figure from `` {cite}`Ljungqvist2012` ``, and the solution reuses `plot_global_results` and `compute_η_path` rather than rebuilding the plot.

## Recommended actions

1. Fix the Experiment 2 heading at line 497 - it currently duplicates Experiment 1's heading and describes the wrong shock.
2. Move the eight embedded matplotlib titles out of `plot_global_results` (351, 358, 364, 374, 380, 387) and the two in the solution (580) into figure captions (qe-fig-003, 6 occurrences), and add `label=` plus `ax.legend()` so the domestic/foreign encoding is in the figure rather than in one sentence of prose.
3. Delete the unused imports at 36-37 and the precision settings at 40-41: `mp`, `mpf` and `warn` are never referenced anywhere in the file, and removing `mpmath` also removes the only non-Anaconda dependency (qe-code-003).
4. Move `f` and `f_prime` (401-411) above their first caller at 150, and cut the restatement at 394 - line 65 already says the technology is Cobb-Douglas with identical parameters in both countries.
5. Reconcile the two production functions: `f`/`f_prime` take their own `A=1` default (401, 407) while `compute_steady_state_global` uses `model.A` (266); both are 1.0 at present, so a change to `model.A` would silently be honoured in one place and ignored in the other.
6. Add `mystnb: figure: caption/name` metadata to the three code-cell figures at 441, 503 and 569 (qe-fig-005, 3 occurrences), drop the `figsize=` override at 329 (qe-fig-001), and set `lw=2` on the two calls at 577-578 (qe-fig-008, 2 occurrences).
7. Sweep the whitespace and casing: sentence-case the H2s at 44 and 79 (qe-writing-006, 2 occurrences), collapse the eight double spaces at 18, 22, 65, 394 and 588 (qe-writing-008, 8 occurrences), split the two-sentence paragraph at 83 (qe-writing-001), strip the 35 trailing-whitespace code lines, and fix "As in our in the one-country model" at 394.
