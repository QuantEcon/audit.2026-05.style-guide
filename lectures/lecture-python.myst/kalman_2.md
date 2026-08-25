# kalman_2

- **Series:** lecture-python.myst
- **File:** `lectures/kalman_2.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-002` ×5; `qe-writing-005` ×3; `qe-writing-003` ×3, +2 more. |
| Math         | 7.5/10 | `qe-math-002` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×5; `qe-fig-004` ×7; `qe-fig-008` ×6, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 179, 211, 297, 535, 566. *Example:* fifteen lines inside code cells consist of whitespace only (PEP8 W293: 179, 189, 193, 268, 347, 350, 357, 364, 502, 509, 517, 521, 540, 544, 634), and 51 lines in the file carry trailing whitespace overall; 211 and 624 write `np.zeros((2,2))` with no space after the comma (E231) where the rest of the file writes `(2, 2)`; 297, 463 and 546 under-indent continuation lines relative to the opening bracket (E128), so `linestyle='dashed'` sits left of `color='grey'`; 535 has a space before the colon in `if diff :` (E203); and 566-567 write `4+2*i` unspaced in both the call and the label.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 64, 65, 339, 563, 587, 620, 653. *Example:* style override.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 293, 301, 354, 459, 467. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 7. *Lines:* 281, 324, 426, 554, 580, 613, 645. *Example:* caption of 9 words.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 290, 296, 456, 462, 536, 545. *Example:* plot() without lw=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 246, 249, 252. *Example:* apostrophe transpose `G'`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 41, 220, 277, 399, 607. *Example:* 41 is a 45-word sentence with three coordinated clauses; 607 is 52 words and carries the mechanism, the stability caveat and the conclusion together; 220 and 277 are both 36 words. 275-279 says the same thing twice - "We also plot $\mathbb{E}[u_0 | y^{t-1}]$, which is the firm's inference about a worker's hard-wired work ethic" at 277 and "We can watch how the firm updates its inference $\mathbb{E}[u_0 | y^{t-1}]$ about the worker's work ethic" at 279. The largest instance is 399: "Another way to accomplish the same goal is to use the following code" introduces a second 22-line cell (401-422) that does exactly what 378-397 already did, so the reader reads two recipes for one two-line task.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 16. *Lines:* 33, 35, 36, 99, 103, 111, 123, 200, 222, 223, …. *Example:* 2 spaces.

### Medium severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 232, 308, 672. *Example:* 232 says "Let's code that up now" and is followed not by code but by three display equations and eleven lines of prose (234-254) before the first cell at 256; "## Some computational experiments" at 308 then runs 363 lines to the end of the lecture with six figures, four code recipes and no subheading of any kind, so the table of contents gives the reader no map of the second half; and "## Future extensions" (672-675) is a two-line section that says enlightening experiments are possible and names none, which leaves the lecture without a conclusion.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 105, 225, 277. *Example:* the file bolds exactly one term, **innovation** at 242, and uses scare quotes where the others are coined: a worker's "type" is introduced in quotes at 105 and used again in quotes at 111 even though $(h_0, u_0)$ is the object the whole lecture is about; "innovation representation" appears in quotes at 225 and unquoted as a heading at 227; and hard-wired "work ethic" is introduced in quotes at 277 and then used bare at 301, 552, 574 and 578. Quotation marks read as hedging - the terms are the lecture's own vocabulary and want bold.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 74. *Example:* the model at 74-93 is a three-equation chain in which effort drives human capital which drives observed output, with noise entering at two different points, and the whole point of the lecture is which of those arrows exists - 489-491 turns on $\beta \neq 0$ and $g \neq 0$, and 607 on the composite $g\beta/(1-\alpha)$. That is a four-box diagram ($u_0 \to h_t \to y_t$, with $c\epsilon_{t+1}$ into $h$ and $v_t$ into $y$, and the firm's information set drawn around $y$ only), and the lecture instead asks the reader to assemble it from a display equation and a six-item bullet list. It is the one structural picture missing from a lecture with six figures.


## Strengths

- Every one of the six figures carries `mystnb: figure: caption` and `name` metadata (281, 324, 426, 554, 580, 613, 645) - unusual completeness, and it means each experiment in the second half is separately citable.
- The timing convention inside the filter loops is spelled out in the comments at 263, 269, 443, 449, 526 and 532 - `kalman.x_hat` is recorded as the belief about $x_t$ given $y^{t-1}$ *before* `kalman.update(y[t])` is called - which is precisely the off-by-one that is easiest to get wrong with QuantEcon.py's `Kalman` class.
- The two roles of $\Sigma_0$ are kept apart and the reason is stated: 220 explains that `Sigma_0=np.zeros((2,2))` pins one particular worker's true $(h_0, u_0)$ in the simulation while the firm still filters from its non-degenerate prior, and `simulate_workers` carries that distinction in its parameter names (`Σ_sim_0` against `Σ_prior`, 498-511).
- The innovations representation separates the two gains that most treatments run together: $K_t = A \Sigma_t G' (G \Sigma_t G' + R)^{-1} = A L_t$ at 249, with $L_t$ named at 252 as the filtering gain, and 244 explains why the composite gain appears when $\hat x_t$ conditions on $y^{t-1}$ rather than $y^t$.
- The learning-speed differences in `fig-kalman2-three` are explained rather than left for the reader to notice: 489-491 gives the conditions under which $u_0$ is learnable at all, and 605-609 attributes the observed ordering to $\beta$ through the steady-state gain $g\beta/(1-\alpha)$, naming $R$, $c$ and the prior variances as the other determinants.
- `simulate_workers` produces both the gap plot and the level plot from one code path through its `diff` switch, and in the level branch the dashed true-$u_0$ line is colour-matched to each worker's own curve (546), so three workers can share one axis without ambiguity.

## Recommended actions

1. Delete `mpl.rcParams['text.usetex'] = True` and the `text.latex.preamble` line (64-65). They make every figure in the lecture depend on a working TeX installation in the build image, for labels that matplotlib's own mathtext renders unaided - this is the one change here with build consequences.
2. Replace the three apostrophe transposes with `^\top` (246, 249, 252) - the only qe-math-002 hits in the file and the only place its otherwise clean matrix notation slips.
3. Move the five `set_title` calls (293, 301, 354, 459, 467) into the figure captions those cells already have, and trim the seven captions flagged at 281, 324, 426, 554, 580, 613 and 645 to the caption convention; then add `lw=2` to the six line plots (290, 296, 456, 462, 536, 545).
4. Cut the duplicated code: delete either 378-397 or 401-422, which do the same thing, and replace the 18-line plotting block at 454-471 - a verbatim copy of 288-305 - with a call to `simulate_workers`, which was written for exactly this.
5. Give "## Some computational experiments" (308) subsections; as it stands one H2 covers 363 lines and six experiments. Then either fill in "## Future extensions" (672) with two or three named experiments or remove it and end on the result at 670.
6. Strip the trailing whitespace on 51 lines, including the 15 whitespace-only lines inside code cells, and close the 16 double spaces (33, 35, 36, 99, 103, 111, 123, 200, 222, 223 and 6 more).
7. Add the $u_0 \to h_t \to y_t$ diagram described above, bold the coined terms at 105, 225 and 277 instead of quoting them, and replace the plain-TeX `\cr` line breaks with `\\` inside the four `aligned` blocks (139-141, 148-152, 158-161, 236-238).
