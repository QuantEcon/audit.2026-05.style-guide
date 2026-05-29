# Style Audit — python_essentials

- **Series:** lecture-python-programming
- **File:** `lectures/python_essentials.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10| Pervasive Title Case in section headings. |
| Math         | N/A   | Only trivial inline content. |
| Code         | 9/10  | Only Anaconda packages (numpy); Greek unicode (ϵ) used in list comprehension exercise per qe-code-002; PEP8 clean; no benchmarking magics; demonstrates PEP8 explicitly in section "Python style guidelines: PEP8". |
| JAX          | out of scope | — |
| Figures      | N/A   | No figures. |
| References   | N/A   | No citations. |
| Links        | 9/10  | External docs links only; no improper cross-series URLs. |
| Admonitions  | 9/10  | Six `{exercise-start}` and one `{exercise}` (pyess_ex4 line 940, pyess_ex5 line 995) — both non-gated `{exercise}` bodies contain only prose/math, no code, so borderline. Six `{solution-start}` blocks all use `:class: dropdown` and matching `:label:` per qe-admon-005. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** *(carry-forward W3)* — Section headings use Title Case rather than sentence case. *Examples:* line 31 `## Data Types`, line 58 `### Primitive Data Types`, line 61 `#### Boolean Values`, line 111 `#### Numeric Types`, line 127 `### Containers`, line 284 `## Input and Output`, line 408 `### Paths`, line 424 `## Iterating`, line 435 `### Looping over Different Objects`, line 485 `### Looping without Indices`, line 538 `### List Comprehensions`, line 567 `## Comparisons and Logical Operators`, line 569 `### Comparisons`, line 631 `### Combining Expressions`, line 682 `## Coding Style and Documentation`, line 687 `### Python Style Guidelines: PEP8`, line 709 `### Docstrings`, line 767 `## Exercises`. *Count:* 18 occurrences.

### Medium severity
_None found._

### Low severity
- **[qe-writing-001]** *(carry-forward W1)* — Some multi-sentence paragraphs (e.g., line 76).
- **[qe-writing-004]** *(carry-forward W7)* — "Floating Point Unit (FPU)" on line 47 is capitalized — acceptable as a proper-noun acronym expansion but worth noting.
- **[qe-admon-001]** — `pyess_ex4` and `pyess_ex5` use bare `{exercise}` rather than gated `{exercise-start}` / `{exercise-end}`; bodies are prose-only.

## Strengths
- Lecture title "Python Essentials" follows qe-writing-006.
- Bold for definitions used consistently per qe-writing-005 ("**Boolean values**", "**Boolean arithmetic**", "**Complex numbers**", "**immutable**", "**mutable**", "**tuples**").
- One-sentence paragraphs dominant.
- Six exercise/solution pairs with `:class: dropdown` and matching `:label:` per qe-admon-002/qe-admon-005.
- No qe-code-* violations.

## Recommended actions
1. Convert all H2/H3/H4 headings to sentence case ("Data types", "Primitive data types", "Boolean values", "Numeric types", "Containers", "Input and output", "Paths", "Iterating", "Looping over different objects", "Looping without indices", "List comprehensions", "Comparisons and logical operators", "Comparisons", "Combining expressions", "Coding style and documentation", "Python style guidelines: PEP8", "Docstrings").
2. Optionally promote `pyess_ex4` and `pyess_ex5` to gated `{exercise-start}` / `{exercise-end}` form for uniformity.
