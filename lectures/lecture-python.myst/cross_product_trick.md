# Style Audit — cross_product_trick

- **Series:** lecture-python.myst
- **File:** `lectures/cross_product_trick.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10 | Section headings use Title Case rather than sentence case. |
| Math         | 3/10 | Broken `{eq}` reference (mismatched braces). |
| Code         | 10/10 | Clean code conventions. |
| JAX          | out of scope | not a JAX lecture |
| Figures      | N/A | No figures. |
| References   | N/A | No citations. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | N/A | No admonitions. |

## Issues

### Critical
- **[qe-math-A6]** — Broken `{eq}` reference (mismatched braces). *Example:* line 133 `{eq}`eq:Kalman102}`.

### High severity
- **[qe-math-002]** — Transpose denoted `'` (prime) instead of `\top` throughout. *Examples:* line 48 `x_t' R x_t`, line 63 `B'PB`, line 67 `A'PA`, lines 82–88 inside `\begin{align*}`, lines 119–143 (Kalman filter formulas). *Count:* 30+ occurrences.

### Medium severity
- **[qe-writing-006]** — Section headings use Title Case rather than sentence case. *Examples:* line 33 `## Undiscounted Dynamic Programming Problem`, line 92 `## Kalman Filter`. *Count:* 2 occurrences.

### Low severity
- **[qe-writing-A1]** — Uses "i.i.d." rather than "IID". *Example:* line 110 `is an i.i.d. $p \times 1$ random vector`.
- **[qe-writing-001]** — Several multi-sentence paragraphs (e.g. lines 80, 94–95) that could be split into single-sentence units.

## Strengths
- Title H1 uses Title Case correctly.
- Uses `aligned`/`align*` MyST math (not `align` inside `$$`).
- No bold vectors or `\mathcal{N}` issues.

## Recommended actions
1. Address `qe-math-A6`: Broken `{eq}` reference (mismatched braces).
2. Address `qe-math-002`: Transpose denoted `'` (prime) instead of `\top` throughout.
3. Address `qe-writing-006`: Section headings use Title Case rather than sentence case.
4. Address `qe-writing-A1`: Uses "i.i.d." rather than "IID".
5. Address `qe-writing-001`: Several multi-sentence paragraphs (e.g. lines 80, 94–95) that could be split into single-sentence units.
