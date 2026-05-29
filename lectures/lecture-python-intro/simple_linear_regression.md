# Style Audit — simple_linear_regression

- **Series:** lecture-python-intro
- **File:** `lectures/simple_linear_regression.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Lecture has only 2 H2 sections; lacks an Overview/structure; many random sentences ending without period; capitalization issues in prose. |
| Math         | 7/10  | Equations basic; no clear M violations; minor style. |
| Code         | 8/10  | Unicode Greek (`α`, `β`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 8/10  | No `figsize=`/`ax.set_title`/spine violations. |
| References   | N/A   | no `{cite}` citations |
| Links        | N/A   | no cross-series links |
| Admonitions  | N/A   | no exercises / solutions |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W1** — Many short paragraphs lack period termination ("Let's start with $\alpha = 5$ and $\beta = 10$" line 83, "Let's first look at the Life Expectancy Data" line 463, "Which country does report this data?" 472, etc.). Many sentences in the body lack punctuation, indicating a draft-quality lecture.
- **W7** — Random Title Case mid-sentence: "Life Expectancy Data" (line 463), "Year 1543" (470), "Get Data from DataFrame" (530), "Sums" (542), "GDP per Capita" (511).

### Low severity
- **W3** — "## How does error change with respect to $\alpha$ and $\beta$" lacks final question mark/period (line 191).
- **W4/W5** — Quoted "best" (line 30, 77, 106) used inconsistently; better to use *italic* for emphasis.

## Strengths
- H1 in Title Case (W2 OK).
- Simple, clear walkthrough.
- Unicode Greek in code (qe-code-002 OK).
- No matplotlib title/figsize/spine violations.

## Recommended actions
1. Finish punctuation on sentences throughout.
2. Add a proper Overview H2 and structural sections.
3. Fix random Title Case in prose (W7).
4. Switch quoted emphasis to italic.
5. Consider adding exercises/solutions with gated form and `:class: dropdown` to align with series convention.
