# Style Audit — python_advanced_features

- **Series:** lecture-python-programming
- **File:** `lectures/python_advanced_features.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 9.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Headings mostly sentence case; minor stragglers. |
| Math         | N/A   | No math content. |
| Code         | 9/10  | Only Anaconda packages used (no install needed); PEP8 clean; demonstrates type hints, decorators, descriptors, generators idiomatically; no benchmarking patterns. |
| JAX          | out of scope | — |
| Figures      | N/A   | No figures. |
| References   | N/A   | No citations. |
| Links        | 10/10 | Uses `` {doc}`earlier discussion <need_for_speed>` `` and `` {doc}`need for speed <need_for_speed>` `` correctly per qe-link-001. |
| Admonitions  | 9/10  | One `{exercise-start}` / `{solution-start}` pair (advanced exercises) correctly gated; `:class: dropdown` on solution; `:label:` matched per qe-admon-005; `{note}` admonitions used. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Several H3/H4 headings use Title Case. *Clear violations:* line 579 `### Decorators`, line 737 `### Descriptors`, line 1166 `## Exercises`. *Count:* 3–4 occurrences.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs (e.g., lines 473–474 combine two thoughts).

## Strengths
- Lecture title "More Language Features" follows qe-writing-006.
- H2 headings consistently use sentence case ("Iterables and iterators", "Type hints", "Decorators and descriptors", "Generators", "`*` and `**` operators").
- Most H3/H4 already use sentence case ("Basic syntax", "Common types", "Hints don't enforce types", "Why use type hints?", "Type hints in scientific Python", "An example").
- Bold used for definitions per qe-writing-005 ("**type hints**"); italic for emphasis.
- No qe-code-* violations: PEP8 idiomatic; no `time.time()`, no `%timeit`, no non-Anaconda imports.
- Exercise/solution pair fully compliant per qe-admon-001/qe-admon-002/qe-admon-005.

## Recommended actions
1. Convert remaining Title Case headings to sentence case ("Decorators", "Descriptors" are single-word so naturally sentence case once typed; only need to verify "Exercises" matches the series convention).
