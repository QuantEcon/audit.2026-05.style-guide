# lqramsey

- **Series:** lecture-dp
- **File:** `lectures/lqramsey.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2/H3 mostly sentence case. |
| Math         | 8/10  | `\mathbb E` consistently without braces; otherwise clean. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 2×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 6/10  | Three Title-Case `'Time'` xlabels; no embedded titles; figsize 2×. |
| References   | 6/10  | Three narrative-author `{cite}` patterns (e.g. "Lucas-Stokey (1983) {cite}…"). |
| Links        | 9/10  | No raw cross-series URLs. |
| Admonitions  | 9/10  | One `exercise-start`/`exercise-end` + `solution-start`/`solution-end` with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-math-010 (proposed)]** — `\mathbb E` written without braces in nearly every display equation (lines 117, 128, 206, 262, 275, 331). *Count:* 6+.
- **[qe-writing-004]** — `\mathscr L` used for the Lagrangian (line 274); prefer plain letter or `\mathcal{L}`.
- **[qe-ref-001]** — Three narrative-author `{cite}` patterns. Should be `{cite:t}`.
- **[qe-fig-006]** — Three Title-Case `xlabel('Time')` calls. *Lines:* 780, 835, 842.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` set 2 times.

## Strengths
- Lecture title in correct Title Case.
- H2/H3 headings sentence case.
- Definitions italic/bold consistent (*feasible*, *equilibrium*, *Ramsey problem*, *Ramsey plan*).
- "IID" used correctly.
- Equation labels and `{eq}` references used cleanly.
- No transpose violations, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek in code.
- Exercise uses `exercise-start`/`solution-start` with `:label:` and dropdown.

## Recommended actions
1. Add braces consistently: `\mathbb E` → `\mathbb{E}`.
2. Replace `\mathscr L` with `\mathcal{L}` or plain `L`.
3. Switch narrative `Author {cite}…` to `{cite:t}` form.
4. Lowercase `'Time'` axis labels.
