# risk_aversion_or_mistaken_beliefs

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/risk_aversion_or_mistaken_beliefs.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case (with `?`); sentence-case headings; one-sentence paragraphs. |
| Math         | 4/10  | 18 `\mathcal{N}`; 10 bare `E_t`; 69 correct `\top` for transpose. |
| Code         | 6/10  | Mixed spelled/unicode Greek (10 spelled vs 5 unicode); no install cell (uses numpy/scipy — OK). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 4/10  | 10 `figsize=`; 3 `set_xlabel` with capitalised content; 3 `{figure}` static images. |
| References   | 9/10  | 12 `{cite}` and 12 `{cite:t}` correctly distinguished. |
| Links        | 8/10  | 13 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | 8/10  | 3 gated exercises and 3 solutions with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-011 (proposed)]** — 18 `\mathcal{N}` used as Normal distribution. *Count:* 18 occurrences.
- **[qe-math-010 (proposed)]** — 10 bare `E_t` instead of `\mathbb{E}_t`. *Count:* 10 occurrences.
- **[qe-fig-001]** — 10 `figsize=` settings — systemic.

### Medium severity
- **[qe-fig-006]** — `set_xlabel` with capitalised labels (e.g. "Mean", "Probability") — 3 occurrences.
- **[qe-fig-002]** — 3 `{figure}` directives reference static PNGs.
- **[qe-code-002]** — Mixed spelled/unicode Greek (10 spelled vs 5 unicode).

### Low severity
- **[qe-fig-005]** — Some figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case with question mark (qe-writing-006).
- Sentence-case headings (qe-writing-006).
- One-sentence paragraph rule followed (qe-writing-001).
- Heavy correct use of `{cite:t}` (qe-ref-001) — 12 occurrences.
- `\top` heavily used for transpose (69 occurrences) (qe-math-002).
- Modern figure metadata with captions and names where present (qe-fig-005).
- Exercises gated; solutions with `:class: dropdown` (qe-admon-001, qe-admon-002).
- `{doc}` for cross-series references (qe-link-002).

## Recommended actions
1. Replace `\mathcal{N}` with `N` (qe-math-011, proposed).
2. Convert bare `E_t` to `\mathbb{E}_t` (qe-math-010, proposed).
3. Reduce `figsize=` usage (qe-fig-001).
4. Lowercase axis labels (qe-fig-006).
5. Code-generate static figures where feasible (qe-fig-002).
6. Standardise on unicode Greek in code (qe-code-002).
