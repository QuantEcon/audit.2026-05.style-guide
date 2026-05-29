# Style Audit — cross_product_trick

- **Series:** lecture-dp
- **File:** `lectures/cross_product_trick.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 5.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Title-Case H2 headings, `i.i.d.` used, several multi-sentence paragraphs. |
| Math         | 3/10  | Apostrophe transpose universal; bare `align*` outside `$$`; broken `{eq}` ref. |
| Code         | N/A   | Single empty code cell — effectively no code content. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | N/A   | No figures. |
| References   | N/A   | No citations. |
| Links        | 8/10  | Single `{doc}` reference, used correctly. |
| Admonitions  | N/A   | No admonitions. |

## Issues

### Critical
- **[qe-math-013 (proposed)]** — Broken equation reference: `{eq}`eq:Kalman102}` has a closing `}` instead of a backtick (line 133). The label `(eq:Kalman102)` is also attached to a bare `align*` block (line 121) rather than a numbered `$$ … $$` block, so the label won't bind even if the syntax is fixed. Build risk: will render as raw text.

### High severity
- **[qe-math-002]** — Apostrophe `'` used as transpose throughout (e.g. `x_t' R x_t`, `B'PB`, `A'PA`, `D \Sigma_t D'`). *Lines:* 48, 63, 68, 119-121, 142, 164-167. *Count:* 30+ occurrences.
- **[qe-math-006]** — Bare `\begin{align*} … \end{align*}` blocks (not wrapped in `$$`) appear in five places. *Lines:* 82-88, 104-107, 118-121, 126-129, 140-143. These should be `$$ \begin{aligned} … \end{aligned} $$` to render correctly in PDF.

### Medium severity
- **[qe-writing-006]** — H2 headings use Title Case. *Examples:* `## Undiscounted Dynamic Programming Problem` (line 33), `## Kalman Filter` (line 92).
- **[qe-writing-009 (proposed)]** — `i.i.d.` used in narrative (line 110). Should be `IID`.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs (e.g. 80-89, 94-95, 145-151).
- **[qe-writing-005]** — "**duality**" used for emphasis but is not a definition (line 94); reserve bold for definitions.

## Strengths
- Lecture title in Title Case.
- Math symbols ($P$, $R$, $Q$) use plain letters consistent with qe-writing-004.
- Cross-reference `{doc}`Linear Control: Foundations <lqcontrol>`` used correctly.

## Recommended actions
1. **Fix the broken `{eq}` reference and bare `align*` blocks** — wrap each in `$$ … $$ (label)` form using `aligned`. This is the highest-priority action because it is a build-risk.
2. Replace every `'` used as transpose with `^\top`.
3. Rename H2 headings to sentence case ("Undiscounted dynamic programming problem", "Kalman filter").
4. Replace `i.i.d.` with `IID`.
5. Remove the trailing empty code cell on line 173-175.
