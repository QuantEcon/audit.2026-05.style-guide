# oop_intro

- **Series:** lecture-python-programming
- **File:** `lectures/oop_intro.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | A handful of Title Case H3/H2 stragglers; otherwise solid. |
| Math         | N/A   | No math content. |
| Code         | 8/10  | `!pip install rich` at top with `hide-output` (qe-code-003 compliant — `rich` is not in default Anaconda); PEP8 clean; no Greek identifiers needed. |
| JAX          | out of scope | — |
| Figures      | N/A   | No figures. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `` {doc}`later <python_oop>` `` correctly per qe-link-001. |
| Admonitions  | 9/10  | `{exercise-start}` / `{solution-start}` correctly gated; `:class: dropdown` on solution and hint; `:label:` correctly matched per qe-admon-005. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Several H2/H3 headings use Title Case rather than sentence case. *Examples:* line 84 `### Type`, line 145 `### Identity`, line 168 `### Object Content: Data and Attributes`, line 204 `### Methods`, line 261 `## Inspection Using Rich`, line 283 `## A Little Mystery`, line 333 `## Summary`, line 349 `## Exercises`. *Count:* 8 occurrences.

### Low severity
- **[qe-writing-001]** — Mostly one-sentence paragraphs; a few multi-sentence paragraphs (e.g., lines 50–56).

## Strengths
- Lecture title "OOP I: Objects and Methods" follows qe-writing-006.
- Bold for definitions used (e.g., **methods**) per qe-writing-005.
- Italic used for emphasis (`*is*`, `*everything is an object*`).
- `!pip install rich` correctly placed at top with `hide-output` per qe-code-003 (rich is not in default Anaconda).
- Exercise/solution pair fully compliant with qe-admon-001/qe-admon-002/qe-admon-005.

## Recommended actions
1. Convert headings to sentence case ("Type", "Identity", "Object content: data and attributes", "Methods", "Inspection using Rich", "A little mystery", "Summary").
