# Style Audit — python_oop

- **Series:** lecture-python-programming
- **File:** `lectures/python_oop.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Heading Title Case. |
| Math         | 6/10  | `\mathbf{1}` indicator violates qe-math-003/qe-math-004; otherwise clean. |
| Code         | 9/10  | Only Anaconda packages (numpy, matplotlib, scipy); Greek unicode (α, β, δ) used per qe-code-002; PEP8 clean. |
| JAX          | out of scope | — |
| Figures      | 7/10  | One `figsize=(9, 6)` at line 444 (qe-fig-001); no embedded titles (`set_xlabel`/`set_ylabel` used with lowercase or math-mode labels per qe-fig-006); no code-generated figure has `name:` metadata. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `` {doc}`earlier lecture <oop_intro>` `` correctly per qe-link-001. |
| Admonitions  | 9/10  | Two `{exercise-start}` / `{solution-start}` pairs gated; `:class: dropdown` and `:label:` cross-linked per qe-admon-005. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 64 `## OOP Review`, line 75 `### Key Concepts`, line 126 `### Why is OOP Useful?`, line 146 `## Defining Your Own Classes`, line 199 `### Example: A Consumer Class`, line 353 `### Example: The Solow Growth Model`, line 460 `### Example: A Market`, line 595 `### Example: Chaos`, line 695 `## Special Methods`, line 747 `## Exercises`. *Count:* 10 occurrences.

### Medium severity
- **[qe-math-008]** — Indicator function uses bold `\mathbf{1}` rather than blackboard `\mathbb{1}`, and the bold violates qe-math-004 (no bold for matrices/vectors). *Examples:* line 758 `\sum_{i=1}^n \mathbf{1}\{X_i \leq x\}`; line 762 narrative reference. *Count:* 2 occurrences.

### Low severity
- **[qe-fig-001]** — One `figsize=(9, 6)` at line 444 — borderline; the subplot serves the Solow time-series comparison.
- **[qe-fig-005]** — Code-generated figures (bifurcation, time series, market) lack `name:` metadata.

## Strengths
- Lecture title "OOP II: Building Classes" follows qe-writing-006.
- Equation labels and `{eq}` references used correctly (`solow_lom` at line 364; `{eq}` refs at lines 377, 384, 385) per qe-math-013 (proposed).
- Sequences use curly brackets correctly (`$\{X_i\}_{i=1}^n$` line 753) per qe-math-005.
- "IID" used correctly per qe-writing-009 (proposed) (line 765).
- Bold for definitions per qe-writing-005 ("**class definitions**", "**bundled together**", "**steady state**").
- Greek unicode (α, β, δ) used in code per qe-code-002.
- All axis labels lowercase or math-mode per qe-fig-006 (e.g., `'$t$'`, `'quantity'`, `'price'`, `'$r$'`, `'$x_t$'`).
- Exercise/solution structure fully compliant per qe-admon-001/qe-admon-002/qe-admon-005.

## Recommended actions
1. Convert section headings to sentence case ("OOP review", "Key concepts", "Why is OOP useful?", "Defining your own classes", "Example: a consumer class", "Example: the Solow growth model", "Example: a market", "Example: chaos", "Special methods").
2. Replace `\mathbf{1}` indicator with `\mathbb{1}` per qe-math-003 (and remove the bold per qe-math-004); add a short explanation per qe-math-008.
3. Remove the `figsize=(9, 6)` on line 444 unless justified.
