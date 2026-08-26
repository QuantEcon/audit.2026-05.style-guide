# sympy

- **Series:** lecture-python-programming
- **File:** `lectures/sympy.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×3; `qe-writing-005` ×2; `qe-writing-003` ×2, +1 more. |
| Math         | 8/10  | `qe-math-001` ×4. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 10/10 | no mechanical violations detected. |
| References   | N/A   | no citations in this lecture. |
| Links        | 8/10  | `qe-link-002` ×3. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 45, 371, 515. *Example:* H2 Title Case: 'Getting Started' (Started).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 50, 264, 364, 488. *Example:* `from sympy import *` (50) is the wildcard import PEP8 rules out, and it is what lets `E`, `density` and `cdf` (53) shadow other names and what hides that `reduce_rational_inequalities` (52) is never used while `reduce_inequalities` (249) - which arrives through the wildcard - is; spaces around `=` in keyword arguments, `Symbol("λ", positive = True)` (364) and `legend = True, show = False` (488, 492); and continuation lines that do not align with their opening parenthesis (264-266, 491-492, 505-506, 599-600).
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 3. *Lines:* 200, 313, 664. *Example:* raw link to python.quantecon.org.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 4. *Lines:* 671, 678. *Example:* unicode `θ` inside a math environment.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 282, 292, 442. *Example:* the bank-deposit example is described in a time index that never appears in its mathematics: 'Imagine a bank with $D_0$ as the deposit at time $t$' (282) - $D_0$ is the deposit at time 0 - and 'Let's compute the deposits at time $t$' (292), where the sum at 288-290 and the code at 297-298 run over $i$ to infinity with no $t$ in them. At 442 the exponential CDF is called a 'cumulative density function', conflating the two objects the section is distinguishing.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 416, 439. *Example:* the lecture silently rebinds its symbols across cells with different assumptions - `λ` at 327 (`symbols('lambda')`), 364 (`Symbol("λ", positive=True)`) and 416 (`Symbol('lambda', positive=True)`), and `x` at 263, 330, 417, 537 and 688 - with no note that a reader running cells out of order gets different objects; that habit is exactly what lets the stale `r` in the exercise solution at 690 pass unnoticed. Then 439 presents `E(X**t)` as the `Stats`-module counterpart of the moment-generating function computed by `integrate(exp(t*x) * pdf, ...)` at 424, but $E[X^t]$ is not $E[e^{tX}]$, so the two cells answer different questions under one sentence of setup (428).
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 72, 552. *Example:* the lecture uses no bold or italic anywhere, so its two definitional sentences carry no marking: 'Symbols are the basic units for symbolic computation in SymPy' (72), which defines the central object of the lecture, and 'a point is Pareto efficient when the allocation is optimal for one person given the allocation for the other person' (552), which the code at 561-565 then implements.

### Low severity
_None found._


## Strengths

- Every symbolic result is checked against something the reader can verify independently: the Solow fixed point is derived with pen and paper first (216-220) and then re-derived by `solve` (236-241), and the geometric-series result is matched against the money-multiplier example in the intro lectures (313).
- Both probability examples are done twice - the Poisson expectation by an explicit `Sum` (342-354) and then by `sympy.stats.E` (363-368), the exponential moment by `integrate` (424) and then by `moment` (435) - so the reader sees what the convenience function is doing.
- Density and PMF case discipline is right throughout: lowercase $f$ for the Poisson PMF (323), the exponential density (412) and the binomial PMF (671), which is what proposed qe-math-015 (proposed) asks for.
- The plotting section escalates deliberately - one curve (476-481), a customised two-curve figure with labels (485-496), implicit functions and an inequality region (500-507), then a 3-D surface (511-513).
- The contract-curve application closes by asking the reader to weigh a NumPy implementation against the symbolic one (605-608), which is the honest comparison for a lecture about symbolic algebra.

## Recommended actions

1. Fix the bug in the MLE solution: `factorial(n-r)` at 690 should be `factorial(n-x)`. `r` is the reserve ratio left over from the bank example at 296, so the cell runs and silently prints the wrong binomial coefficient - and everything downstream (695-711) inherits it.
2. Replace `from sympy import *` (50) with explicit imports: it is what makes `E`, `density` and `cdf` (53) shadow other names, and it conceals both the unused import at 52 and the undefined-looking `reduce_inequalities` at 249.
3. Lower-case the three Title Case H2s (45, 371, 515) - qe-writing-006, 3 occurrences.
4. Convert the three raw `quantecon.org` URLs to `{doc}` references (200, 313, 664) - qe-link-002, 3 occurrences.
5. Write `\theta` inside the math at 671 and 678 instead of the Unicode θ (qe-math-001, 4 occurrences); the rest of the lecture already writes `\alpha`, `\beta` and `\lambda` in math and keeps Unicode for the code.
6. Say what the bank example measures: $D_0$ is the deposit at time 0 (282) and 292 computes the discounted stock over an infinite horizon, not 'the deposits at time $t$'; and call the CDF a cumulative distribution function at 442.
7. Stop rebinding `λ` and `x` with different assumptions from cell to cell (327, 364, 416; 263, 330, 417, 537, 688), and separate `E(X**t)` (439) from the moment-generating function at 424.
