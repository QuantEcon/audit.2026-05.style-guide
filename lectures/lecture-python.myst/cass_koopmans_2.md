# cass_koopmans_2

- **Series:** lecture-python.myst
- **File:** `lectures/cass_koopmans_2.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×13; `qe-writing-005` ×5; `qe-writing-003` ×3, +3 more. |
| Math         | 9.5/10 | `qe-math-009` ×1. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×2; `qe-fig-008` ×4, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7/10  | `qe-link-002` ×2; `qe-link-001` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 50, 61, 188, 306, 663. *Example:* line 50 writes the trick's name as `A **Big** $K$ **, little** $k$ trick`, so the bold spans break around the inline math and end up bolding the comma; the same construction is repeated at 425. The other four are bold used for emphasis, not definition: **prices** at 61, **single** at 188 and again at 357, **equilibrium** at 306, and `**Normalization:**` at 663 used as a heading.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 13. *Lines:* 75, 127, 134, 180, 221, 241, 318, 404, 414, 502, …. *Example:* H2 Title Case: 'Review of Cass-Koopmans Model' (Model).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 61. *Lines:* 29, 30, 37, 39, 45, 56, 63, 136, 138, 163, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 704, 737, 856. *Example:* line 704 writes `if γ!= 1` with no space before the operator; line 737 opens a docstring with four quotes (`''''`), so its first character is a stray apostrophe; lines 856 and 894 both bind `fix, axs = plt.subplots(...)` - a typo for `fig`, and the name is never used. `def r(pp, t0, q_path)` at 969 also takes two parameters it never reads.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 856, 894, 976. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 872, 908, 984, 987. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 853, 890. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 871, 907, 983, 986. *Example:* plot() without lw=.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 2. *Lines:* 52, 426. *Example:* full URL to own series (python.quantecon.org).
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 53, 427. *Example:* raw link to python-advanced.quantecon.org.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 29, 211, 263. *Example:* the phrase "this lecture `` {doc}`Cass-Koopmans Planning Model <cass_koopmans_1>` ``" - "this lecture" naming a *different* lecture - is used seven times (29, 129, 139, 416, 553, 671, 823), where "the previous lecture" or just the `{doc}` link would read correctly. Line 211 is not a sentence: "Because  is a **relative price**. the unit of account  in terms of which the prices $q^0_t$ are stated is; we are free to re-normalize them..." - it has no subject, a full stop in the middle and a trailing "is;". Line 263 reads "because we it  displays constant returns to scale".
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 632, 648, 995. *Example:* lines 632 and 641 are the same sentence twice ("If we plug `` {eq}`eq-pl` `` into `` {eq}`Zero-profits` `` for all t, we get" / "If we now plug...") but derive two different results, and the first should point at the *capital* zero-profit condition at 245-247, which carries no label at all - only the labour condition at 251-255 is labelled `Zero-profits`. Line 648 says the wage result "is exactly `` {eq}`eq-pr4` ``", but `eq-pr4` (459-463) is the household's capital-choice function $k^*_t(\vec q, \vec w, \vec \eta)$; the wage guess is `eq-price2`. And the lecture stops at line 999 immediately after "Now we plot when $t_0=20$" - the two yield-curve figures at 990-999 get no interpretation and there is no closing section, where the sibling lecture ends with "## Concluding Remarks".
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 180, 871. *Example:* sections "Market Structure", "Firm Problem" and "Household Problem" (180-402) describe a circular flow in words - the household owns labour and capital and rents both to the firm, the firm sells output back to the household, and all trades happen once in a single grand market just before date 0 (400-402) - and there is no diagram of it, in a lecture whose whole point is the correspondence between that structure and the planner's. Separately the six-panel figure at 853-879 plots four horizons with no `label=` and no legend, so nothing identifies which curve is $T=250$ and which is $T=50$; the very next figure (890-916) plots four values of $\gamma$ with `label=fr'$\gamma = {γ}$'` and `axs[0, 0].legend()`, so the fix is already in the file.

### Low severity
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 516. *Example:* the household's Lagrangian is written $\mathcal{L}(\vec c, \vec k, \lambda)$ at 516 and 523; the letter $L$ is otherwise unused in this lecture, so the calligraphic form buys no disambiguation, and the sibling lecture writes the same kind of object as a plain $L$ (cass_koopmans_1:128).


## Strengths

- The verification is done term by term and each step names the planning-problem condition it reproduces: `` {eq}`cond1` `` plus the price guess gives "which is `` {eq}`constraint1` ``" (561), `` {eq}`cond2` `` gives `` {eq}`constraint2` `` (585), `` {eq}`cond3` `` gives `` {eq}`constraint3` `` (607), `` {eq}`cond4` `` gives `` {eq}`constraint4` `` (621) - the reader can check the correspondence claim one line at a time.
- The guess-and-verify strategy is stated as four explicit operations (432-435) before any algebra: derive both sets of first-order conditions, substitute the planning allocation into them, solve for prices, then check the allocations coincide.
- Euler's theorem on homogeneous functions is derived rather than cited (259-298), and the no-arbitrage argument is then run in both directions - what a firm would do if the marginal product exceeded the rental rate (300-307) and if it fell short (312-313).
- The units of every price are stated explicitly (379-383): the wage in time-$t$ goods per unit of time-$t$ labour, the rental in time-$t$ goods per unit of capital, and $q^0_t$ in numeraire per time-$t$ good - which is what makes the normalisation discussion at 657-665 meaningful.
- The curvature experiment (882-926) varies $\gamma$ with $T$ held fixed and reads the result back in terms of the economics (higher $\gamma$ means more smoothing means slower convergence), rather than leaving four overlaid curves to speak for themselves.

## Recommended actions

1. Resolve the eight `{eq}` references to labels that exist only in `` {doc}`cass_koopmans_1` `` - `utility-functional` and `allocation` at 130, and `constraint1`-`constraint4` at 553, 561, 585, 607 and 621; the displays at 102-104 and 121-123 in this file carry no labels, so as written these are broken cross-references in the argument the lecture is built on.
2. Fix the mis-referenced and mis-typed mathematics: `{eq}`eq-pr4`` at 648 should be `eq-price2`; the first of the two identical sentences at 632 and 641 should cite the capital zero-profit condition, which needs a label at 245-247; `\frac{\partial \tilde k_t}{\partial \tilde k_t}` at 312 should be $\partial F/\partial \tilde k_t$; `\vec{\eta)}` at 462 has its brace and paren transposed; `q_0^{T+1}` at 549 has the base year and the date swapped; and 645 uses $\tilde K_t$ and $\tilde L_t$ where the lecture's variables are $\tilde k_t$ and $\tilde n_t$.
3. Sentence-case the thirteen Title Case headings at 75, 127, 134, 180, 221, 241, 318, 404, 414, 502, 511, 627, 882 and 928 (qe-writing-006, 13 occurrences) and collapse the 61 double spaces (qe-writing-008, 61 occurrences).
4. Rewrite line 211, which is currently not a sentence, and fix the typos at 263 ("we it"), 504 ("firsts"), 674 ("the characterize"), 825 ("equilibium") and 573 (`u'>0` written outside math delimiters).
5. Add `label=` and a legend to the six-panel figure at 853-879 so the four horizons are identifiable, and move the ten embedded titles out of `ax.set(title=...)` at 872, 908, 984 and 987 into figure captions (qe-fig-003, 4 occurrences).
6. Convert the four raw URLs to cross-references: `python.quantecon.org/rational_expectations.html` at 52 and 426 should be markdown links within this series (qe-link-001, 2 occurrences) and `python-advanced.quantecon.org/dyn_stack.html` at 53 and 427 should be `{doc}` references (qe-link-002, 2 occurrences).
7. Normalise the code cells to `ipython3` - ten cells are declared `{code-cell} python3` and one `{code-cell} ipython` (68) - then drop the three `figsize=` overrides at 856, 894 and 976 (qe-fig-001, 3 occurrences), add figure metadata at 853 and 890 (qe-fig-005, 2 occurrences), set `lw=2` on the four plot calls at 871, 907, 983 and 986 (qe-fig-008, 4 occurrences), and fix `γ!= 1` (704), the four-quote docstring (737) and the `fix`/`fig` typo (856, 894).
