# scipy

- **Series:** lecture-python-programming
- **File:** `lectures/scipy.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×8; `qe-writing-001` ×2; `qe-writing-005` ×2, +4 more. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×2. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×4; `qe-fig-008` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 461, 560. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 105, 167, 183, 200, 315, 350, 359, 401. *Example:* H3 Title Case: 'Random Variables and Distributions' (Variables, Distributions).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 215, 521, 580, 628. *Example:* `f = lambda x: np.sin(4 * (x - 1/4)) + x + x**20 - 1` binds a lambda to a name where PEP8 asks for a `def` (215, and again in the exercise solution at 628) - and this is the lecture's central test function, referenced by `` {eq}`root_f` `` throughout; trailing whitespace after `y_grid = g(x_grid)` (521) and `P = β**n * np.mean(return_draws)` (580).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 130, 173, 214, 511. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 219, 524. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 457, 482. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 65, 471. *Example:* line 65 opens '## SciPy versus NumPy' by restating the Overview's first sentence - 'SciPy is a package that contains various tools that are built on top of NumPy' against 'SciPy builds on top of NumPy to provide common tools for scientific programming' (43) - so the comparison section spends its opening on a repetition; and 471 is a 38-word sentence that names Amazon and the strike price $K$ twice each ('if the call option is to buy stock in Amazon at strike price $K$, the owner has the right (but not the obligation) to buy 1 share in Amazon at price $K$ after $n$ days').
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 350, 401, 442. *Example:* three consecutive sections deliver a heading and a documentation link and nothing else, breaking the demonstrate-then-explain pattern the rest of the lecture keeps: '### Multivariate Root-Finding' is two sentences ending in 'See the documentation for details' (350-357); '### Multivariate Optimization' lists nine function names and does the same (401-410); '## Linear Algebra' says SciPy has a `linalg` module too and leaves the reader to investigate (442-453), with no code at all. Every other section in the lecture runs an example.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 236, 322. *Example:* 'A **root** or **zero** of a real function' (202) and 'A **fixed point** of a real function' (361) set the convention, and then two more terms are introduced in italics instead: 'One of the most common algorithms for numerical root-finding is *bisection*' (236) and 'most default algorithms ... use *hybrid* methods' (322), the latter the term its own section heading is named after (315).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 434, 458, 482. *Example:* 2 spaces.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 309. *Example:* 'But other initial conditions lead to failure of convergence' (309) is demonstrated only by the number that `newton(f, 0.7)` happens to print (311-313). Newton-Raphson failure is the most visual result in the section - the tangent at 0.7 sends the next iterate off the interval - and the lecture already has the plot of $f$ (214-225) to draw it on. The neighbouring bisection subsection gets an intuition (the guess-the-number game, 238-247); this one gets a bare output.


## Strengths

- The speed comparison uses the `qe.Timer` context manager (341-348) rather than `%timeit` or `time.time()`, so qe-code-004 and qe-code-005 have nothing to report.
- `quantecon` is installed in the first code cell with `:tags: [hide-output]` (28-32) and the imports follow immediately at 36-39.
- Bisection is motivated by the guess-the-number game (238-247) before any code appears, and the homemade `bisect` is labelled `(bisect_func)` (253) and then genuinely re-used by exercise sp_ex1 (595).
- `` {eq}`root_f` `` is cited three times (272, 280, 597), so the same function carries the whole root-finding discussion instead of a new example per method.
- Density and CDF discipline is exact: lowercase $f$ for the beta density (119) and the lognormal density (482, 485, 491), `q.cdf` and `q.ppf` for the distribution and quantile functions (147, 151) - proposed qe-math-015 (proposed) holds.

## Recommended actions

1. Lower-case the 8 Title Case headings (105, 167, 183, 200, 315, 350, 359, 401) - qe-writing-006, 8 occurrences and the largest routine fix.
2. Add braces to the two blackboard expectations: `\mathbb E` -> `\mathbb{E}` at 461 and 560 (qe-math-010, proposed, 2 occurrences).
3. Give the three stub sections (350, 401, 442) one runnable example each, or fold them into the Overview's list of subpackages - as they stand a reader hits three headings in a row that deliver only a link.
4. Plot the Newton-Raphson failure at 309 on the existing figure of $f$: the divergent step is the reason the method needs a hybrid fallback, and the next section (315) assumes the reader has seen it.
5. Turn the two named lambdas into `def f(x)` (215, 628) and strip the trailing whitespace at 521 and 580.
6. Fix the small defects: `{P:3f}` -> `{P:.3f}` at 581 (545 gets it right), the `1./2./2./3.` numbering at 466-469, the exercise labels that jump from `sp_ex03` to `sp_ex1` (591), and the equation label `betadist2` (117), which is never cited.
7. Add `:name:`/caption metadata to the four code-cell figures (130, 173, 214, 511) and `lw=2` at 219 and 524 (qe-fig-005, qe-fig-008), and move `import matplotlib.pyplot as plt` (132) up to the import cell at 36.
