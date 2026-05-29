# robustness

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/robustness.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 4.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title in Title Case; sentence-case headings; mostly one-sentence paragraphs. |
| Math         | 2/10  | Pervasive prime as transpose; `\mathbf w` for vector. |
| Code         | 7/10  | Mixed unicode/spelled Greek (7 vs 4); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 3 `{figure}` directives reference static PNGs; no `figsize=`; no `:name:` fields. |
| References   | 7/10  | 3 `{cite}` used; never `{cite:t}`. |
| Links        | 3/10  | 5 raw `python.quantecon.org/lqcontrol.html` URLs throughout. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Prime `'` used as transpose throughout. *Example:* `J(x) = x' P x`, `B' \mathcal D(P) B`, `w_t' w_t`, `(I - \theta^{-1} C' P C)^{-1}`. *Count:* ~93 occurrences.
- **[qe-math-004]** — Bold `\mathbf w` used for vectors throughout. *Example:* `lectures/robustness.md:388`, `:389`, `:397`, `:412`, `:417`, `:429`, `:441`, `:450`, `:510`, `:530`. *Count:* ~13 occurrences.
- **[qe-link-002]** — 5 raw `python.quantecon.org/lqcontrol.html` URLs. *Example:* `lectures/robustness.md:164`, `:319`, `:452`, `:617`, `:1154`. *Count:* 5 occurrences.

### Medium severity
- **[qe-fig-002]** — 3 `{figure}` directives reference static schematic PNGs.

### Low severity
- **[qe-writing-005]** — `*robust*`, `*Robust*`, `*approximating model*`, `*secret weapon*`, `*bounds*` italics for emphasis — borderline OK.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case subheadings (qe-writing-006).
- One-sentence paragraph rule respected (qe-writing-001).
- Equation labels and `{eq}` references (qe-math-007).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Replace `'` with `^\top` for transpose throughout (qe-math-002).
2. Replace `\mathbf w` with plain `w` (qe-math-004).
3. Convert raw `python.quantecon.org/lqcontrol.html` URLs to `{doc}\`intermediate:lqcontrol\`` (qe-link-002).
4. Add `:name: fig-...` fields (qe-fig-005).
