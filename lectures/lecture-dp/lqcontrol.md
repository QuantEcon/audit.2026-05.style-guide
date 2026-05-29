# Style Audit — lqcontrol

- **Series:** lecture-dp
- **File:** `lectures/lqcontrol.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 5.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | Title Case H2/H3 headings throughout; some short paragraphs. |
| Math         | 3/10  | Apostrophe transpose everywhere; matrices use `\left(\begin{array}\right)` not `bmatrix`. |
| Code         | 7/10  | Unicode Greek; pip-install at top; PEP8 mostly OK; figsize used 5×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | Title-Case `'Time'` xlabel (4×); `figsize=` 5×; 5 static PNG figures used as solutions. |
| References   | 7/10  | All citations parenthetical via `{cite}`; no narrative-author cases requiring `{cite:t}`. |
| Links        | 4/10  | Two raw markdown links to `python-advanced.quantecon.org` instead of `{doc}` form. |
| Admonitions  | 8/10  | Exercises use labels + `exercise-start`/`solution-start` correctly; `:class: dropdown` on solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Apostrophe `'` used as transpose throughout the file (e.g. `x_t' R x_t`, `u_t' Q u_t`, `A' P_T A`, `B' P_T B`). *Lines:* 100, 253, 271, 293, 316, 480, 494-495, 503, 513-514, 524, 536, 600, 809, 940. *Count:* 70+ occurrences.
- **[qe-math-003]** — Matrices use `\left( \begin{array}{...} ... \end{array} \right)` rather than `bmatrix`. *Lines:* 170, 176, 182, 188, 195, 213, 221, 229, 237, 623, 631, 976, 986, 996, 1006, 1028, 1038. *Count:* 17 array-matrix blocks.
- **[qe-writing-006]** — Systemic Title Case on H2/H3 headings. *Examples:* `### The Law of Motion` (84), `## Optimality -- Finite Horizon` (298), `### The Objective` (305), `### Time-Varying Parameters` (785), `### Adding a Cross-Product Term` (800), `### Infinite Horizon` (842), `### Certainty Equivalence` (910), `## Further Applications` (920), `### Application 1: Age-Dependent Income Process` (923). *Count:* 12+ headings.

### Medium severity
- **[qe-math-010 (proposed)]** — Expectation uses bare `\mathbb E` without braces (line 100). *Count:* 1.
- **[qe-fig-006]** — Title-Case `xlabel('Time')` on 4 figures. *Lines:* 702, 770, 1348, 1497. Should be lowercase `'time'`.
- **[qe-fig-001]** — `figsize=` set 5 times. *Lines:* 683, 753, 1330, 1479, 1542. Most plots do not need an explicit `figsize`.
- **[qe-fig-002]** — 5 static PNG figures referenced (`solution_lqc_ex1.png`, `solution_lqc_ex2.png`, `solution_lqc_ex3_g1.png`, `solution_lqc_ex3_g10.png`, `solution_lqc_ex3_g50.png`). *Lines:* 1051, 1121, 1197, 1201, 1205. Prefer code-generated figures.
- **[qe-link-002]** — Two raw markdown links to `python-advanced.quantecon.org` (`lu_tricks.html`, `classical_filtering.html`) where `{doc}` with intersphinx is preferred. *Line:* 54. *Count:* 2.
- **[qe-writing-001]** — Many multi-sentence paragraphs (e.g. 138-140, 156-162).

### Low severity
- **[qe-writing-005]** — "**Riccati equations**" (line 53) bolded but never formally introduced as a definition.

## Strengths
- Lecture title correctly Title Case.
- Equation labels and `{eq}` cross-references used cleanly throughout.
- No `\tag`, no `align` inside `$$`, no `i.i.d.`.
- Greek letters in narrative and code use plain Unicode where relevant.
- pip install correctly placed at top of lecture.
- Exercises use proper `exercise-start`/`solution-start` gating with labels.
- Solutions wrapped in `:class: dropdown`.

## Recommended actions
1. Replace every `'` used as transpose with `^\top` — biggest single fix.
2. Replace every `\left(\begin{array}{...} ... \end{array}\right)` matrix with `\begin{bmatrix} ... \end{bmatrix}`.
3. Convert all H2/H3 headings to sentence case.
4. Lowercase `'Time'` axis labels to `'time'`.
5. Replace markdown URL links to `python-advanced.quantecon.org` with `{doc}` intersphinx references.
6. Regenerate the 5 static `solution_lqc_ex*.png` figures from the solution code cells instead of bundling PNGs.
7. Standardize `\mathbb E` to `\mathbb{E}`.
