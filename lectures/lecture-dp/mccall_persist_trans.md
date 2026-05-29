# mccall_persist_trans

- **Series:** lecture-dp
- **File:** `lectures/mccall_persist_trans.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 9.1 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Sentence-case headings; short paragraphs. |
| Math         | 9/10  | `\mathbb E` mostly bare (no braces); otherwise clean. |
| Code         | 9/10  | Unicode Greek; pip install at top; PEP8; uses `qe.Timer`. |
| JAX          | out of scope | uses JAX, but JAX rules out of scope. |
| Figures      | 9/10  | No matplotlib titles; lowercase labels; no figsize. |
| References   | 10/10 | Single `{cite}` parenthetical. |
| Links        | 9/10  | `{doc}` used 6×; no raw cross-series URLs. |
| Admonitions  | 9/10  | One `{exercise}` + `solution-start` with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
- **[qe-math-010 (proposed)]** — Expectation written as `\mathbb E_z` without braces (lines 100, 104, 116, 129, 136); preferred form is `\mathbb{E}_z`.

## Strengths
- Lecture title correctly Title Case.
- All H2/H3 headings sentence case.
- "IID" used correctly.
- No transpose, no bold vectors, no matrix-bracket issues, no `align`/`\tag` violations.
- Equation labels and `{eq}` references clean.
- pip install at top; Unicode Greek; uses `qe.Timer()` (line 283) — qe-code-004 compliant.
- `{doc}` used for cross-series.
- Exercise uses `{exercise}` + `solution-start` with dropdown.

## Recommended actions
1. Add braces to `\mathbb{E}` for consistency with style guide.
