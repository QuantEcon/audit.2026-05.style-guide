# Style Audit — aiyagari

- **Series:** lecture-python.myst
- **File:** `lectures/aiyagari.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions (JAX out of scope)
- **Overall score:** 9.2 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10 | One H2 in Title Case. |
| Math         | 8/10 | `\mathbb E` (without braces) on line 109; spec form `\mathbb{E}` preferred for safety. |
| Code         | 9.5/10 | Mixed Greek conventions in code (word=5, uni=19). |
| JAX          | out of scope | JAX lecture — JAX rules not audited per scope. |
| Figures      | 9/10 | `figsize=` set in 3 places — usually unnecessary. |
| References   | 9/10 | Citation style follows conventions. |
| Links        | 10/10 | Link style follows conventions. |
| Admonitions  | 10/10 | Exercise/solution structure clean. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — One H2 in Title Case. *Example:* line 98 `## The Economy` should be `## The economy`.

### Low severity
- **[qe-math-010 (proposed)]** — `\mathbb E` (without braces) on line 109; spec form `\mathbb{E}` preferred for safety.
- **[qe-code-002]** — Mixed Greek conventions in code (word=5, uni=19).
- **[qe-fig-001]** — `figsize=` set in 3 places — usually unnecessary.
- **[qe-fig-005]** — Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).

## Strengths
- Excellent one-sentence paragraphs.
- No transpose, IID, or distribution-naming issues.
- Titles correctly Title Case (H1).
- Greek symbols used in Python code (α, β, σ) consistent with style guide.
- Solutions use `:class: dropdown` consistently.
- No `ax.set_title()` in main figures.
- Axis labels lowercase.
- No embedded matplotlib titles in main figures.

## Recommended actions
1. Address `qe-writing-006`: One H2 in Title Case.
2. Address `qe-math-010 (proposed)`: `\mathbb E` (without braces) on line 109; spec form `\mathbb{E}` preferred for safety.
3. Address `qe-code-002`: Mixed Greek conventions in code (word=5, uni=19).
4. Address `qe-fig-001`: `figsize=` set in 3 places — usually unnecessary.
5. Address `qe-fig-005`: Figures lack descriptive `name:` fields for cross-referencing (8 plot calls, 0 named).
