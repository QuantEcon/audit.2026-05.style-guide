# Style Audit — lagrangian_lqdp

- **Series:** lecture-python.myst
- **File:** `lectures/lagrangian_lqdp.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10 | Many section headings use Title Case rather than sentence case. |
| Math         | 6/10 | Transpose denoted `'` (prime) and/or `^T` instead of `\top`. |
| Code         | 9/10 | Mixed Greek conventions in code (word=3, uni=5). |
| JAX          | out of scope | not a JAX lecture |
| Figures      | N/A | No figures. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 7/10 | 1 full URL(s) to same series. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Transpose denoted `'` (prime) and/or `^T` instead of `\top`. *Examples:* line 87 `$V(x)= - x'Px$...`. *Count:* 24 occurrences.
- **[qe-writing-006]** — Many section headings use Title Case rather than sentence case. *Examples:* line 70, line 236, line 258. *Count:* 7.
- **[qe-link-002]** — 4 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links. *Examples:* line 61, line 66, line 827.

### Medium severity
_None found._

### Low severity
- **[qe-code-002]** — Mixed Greek conventions in code (word=3, uni=5).
- **[qe-code-005]** — Jupyter `%timeit`/`%%timeit` magic used (2 occurrences); prefer `qe.timeit()`.
- **[qe-link-001]** — 1 full URL(s) to same series. *Examples:* line 676.

## Strengths
- Uses "IID" or no IID terminology.
- No bold vectors/matrices.
- Normal distribution written as plain `N`.
- `aligned` (not `align`) used in `$$` math.

## Recommended actions
1. Address `qe-math-002`: Transpose denoted `'` (prime) and/or `^T` instead of `\top`.
2. Address `qe-writing-006`: Many section headings use Title Case rather than sentence case.
3. Address `qe-link-002`: 4 direct URLs to other QuantEcon series — should use `{doc}` intersphinx links.
4. Address `qe-code-002`: Mixed Greek conventions in code (word=3, uni=5).
5. Address `qe-code-005`: Jupyter `%timeit`/`%%timeit` magic used (2 occurrences); prefer `qe.timeit()`.
