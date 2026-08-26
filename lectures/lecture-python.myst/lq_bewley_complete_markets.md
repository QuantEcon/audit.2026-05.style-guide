# lq_bewley_complete_markets

- **Series:** lecture-python.myst
- **File:** `lectures/lq_bewley_complete_markets.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-005` ×3; `qe-writing-002` ×2; `qe-writing-003` ×1, +1 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×3; `qe-fig-004` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 2. *Lines:* 180, 409. *Example:* `c[:, t+1]` (180) and `c_inc[:, t+1]` (409) omit the spaces around `+` that the same expression carries everywhere else in the file - `mean_c[t + 1]` (293), `c[:, t + 1]` (488), `c_inc[:, t + 1]` (540, 594) - and line 180 sits in the same cell as `np.zeros((N, T_sim + 1))` at 175.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 299, 414. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 305, 311, 421, 429. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 481, 531, 584. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 218, 146. *Example:* line 218 is a 48-word sentence carrying three separate claims (the unit root, the absence of a stationary distribution, and the two initial-draw conventions used in the simulation) and is the only sentence in the lecture that does not fit the one-idea-per-paragraph rhythm the rest of the file keeps; separately, the definition $h = (1-\beta)\check{G}(I-\beta\check{A})^{-1}\check{C}$ is restated verbatim three times (96, 146, 230) when the later two could cite it.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 211, 379, 437. *Example:* bold marks emphasis rather than a definition: **idiosyncratic** at 211 is the second, non-defining use of a term already introduced at 139; **time-invariant** at 379 emphasises a property; and the note at 437 bolds **complete markets** / **incomplete markets** for contrast although both were defined earlier. The lecture italicises emphasis correctly elsewhere (*ex ante* 128, *variance* 261, *constant* 354, *not* 369, *rank* 565), so this is internal inconsistency rather than an unknown convention.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 130, 149, 437. *Example:* 2 spaces.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 389. *Example:* caption of 8 words.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 446. *Example:* line 446 - 'The optimal robust rule takes the same form as the rule above, but under a distorted model of the income process' - refers to a rule 'above' that does not exist in this lecture; it describes the robust rule of lq_robust_bewley, which the reader has not seen, so the paragraph reads as a conclusion drawn from absent material.


## Strengths

- All three figure-producing cells in the body carry full `mystnb: figure: caption/name` metadata (160-166, 266-272, 389-395), so every figure a reader meets in the narrative is captioned and cross-referenceable; the three qe-fig-005 hits are confined to the exercise solutions.
- Equations are referred to only through `` {eq} `` labels, never by number, and the references are dense enough to hold the argument together - eq:pi-crep is recalled at 125 and 143, eq:varspread at 261 and again in the exercise at 456, and eq:kernel with eq:cmdebt are both cited at 375-376 where the verification step needs them.
- The simulations verify the analytics rather than merely decorating them: the theoretical variance path $t\cdot h h^\top$ is overlaid on the simulated one (184-189), and the Bewley market-clearing claim is checked by tracking the cross-section mean online across 10,000 agents (284-294).
- All three exercises use gated `exercise-start`/`exercise-end` with `solution-start :class: dropdown`, and each solution closes with a paragraph of economic interpretation (503-505, 554-556, 612-614) rather than stopping at the plot.
- The lecture states its place in the four-lecture LQ permanent-income sequence up front with `` {doc} `` links (42, 50, 52) and returns to them at the close (442-444), so a reader always knows what has been assumed and what comes next.

## Recommended actions

1. Delete the four `.set_title` calls (305, 311, 421, 429) - each of those cells already has a mystnb caption, so the title is duplicated inside the image (qe-fig-003, 4 occurrences).
2. Add `mystnb: figure: caption/name` metadata to the three solution-cell figures (481, 531, 584) so the exercise figures match the body figures (qe-fig-005, 3 occurrences).
3. Split line 218 into two sentences - one for why the permanent component has no stationary distribution, one for the initial draws used in the simulation - and replace the second and third restatements of $h$ (146, 230) with a reference to `` {eq}`eq:pi-crep` ``.
4. Repair the mid-sentence line breaks that leave orphan words at the start of a paragraph (252 'The', 255-256, 263 'Initial', 213-214, 220-221) and delete the whitespace-only line at 258; the source currently wraps in the middle of clauses although every paragraph is a single sentence.
5. Rewrite line 446 so it does not appeal to 'the rule above' - either state that the robust rule is derived in lq_robust_bewley, or drop the sentence.
6. Change the three emphasis-bolds to italic (211, 379, 437), fix the double space in the caption at 393 and the three narrative double spaces at 130, 149, 437 (qe-writing-008, 3 occurrences).
7. Drop `figsize=(12, 4)` at 299 and 414 unless the two-panel aspect ratio is deliberate (qe-fig-001, 2 occurrences), shorten the 8-word caption at 389 (qe-fig-004), and space the `t+1` indices at 180 and 409.
