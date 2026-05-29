# Style Audit — five_preferences

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/five_preferences.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.8 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | Title in Title Case; sentence-case headings; many bolded keyword definitions. |
| Math         | 6.5/10 | `{\mathcal N}` and `{\cal N}` for Normal distribution. |
| Code         | 6/10  | 18 spelled Greek vs 12 unicode; no install cell (scipy/numpy only). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 5/10  | 1 `ax.set_title`; 13 `figsize=`; captions present in some cells. |
| References   | 8/10  | 16 `{cite}` used; never `{cite:t}` despite some narrative refs. |
| Links        | 9/10  | No cross-series URL links; self-contained. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — `figsize=` set 13 times — systemic. *Count:* 13 occurrences.

### Medium severity
- **[qe-math-A3]** — `{\mathcal N}` / `{\cal N}` used as Normal distribution (carry-forward from v1 M9). *Example:* `lectures/five_preferences.md:693`, `:1897`. *Count:* 2 occurrences.
- **[qe-writing-005]** — Heavy decorative bolding for terms like `**risk**`, `**uncertainty**`, `**uncertainty aversion**`, `**Knightian uncertainty**`, `**Remark:**` mixes definitional and emphasis use.
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.
- **[qe-code-002]** — Mixed spelled/unicode Greek (18 spelled vs 12 unicode).

### Low severity
- **[qe-math-004]** — `\mathbf{T}` in plot label at L556 (carry-forward from v1 M5).
- Backtick-and-apostrophe quotation style and single-quoted `'penalty parameter'` (L162, L469) is unusual; prefer markdown italics.

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case headings (qe-writing-006).
- `\begin{bmatrix}` used (qe-math-003).
- Sequences in curly brackets (qe-math-005).
- Equation labels and `{eq}` references (qe-math-007).
- Some figures use `mystnb` captions and `name:` fields (qe-fig-005).

## Recommended actions
1. Replace `{\mathcal N}` / `{\cal N}` with `N` (qe-math-A3).
2. Reduce decorative bolding; use italics for non-definition emphasis (qe-writing-005).
3. Remove unnecessary `figsize=` settings (qe-fig-001).
4. Remove `ax.set_title` call (qe-fig-003).
5. Standardise on unicode Greek in code (qe-code-002).
