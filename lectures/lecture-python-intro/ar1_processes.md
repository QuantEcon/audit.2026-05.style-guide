# Style Audit — ar1_processes

- **Series:** lecture-python-intro
- **File:** `lectures/ar1_processes.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3 sentence case; clean one-sentence paragraphs. |
| Math         | 7/10  | Sequences `\{X_t\}` OK; "iid" used (W6 violation) in one place; uses `\mathbb E` for expectation. |
| Code         | 8/10  | Unicode Greek used in code (`α`, `β`, etc.); `plt.rcParams["figure.figsize"]` set globally (line 46). |
| JAX          | out of scope | — |
| Figures      | 7/10  | Global `plt.rcParams["figure.figsize"]` override (line 46); no `:name:` on figures; no `ax.set_title` violations outside exercises. |
| References   | 7/10  | `{cite}` used; line 335 "textbook by {cite}\`MeynTweedie2009\`" is in-text and should be `{cite:t}`. |
| Links        | N/A   | no external cross-series links |
| Admonitions  | 9/10  | `{prf:example}` used (qe-admon-004 OK); solutions use `:class: dropdown` and exercise labels (qe-admon-002, qe-admon-005 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W6** — "iid" written lowercase on line 563 in an exercise; "IID" used correctly elsewhere (line 83). *Count:* 1 inconsistency.
- **[qe-ref-001]** — In-text citation should use `{cite:t}` not `{cite}`. *Example:* `lectures/ar1_processes.md:335` ("The textbook by {cite}\`MeynTweedie2009\`"). *Count:* 1 occurrence.

### Low severity
- **W1** — A few two-sentence paragraphs.
- **W7** — `\psi_t` label inside string with leading `$\psi_t$` — fine.
- **[qe-fig-001]** — Sets `plt.rcParams["figure.figsize"] = (11, 5)` globally (line 46) — overrides `_config.yml` defaults.
- **[qe-fig-005]** — No figures use the `{figure}` directive with `:name:` for cross-referencing.

## Strengths
- Sequences use `\{X_t\}` (M6 OK).
- `\mathbb E` for expectation (M7 OK).
- Distribution name `N(\mu, \sigma^2)` plain (M9 OK).
- Equation labels with `{math}` `:label:` (M14 OK).
- Bold for definitions (**AR(1) model**, **stochastic difference equation**).
- Unicode Greek letters used in code (qe-code-002 OK).
- Solutions use `:class: dropdown` and reference their exercise labels (qe-admon-002, qe-admon-005 OK).

## Recommended actions
1. Change "iid" → "IID" on line 563.
2. Convert "by {cite}\`MeynTweedie2009\`" to `{cite:t}` form on line 335.
3. Remove the global `plt.rcParams["figure.figsize"]` override and rely on `_config.yml` defaults.
