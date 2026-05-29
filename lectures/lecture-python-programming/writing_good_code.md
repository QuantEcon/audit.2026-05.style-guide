# Style Audit — writing_good_code

- **Series:** lecture-python-programming
- **File:** `lectures/writing_good_code.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Heading Title Case throughout H2/H3. |
| Math         | 7.5/10| Clean math; no `\mathbb E` here (re-check: lecture uses no `\mathbb E` at all). |
| Code         | 9/10  | Only Anaconda packages (numpy, matplotlib, scipy); Greek unicode (α, β, γ, δ) used heavily per qe-code-002; PEP8 demonstrated as a teaching topic; no benchmarking magics. |
| JAX          | out of scope | — |
| Figures      | 5/10  | One `figsize=(8, 16)` in the deliberately-poor-code section (line 80) — intentional bad example; same `figsize=(8, 16)` in the "good" version (line 270) — would be cleaner without; lowercase axis labels per qe-fig-006; no embedded titles; no `name:` on figures. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `` {doc}`we've seen in previous lectures <numba>` `` correctly per qe-link-001. |
| Admonitions  | 9/10  | One `{exercise-start}` / `{solution-start}` pair gated; `:class: dropdown` on solution; `:label: wgc-exercise-1` matched per qe-admon-005. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** *(carry-forward W3)* — Section headings use Title Case rather than sentence case. *Examples:* line 45 `## An Example of Poor Code`, line 142 `## Good Coding Practice`, line 156 `### Don't Use Magic Numbers`, line 176 `### Don't Repeat Yourself`, line 196 `### Minimize Global Variables`, line 226 `### Use Functions or Classes`, line 246 `## Revisiting the Example`, line 291 `## Exercises`. *Count:* 8 occurrences.

### Medium severity
- **[qe-fig-001]** — Two `figsize=(8, 16)` calls (lines 80 and 270). The first is in the "Example of Poor Code" section so could be argued as part of the demonstration; the second is in the "Revisiting the example" section, which is presented as the *good* version — so this one is inconsistent.

### Low severity
- **[qe-fig-005]** — Code-generated figures lack `name:` metadata.

## Strengths
- Lecture title "Writing Good Code" follows qe-writing-006.
- Equation label `gc_solmod` and `{eq}` reference at line 66 — correct usage per qe-math-A6.
- Bold for emphasis sparingly per qe-writing-005 ("**a great deal**", "**automate**", "**not**", "**parameters**").
- Math display blocks use clean LaTeX; no `align`, no `\tag`, no bold vectors, no `^T`, no `*` for multiplication.
- Greek unicode (α, β, γ, δ) used pervasively per qe-code-002 — well-aligned with the lecture's own advice.
- Axis labels lowercase per qe-fig-006.
- Exercise/solution pair compliant per qe-admon-001/qe-admon-002/qe-admon-005.

## Recommended actions
1. Convert section headings to sentence case ("An example of poor code", "Good coding practice", "Don't use magic numbers", "Don't repeat yourself", "Minimize global variables", "Use functions or classes", "Revisiting the example").
2. Remove the `figsize=(8, 16)` in the "good code" section (line 270); keep or annotate the one in the "poor code" section.
