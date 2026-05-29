# doubts_or_variability

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/doubts_or_variability.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case (with `?`); sentence-case headings; one-sentence paragraphs. |
| Math         | 4/10  | 50 bare `E_t`/`E_0`; 23 `\mathcal{N}`; uses `\top` correctly however. |
| Code         | 6/10  | Mixed spelled/unicode Greek (34 spelled vs 21 unicode); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 9 `figsize=`; modern figure metadata; mixed capitalisation in axis labels. |
| References   | 9/10  | 28 `{cite}` and 20 `{cite:t}` correctly used. |
| Links        | 8/10  | 5 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | 8/10  | 11 gated exercises and 11 solutions with `:class: dropdown` — exemplary. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — 50 bare `E_t`/`E_0` for expectation instead of `\mathbb{E}`. *Count:* 50 occurrences.
- **[qe-math-011 (proposed)]** — 23 `\mathcal{N}` used as Normal distribution. *Count:* 23 occurrences.

### Medium severity
- **[qe-fig-001]** — 9 `figsize=` settings.
- **[qe-code-002]** — Spelled-out Greek (34 occurrences) mixed with unicode.

### Low severity
- **[qe-writing-009 (proposed)]** — 3 "i.i.d." occurrences in text.

## Strengths
- Title in Title Case with question mark (qe-writing-006).
- One-sentence paragraph rule followed (qe-writing-001).
- `\top` used for transpose (16 occurrences) (qe-math-002).
- Heavy correct use of `{cite:t}` and `{cite}` (qe-ref-001).
- Modern figure metadata with `mystnb: figure: caption: ... name: fig-...` (qe-fig-005).
- Exercises gated; solutions with `:class: dropdown` (qe-admon-001, qe-admon-002).
- `{doc}` for cross-series references (qe-link-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert bare `E_t`/`E_0` to `\mathbb{E}` notation (qe-math-010, proposed).
2. Replace `\mathcal{N}` with `N` (qe-math-011, proposed).
3. Reduce `figsize=` usage (qe-fig-001).
4. Standardise on unicode Greek in code (qe-code-002).
5. Replace "i.i.d." with "IID" (qe-writing-009, proposed).
