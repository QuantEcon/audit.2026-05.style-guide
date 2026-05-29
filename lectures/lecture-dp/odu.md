# Style Audit — odu

- **Series:** lecture-dp
- **File:** `lectures/odu.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.7 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Many Title Case H3 headings; right curly quotes. |
| Math         | 7/10  | `\mathbf{1}` indicator; `\operatorname{Beta}` instead of `\mathrm{Beta}`. |
| Code         | 5/10  | Installs `interpolation` (binary, non-Anaconda) without notes; Unicode Greek; figsize 7×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 6/10  | One `ax.set_title('Unemployment rate')`; one Title-Case xlabel `'Time'`; figsize 7×. |
| References   | 9/10  | 5 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 6/10  | Four raw markdown links to `python.quantecon.org` / `python-intro.quantecon.org`. |
| Admonitions  | 8/10  | Exercises labelled + dropdown solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Many Title Case H2/H3 headings. *Examples:* `### Model Features` (70), `### The Basic McCall Model` (82), `### Offer Distribution Unknown` (116), `### Parameterization` (211), `### Looking Forward` (242), `## Take 1: Solution by VFI` (269), `## Take 2: A More Efficient Method` (484), `## Another Functional Equation` (499), `## Solving the RWFE` (551), `## Appendix A` (769), `## Appendix B` (855), `## Examples` (1062). *Count:* 10+ headings.
- **[qe-code-006]** — `!pip install interpolation` (line 33) — binary/scientific-Python package not in Anaconda, no installation notes provided.

### Medium severity
- **[qe-math-008]** — `\mathbf{1}` used as indicator function (line 113). Should be `\mathbb{1}` and explained.
- **[qe-math-011 (proposed)]** — `\operatorname{Beta}` (lines 216, 217) used for the distribution; style guide recommends `\mathrm{Beta}`.
- **[qe-fig-001]** — `figsize=` set 7 times — high.
- **[qe-fig-003]** — `ax.set_title('Unemployment rate')` on line 850.
- **[qe-fig-006]** — Title-Case `xlabel('Time')` on line 849.
- **[qe-link-002]** — Four raw markdown links to `python.quantecon.org` / `python-intro.quantecon.org` instead of `{doc}` form.

### Low severity
- **[qe-writing-009 (proposed)]** — Right curly apostrophes ’ used in narrative instead of straight `'` (lines 27, 38, 41, 78, 118).

## Strengths
- Lecture title correctly Title Case.
- `\mathbb{P}` used for probability with `\{ \}` for events (lines 167-175).
- `\mathbb{E}` used (line 97).
- "IID" used correctly.
- Equation labels and `{eq}` references used cleanly.
- No transpose violations, no matrix-bracket issues, no `\tag`, no `align` issues.
- Unicode Greek in code (`σ`, `π`, `β`).
- Exercises use labels + dropdown solutions.

## Recommended actions
1. Convert all Title Case H2/H3 headings to sentence case.
2. Replace `\mathbf{1}\{ … \}` with `\mathbb{1}\{ … \}` and introduce the notation.
3. Replace `\operatorname{Beta}` with `\mathrm{Beta}`.
4. Add a note about the `interpolation` package installation requirements, or move installation to a `pip install` cell in a way consistent with other lectures.
5. Remove the `ax.set_title(...)` call; lowercase the `'Time'` xlabel.
6. Convert 4 raw cross-series markdown URLs to `{doc}` form.
7. Normalise smart-quotes back to straight `'`.
