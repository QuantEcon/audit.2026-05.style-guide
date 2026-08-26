# fitting_distributions

- **Series:** lecture-python-intro
- **File:** `lectures/fitting_distributions.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10 | `qe-writing-005` ×2; `qe-writing-002` ×2; `qe-writing-003` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 786, 854. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 307, 589. *Example:* line 307-309 is a 41-word sentence with three clauses chained through a colon and a "so" ("The points curve away from the line, and the departure has a clear meaning: towards the right, ... so the data have a longer right tail than the normal distribution allows"), where the lecture's other sentences run to a single idea; lines 589-590 restate the third warning of 492-495 almost word for word ("it is only the best of the candidates we happened to try") rather than referring back to it the way line 649 refers to the second warning.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 243, 670. *Example:* two definitions set in italics in a lecture that bolds nine others: "They are called *plotting positions*" at 243 and "an additional parameter $\nu > 0$, called the *degrees of freedom*" at 670 - both are the "called X" pattern that **parametric class** (33), **method of moments** (84), **Q-Q plot** (202), **Kolmogorov-Smirnov statistic** (358) and **Student's t distributions** (668) all get bold for.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 497. *Example:* "We take up that point below" at 497 is answered by the "When the normal fails" section at 581, but the Count data section (500-578) is inserted between them - it introduces the Poisson class, a discrete data set and a new diagnostic, and belongs either before the three warnings or after they are resolved.


## Strengths

- Nine of the eleven figures carry full `mystnb: figure:` metadata with both a caption and a `name` (169, 271, 294, 322, 382, 457, 550, 612, 707), so the figures are nameable and cross-referenceable without further work.
- One `qq_plot` helper is defined at 253-263 and then applied to seven different samples (283, 301, 331, 619, 714, 793, 861) - the reader learns to read one kind of figure once and then reads it seven times, which is what makes the S-shape at 623 land.
- Case discipline on distribution functions is exact and matches the proposed qe-math-015 (proposed) convention: uppercase $F$, $F_n$, $F^{-1}$ for the CDF, ECDF and quantile function (237, 361, 372), with densities left to `u.pdf`; `\mathbb{E}` and `\mathbb{V}` are correctly braced at 109 and 111.
- The five `{note}` admonitions (240, 338, 415, 637, 732) park every caveat - alternative plotting positions, `sm.qqplot`, the KS-test trap, $D$ not being comparable across sample sizes, the unreliability of $\hat\nu$ - outside the argument instead of interrupting it.
- Failures are diagnosed rather than merely recorded: the S-shape at 623 motivates the t class at 668, and the earthquake exercise turns a failed exponential fit (797) into a variance-to-mean clustering diagnostic (818-826) that connects back to independence.

## Recommended actions

1. Add `mystnb: figure: caption/name` metadata to the two solution-cell figures at 786 and 854 - they are the only two of the lecture's eleven figures without it (qe-fig-005 x2).
2. Bold the two definitions currently in italics: **plotting positions** at 243 and **degrees of freedom** at 670.
3. Move the Count data section (500-578) so that it does not stand between the third warning at 492-497 and the section that resolves it at 581, or replace "We take up that point below" with a `{ref}` to `When the normal fails`.
4. Split the 41-word sentence at 307-309 into the observation and its interpretation, and replace the restatement at 589-590 with a back-reference in the style of line 649 ("This illustrates the second warning above").
5. Lift the `fits` dictionary out of the plotting cell at 175-177 into its own cell: it is the object that carries the three fitted classes to 443 and 467, and a reader who skims the figure cell loses it.
