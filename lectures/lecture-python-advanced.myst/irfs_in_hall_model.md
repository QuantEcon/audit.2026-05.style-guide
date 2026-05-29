# irfs_in_hall_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/irfs_in_hall_model.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Mostly one-sentence paragraphs; sentence-case headings used correctly. |
| Math         | 6/10  | `\begin{array}` once, prime as transpose once. |
| Code         | 7/10  | Mixed unicode/spelled Greek (2 spelled vs 3 unicode); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | No `ax.set_title`; no `figsize=`; no `:name:` fields. |
| References   | 8/10  | 2 `{cite}` used; never `{cite:t}` despite "Hall (1978)" narrative ref. |
| Links        | 8/10  | 1 `{doc}` reference; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-003]** — Initial-condition vector uses `\begin{array}{ccccc}` rather than `\begin{bmatrix}`. *Example:* `lectures/irfs_in_hall_model.md:77`-`80`. *Count:* 1 occurrence.
- **[qe-math-002]** — Prime `'` used as transpose on the same row vector. *Example:* `lectures/irfs_in_hall_model.md:80`. *Count:* 1 occurrence.
- **[qe-ref-001]** — Narrative "Hall (1978)" + `{cite}` pattern should use `{cite:t}`. *Count:* 2 occurrences.

### Low severity
- **[qe-writing-001]** — A couple of two-sentence paragraphs could be split, e.g. L118-119.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006).
- Section headings in sentence case (qe-writing-006).
- `\mathbb{E}` used for expectation (qe-math-010, proposed).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace the `\begin{array}` block with `\begin{bmatrix}` (qe-math-003).
2. Replace `]'` with `]^\top` (qe-math-002).
3. Use `{cite:t}` for narrative refs (qe-ref-001).
