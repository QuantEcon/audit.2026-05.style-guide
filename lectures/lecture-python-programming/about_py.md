# Style Audit — about_py

- **Series:** lecture-python-programming
- **File:** `lectures/about_py.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10| Pervasive Title Case in H3 section headings; one H2 also Title Case. |
| Math         | N/A   | Only a trivial inline integral example. |
| Code         | 8/10  | Demo code snippets are well-formed; `skip-execution` tag used on Python CSV demo; no non-Anaconda packages needed (networkx, scipy are demo only and Anaconda-shipped). |
| JAX          | out of scope | — |
| Figures      | 6/10  | Four static `{figure}` directives use scaled PNGs without `name:` labels or captions (lines 140, 411, 417, 423); the PyTorch chart could plausibly be re-generated programmatically but is a Stack Overflow Trends screenshot, so static is justified. |
| References   | N/A   | No citations. |
| Links        | 7/10  | One bare URL to a sibling series: line 84 `[JAX](https://jax.quantecon.org/intro.html)` — should be `{doc}`jax:intro` per qe-link-002. |
| Admonitions  | 9/10  | `{epigraph}`, `{index}` and `{code-block}` directives used cleanly; no nested-tick risk. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Most H3 section headings are Title Case rather than sentence case. *Examples:* line 50 `### Can't I Just Use LLMs?`, line 69 `### Isn't MATLAB Better?`, line 101 `### Common Uses`, line 127 `### Relative Popularity`, line 146 `### Features`, line 159 `### Syntax and Design`, line 252 `### The AI Connection`, line 291 `### NumPy`, line 347 `### NumPy Alternatives`, line 396 `### Graphics`, line 438 `### Networks and Graphs`, line 493 `### Other Scientific Libraries`. *Count:* 12+ occurrences.

### Medium severity
- **[qe-writing-006]** — One H2 section heading uses Title Case: line 269 `## Scientific Programming with Python`.
- **[qe-link-002]** — Direct URL to a sibling series instead of `{doc}` link with intersphinx prefix. *Example:* line 84 `[JAX](https://jax.quantecon.org/intro.html)` — should be `` {doc}`jax:intro` ``.
- **[qe-fig-005]** — All four `{figure}` directives lack a `name:` field, so they cannot be cross-referenced via `{numref}`. *Lines:* 140, 411, 417, 423.

### Low severity
- **[qe-writing-001]** — A few paragraphs combine two ideas into a single multi-line paragraph, but most paragraphs follow the one-sentence rule.
- **[qe-fig-004]** — Three of the four figures have no caption (just the directive), and the first one places the descriptive sentence outside the directive (line 142 "Pytorch is just one of several …").

## Strengths
- Lecture title "About These Lectures" follows qe-writing-006.
- Bold/italic emphasis usage is consistent with qe-writing-005.
- Code demos use appropriate cell tags (`skip-execution`) and only standard-Anaconda imports.
- The Python code cell at lines 232–248 shows clean, idiomatic Python (PEP8 per qe-code-001).

## Recommended actions
1. Convert all section/subsection headings to sentence case (e.g., "Common uses", "Relative popularity", "The AI connection", "NumPy alternatives", "Scientific programming with Python").
2. Replace the bare JAX URL on line 84 with `` {doc}`jax:intro` `` (or with custom title text).
3. Add descriptive `name:` and caption fields to the four figures for cross-referencing.
