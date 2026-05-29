# Style Audit — mccall_q

- **Series:** lecture-dp
- **File:** `lectures/mccall_q.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | Systemic Title Case H2s; many compound paragraphs. |
| Math         | 6/10  | `\cr` separators; `\mathcal{W}`; inconsistent eq-label prefix. |
| Code         | 7/10  | Unicode Greek; pip install at top; figsize 5×; PEP8 mostly OK. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 7/10  | No matplotlib titles; lowercase axis labels; figsize used 5×. |
| References   | 9/10  | 2 `{cite}` parenthetical; no narrative-author misuse. |
| Links        | 9/10  | Six `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Title Case H2 headings throughout. *Examples:* `## Review of McCall Model` (85), `## Implied Quality Function $Q$` (242), `## From Probabilities to Samples` (316), `## Q-Learning` (373), `## Employed Worker Can't Quit` (707), `## Possible Extensions` (747). *Count:* 6 of 7 H2s violate.

### Medium severity
- **[qe-math-001]** — `aligned` blocks use `\cr` instead of `\\` for row separation. *Lines:* 322-323, 336-337, 357-358. *Count:* 3 blocks.
- **[qe-writing-004]** — `\mathcal{W}`, `\mathcal{A}` used as plain index sets (lines 258, 260, 262, 295). Prefer plain letters.
- **[qe-writing-001]** — Many multi-sentence paragraphs (e.g. 28-31, 33-40, 53-54, 707-721).
- **[qe-fig-001]** — `figsize=` set 5 times.

### Low severity
- **[qe-math-013 (proposed)]** — Mixed equation labels — `$$ (eq_mccallbellman)` (line 112) lacks colon prefix.
- **[qe-writing-005]** — Inconsistent capitalisation: "Q-learning" sometimes, "Q-Learning" elsewhere.

## Strengths
- Lecture title correctly Title Case.
- `\mathbb{E}` used (line 101).
- Equation labels used consistently and referenced via `{eq}` syntax.
- No transpose violations, no bold vectors, no `\tag`, no `i.i.d.`.
- pip install at top; Unicode Greek (β, σ, etc.) in code.
- `{doc}` used for cross-series references (no raw URLs).
- No matplotlib title, spine, or Title-Case label violations.

## Recommended actions
1. Convert all H2 headings to sentence case.
2. Replace `\cr` with `\\` inside `aligned` blocks.
3. Drop `\mathcal{W}`/`\mathcal{A}` in favour of plain `W`/`A` where unambiguous.
4. Split compound paragraphs to one sentence each.
5. Normalise eq label prefix to `eq:` throughout.
6. Remove unnecessary `figsize=` declarations.
