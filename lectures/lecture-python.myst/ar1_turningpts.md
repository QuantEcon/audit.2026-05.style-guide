# ar1_turningpts

- **Series:** lecture-python.myst
- **File:** `lectures/ar1_turningpts.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×7; `qe-writing-001` ×3; `qe-writing-005` ×3, +4 more. |
| Math         | 7.5/10 | `qe-math-011` (proposed) ×2; `qe-math-009` ×2. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×1; `qe-fig-001` ×4; `qe-fig-008` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 74, 357, 435, 452, 517, 619, 685. *Example:* H2 Title Case: 'A Univariate First-Order Autoregressive Process' (Univariate, First-Order, Autoregressive, Process).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 204, 315, 545, 659. *Example:* the code cells carry PEP8 whitespace problems on four distinct patterns: 29 lines have trailing whitespace (204, 210, 213, 247, 257, 269, 293, 299, 303, 311, 534, 542, 547, 550, 552, 559, 561, 569, 571, 572, 585, 594, 659, 662, 668, 670, 731, 744, 746); ten closing brackets are indented to the continuation column rather than to the opening line or its indent (315, 322, 325, 329, 541, 546, 551, 587, 702, 710); five lines exceed 79 characters (324, 540, 545, 550, 560); and the tuple unpacking at 659-661 and 731-733 under-indents its continuation line relative to the open paren.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 70, 674, 749, 769. *Example:* style override.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 92, 98. *Example:* `{\mathcal N}` is used for the normal distribution at 92 and 98 - the only decorated symbols in the file - where the sibling lecture `` {doc}`ar1_bayes` ``, modelling exactly the same process, writes a plain `N`; the calligraphic form buys nothing here and makes the two lectures disagree on notation for the same object.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 2. *Lines:* 92, 98. *Example:* decorated distribution `{\mathcal N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 119, 182, 515. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 117, 383, 515, 760. *Example:* line 117 ("Predictive distribution `` {eq}`ar1-tp-eq3` `` assumes that parameters $(\rho,\sigma)$ are known") restates line 101-102 ("The predictive distribution `` {eq}`ar1-tp-eq3` `` assumes that the parameters $\rho, \sigma$ are known") almost word for word, sixteen lines later; line 383 opens "By Wecker's definition, period $t$ is a turning point" with no stated hypothesis, so the clause asserts something unconditionally that is only true under the case at 376; the second sentence of 515 runs to 40 words covering both columns of the trace figure; line 760 is a 37-word sentence whose object is tangled ("we plot both the original Wecker method and the extended method with parameter values drawn from the posterior together").
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 355, 447. *Example:* line 355 is a one-line tangent to an unrelated lecture ("the coverage intervals have shapes like those described in `` {doc}`perm_income_cons` ``"), with no explanation of the connection and no closing period, dropped between a figure and a new H2; and the algorithm stated at 435-449 does not describe the code that follows - it asks for $W_t(\omega_i), W_{t+1}(\omega_i), \dots, W_{t+N}$ per path and treats each date's set as a separate predictive distribution, whereas `compute_path_statistics` (529-588) returns one scalar per path (the *first* occurrence), and nothing bridges the two.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 365, 385, 391. *Example:* the same term is set in italic in one place and bold in another: *time until the next turning point* is italic at 365 and 371 but bold at 385; *turning point* is italic at 391 but bold at 402 and 367. In the other direction, *stopping time* at 385 is a term being defined and is set in italic where the rule asks for bold.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 104, 121. *Example:* 2 spaces.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 51. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 317. *Example:* plot() without lw=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 374. *Example:* the whole of "Predictive Distributions of Path Properties" (357-433) defines five path statistics - $Z_t$, $W_t$, $M_t$, $T_t$, $P_t$ - purely as chains of inequalities between consecutive $Y$ values, i.e. purely as *shapes* of a sample path, and there is no figure; a single simulated path with a recession, a severe recession and a positive and a negative turn marked on it would make all five definitions readable at a glance, and the lecture already has the machinery to draw it.


## Strengths

- Four of the five figures already carry `mystnb: figure: caption/name` metadata (336, 462, 623, 692, 762) - the only lecture in this batch that does this by default rather than as an exception.
- The comparison figure at 762-775 overlays the two methods on the same axes rather than presenting them as two separate figures the reader must hold in mind, and the prose at 777-783 states the direction of the difference (extended is more dispersed) and its cause.
- `create_ar1` (173-179) validates $|\rho| < 1$ and $\sigma > 0$ and raises with a message naming the restriction, so the stationarity assumption stated at line 84 is enforced rather than assumed.
- The lecture states its two sources of uncertainty at the outset (29-31) and the conclusion (785-795) closes on exactly those two, with the final sentence naming the cost of ignoring the second.
- The choice of the conditioning assumption is justified rather than inherited: line 460 says why it is right *here* ($y_0 = 10$ is atypical) and points at `` {doc}`ar1_bayes` `` for the argument.

## Recommended actions

1. Sentence-case the seven Title Case H2s at 74, 357, 435, 452, 517, 619 and 685 - e.g. `## A univariate first-order autoregressive process` (qe-writing-006, 7 occurrences, the largest mechanical item here).
2. Reconcile the algorithm at 435-449 with the code at 527-588: either compute the statistic at every date $t, \dots, t+N$ as the algorithm says, or restate the algorithm as "compute the first occurrence per path", which is what the code does.
3. Add a figure to the path-properties section showing one simulated path with a recession, a severe recession and both kinds of turning point marked - the definitions at 374-423 are all about path shape and currently have no picture.
4. Replace `{\mathcal N}` with `N` at 92 and 98 to match `` {doc}`ar1_bayes` ``, and rename the two overloaded capitals: $N$ is at once the negative-turning-point indicator (429), the simulated path length (441) and the number of paths in the code (`N=1000`, 630, 700), while $T$ is at once the turning-point indicator $T_t$ (407) and the path lengths $T_0$, $T_1$ (130-132).
5. Drop the four `figsize=` overrides at 70, 674, 749 and 769 and the `sns.set_style('white')` at 70 (qe-fig-001, 4 occurrences), add figure metadata to the imports-adjacent cell at 51 (qe-fig-005), and set `lw=2` at 317 (qe-fig-008).
6. Replace the two `for n in range(N)` loops with `.at[n].set(...)` (657-667, 725-739) by a `jax.vmap` over `compute_path_statistics` - the lecture already uses `vmap` at 259 and `lax.scan` at 212 and 560, so 2000 single-element scatter updates are out of character and slow.
7. Strip the 29 trailing-whitespace code lines, wrap the five over-length lines (324, 540, 545, 550, 560), rename the builtin-shadowing `vars` at 298, split the three two-sentence paragraphs at 119, 182 and 515, collapse the double spaces at 104 and 121, and delete the stray trailing `\` at line 92 inside the display math.
