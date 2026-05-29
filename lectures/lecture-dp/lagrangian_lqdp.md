# Style Audit — lagrangian_lqdp

- **Series:** lecture-dp
- **File:** `lectures/lagrangian_lqdp.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Several Title-Case H2 headings. |
| Math         | 3/10  | Apostrophe + `^\prime` transpose throughout; `pmatrix` and `\cr`. |
| Code         | 6/10  | Two `%%timeit` magics; pip install at top; Unicode Greek; otherwise PEP8. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 9/10  | No matplotlib titles; no spine issues; no figsize calls. Clean. |
| References   | 8/10  | Single `{cite}` — no narrative-author misuse to flag. |
| Links        | 4/10  | Four raw markdown links to `python-advanced.quantecon.org` / `python.quantecon.org` instead of `{doc}`. |
| Admonitions  | N/A   | No exercises / proofs / notes. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Apostrophe `'` and `^\prime` used as transpose throughout. *Lines:* 76, 87, 94, 103, 107, 113, 125, 132, 161-162, 173, 181, 216-217. *Count:* 60+ occurrences.
- **[qe-writing-006]** — Multiple Title Case H2/H3 headings: `## Undiscounted LQ DP Problem` (70), `## State-Costate Dynamics` (236), `## Reciprocal Pairs Property` (258), `## Other Applications` (669), `## Discounted Problems` (696), `### Transforming States and Controls to Eliminate Discounting` (702), `### Lagrangian for Discounted Problem` (780).

### Medium severity
- **[qe-math-003]** — `pmatrix` used instead of `bmatrix`. *Count:* 6 `pmatrix` blocks.
- **[qe-math-001]** — `\cr` row separator used inside `aligned` blocks instead of `\\`. *Lines:* 172-175, 208-211, 216-217, 223-225, etc.
- **[qe-link-002]** — Four raw markdown links to other QuantEcon series instead of `{doc}` intersphinx form: `python-advanced.quantecon.org/lu_tricks.html`, `python-advanced.quantecon.org/classical_filtering.html`, `python-advanced.quantecon.org/dyn_stack.html` (×2), `python.quantecon.org/re_with_feedback.html`. *Lines:* 61, 66, 676, 827.
- **[qe-code-005]** — Uses `%%timeit` IPython magics for benchmarking. *Lines:* 662, 667. Style guide prefers `quantecon.timeit`.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs.
- **[qe-writing-A1]** — Smart quotes ’ used in narrative.

## Strengths
- Lecture title in correct Title Case.
- Definitions bolded ("**invariant subspace**", "**symplectic**", "**reciprocal pairs**", "**states**", "**costates**", "**algebraic matrix Riccati**").
- Many equation labels and `{eq}` references used cleanly (24 labels).
- `aligned` properly inside `$$` (mostly qe-math-006 compliant).
- No `\tag`, no bold vectors, no `align`-inside-`$$` issues.
- pip install at top.
- No matplotlib titles, no figsize, no axis-label or spine issues.

## Recommended actions
1. Replace every `'` and `^\prime` used as transpose with `^\top`.
2. Replace `pmatrix` with `bmatrix`.
3. Convert H2/H3 headings to sentence case.
4. Replace `\cr` with `\\` inside `aligned`.
5. Convert raw `python-advanced.quantecon.org` / `python.quantecon.org` markdown links to `{doc}` intersphinx references.
6. Replace `%%timeit` with `quantecon.timeit` context.
