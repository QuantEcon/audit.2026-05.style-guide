# Style Audit — mccall_model_with_sep_markov

- **Series:** lecture-dp
- **File:** `lectures/mccall_model_with_sep_markov.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; one "iid" slip. |
| Math         | 9/10  | `\mathbb{1}` used correctly for indicator; clean math. |
| Code         | 7/10  | Unicode Greek; pip install at top; PEP8; figsize 5×. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 7/10  | One `ax.set_title(...)` with f-string; figsize 5×; lowercase labels. |
| References   | N/A   | No `{cite}` directives. |
| Links        | 9/10  | `{doc}` used 3×; no raw cross-series URLs. |
| Admonitions  | 9/10  | Exercise + solution-start with dropdown. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-009 (proposed)]** — "iid" used in narrative on line 713. Should be "IID".
- **[qe-fig-003]** — One f-string `ax.set_title(f'Cross-sectional distribution at t={t_snapshot}, ...')` (line 880).
- **[qe-fig-001]** — `figsize=` set 5 times.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs (e.g. 43-47, 700-706, 720-726).

## Strengths
- Lecture title correctly Title Case.
- All H2/H3 headings sentence case.
- `\mathbb{1}` used for the indicator (line 734).
- No transpose violations; no bold vectors; equation labels and references clean.
- "IID" correctly capitalised elsewhere (e.g. line 41, line 100).
- pip install at top; Unicode Greek in code.
- `{doc}` used for cross-series.
- Exercise uses `{exercise}` + `solution-start` with `:class: dropdown`.

## Recommended actions
1. Change "iid" → "IID" on line 713.
2. Remove the f-string `ax.set_title(...)` call.
3. Reduce unnecessary `figsize=` usage.
4. Tighten the few multi-sentence paragraphs.
