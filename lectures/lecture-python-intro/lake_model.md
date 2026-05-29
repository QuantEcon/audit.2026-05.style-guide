# Style Audit — lake_model

- **Series:** lecture-python-intro
- **File:** `lectures/lake_model.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case; H2 mostly sentence case; "## The Lake model" minor concern. |
| Math         | 9/10  | `\top` for transpose; `\mathbb{1}` for ones vector (M3 compliant); bmatrix. |
| Code         | 8/10  | Unicode Greek (`α`, `b`, etc.) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 5/10  | `figsize=` on lines 171, 315, 470, 552; 3 `ax.set_title('Unemployment'/'Employment'/'Labor force')` outside exercise context (175, 178, 181) — short Title-Case labels; 1 `{figure}` directive (line 42) with `:name: lake_model_graphviz` — qe-fig-005 OK; 2 spines manipulations. |
| References   | N/A   | no `{cite}` citations |
| Links        | N/A   | no cross-series links |
| Admonitions  | 8/10  | 1 solution gated, dropdown, exercise-linked; 2 exercises. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-fig-001]** — `figsize=` overrides on lines 171, 315, 470, 552. *Count:* 4 occurrences.
- **[qe-fig-003]** — `ax.set_title('Unemployment')`, etc. outside exercise context. *Examples:* lines 175, 178, 181. *Count:* 3 occurrences.

### Low severity
- **W3** — "## The Lake model" (line 25) — "Lake model" is debatable; if treated as proper-noun-like model name, fine; otherwise sentence case would prefer "## The lake model".
- **W1** — Some short two-sentence paragraphs.
- **[qe-fig-007]** — 2 `spines[*].set_color(...)` / `set_position(...)` calls (similar to qe-fig-007).

## Strengths
- M3 compliant: uses `\mathbb{1}` with explicit explanation ("let $\mathbb{1}=[1,1]^\top$ be a vector of ones").
- Transpose `^\top` consistent (M2 OK).
- bmatrix throughout (M4 OK).
- Section headings generally sentence case.
- 1 `{figure}` directive with `:name: lake_model_graphviz` (qe-fig-005 partially compliant).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Move `ax.set_title` content (Unemployment/Employment/Labor force) into mystnb metadata or `{figure}` captions.
2. Remove `figsize=` overrides.
3. Drop spine manipulations.
