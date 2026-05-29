# Style Audit — lucas_asset_pricing_dles

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/lucas_asset_pricing_dles.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.0 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Sentence-case headings; in-code comments use Title Case. |
| Math         | 4/10  | Systemic use of `\begin{array}` for matrices; primes used as transpose throughout. |
| Code         | 8/10  | Unicode Greek used (3 occurrences); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | No `figsize=`; no `:name:` fields. |
| References   | 7/10  | 3 `{cite}` used; one narrative author ref. |
| Links        | 8/10  | 2 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — Every matrix written with `\begin{array}{ccc}...\end{array}` inside `\left[...\right]` instead of `\begin{bmatrix}`. *Example:* `lectures/lucas_asset_pricing_dles.md:89`-`93`, `:99`-`109`, `:113`-`117`, `:121`-`125`, `:129`-`133`. *Count:* ~7 occurrences.
- **[qe-math-002]** — Prime `'` used as transpose throughout the math. *Example:* `lectures/lucas_asset_pricing_dles.md:132`, `:141`, `:147`, `:151`, `:157`. *Count:* ~12 occurrences.

### Medium severity
_None found._

### Low severity
- **[qe-writing-006]** — Markdown comment-style "panel" headings (L220, L239, L268, L285) inside code cells are Title Case ("Left panel of Fig 7.12.2 from p.148 of HS2013"); preference-level.
- **[qe-writing-001]** — Multi-sentence paragraphs in places, e.g. L233-236.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- `\mathbb{E}` used for expectation (qe-math-010, proposed) at L63.
- Title in Title Case (qe-writing-006), sub-headings in sentence case.
- No `\tag`, no `align` inside `$$`.
- Unicode Greek in code (qe-code-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace every `\begin{array}` with `\begin{bmatrix}` and drop `\left[ \right]'` (qe-math-003).
2. Replace all `'` transposes with `^\top` (qe-math-002).
3. Add `:name: fig-...` fields (qe-fig-005).
