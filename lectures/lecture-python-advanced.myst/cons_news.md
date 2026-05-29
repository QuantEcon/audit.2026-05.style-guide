# cons_news

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/cons_news.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Sentence-case headings; "i.i.d." used in narrative. |
| Math         | 4/10  | Heavy `\begin{array}` usage instead of `\begin{bmatrix}`. |
| Code         | 7/10  | Spelled Greek (5 occurrences); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | N/A   | no figures |
| References   | 8/10  | 4 `{cite}`; two narrative refs would benefit from `{cite:t}`. |
| Links        | 7/10  | Two raw `python-intro.quantecon.org` URLs (L36, L56) alongside `{doc}`. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — `\begin{array}{...}` used for matrices throughout instead of `\begin{bmatrix}`. *Example:* `lectures/cons_news.md:549`-`565`. *Count:* 17 occurrences.

### Medium severity
- **[qe-writing-009 (proposed)]** — "i.i.d." used in text instead of "IID". *Example:* `lectures/cons_news.md:127`, `:146`, `:149`, `:481`. *Count:* 4 occurrences.
- **[qe-link-002]** — Two raw `python-intro.quantecon.org/perm_income_cons.html` URLs. *Example:* `lectures/cons_news.md:36`, `:56`. *Count:* 2 occurrences.

### Low severity
- **[qe-writing-005]** — Bold for keywords like `**news**`, `**noise**`, `**Ricardian equivalence**` is borderline definitional.
- **[qe-code-002]** — Spelled-out Greek in code parameters.
- Note: `^T` instances at L816, L823, L840 are time horizons, not transpose — no qe-math-002 violation.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- Sequences in curly brackets (qe-math-005).
- 5 `{doc}` cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `\begin{array}` matrices with `\begin{bmatrix}` (qe-math-003).
2. Replace "i.i.d." with "IID" in narrative (qe-writing-009, proposed).
3. Convert raw `python-intro.quantecon.org` URLs to `{doc}\`intermediate:perm_income_cons\`` (qe-link-002).
