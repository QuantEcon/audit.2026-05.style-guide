# Style Audit — additive_functionals

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/additive_functionals.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 4/10  | Systemic bare `E_0`/`E[\cdot]`; `{\cal N}` for Normal distribution. |
| Code         | 6/10  | `alpha`, `beta`, `gamma` spelled out; `ax.set_title` used in one cell. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 9 `figsize=` settings; `ax.set_title` (L?); no `:name:` fields. |
| References   | 7/10  | `{cite}` used 8 times; never uses `{cite:t}` despite multiple in-text author refs. |
| Links        | 6/10  | Three raw `python.quantecon.org` / `python-intro.quantecon.org` URLs alongside no `{doc}`. |
| Admonitions  | 7/10  | 3 exercises and 3 solutions with `:class: dropdown`; not using `prf:` prefix for non-existent proofs (N/A). |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Bare `E_0`, `E_t`, `E[...]` used throughout instead of `\mathbb{E}`. *Example:* `lectures/additive_functionals.md:951`, `:1007`, `:1029`, `:1098`, `:1294`, `:1296`, `:1318`, `:1327`, `:1400`. *Count:* 12 occurrences.
- **[qe-fig-001]** — `figsize=` set 9 times without justification (qe-fig-001 plus systemic pattern). 

### Medium severity
- **[qe-math-011 (proposed)]** — `{\cal N}` used as the Normal distribution. *Example:* `lectures/additive_functionals.md:101`, `:103`, `:120`. *Count:* 4 occurrences.
- **[qe-link-002]** — Raw cross-series URLs (`python-intro.quantecon.org/linear_models.html`, `python.quantecon.org/likelihood_ratio_process.html`). *Example:* `lectures/additive_functionals.md:128`, `:226`, `:772`, `:1278`, `:1284`. *Count:* 3-5 occurrences.
- **[qe-code-002]** — Spelled-out Greek (`alpha`, `beta`, `gamma`) in code parameters instead of unicode. *Count:* ~7 assignments.
- **[qe-ref-001]** — Multiple narrative-style author references (e.g. Hansen and Scheinkman 2009) without converting to `{cite:t}`. 

### Low severity
- **[qe-fig-003]** — One `ax.set_title` occurrence.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- `\begin{bmatrix}` used consistently (qe-math-003) at L133–174.
- Sequences in curly brackets `\{y_t\}` (qe-math-005) at L106, L123.
- Title in Title Case (qe-writing-006); subheadings sentence case (qe-writing-006).
- Equation labels and `{eq}` references used throughout (qe-math-007).
- Install cell at top with `hide-output` (qe-code-003).
- Exercises gated; solutions use `:class: dropdown` (qe-admon-002).

## Recommended actions
1. Replace all bare `E` / `E_t` / `E[...]` with `\mathbb{E}` / `\mathbb{E}_t` (qe-math-010, proposed).
2. Replace `{\cal N}` with `N` (qe-math-011, proposed).
3. Convert raw cross-series URLs to `{doc}\`intermediate:linear_models\`` style (qe-link-002).
4. Use unicode Greek letters in code (qe-code-002).
5. Add `:name: fig-...` to figures (qe-fig-005).
