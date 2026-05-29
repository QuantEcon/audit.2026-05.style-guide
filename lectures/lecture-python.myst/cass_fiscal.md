# Style Audit — cass_fiscal

- **Series:** lecture-python.myst
- **File:** `lectures/cass_fiscal.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section/subsection headings use Title Case rather than sentence case. |
| Math         | 10/10 | No math issues. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=12, uni=18). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 9/10 | `figsize=` set in 9 places — usually unnecessary (defaults from `_config.yml`). |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section/subsection headings use Title Case rather than sentence case. *Examples:* line 39, line 112, line 169. *Count:* 12 headings affected.

### Medium severity
- **[qe-fig-001]** — `figsize=` set in 9 places — usually unnecessary (defaults from `_config.yml`).

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=12, uni=18).

## Strengths
- Uses "IID" or no IID terminology.
- Transpose notation uses `\top` consistently (no prime/`^T`).
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.

## Recommended actions
1. Address `qe-writing-006`: Section/subsection headings use Title Case rather than sentence case.
2. Address `qe-fig-001`: `figsize=` set in 9 places — usually unnecessary (defaults from `_config.yml`).
3. Address `qe-code-002`: Mixed Greek conventions in code (word=12, uni=18).
