# Style Audit — names

- **Series:** lecture-python-programming
- **File:** `lectures/names.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10| Heading Title Case is pervasive. |
| Math         | N/A   | No math expressions. |
| Code         | 9/10  | Only Anaconda packages; no Greek identifiers needed; PEP8 clean; no benchmarking magics. |
| JAX          | out of scope | — |
| Figures      | 6/10  | Nine static `{figure}` directives (lines 453, 459, 469, 477, 524, 529, 536, 560, 564) for namespace-diagram screenshots. None have `name:`, captions are brief sentences placed outside the directive. |
| References   | N/A   | No citations. |
| Links        | 9/10  | External links only; no improper cross-series URLs. |
| Admonitions  | N/A   | No exercises or admonitions in the body. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 35 `## Variable Names in Python`, line 97 `## Namespaces`, line 180 `## Viewing Namespaces`, line 212 `## Interactive Sessions`, line 266 `## The Global Namespace`, line 295 `## Local Namespaces`, line 327 `## The \`__builtins__\` Namespace`, line 367 `## Name Resolution`, line 482 `### Mutable Versus Immutable Parameters`. *Count:* 9 occurrences.

### Medium severity
- **[qe-fig-005]** — None of the nine `{figure}` directives have a `name:` field, preventing `{numref}` cross-referencing.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs (e.g., lines 28–32 span two ideas across two paragraphs but fine).
- **[qe-fig-002]** — Several diagrams could plausibly be redrawn programmatically (e.g., box-and-arrow namespace diagrams), but the current static images are acceptable given the diagrammatic nature.

## Strengths
- Lecture title "Names and Namespaces" follows qe-writing-006.
- Bold (`**name**`, `**binds**`, `**rebound**`) used for key concept definitions per qe-writing-005.
- One-sentence paragraphs dominate.
- No code-style violations.

## Recommended actions
1. Convert section headings to sentence case ("Variable names in Python", "Namespaces", "Viewing namespaces", "Interactive sessions", "The global namespace", "Local namespaces", "The `__builtins__` namespace", "Name resolution", "Mutable versus immutable parameters").
2. Add `name:` metadata to each `{figure}` for cross-referencing.
