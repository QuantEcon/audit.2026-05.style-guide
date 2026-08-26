# bivariate_dist

- **Series:** lecture-python-intro
- **File:** `lectures/bivariate_dist.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-002` ×11; `qe-writing-003` ×1. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×15. |
| Code         | 6/10  | `qe-code-002` ×6; `qe-code-003` ×1; `qe-code-001` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×8; `qe-fig-006` ×2; `qe-fig-005` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 6. *Lines:* 488, 491, 493, 495. *Example:* spelled-out `sigma`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 172, 271, 311, 352, 490. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 8. *Lines:* 174, 177, 275, 313, 317, 355, 359, 497. *Example:* .set_title.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 15. *Lines:* 93, 195, 198, 377, 380, 384, 399, 464, 467, 470, …. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 11. *Lines:* 157, 161, 294, 296, 366, 382, 614, 616, 628, 630, …. *Example:* eleven single-sentence paragraphs run 35-44 words. The recurring mechanism is an em-dash clause bolted onto an already complete sentence: line 296 (44 words) states that neither marginal depends on rho, explains what correlation describes, then adds '--- the same lesson the discrete example taught us above'; lines 157, 161, 294, 366, 614, 616, 630 and 647 all follow the same three-clause shape. Each would read better as two paragraphs.

### Medium severity
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 798. *Example:* install cell at line 798 of 841 (not near the top).
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 829, 830. *Example:* axis label `Amazon monthly return (%)`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 312, 316. *Example:* plot() without lw=.

### Low severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 1. *Lines:* 337. *Example:* the continuation line at 337 is indented 34 spaces where the visual-indent target is 33 (the column after `pd.DataFrame(` on line 336), so the second argument does not line up under the first.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 818. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 391. *Example:* the note at lines 386-392 promises 'We will see an example of this below, in the discussion of the bivariate normal distribution' - an example of zero covariance without independence - but the bivariate normal discussion at lines 507-517 shows the opposite (for the bivariate normal, zero correlation IS equivalent to independence), and the counterexample at lines 552-620 is about normal marginals not implying joint normality, with a covariance that is not zero. The forward reference has no destination.


## Strengths

- Fourteen of the fifteen figures carry full mystnb metadata - both a `caption:` and a `name:` in the `fig:bivariate-*` namespace - which is the most consistent figure labelling in the series; only the exercise-solution cell at line 818 is missing it.
- Both proposed math conventions hold without exception: `\mathbb P` takes braces for events (`\mathbb P\{X = x, Y = y\}` at line 93, `\mathbb P\{(X,Y) \in A\}` at lines 195 and 198), and every density is lowercase (p, p_X, p_Y).
- Bold and italic never cross over: nine bolded defined terms (lines 30, 90, 146, 186, 204, 325, 374, 396, 628) and fourteen italicized emphases (157, 161, 296, 333, 420, 452, 476, 517, 523, 528, 594, 618) with no instance of bold doing an emphasis job.
- The 'word of caution' section (lines 552-620) earns its conclusion instead of asserting it: it constructs the counterexample, shows the marginal histograms look normal, shows skewness and kurtosis are near zero, and only then produces the X+Y histogram that gives the game away.
- The 3D surface at line 235 followed immediately by the contour plots at line 264 makes the contour representation legible - the reader sees the hill before being asked to read a topographic map of it.

## Recommended actions

1. Break the eleven 35-44 word sentences at lines 157, 161, 294, 296, 366, 382, 614, 616, 628, 630 and 647 into separate paragraphs; in almost every case the em-dash clause at the end is a second thought that can stand as its own sentence.
2. Remove the eight embedded matplotlib titles at lines 174, 177, 275, 313, 317, 355, 359 and 497 and move that information into the figure captions or panel legends (qe-fig-003, 8 occurrences).
3. Brace the blackboard-bold arguments throughout - `\mathbb P` to `\mathbb{P}`, `\mathbb E` to `\mathbb{E}`, `\mathbb V` to `\mathbb{V}`, `\mathbb R` to `\mathbb{R}` - at the 15 flagged sites starting at lines 93, 195, 198, 377, 380, 384, 399, 464, 467 and 470; line 754 already does it correctly, so the file is currently inconsistent with itself (qe-math-010 (proposed), proposed).
4. Either deliver the example promised in the note at line 391 - a pair with zero covariance that is not independent - or rewrite the pointer, since the section it points at proves the reverse.
5. Drop the `figsize=` overrides at lines 172, 271, 311, 352 and 490 (qe-fig-001), set `lw=2` on the two marginal-density plots at lines 312 and 316 (qe-fig-008), lowercase the axis labels at lines 829-830 (qe-fig-006), and add mystnb metadata to the solution figure at line 818 (qe-fig-005).
6. Rename the genuinely spelled-out Greek variables in the signal-and-noise cell - `sigma_U_vals` and `sigma_U` at lines 488, 491 and 493, and `rho` at line 495 - to Unicode forms; note that the other nine lines the scanner lists are matplotlib `alpha=` keywords and must not be touched (see scanner doubt).
7. Fix the continuation indent at line 337, wrap the 94-character `sns.heatmap` call at line 129, and move the `!pip install --upgrade yfinance` cell at line 801 up to the top of the lecture beside the other imports (qe-code-003).
