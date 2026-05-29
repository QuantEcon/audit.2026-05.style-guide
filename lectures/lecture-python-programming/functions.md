# Style Audit — functions

- **Series:** lecture-python-programming
- **File:** `lectures/functions.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10| Section headings systematically use Title Case. |
| Math         | N/A   | Only trivial `$f(x) = 2x+1$` style expressions. |
| Code         | 8/10  | PEP8 compliant; only Anaconda packages (numpy); no benchmarking patterns; no Greek identifiers needed. |
| JAX          | out of scope | — |
| Figures      | N/A   | No figures. |
| References   | N/A   | No citations. |
| Links        | 9/10  | Uses `` {doc}`previous lecture <python_by_example>` ``, `` {doc}`later <writing_good_code>` ``, `` {doc}`previous lecture <python_by_example>` `` correctly. |
| Admonitions  | 9/10  | Five `{exercise-start}` / `{solution-start}` pairs correctly gated; all solutions use `:class: dropdown`; `:label:` cross-links present and correct. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** *(carry-forward W3)* — Almost every H2/H3 section heading uses Title Case rather than sentence case. *Examples:* line 47 `## Function Basics`, line 55 `### Built-In Functions`, line 80 `### Third Party Functions`, line 94 `## Defining Functions`, line 100 `### Basic Syntax`, line 168 `### Keyword Arguments`, line 213 `### The Flexibility of Python Functions`, line 227 `### One-Line Functions: \`lambda\``, line 266 `### Why Write Functions?`, line 277 `## Applications`, line 279 `### Random Draws`, line 324 `### Adding Conditions`, line 408 `## Recursive Function Calls (Advanced)`, line 462 `## Exercises`, line 619 `## Advanced Exercises`. *Count:* 15+ occurrences.

### Medium severity
_None found._

### Low severity
- **[qe-writing-001]** *(carry-forward W1)* — A few multi-sentence paragraphs (e.g., around line 297, a bulleted explanation embedded in a paragraph).
- **[qe-code-001]** — Some solution snippets have inconsistent operator spacing (e.g., line 605 `count + ( 1 if ... else 0 )` with internal parenthesis padding). Minor PEP8 nit.

## Strengths
- Lecture title "Functions" follows qe-writing-006.
- Clean prose, code-block formatting, inline backticks.
- Exercise/solution structure is exemplary — gated syntax (qe-admon-001), dropdown class (qe-admon-002), `:label:` linkage (qe-admon-005).
- All five exercises use gated `exercise-start`/`exercise-end` syntax (no bare `{exercise}` directives that would block embedded code cells).
- No benchmarking magic, no `time.time()`, no `tic`/`toc`.

## Recommended actions
1. Convert all H2/H3 headings to sentence case ("Function basics", "Built-in functions", "Third party functions", "Defining functions", "Basic syntax", "Keyword arguments", "The flexibility of Python functions", "One-line functions: `lambda`", "Why write functions?", "Random draws", "Adding conditions", "Recursive function calls (advanced)", "Advanced exercises").
2. Tighten spacing in code (e.g., line 605) for PEP8 consistency.
