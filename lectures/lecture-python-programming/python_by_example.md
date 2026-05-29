# Style Audit — python_by_example

- **Series:** lecture-python-programming
- **File:** `lectures/python_by_example.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10| Heading Title Case throughout. |
| Math         | 7/10  | One qe-math-012 (proposed) violation (`*` for multiplication) inside `$...$`. |
| Code         | 9/10  | Only Anaconda packages (numpy, matplotlib); Greek unicode (ϵ, α) used per qe-code-002; PEP8 clean; no benchmarking patterns. |
| JAX          | out of scope | — |
| Figures      | 7/10  | One static `{figure}` (line 46) is an output preview; code-generated plots are simple `plt.plot` (no `figsize`, no `set_title`); no `name:` on the static figure. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `` {doc}`lecture <getting_started>` ``, `` {doc}`NumPy <numpy>` ``, `` {doc}`later on <oop_intro>` `` correctly per qe-link-001. |
| Admonitions  | 9/10  | Five `{exercise-start}` / `{solution-start}` pairs gated; `:class: dropdown` on all solutions; `:label:` cross-linked per qe-admon-005; `{hint}` and `{note}` admonitions used. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 39 `## The Task: Plotting a White Noise Process`, line 56 `## Version 1`, line 74 `### Imports`, line 99 `#### Why So Many Imports?`, line 109 `#### Packages`, line 134 `#### Subpackages`, line 147 `### Importing Names Directly`, line 174 `### Random Draws`, line 192 `## Alternative Implementations`, line 201 `### A Version with a For Loop`, line 229 `### Lists`, line 291 `### The For Loop`, line 335 `### A Comment on Indentation`, line 361 `### While Loops`, line 396 `## Another Application`, line 440 `## Exercises`. *Count:* 15+ occurrences.

### Medium severity
- **[qe-math-012 (proposed)]** — `*` used as multiplication inside inline math. *Example:* line 690 `$area = \pi * radius^2$`. *Count:* 1 occurrence.

### Low severity
- **[qe-fig-005]** — The static `{figure}` at line 46 lacks `name:` metadata.

## Strengths
- Lecture title "An Introductory Example" follows qe-writing-006.
- "IID" used correctly per qe-writing-009 (proposed) (line ~689).
- Bold for definitions per qe-writing-005 ("**package**", "**modules**", "**subpackage**").
- Sequences notation correct (`$\epsilon_0, \epsilon_1, \ldots$`) per qe-math-005.
- Greek unicode (ϵ, α) used in code per qe-code-002.
- Exemplary exercise/solution structure across all 5 pairs per qe-admon-001/qe-admon-002/qe-admon-005.

## Recommended actions
1. Convert all H2/H3/H4 headings to sentence case ("The task: plotting a white noise process", "Version 1", "Imports", "Why so many imports?", "Packages", "Subpackages", "Importing names directly", "Random draws", "Alternative implementations", "A version with a `for` loop", "Lists", "The `for` loop", "A comment on indentation", "While loops", "Another application").
2. Replace `\pi * radius^2` with `\pi r^2` (juxtaposition) or `\pi \cdot r^2`.
3. Add `name:` to the static preview figure.
