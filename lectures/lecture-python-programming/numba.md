# numba

- **Series:** lecture-python-programming
- **File:** `lectures/numba.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title Case in H3/H4 headings throughout. |
| Math         | 8/10  | Clean math; `\mathbb E` without braces (lines 700, 739) is the only nit. |
| Code         | 9/10  | `!pip install quantecon` at top with `hide-output`; Greek unicode (α, β, μ, ρ, ν, σ, ξ, η) used throughout; `qe.Timer()` used for 8+ benchmark blocks (qe-code-004); PEP8 clean. |
| JAX          | out of scope | (Mentions JAX as a future direction.) |
| Figures      | 8/10  | Two code-generated plots use `ax.set_xlabel('$t$', fontsize=12)` / `ax.set_ylabel('$x_{t}$', fontsize=12)` (lines 115-116, 350-351) — lowercase, math-mode labels per qe-fig-006; one static `{image}` (line 506) is used inside an exercise per qe-fig-011. No embedded titles outside exercise/solution context. |
| References   | N/A   | No citations. |
| Links        | 7/10  | Uses `` {doc}`troubleshooting` ``, `` {doc}`need_for_speed` ``, `` {doc}`jax_intro` ``, `` {doc}`scipy` `` cleanly. One bare URL to `intro.quantecon.org` at line 497 should be `` {doc}`intro:intro` ``. |
| Admonitions  | 8/10  | Three `{exercise-start}` / four `{exercise}` directives; four `{solution-start}` blocks with `:class: dropdown` and matched `:label:`. Note: `{exercise}` (non-gated) is used twice (`speed_ex1` line 439, `numba_ex3` line 613, `numba_ex4` line 688) — but their bodies contain only math and prose (no embedded code cells or nested directives), so this is borderline rather than a clear qe-admon-001 violation. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case. *Examples:* line 80 `## Compiling Functions`, line 87 `### An Example`, line 100 `#### Base Version`, line 132 `#### Acceleration via Numba`, line 183 `### How and When it Works`, line 217 `## Sharp Bits`, line 223 `### Typing`, line 267 `### Global Variables`, line 300 `## Multithreaded Loops in Numba`, line 437 `## Exercises`. *Count:* 10+ occurrences.
- **[qe-link-002]** — One bare URL to a sibling series. *Example:* line 497 `[Introduction to Quantitative Economics with Python](https://intro.quantecon.org/intro.html)` — should use `` {doc}`intro:intro` `` (or with custom title).
- **[qe-fig-005]** — Two code-generated figures (lines 113, 341) lack `name:` metadata.

### Low severity
- **[qe-math-010 (proposed)]** — `\mathbb E` without braces in display math (lines 700, 739). Renders identically but inconsistent.
- **[qe-admon-001]** — Three exercises use bare `{exercise}` rather than gated `{exercise-start}` / `{exercise-end}` syntax (lines 439, 613, 688). Their bodies contain math and prose only, so this is a borderline preference rather than a hard violation.

## Strengths
- Lecture title "Numba" follows qe-writing-006 (single word).
- Math conventions clean: no `^T`, no bold vectors, no `*` for multiplication, no `\tag`, no `align` inside `$$`.
- Sequences use `\{...\}` per qe-math-005 (e.g., `$\{\xi_t\}$` line 726).
- "IID" used correctly per qe-writing-009 (proposed) (line 726).
- `qe.Timer()` consistently used for benchmarking (qe-code-004 exemplary).
- Greek unicode (α, β, μ, ρ, ν, σ, ξ, η) used in code throughout per qe-code-002.
- `{image}` directive used inside `exercise-start`/`exercise-end` for the Markov chain transition graph per qe-fig-011.

## Recommended actions
1. Convert H3/H4 headings to sentence case ("An example", "Base version", "Acceleration via Numba", "How and when it works", "Sharp bits", "Typing", "Global variables", "Multithreaded loops in Numba").
2. Replace the bare `intro.quantecon.org/intro.html` URL on line 497 with `` {doc}`intro:intro` ``.
3. Tighten `\mathbb E` → `\mathbb{E}` for consistency.
4. Optionally convert the three bare `{exercise}` blocks to gated syntax for uniformity with the rest of the lecture.
