# classical_filtering

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/classical_filtering.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-001` ×2; `qe-writing-005` ×3; `qe-writing-002` ×3, +4 more. |
| Math         | 3.5/10 | `qe-math-002` ×17; `qe-math-003` ×5. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 17. *Lines:* 77, 113, 119, 129, 429, 430, 982, 983, 989, 1001, …. *Example:* \prime transpose.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 5. *Lines:* 371, 444, 461, 484, 491. *Example:* matrix environment.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 40. *Lines:* 27, 39, 59, 81, 87, 93, 106, 107, 122, 132, …. *Example:* 2 spaces.

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 43. *Example:* raw link to python-intro.quantecon.org.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 602, 724. *Example:* {cite} in narrative flow: 'in {cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 52, 938. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 210, 240, 384. *Example:* line 210-212 is a 44-word sentence that names both halves of an orthogonal decomposition, the space each lies in, and defines "orthogonal complement" on the way past; 240-241 is 38 words of forward reference before the point of the example arrives; 384-388 is 41 words with the covariance-stationarity qualification nested inside the claim it qualifies.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 973. *Example:* mid-sentence 'Prediction'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 767, 907, 973. *Example:* bold is used as a substitute for a heading or a directive in three places - `**Proposition**` at 767 (which should be a `{prf:proposition}`), `**Blaschke factors**` at 907 (a subsection in all but markup), and `**Multivariable Prediction:**` at 973 (an exercise title) - none of the three is a definition or an emphasis, which is what the rule reserves bold and italic for.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 278, 390, 909. *Example:* 1047 lines with no figure at all, and three passages that ask for one: line 278 and 286 tell the reader to "notice how the lower rows ... are converging" in the raw `print(Li)` / `print(L)` output of 281-291; lines 390-401 state the central convergence result (bottom rows of $L^{-1}$ tend to the Wold moving-average coefficients) without plotting a single coefficient sequence; and the Blaschke-factor section at 909-930 turns entirely on which zeros lie inside the unit circle, which is a picture of the complex plane.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 312. *Example:* Example 2 (294-341) says "We proceed in the same way as in example 1" and then fires five code cells in a row (314, 324, 328, 333, 338) with no prose between any of them, dropping the step-by-step narration that made Example 1 readable at 255, 267-271, 278 and 286; line 335 silently switches to `Li[-3:, :]` and never says that the last three rows are the point.


## Strengths

- `\mathbb{E}` is written with braces in all 40 places it appears, and the conditional-expectation operator is consistently the distinct `\mathbb{\hat E}` - the notation for expectation never wobbles across 1047 lines.
- Duality between LQ control and least-squares prediction is set up as the organising idea in the Overview (32-48) and then actually used: the finite-dimensional prediction formula {eq}`eq_58` is reused to represent the solution of the control problem at 378 and again in the combined section at 417.
- Labelled equations are genuinely cross-referenced rather than decorative - `eq_36` is cited forward at 241 and 309, `eq_54`/`eq_55` back at 380-382, `eq_57` at 210, `onetwenty` at 994.
- The relationship to the companion lecture is stated in the first line with a `{doc}` reference to `lu_tricks` (25) and the shared implementation is loaded from it rather than duplicated (225).
- The two problem statements the whole lecture serves - the linear least squares prediction problem (548) and filtering problem (555) - are bolded at exactly the point they are defined, each with its own minimand written out.

## Recommended actions

1. Replace `^\prime` with `^\top` throughout - 22 occurrences starting at 77, 113, 119, 129, 408, 409, 429, 430, 470, 982 - the single largest mechanical fix in this file (qe-math-002).
2. Fix the orthogonal decomposition at 210-212: both parts are written `\sum^{t-1}_{j=m} L^{-1}_{t,t-j}\varepsilon_{t-j}`, but per {eq}`eq_57` the component orthogonal to the span of $[x_{t-m}, \ldots, x_1]$ is $\sum_{j=0}^{m-1}$; as written the sentence says a term is orthogonal to its own span (and "knowns as" at 212 is a typo for "known as").
3. Correct the exercise statement at 954: `\mathbb{E} \widehat X_{t+1} \mid X_t, \ldots` puts the hat on $X$ instead of on $\mathbb{E}$ and drops the brackets round the conditioning set; line 961 has the same missing brackets - both should read `\mathbb{\hat E}\left[X_{t+2} \mid X_t, X_{t-1}, \ldots\right]` as the body of the lecture writes it (e.g. 1032).
4. Add the three figures the argument is missing: the Wold coefficient sequences from the bottom rows of $L^{-1}$ as $T$ grows (near 291 and 340), and a unit-circle plot of $\pi(z)$'s zeros before and after root flipping (near 917) - the Blaschke section is the one part of the lecture with no computational counterpart at all.
5. Convert the five `\begin{matrix}` / `\begin{array}` blocks at 371, 444, 461, 484 and 491 to `bmatrix` and drop the hand-written `\left[ \right]` delimiters around them (qe-math-003, 5 occurrences).
6. Collapse the 40 double spaces (27, 39, 59, 81, 87, 93, 106, 107, 122, 132 and 30 more) - they are dense enough to be a source-formatting habit rather than isolated slips (qe-writing-008); while there, replace the raw links at 43 with `{doc}` references (qe-link-002, 3 on that one line), move the four narrative `{cite}` calls at 345, 602, 724 and 1007 out of the sentence flow (qe-ref-001), lower-case `Prediction` at 973 (qe-writing-004), split the two-sentence paragraphs at 52 and 938 (qe-writing-001), and swap the legacy `\hbox` at 310 for `\text`.
7. Give the two exercises at 934 and 968 gated `{solution-start}` / `{solution-end}` blocks - both currently end at `{exercise-end}` with no solution anywhere in the file, which is the only place in the lecture where the reader is left without a check.
