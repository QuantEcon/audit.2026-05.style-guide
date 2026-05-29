# Style Audit — autodiff

- **Series:** lecture-python-programming
- **File:** `lectures/autodiff.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Most H3 use sentence case; two H2s revert to Title Case. |
| Math         | 8/10  | Clean math; no transpose, vectors, or probability content. |
| Code         | 9/10  | `!pip install jax` at top with `:tags: [hide-output]`; Greek unicode (α, β, σ, ϵ, λ, Δ) used in code; no `time.time()` / `%timeit`. |
| JAX          | out of scope | JAX-based lecture. |
| Figures      | 8/10  | All figures are code-generated via matplotlib; no `figsize`, no embedded titles, lowercase axis labels (implicit in `label="$f'$"`); no `name:` for cross-referencing. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `` {doc}`our brief preview <jax_intro>` `` (line 23) correctly per qe-link-001/qe-link-002. |
| Admonitions  | 9/10  | `{exercise-start}`/`{exercise-end}` and `{solution-start}`/`{solution-end}` correctly used; solution has `:class: dropdown`; `:label:` properly cross-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Two H2 section headings use Title Case rather than sentence case. *Examples:* line 295 `## Gradient Descent`, line 460 `## Exercises`. *Count:* 2 occurrences.

### Low severity
- **[qe-writing-001]** — A handful of paragraphs combine two short sentences with the `+++` cell separator instead of staying as single-sentence units; mostly acceptable.
- **[qe-fig-005]** — Plots within code cells could benefit from `mystnb` figure metadata with `name:` for downstream cross-referencing; currently no figures are named.

## Strengths
- Lecture title "Adventures with Autodiff" follows qe-writing-006.
- Most section headings already use sentence case (e.g., "What is automatic differentiation?", "Some experiments").
- Math display blocks use proper `$$` and clean LaTeX; no `align`, no `\tag`.
- Greek unicode (α, β, σ, ϵ, λ, Δ) consistently used in code per qe-code-002.
- Single `!pip install` at top with `hide-output` per qe-code-003.
- Solution correctly uses `:class: dropdown` per qe-admon-002 and `:label:` matching exercise per qe-admon-005.

## Recommended actions
1. Rename `## Gradient Descent` to `## Gradient descent` and `## Exercises` consistency check.
2. Optionally add `name:` metadata to inline figures for cross-referencing.
