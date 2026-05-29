# Style Audit — dovis_accounting_mf

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/dovis_accounting_mf.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; one-sentence paragraphs. |
| Math         | 7/10  | Some `\mathcal{N}` use; `\top` used correctly. |
| Code         | 7/10  | Mixed unicode Greek (12 spelled vs 20 unicode); install cell with `hide-output`. JAX-related (out-of-scope per instructions). |
| JAX          | N/A   | JAX is out of scope per series instructions. |
| Figures      | 5/10  | 7 `figsize=`; 1 `ax.set_title`; 2 `spines.set_visible(False)` (qe-fig-007). |
| References   | 9/10  | 20 `{cite}` and 18 `{cite:t}` correctly distinguished. |
| Links        | 8/10  | 2 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | 8/10  | 2 gated exercises and 2 solutions with `:class: dropdown`; GPU warning admonition correctly tagged. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — 7 `figsize=` settings without justification.
- **[qe-fig-007]** — 2 `ax.spines[...].set_visible(False)` removing default box.

### Medium severity
- **[qe-math-011 (proposed)]** — `\mathcal{N}` used as Normal distribution. *Count:* 1 occurrence.
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.
- **[qe-code-002]** — Mixed unicode/spelled Greek in code.

### Low severity
_None found._

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case headings (qe-writing-006).
- One-sentence paragraph rule followed (qe-writing-001).
- Heavy correct use of `{cite:t}` (qe-ref-001) — 18 occurrences.
- `\top` used for transpose (qe-math-002).
- Modern figure metadata with captions and names (qe-fig-005).
- Exercises gated; solutions with `:class: dropdown` (qe-admon-001, qe-admon-002).
- GPU warning admonition (qe-code-006).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Reduce `figsize=` usage (qe-fig-001).
2. Remove `spines.set_visible(False)` calls (qe-fig-007).
3. Replace `\mathcal{N}` with `N` (qe-math-011, proposed).
4. Remove `ax.set_title` (qe-fig-003).
5. Standardise on unicode Greek in code (qe-code-002).
