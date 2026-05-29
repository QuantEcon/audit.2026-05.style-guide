# Style Audit — matplotlib

- **Series:** lecture-python-programming
- **File:** `lectures/matplotlib.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Heading Title Case is pervasive; otherwise good prose. |
| Math         | N/A   | Only `y = sin(x)` label decorations. |
| Code         | 7/10  | Only Anaconda packages; Greek unicode (θ) used in solution; teaches `figsize`, `set_title`, `rcParams` overrides — pedagogically necessary but conflicts with figure rules elsewhere; mixes `from random import uniform` with NumPy. |
| JAX          | out of scope | — |
| Figures      | 4/10  | This is a Matplotlib tutorial, so qe-fig-003 (`ax.set_title('Test plot')` at line 137; `plt.suptitle(f'Style: {style_name}', ...)` at line 317), qe-fig-001 (`figsize=(10, 12)` line 183; `figsize=(10, 6)` line 213; `figsize=(10, 3)` line 289; `figure.figsize` set in `rcParams` line 392), and qe-fig-009 are all *demonstrated* on purpose. Even so, the lecture does not explicitly call out that these are anti-patterns elsewhere. |
| References   | N/A   | No citations. |
| Links        | 9/10  | Only external doc links; no improper cross-series URLs. |
| Admonitions  | 8/10  | `{exercise-start}` / `{solution-start}` pair correctly gated; `:class: dropdown`; `{note}` admonition used; one `{image}` inside the exercise body (qe-fig-011 compliant). |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Section headings systematically use Title Case. *Examples:* line 38 `### Matplotlib's Split Personality`, line 50 `## The APIs`, line 55 `### The MATLAB-style API`, line 78 `### The Object-Oriented API`, line 99 `### Tweaks`, line 141 `## More Features`, line 148 `### Multiple Plots on One Axis`, line 172 `### Multiple Subplots`, line 194 `### 3D Plots`, line 226 `### A Customizing Function`, line 265 `### Style Sheets`, line 439 `## Further Reading`, line 447 `## Exercises`. *Count:* 13 occurrences.
- **[qe-fig-003]** — Embedded titles in matplotlib figures. *Examples:* line 137 `ax.set_title('Test plot')`, line 317 `plt.suptitle(f'Style: {style_name}', fontsize=13)`. *Context:* this is a Matplotlib teaching lecture, so titles are part of the exposition — arguably an instructional exception, but they should be flagged or the demos converted to use figure-directive titles.
- **[qe-fig-001]** — Multiple explicit `figsize` values (lines 183, 213, 289, 392). Same caveat as above: this lecture explicitly teaches how to use these knobs.

### Medium severity
- **[qe-fig-005]** — No `name:` metadata on any of the code-generated figures.

### Low severity
- **[qe-writing-001]** — A few descriptive paragraphs combine clauses (e.g., lines 88–91 enumeration could be condensed).
- **[qe-code-001]** — `from random import uniform` (line 159) is used alongside numpy code; idiomatic in matplotlib examples but mixes RNG sources.

## Strengths
- Lecture title uses `{index}` role with proper case per qe-writing-006.
- Clean MyST roles and code-cells.
- One-sentence paragraphs are the dominant style.
- The exercise uses `{image}` (not `{figure}`) inside the gated `exercise-start`/`exercise-end` block per qe-fig-011.
- Greek unicode (θ) used in the exercise solution per qe-code-002.

## Recommended actions
1. Convert headings to sentence case ("Matplotlib's split personality", "The APIs", "The MATLAB-style API", "The object-oriented API", "Tweaks", "More features", "Multiple plots on one axis", "Multiple subplots", "3D plots", "A customizing function", "Style sheets", "Further reading").
2. Either add inline notes that `ax.set_title(...)` and `figsize` are demonstrated-but-discouraged in production lectures, or convert the relevant demos to figure-directive titles where possible.
3. Add `name:` metadata to a handful of representative figures.
