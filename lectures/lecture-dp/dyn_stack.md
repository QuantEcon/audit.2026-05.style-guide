# dyn_stack

- **Series:** lecture-dp
- **File:** `lectures/dyn_stack.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Mostly sentence-case headings; proper-noun capitalisation correct. |
| Math         | 4/10  | Apostrophe transpose throughout LQ section; `\vec` used. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize used 3×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | Three `ax.set_title(...)` calls and 3 Title-Case axis labels. |
| References   | 9/10  | Citations parenthetical via `{cite}`; no narrative-author misuse. |
| Links        | 3/10  | Five raw markdown links to `python.quantecon.org` / `python-intro.quantecon.org` instead of `{doc}`. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Apostrophe `'` used as transpose throughout the LQ derivation (e.g. `y' R y`, `u' Q u`, `B'PB`, `B'PA`, `A'PB`, `\Sigma_t A'`, `CC'`, `F'P F'`). *Lines:* 355 onwards. *Count:* 30+ occurrences.
- **[qe-link-002]** — Five raw markdown links to other QuantEcon series: `python.quantecon.org/lagrangian_lqdp.html` (line 42), `python-intro.quantecon.org/lqcontrol.html` (lines 324, 519), `python-intro.quantecon.org/rational_expectations.html` (line 814), `python.quantecon.org/markov_perf.html` (line 1411). Should be `{doc}` intersphinx references.

### Medium severity
- **[qe-math-004]** — `\vec a`, `\vec y`, `\vec u`, `\vec q` used 24 times.
- **[qe-fig-003]** — Three `ax.set_title(...)` calls. *Lines:* 1031, 1364, 1429.
- **[qe-fig-006]** — Three Title-Case axis labels: `set_xlabel('Time')` etc.

### Low severity
- **[qe-fig-001]** — `figsize=` set 3 times.
- **[qe-writing-001]** — Several multi-sentence paragraphs.

## Strengths
- Lecture title in correct Title Case.
- H2/H3 headings mostly sentence case with proper-noun capitalisation (Stackelberg, Markov, Bellman).
- Matrices use `bmatrix` consistently (42 matrix blocks).
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- `aligned` used inside `$$`.
- pip install at top; Unicode Greek.
- No `\tag`, no bold vectors (apart from `\vec`), no `align`-inside-`$$` issues.

## Recommended actions
1. Replace every `'` used as transpose with `^\top` (highest priority).
2. Drop `\vec` arrows on sequence symbols.
3. Remove the 3 `ax.set_title(...)` calls.
4. Convert raw markdown URLs to `{doc}` intersphinx references for 5 cross-series links.
5. Lowercase Title-Case axis labels.
6. Tighten multi-sentence paragraphs.
