# imp_sample

- **Series:** lecture-python.myst
- **File:** `lectures/imp_sample.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 6.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-002` ×5; `qe-writing-005` ×3; `qe-writing-003` ×3, +2 more. |
| Math         | 4/10  | `qe-math-010` (proposed) ×7; `qe-math-001` ×3; `qe-math-009` ×38. |
| Code         | 7.5/10 | `qe-code-002` ×9. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-003` ×1; `qe-fig-004` ×1; `qe-fig-001` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 9. *Lines:* 48, 101, 104, 221, 274, 275, 534, 536, 538. *Example:* spelled-out `beta`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 38. *Lines:* 31, 58, 61, 68, 71, 74, 76, 80, 147, 151, …. *Example:* `\left(\omega\right)` is used in place of plain `(\omega)` on 38 lines - `\ell \left(\omega_t\right)`, `f\left(\omega\right)`, `L\left(\omega^t\right)` - where the argument is a single symbol and the delimiters have nothing to size themselves to. It roughly doubles the length of every expression in the file, and it is not even self-consistent: line 196 writes `\ell\left(\omega\right)` and `\ell(\omega)` in the same display, and line 501 does the same with `\frac{g(\omega)}{f(\omega)}` against `\frac{g\left(\omega_i^f\right)}{f\left(\omega_i^f\right)}`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 7. *Lines:* 74, 76, 155, 231, 300, 318, 494. *Example:* bare expectation `E \left[`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 27, 82, 155, 157, 484. *Example:* line 155 is a 52-word sentence chaining four steps of the Monte Carlo procedure ("would repeatedly draw ... form the product ... for each such sequence, then average these products across independently drawn sequences") and reads as a paragraph compressed into one line; 157 is 45 words and pads with "in order to do a good job of approximating"; 27 is 41 words with a parenthetical aside plus a trailing relative clause; 484 is 48 words carrying three separate claims (the median falls, the variance is infinite, a different seed moves the mean); and 82 has its adverbs in the wrong place - "makes it difficult efficiently and accurately to estimate the mean".
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 27. *Lines:* 25, 31, 68, 76, 82, 157, 173, 183, 193, 201, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 432. *Example:* .set_title.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 3. *Lines:* 484. *Example:* unicode `μ` inside a math environment.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 233, 488, 545. *Example:* line 233 says "our plan is to draw sequences $\omega^t$ from $q$" and 238 puts $p$ and $q$ into a display equation, but neither symbol is introduced until 252 ("given any beta distributions $p$, $q$") - the reader has to guess that $p$ generalises $g$ and $q$ generalises $h$; the two section headings "## Selecting a sampling distribution" (199) and "## Choosing a sampling distribution" (488) are near-synonyms 289 lines apart, so the table of contents gives no hint which is which; and 545-559 introduces $h_1$, $h_2$ and $h_3$ after the figure at 523-543 has already plotted and labelled all three.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 165, 339, 571. *Example:* 165 italicises the term being named ("a _change of distribution_ called **importance sampling**") where the rule asks for bold on a definition; 339 and 571 use bold for pure emphasis - "has **infinite variance**" and "diverges at **both** endpoints" - which the rule reserves for italic.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 424. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 460. *Example:* Title Case caption (Carlo).
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 66. *Example:* i.i.d..


## Strengths

- Every one of the seven figures carries `mystnb: figure: caption` and `name` metadata, and the prose actually uses them: 147 and 149 refer to `fig-imp-densities` and `fig-imp-likelihood-ratio` by `{numref}` rather than saying "the figure above".
- The lecture does not stop at simulation - 339-355 proves that the Monte Carlo estimator has infinite variance, 563-567 turns that into a finite-variance criterion, and the criterion then correctly predicts before the fact that $h_1$ and $h_2$ work while $h_3$ fails (569-573), so the histograms at 589 and 608 confirm a stated theory instead of being reported bare.
- Density-case discipline is exact throughout: $f$, $g$, $h$, $p$, $q$ are all lowercase for densities, matching proposed qe-math-015 (proposed), with no uppercase letter ever pressed into service as a density.
- The log scale at 138 is justified in the prose immediately after it (144-145), and both tail behaviours of the likelihood ratio are given explicit rates - $\omega^{-2}$ at the left edge, $(1-\omega)^{-1/5}$ at the right (149, 153).
- `plot_estimates` is written once and reused for all three importance distributions (470, 589, 608), and the Monte Carlo baseline `mc` is computed once at 456 and shared across the three figures rather than recomputed.

## Recommended actions

1. Add braces to the seven bare expectation operators - `E \left[` -> `\mathbb{E}` at 74, 76, 155, 231, 300, 318, 494 - and to the `${E}`/`\hat{E}` variants at 175, 231, 381, 403; this is the largest single fix in the lecture (qe-math-010 (proposed), proposed).
2. Strip the 38 `\left(...\right)` wrappers around single-symbol arguments listed above; the equations at 196, 245 and 501 shorten by roughly half and stop contradicting themselves.
3. Introduce $p$ and $q$ before line 233 - one sentence saying that $p$ is the data-generating density and $q$ the sampling density, so the general estimator at 238-245 can be read on first pass - and rename one of the two "...ing a sampling distribution" headings (199, 488).
4. Close the 27 repeated spaces (qe-writing-008; 25, 31, 68, 76, 82, 157, 173, 183, 193, 201 and 17 more) - they cluster in exactly the passages that are hardest to read.
5. Replace the unicode Greek inside math with LaTeX: `$μ_L$` (430), `$\hat{μ}$` and `$\hat{σ}^2$` (444, 484) -> `\mu`, `\sigma` (qe-math-001); and write "IID" at 66 instead of "i.i.d." (qe-writing-009 (proposed), proposed).
6. Move `ax.set_title(f'$T$={T}')` at 432 into the panel caption or drop it, since `fig-imp-estimates` already has a caption; keep the `figsize` at 424 - unlike the usual case it scales with `n_rows` for the 2x2 grid and is doing real work.
7. Switch the emphasis at 339 and 571 to italic, bold "change of distribution" at 165, and write `$T=1$` rather than bare `T=1` in the prose at 381 and 498.
