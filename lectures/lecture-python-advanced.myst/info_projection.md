# Style Audit — info_projection

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/info_projection.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; one-sentence paragraphs. |
| Math         | 6/10  | 14 bare `E[`/`E(`; no `\mathcal{N}`; no transpose violations. |
| Code         | 7/10  | Mixed unicode (8) and spelled (7) Greek; no install cell (uses numpy/scipy — OK). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | Modern figure metadata with captions and names; 2 `figsize=`. |
| References   | 9/10  | 12 `{cite}` and 8 `{cite:t}` correctly distinguished. |
| Links        | 8/10  | 3 `{doc}` references (incl. `intermediate:divergence_measures`, `intermediate:linear_models`); no raw cross-series URLs. |
| Admonitions  | 8/10  | 4 gated exercises and 4 solutions with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-010 (proposed)]** — 14 bare `E[`/`E(` instead of `\mathbb{E}`. *Count:* 14 occurrences.
- **[qe-code-002]** — Mixed spelled/unicode Greek in code.

### Low severity
- **[qe-fig-001]** — 2 `figsize=` settings.

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case headings (qe-writing-006).
- One-sentence paragraph rule followed (qe-writing-001).
- Heavy correct use of `{cite:t}` for narrative author refs (qe-ref-001).
- Modern figure metadata with `caption:` and `name: fig-...` (qe-fig-005).
- Exercises gated; solutions with `:class: dropdown` (qe-admon-001, qe-admon-002).
- `{doc}\`intermediate:...\`` for cross-series references (qe-link-002).

## Recommended actions
1. Convert bare `E[`/`E(` to `\mathbb{E}` notation (qe-math-010, proposed).
2. Standardise on unicode Greek in code (qe-code-002).
