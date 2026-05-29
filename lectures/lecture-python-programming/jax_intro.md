# Style Audit — jax_intro

- **Series:** lecture-python-programming
- **File:** `lectures/jax_intro.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Mixed heading conventions — many sentence case, several Title Case offenders. |
| Math         | N/A   | Only trivial inline math. |
| Code         | 9/10  | `!pip install jax quantecon` at top with `hide-output`; Greek unicode (β, μ, ρ, ν) used throughout; `qe.Timer()` used for benchmarking per qe-code-004; no `%timeit`. |
| JAX          | out of scope | JAX-introductory lecture. |
| Figures      | 7/10  | One `ax.set_title("PRNG Key Splitting Tree", ...)` at line 560 violates qe-fig-003; one `figsize=(8,4)` at line 498 (qe-fig-001); no `name:` metadata. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `` {doc}`our lecture on autodiff <autodiff>` `` (line 901), `` {doc}`our lecture on Numba <numba>` `` (line 912), `` {ref}`used Monte Carlo to price ... <numba_ex4>` `` (line 912). |
| Admonitions  | 9/10  | `{include} _admonition/gpu.md` for GPU note; one `{exercise-start}`/`{solution-start}` pair correctly gated with `:label:` and `:class: dropdown`; `{note}` admonitions used. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — Embedded title in matplotlib figure outside an exercise/solution context. *Example:* line 560 `ax.set_title("PRNG Key Splitting Tree", fontsize=13, pad=10)`. *Count:* 1 occurrence.

### Medium severity
- **[qe-writing-006]** — Several H2/H3 headings use Title Case. *Examples:* line 51 `## JAX as a NumPy Replacement`, line 101 `### Differences`, line 429 `### NumPy / MATLAB Approach`, line 596 `### Benefits`, line 606 `## JIT Compilation`, line 617 `### With NumPy`, line 653 `### With JAX`, line 696 `### Compiling the Whole Function`, line 905 `## Exercises`. *Count:* ~10 occurrences.

### Low severity
- **[qe-writing-001]** — A couple of paragraphs combine two sentences (e.g., lines 900–902).
- **[qe-fig-001]** — One explicit `figsize=(8, 4)` at line 498 without strong justification.
- **[qe-fig-005]** — No code-generated figures have `name:` metadata for `numref` cross-referencing.

## Strengths
- Lecture title "JAX" follows qe-writing-006 (single word).
- Some headings already use sentence case ("Random numbers", "Functional programming", "Pure functions").
- Math notation clean.
- Greek unicode (β, μ, ρ, ν, ξ, η) used in code per qe-code-002.
- `qe.Timer()` correctly used for performance benchmarking per qe-code-004.
- `{include} _admonition/gpu.md` is the canonical pattern for GPU-required lectures.
- Exercise/solution pair correctly gated with linked label per qe-admon-005.

## Recommended actions
1. Standardize all section headings to sentence case ("JAX as a NumPy replacement", "JIT compilation", "Compiling the whole function", "With NumPy", "With JAX", "Combining transformations").
2. Remove the `ax.set_title("PRNG Key Splitting Tree", ...)` call on line 560 and convert it to figure-directive metadata or move the title into the body text.
3. Remove or justify the `figsize=(8, 4)` on line 498.
