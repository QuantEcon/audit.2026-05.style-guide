# Style Audit — scipy

- **Series:** lecture-python-programming
- **File:** `lectures/scipy.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10| Heavily Title Case section headings. |
| Math         | 7.5/10| Clean overall; `\mathbb E` without braces (lines 461, 560) is the only nit. |
| Code         | 9/10  | `!pip install --upgrade quantecon` at top with `hide-output`; Greek unicode (μ, σ, β) used throughout per qe-code-002; `qe.Timer(unit="milliseconds")` used for benchmarking (qe-code-004); PEP8 clean. |
| JAX          | out of scope | — |
| Figures      | 8/10  | One code-generated plot uses `ax.set_xlabel('$x$', fontsize=12)` / `set_ylabel('$f(x)$', fontsize=12)` (lines 221-222) — math-mode labels per qe-fig-006; no embedded titles; no `figsize`. |
| References   | N/A   | No citations. |
| Links        | 9/10  | External docs links only; no improper cross-series URLs. |
| Admonitions  | 8/10  | Three `{exercise-start}` and three `{exercise}` (sp_ex02, sp_ex03, sp_ex1) — non-gated bodies are prose-only. Four `{solution-start}` use `:class: dropdown` and `:label:` per qe-admon-005. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 63 `## SciPy versus NumPy`, line 94 `## Statistics`, line 105 `### Random Variables and Distributions`, line 167 `### Alternative Syntax`, line 183 `### Other Goodies in scipy.stats`, line 200 `## Roots and Fixed Points`, line 231 `### Bisection`, line 288 `### The Newton-Raphson Method`, line 315 `### Hybrid Methods`, line 350 `### Multivariate Root-Finding`, line 359 `### Fixed Points`, line 377 `## Optimization`, line 401 `### Multivariate Optimization`, line 412 `## Integration`, line 442 `## Linear Algebra`, line 455 `## Exercises`. *Count:* 16 occurrences.

### Medium severity
- **[qe-fig-005]** — The single code-generated figure (line 218-225) lacks `name:` metadata.

### Low severity
- **[qe-math-010 (proposed)]** — `\mathbb E` without braces in display math at lines 461, 560.
- **[qe-admon-001]** — Three exercises use bare `{exercise}` rather than gated syntax; bodies are prose-only.

## Strengths
- Lecture title "SciPy" follows qe-writing-006.
- Equation labels (`betadist2`, `root_f`) and `{eq}` references used per qe-math-013 (proposed).
- Bold for definitions per qe-writing-005 ("**root** or **zero**").
- Sequences/sets use proper bracketing; lowercase `f` for density per qe-math-015 (proposed).
- No bold vectors, no `^T`, no `*` for multiplication, no `\tag`, no `align` inside `$$`.
- `qe.Timer(unit="milliseconds")` used for benchmarking per qe-code-004.
- Greek unicode (μ, σ, β) used in code per qe-code-002.
- `!pip install --upgrade quantecon` at top with `hide-output` per qe-code-003.

## Recommended actions
1. Convert section headings to sentence case ("SciPy versus NumPy", "Statistics", "Random variables and distributions", "Alternative syntax", "Other goodies in `scipy.stats`", "Roots and fixed points", "Bisection", "The Newton-Raphson method", "Hybrid methods", "Multivariate root-finding", "Fixed points", "Optimization", "Multivariate optimization", "Integration", "Linear algebra").
2. Normalize `\mathbb E` → `\mathbb{E}`.
3. Optionally promote bare `{exercise}` blocks to gated `{exercise-start}` / `{exercise-end}` for uniformity.
