# debugging

- **Series:** lecture-python-programming
- **File:** `lectures/debugging.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10| Pervasive Title Case in section headings. |
| Math         | N/A   | No math content. |
| Code         | 8/10  | PEP8-compliant Python demos; only Anaconda packages (numpy, matplotlib); no Greek identifiers needed; debugger `%debug` magic discussed but not used as benchmarking magic (qe-code-005 N/A). |
| JAX          | out of scope | — |
| Figures      | 9/10  | No matplotlib figures generated; demos use `print()` output only; figure metadata not applicable. |
| References   | N/A   | No citations. |
| Links        | 9/10  | Only external links to docs; no cross-series quantecon URLs to convert. |
| Admonitions  | 8/10  | One `{exercise-start}`/`{exercise-end}` and `{solution-start}` pair correctly gated; solution uses `:class: dropdown`; `:label:` correctly matches exercise (`debug_ex1`). |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Most H2/H3 section headings are Title Case rather than sentence case. *Examples:* line 46 `## Debugging`, line 65 `### The \`debug\` Magic`, line 183 `### Setting a Break Point`, line 247 `### Other Useful Magics`, line 260 `## Handling Errors`, line 293 `### Errors in Python`, line 356 `### Assertions`, line 390 `### Handling Errors During Runtime`, line 490 `## Exercises`, plus H4 `#### Catching Exceptions`. *Count:* 10+ occurrences.

### Medium severity
_None found._

### Low severity
- **[qe-writing-001]** — A small number of multi-sentence paragraphs (e.g., the introduction around lines 286–288 uses a multi-bullet "Why?" explanation; mostly fine).

## Strengths
- Lecture title "Debugging and Handling Errors" follows qe-writing-006.
- Bullet rationales (the "Why?" pattern) are short and readable.
- Inline backticks for code identifiers are used consistently.
- No use of `time.time()`, `tic`/`toc`, or `%timeit` magics.
- Exercise/solution pair correctly gated and labelled per qe-admon-001/qe-admon-005.

## Recommended actions
1. Convert section headings to sentence case ("Debugging", "The debug magic", "Setting a break point", "Other useful magics", "Handling errors", "Errors in Python", "Handling errors during runtime").
