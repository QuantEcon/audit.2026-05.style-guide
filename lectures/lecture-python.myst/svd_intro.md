# Style Audit — svd_intro

- **Series:** lecture-python.myst
- **File:** `lectures/svd_intro.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 8/10 | Transpose denoted `'` (prime) or `^T` instead of `\top`. |
| Code         | 8.5/10 | Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms... |
| JAX          | out of scope | not a JAX lecture |
| Figures      | 10/10 | `figsize=` set in 2 place(s). |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 31, line 61, line 127. *Count:* 8.

### Medium severity
- **[qe-math-002]** — Transpose denoted `'` (prime) or `^T` instead of `\top`. *Examples:* line 747 (`^T`). *Count:* 4 occurrences.
- **[qe-code-002]** — Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=2, uni=1).

### Low severity
- **[qe-fig-001]** — `figsize=` set in 2 place(s).

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.
- Solutions use `:class: dropdown` consistently.
- Cross-series links use `{doc}` intersphinx form.

## Recommended actions
1. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
2. Address `qe-math-002`: Transpose denoted `'` (prime) or `^T` instead of `\top`.
3. Address `qe-code-002`: Spelled-out Greek (alpha/beta/etc.) used predominantly in code; mixed with unicode forms (word=2, uni=1).
4. Address `qe-fig-001`: `figsize=` set in 2 place(s).
