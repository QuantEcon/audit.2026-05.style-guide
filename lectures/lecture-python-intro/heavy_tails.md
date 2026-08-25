# heavy_tails

- **Series:** lecture-python-intro
- **File:** `lectures/heavy_tails.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-001` ×4; `qe-writing-005` ×2; `qe-writing-003` ×1, +1 more. |
| Math         | 5.5/10 | `qe-math-010` (proposed) ×23. |
| Code         | 6.5/10 | `qe-code-001` ×7; `qe-code-002` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×4; `qe-fig-005` ×4; `qe-fig-004` ×3, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 9/10  | `qe-link-001` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 551, 552, 571, 572, 679, 760, 765. *Example:* PEP8 spacing/naming slips in otherwise clean code: a space after the unary minus in `np.exp(- alpha * x)` and `x**(- alpha)` (551-552, 571-572), whitespace before the closing paren from a dangling comma in `sm.qqplot(data, line='45', ax=ax, )` (679), a lambda bound to a name instead of a `def` in `pdf = lambda x: np.interp(...)` (760), and a missing space after the operator in `y_vals[i] = 1- j` (765).
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 8. *Lines:* 354, 627, 675, 829, 857, 886, 934, 1224. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 13. *Lines:* 95, 123, 205, 237, 363, 370, 417, 474, 551, 552, …. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 23. *Lines:* 431, 491, 528, 529, 530, 694, 702, 958, 964, 967, …. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 6. *Lines:* 161, 1021, 1036, 1037, 1293. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 551, 552, 571, 572. *Example:* spelled-out `alpha`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 365, 372, 680, 789. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 3. *Lines:* 193, 225, 871. *Example:* Title Case caption (Amazon).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 665, 673, 1216, 1374. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 161, 1021, 1120, 1292. *Example:* 3 sentences in one paragraph.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 710, 1118. *Example:* emphasis re-applied to terms already defined: **Pareto tail** and **tail index** are bolded at 707 and bolded again three lines later at 710 in a sentence that restates 707; **light-tailed** is bolded at 1116 and again at 1118.

### Low severity
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 1. *Lines:* 649. *Example:* full URL to own series (intro.quantecon.org).
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 1062. *Example:* "we saw above that if every $X_i$ is Cauchy, then so is $Y_n$" points backwards, but the stability of the Cauchy under averaging is not established anywhere above - it is derived only in exercise `ht_ex_cauchy` at line 1410ff, 350 lines later.


## Strengths

- Every labelled equation is actually cited: `pareto` (428) at 1272 and 1308, `plrt` (699) at 1176, `lln_cch` (1415) at 1445 - no orphan labels and no manual "equation (3)" references.
- Probability events are written with braces throughout - `\mathbb P\{X > x\}`, `\mathbb P\{\bar X_n \to \mu\}` - so the proposed qe-math-014 (proposed) convention is already satisfied even though \mathbb P is missing its braces.
- Density/CDF case discipline is consistent: lowercase $f$ for the density (67, 1094), uppercase $F$ for the CDF and $G$, $\hat G$ for the counter-CDF (488, 593).
- All four exercises use the gated `exercise` / `solution-start` / `solution-end` form with `:class: dropdown`, and `{numref}` is used to point back at a generated figure (1202).
- Writes "IID" in the correct form at line 956 rather than "i.i.d.".

## Recommended actions

1. Add braces to every blackboard operator - `\mathbb P` -> `\mathbb{P}`, `\mathbb E` -> `\mathbb{E}`, `\mathbb R` -> `\mathbb{R}`, `\mathbb 1` -> `\mathbb{1}` - 23 occurrences and the single largest fix in this lecture (qe-math-010 (proposed), proposed).
2. Replace spelled-out Greek names in code with Unicode letters (`alpha` -> `α` and similar), 23 occurrences; the exercise solutions at 1337-1368 already do this, so make the earlier cells match them.
3. Set `lw=2` on the 13 line plots that currently take the matplotlib default, and drop the 8 hand-set `figsize=` arguments unless a specific aspect ratio is needed.
4. Move the four `ax.set_title(...)` calls (365, 372, 680, 789) out of the code and into mystnb figure captions, and add `mystnb: figure: caption/name` metadata to the two Q-Q plot cells at 665 and 673 so they can be cross-referenced.
5. Fix the PEP8 spacing noted above: `np.exp(-alpha * x)`, `x**(-alpha)`, drop the dangling comma at 679, turn the lambda at 760 into a `def`, and space the operator at 765.
6. Replace the hard-coded `https://intro.quantecon.org/heavy_tails.html#...` self-link at 649 with a `{ref}` to the in-page label, and lower-case the Title Case figure captions at 193, 225, 562, 871.
7. Repair the forward reference at 1062 - either state the Cauchy-stability result where it is first used or point at the exercise with `{ref}` - and delete the redundant re-bolded sentence at 710.
