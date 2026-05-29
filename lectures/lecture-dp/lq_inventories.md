# lq_inventories

- **Series:** lecture-dp
- **File:** `lectures/lq_inventories.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Two Title-Case H2 headings; some long paragraphs. |
| Math         | 4/10  | Apostrophe transpose; array-environment matrices alongside `bmatrix`; `\cr` separators. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8 generally fine; figsize used once. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 8/10  | No matplotlib titles; lowercase axis labels; minimal figsize. |
| References   | 9/10  | Single `{cite}` used parenthetically — appropriate. |
| Links        | 9/10  | Two `{doc}` references; no problematic raw URLs. |
| Admonitions  | 8/10  | Exercises use `:label:` and dropdown solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Apostrophe `'` (and `^\prime`) used as transpose throughout the LQ derivation. *Lines:* 131, 137, 148-149, 151, 153. *Count:* 12+ occurrences.
- **[qe-math-003]** — Mixed `bmatrix` and `\left[\begin{array}{cc} … \end{array}\right]` matrix delimiters. *Lines:* 114-117, 150-171. *Count:* 11 array-matrix blocks.

### Medium severity
- **[qe-writing-006]** — Two H2 headings in Title Case: `## Inventories Not Useful` (417), `## Inventories Useful but are Hardwired to be Zero Always` (448).
- **[qe-math-001]** — `aligned` blocks use `\cr` row separator instead of `\\`. *Lines:* 101, 107, 113-120, 144-149.
- **[qe-math-010 (proposed)]** — Bare `E_0` used for expectation in display equation (line 195). Should be `\mathbb{E}_0`.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs.
- **[qe-writing-009 (proposed)]** — Smart quotes ’ used in narrative (lines 50, 58, 82, 89-91, 129-132).

## Strengths
- Lecture title in correct Title Case.
- Most H2 headings sentence case ("Overview", "Example 1-6", "Exercises").
- Definitions bolded ("**state**", "**control**").
- "IID"/Greek-letter conventions consistent.
- pip install at top.
- Exercises use labels + `solution-start`/`solution-end` with dropdown solutions.
- No `\tag`, no bold vectors, no matplotlib title / spine / Title-Case-label issues.

## Recommended actions
1. Replace every `'` and `^\prime` used as transpose with `^\top`.
2. Replace `\left[\begin{array}{cc} … \end{array}\right]` with `\begin{bmatrix} … \end{bmatrix}` consistently.
3. Convert H2 headings to sentence case.
4. Replace `\cr` with `\\` inside `aligned`.
5. Replace bare `E_0` with `\mathbb{E}_0`.
