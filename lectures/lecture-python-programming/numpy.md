# numpy

- **Series:** lecture-python-programming
- **File:** `lectures/numpy.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10| Heavily Title Case section headings; otherwise clean prose. |
| Math         | 7.5/10| Mostly clean; `\mathbb P` without braces is the only nit. |
| Code         | 8/10  | `!pip install quantecon` at top with `hide-output` (qe-code-003); Greek unicode (λ) used; `qe.Timer()` used for benchmarking in exercise (qe-code-004); one duplicate `!pip install quantecon` at line 1437 inside an exercise — historical leftover. |
| JAX          | out of scope | — |
| Figures      | 7/10  | Two `figsize=(...)` in body (line 80 not in this file — checked, none in top half; in exercise-block at line 1392 `fig, ax = plt.subplots()` — no figsize); one static `{figure}` of htop screenshot (line 1109) appropriately used; no embedded titles in matplotlib code. |
| References   | N/A   | No citations. |
| Links        | 9/10  | Uses `` {doc}`later in the course <python_advanced_features>` `` and `` {doc}`soon <scipy>` `` correctly. |
| Admonitions  | 8/10  | Four `{exercise-start}` / one `{exercise}` (np_ex3); four `{solution-start}` pairs with `:class: dropdown` and `:label:`; `{hint}` admonitions used. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case throughout. *Examples:* line 69 `## NumPy Arrays`, line 81 `### Basics`, line 122 `### Shape and Dimension`, line 161 `### Creating Arrays`, line 222 `### Array Indexing`, line 314 `### Array Methods`, line 383 `## Arithmetic Operations`, line 432 `## Matrix Multiplication`, line 460 `## Broadcasting`, line 836 `## Mutability and Copying Arrays`, line 848 `### Mutability`, line 890 `### Making Copies`, line 922 `## Additional Features`, line 927 `### Universal Functions`, line 995 `### Comparisons`, line 1047 `### Sub-packages`, line 1085 `### Implicit Multithreading`, line 1122 `## Exercises`. *Count:* 18+ occurrences.

### Medium severity
- **[qe-code-003]** — A duplicate `!pip install quantecon` cell at line 1437 (inside `np_ex4`) is redundant given the top-of-file install at line 35.
- **[qe-fig-005]** — Code-generated figures (e.g., exercise solutions) and the `{figure}` at line 1109 lack `name:` metadata.

### Low severity
- **[qe-math-010 (proposed)]** — `\mathbb P` without braces at line 1188; renders identically but inconsistent.
- **[qe-admon-001]** — `np_ex3` uses bare `{exercise}` (line 1300) instead of gated syntax; body is prose-only so the violation is borderline.

## Strengths
- Lecture title "NumPy" follows qe-writing-006.
- No bold vectors, no `^T` transpose, no `*` for multiplication, no `\tag`, no `align` inside `$$`.
- Equation labels and `{eq}` references used correctly (e.g., `np_polynom` at line 1132 and `{eq}` ref at line 1137) per qe-math-013 (proposed).
- Crisp single-sentence paragraphs.
- `qe.Timer` used in exercise per qe-code-004 (with custom message string).
- No `%timeit` magics (qe-code-005 compliant).
- Greek unicode (λ) used per qe-code-002.

## Recommended actions
1. Convert all section headings to sentence case ("NumPy arrays", "Shape and dimension", "Creating arrays", "Array indexing", "Array methods", "Arithmetic operations", "Matrix multiplication", "Broadcasting", "Mutability and copying arrays", "Mutability", "Making copies", "Additional features", "Universal functions", "Comparisons", "Sub-packages", "Implicit multithreading").
2. Remove the duplicate `!pip install quantecon` cell at line 1437.
3. Normalize `\mathbb P` → `\mathbb{P}`.
4. Optionally promote `np_ex3` to gated `{exercise-start}` / `{exercise-end}` form for consistency.
