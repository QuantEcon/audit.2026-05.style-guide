# numpy_vs_numba_vs_jax

- **Series:** lecture-python-programming
- **File:** `lectures/numpy_vs_numba_vs_jax.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Mixed heading conventions; ~10 Title Case stragglers. |
| Math         | 8/10  | Clean math; trivial usage. |
| Code         | 9/10  | `!pip install quantecon jax` at top with `hide-output` (qe-code-003); Greek unicode (μ, ν, ρ, β, σ, ξ, η) used; `qe.Timer()` used 17 times for benchmarks (qe-code-004); PEP8 clean. |
| JAX          | out of scope | (JAX comparison lecture.) |
| Figures      | 7/10  | One `figsize=(10, 8)` at line 101 (qe-fig-001); lowercase math-mode axis labels (lines 111–112) per qe-fig-006; no embedded titles in non-exercise context. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `[NumPy](numpy)`, `[Numba](numba)`, `[JAX](jax_intro)` (same-series markdown-link style per qe-link-001); uses `` {doc}`Numba lecture <numba>` ``, `` {doc}`autodiff` `` per qe-link-001. |
| Admonitions  | 9/10  | `{include} _admonition/gpu.md` for GPU note. No exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Several headings still use Title Case. *Examples:* line 77 `### Problem Statement`, line 180 `### Memory Issues`, line 201 `### A Comparison with Numba`, line 243 `### Parallelized Numba`, line 290 `### Vectorized code with JAX`, line 337 `### JAX plus vmap`, line 395 `### Summary`, line 424 `### Numba Version`, line 459 `### JAX Version`, line 559 `### Summary`. *Count:* ~10 occurrences.

### Low severity
- **[qe-fig-001]** — One `figsize=(10, 8)` at line 101 for the 3D surface plot — arguably justified for 3D rendering, but not annotated as such.
- **[qe-fig-005]** — Code-generated 3D plot at line 101 lacks `name:` for cross-referencing.

## Strengths
- Lecture title "NumPy vs Numba vs JAX" follows qe-writing-006.
- H2 headings ("Vectorized operations", "Sequential operations", "Overall recommendations") correctly use sentence case.
- Math conventions clean (no `^T`, no bold vectors, no `*`).
- One-sentence paragraphs throughout.
- Exemplary use of `qe.Timer()` for 17+ benchmark blocks per qe-code-004.
- Greek unicode (μ, ν, ρ, β, σ, ξ, η) used pervasively per qe-code-002.

## Recommended actions
1. Convert Title Case H3 headings to sentence case ("Problem statement", "Memory issues", "A comparison with Numba", "Parallelized Numba", "Vectorized code with JAX", "JAX plus vmap", "Summary", "Numba version", "JAX version").
2. Optional: remove `figsize=(10, 8)` on line 101 or document the 3D-plot rationale.
