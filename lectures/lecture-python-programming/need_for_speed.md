# Style Audit — need_for_speed

- **Series:** lecture-python-programming
- **File:** `lectures/need_for_speed.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10| Mixed case in headings — many already sentence case; ~10 Title Case stragglers. |
| Math         | N/A   | No math content. |
| Code         | 9/10  | `!pip install quantecon` at top with `hide-output`; uses `qe.Timer()` (qe-code-004) for both demos; PEP8 clean; no Greek identifiers needed. |
| JAX          | out of scope | — |
| Figures      | 6/10  | Three static `{figure}` directives (lines 313, 458, 492) for diagrams/screenshots; no `name:` fields, no captions inside the directive. |
| References   | N/A   | No citations. |
| Links        | 9/10  | External docs only; no improper cross-series URLs. |
| Admonitions  | 9/10  | Two `{note}` admonitions used; no exercises or nested directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Several H2/H3 headings still use Title Case. *Examples:* line 70 `## Major Scientific Libraries`, line 103 `### Python's Scientific Ecosystem`, line 130 `## Why is Pure Python Slow?`, line 136 `### Type Checking`, line 217 `### Data Access`, line 250 `### Summary`, line 270 `## Accelerating Python`, line 387 `## Parallelization`, line 409 `### Parallelization on CPUs`, line 441 `#### Which Should We Use?`, line 450 `### Hardware Accelerators`, line 481 `### Accessing GPU Resources`. *Count:* ~10 occurrences.
- **[qe-fig-005]** — Three `{figure}` directives lack `name:` metadata (lines 313, 458, 492).

### Low severity
- **[qe-writing-005]** — Some emphatic phrases use **bold** for terms that are not formal definitions ("**Python is small**", "**Python is slow**" on lines ~82, ~90); overlaps with the definition convention.

## Strengths
- Lecture title "Python for Scientific Computing" follows qe-writing-006.
- Several headings already correctly use sentence case ("Why do we need them?", "Dynamic typing", "Static types").
- Crisp one-sentence paragraphs throughout.
- Uses `qe.Timer()` for both demos (qe-code-004 exemplary).
- `!pip install quantecon` at top with `hide-output` (qe-code-003 compliant).
- `{note}` admonitions used cleanly.

## Recommended actions
1. Convert Title Case headings to sentence case ("Major scientific libraries", "Python's scientific ecosystem", "Why is pure Python slow?", "Type checking", "Data access", "Accelerating Python", "Parallelization", "Parallelization on CPUs", "Which should we use?", "Hardware accelerators", "Accessing GPU resources").
2. Add `name:` metadata to the three figure directives.
