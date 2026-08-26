# cagan_adaptive

- **Series:** lecture-python-intro
- **File:** `lectures/cagan_adaptive.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-002` ×9; `qe-writing-003` ×2; `qe-writing-008` ×32, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7/10  | `qe-code-001` ×12. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×4; `qe-fig-003` ×1; `qe-fig-008` ×12, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 12. *Lines:* 296, 298, 318, 323, 545, 546, 648, 698, 700, 714, …. *Example:* line 298 puts spaces around four keyword defaults and not the fifth (`α = 5, m0 = 1, Eπ0 = 0.5, T=80, λ = 0.9`) - PEP8 wants no spaces on any of them; line 296 indents the namedtuple continuation to column 24 where the visual-indent target is 28; line 318 spaces the same `*` two different ways in one expression (`(1-λ)*B @ C, (1-λ) * B @ μ_seq`); line 323 has a single space before an inline comment where two are required; lines 545, 546, 648, 698 and 700 pad `=` with two to five spaces to line assignments up in a column; lines 714-716 pad after a comma for the same reason.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 346, 347, 348, 349, 350, 351, 487, 564, 571, 651, …. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 9. *Lines:* 23, 25, 67, 388, 418, 434, 443, 445, 465. *Example:* nine sentences of 30-40 words. Lines 23 (40) and 25 (39) open the lecture with two chained clauses each; line 67 is a 32-word sentence that names three logarithms before reaching its verb; lines 388, 418, 434, 443, 445 and 465 each carry two ideas separated by 'namely', 'so by', or a trailing relative clause.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 32. *Lines:* 21, 25, 39, 41, 48, 49, 51, 52, 57, 64, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 345, 482, 563, 705. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 359. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 476, 544, 645, 697. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 469, 599. *Example:* the symbol rho is used at line 469 (exercise ca_ex1, part b: 'print rho') before it exists - the lecture body writes the same quantity only as an unnamed absolute-value expression at line 377 and never names it. Exercise ca_ex3 then states at line 599 that 'the lecture derives that ... pi_{t+1} = rho pi_t' and supplies the definition itself; the derivation at lines 382-386 stops one step short of that reduction and never makes it for constant mu.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 82. *Example:* `` {cite} `` in narrative flow: 'by `` {cite} ``'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 587. *Example:* line 587 uses bold for emphasis - 'the public systematically **over-predicts** inflation' - two lines after line 585 correctly uses italic for the same job ('falls *below* expected inflation').
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 372. *Example:* the stability section (lines 372-394) presents the condition |(lambda - alpha(1-lambda))/(1 - alpha(1-lambda))| < 1, a region in (lambda, alpha) space, and then just prints one number at line 393. Line 390 invites the reader to 'study outcomes in examples that violate condition' with nothing to look at; a plot of the stable region, or of rho against lambda for a few alpha, would carry the whole section.


## Strengths

- Every display equation carries a MyST label and every label is actually cited - eq:caganmd_ad, eq:eqfiscth1, eq:eqpipi, eq:adaptexpn, eq:eq1, eq:eq2, eq:eq4, eq:eq101_ad, eq:mcum_ad, eq:notre and eq:suffcond are all referenced from the surrounding text.
- The three matrix systems are written out in full bmatrix form (lines 101-121, 136-151, 215-231) before being abbreviated to A, B and C, so the reader can check the code at lines 312-314 line by line against the algebra.
- The four exercises go well past re-running with new parameters: they ask for the sensitivity of overshooting to lambda, the sign of the forecast error under each experiment, the empirical decay ratio checked against its analytical value, and fast-versus-slow learning - and each solution verifies the model numerically rather than asserting the answer.
- Code uses Unicode Greek throughout (alpha, lambda, mu, pi, phi, rho, Epi) and bundles parameters in a namedtuple, so the Python at lines 308-333 reads as a transcription of the matrix algebra above it.
- The relationship to cagan_ree is stated at the top (line 19), at the point where the expectations assumption is chosen (line 25), where the non-rational outcome appears (line 281), and at each experiment (lines 416, 432), so the pair of lectures can genuinely be read together.

## Recommended actions

1. Name rho in the lecture body - define it where condition eq:suffcond is introduced around line 377, and add the one step that takes the last line of the deduction at 384 to pi_{t+1} = rho pi_t when mu is constant. Three of the four exercises depend on both, and neither is currently in the lecture.
2. Split the 500-character `aligned` block at line 384 into one equation per source line and put a clause of connective text between the steps; as written it is a single unbroken source line and the reader is handed six chained substitutions with no narration.
3. Break the nine 30-40 word sentences at lines 23, 25, 67, 388, 418, 434, 443, 445 and 465 into one idea per sentence.
4. Remove the 32 double spaces flagged by qe-writing-008 (lines 21, 25, 39, 41, 48, 49, 51, 52, 57, 64 and 22 more) - they are scattered through the prose and make the source read as if it were assembled from fragments.
5. Add mystnb figure metadata to the five figure-producing cells at lines 338, 476, 544, 645 and 697 (qe-fig-005); drop the `figsize=`/`dpi=` overrides at 345, 482, 563 and 705 (qe-fig-001); and move the embedded titles set at line 359 into captions (qe-fig-003).
6. Set `lw=2` on the six `ax[i].plot` calls at lines 346-351 that draw the lecture's five main panels, and on the plot calls at 487, 564, 571, 651, 654 and 714 (qe-fig-008).
7. Fix the twelve PEP8 spacing sites listed above, replace the hard-coded 'Equation (14.8)' in the code comment at line 323 with an `{eq}` reference to eq:eq101_ad, and delete the leftover jupytext `+++ {"user_expressions": []}` markers at lines 303, 336 and 368.
