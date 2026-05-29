# Style Audit — eigen_II

- **Series:** lecture-python-intro
- **File:** `lectures/eigen_II.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case, H2/H3 sentence case; "Perron-Frobenius theorem" / proper nouns OK. |
| Math         | 8/10  | `\top` for transpose consistently; bmatrix; `\mathbb{N}` used as set of naturals. |
| Code         | 9/10  | `!pip install quantecon` at top with `:tags: [hide-output]` (qe-code-003 OK); standard imports otherwise. |
| JAX          | out of scope | — |
| Figures      | N/A   | no matplotlib usage in this lecture |
| References   | 7/10  | `{cite}` used; line 443 "proven in {cite}\`sargent2023economic\`" is in-text and should be `{cite:t}`. |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | `{prf:theorem}` × 4 used (qe-admon-004 OK); 1 solution gated, dropdown, linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-ref-001]** — In-text citation should use `{cite:t}`. *Example:* `lectures/eigen_II.md:443` ("This is proven in {cite}\`sargent2023economic\`"). *Count:* 1 occurrence.

### Low severity
- **W1** — A few short two-sentence paragraphs (e.g. lines 27–29).

## Strengths
- Transpose `^\top` used consistently (M2 OK).
- Headings sentence case (W3 OK), proper nouns retained.
- Equation labels and `{ref}` cross-references used.
- bmatrix throughout.
- Bold for definitions ("**nonnegative**", "**dominant eigenvalue**").
- `{prf:theorem}` for named theorems (qe-admon-004 OK).
- `quantecon` install at top with `hide-output` (qe-code-003 OK).

## Recommended actions
1. Convert in-text citation on line 443 to `{cite:t}` form.
