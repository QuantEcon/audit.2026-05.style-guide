# calvo_machine_learn

- **Series:** lecture-dp
- **File:** `lectures/calvo_machine_learn.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 5.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | H2/H3 mostly sentence case; many long paragraphs. |
| Math         | 3/10  | `^T` transpose throughout; `\mathbf{I}`/`\mathbf{v}`; `\vec` everywhere. |
| Code         | 5/10  | pip install not at top (line 402 — three blocks for `quantecon`, `optax`, `statsmodels`); `optax` is a binary-package install with no notes. |
| JAX          | out of scope | uses JAX but JAX rules out of scope per spec. |
| Figures      | 8/10  | No matplotlib titles, no figsize, no Title-Case labels. |
| References   | 4/10  | Eight narrative-author `{cite}` patterns ("Calvo {cite}…", "Chang {cite}…", etc.) — should be `{cite:t}`. |
| Links        | 5/10  | Some markdown links to other QuantEcon series; `{doc}` used in places. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — `^T` (uppercase T) used as transpose throughout the gradient-descent quadratic-form derivations (e.g. `g^T \vec{\mu}`, `\vec{\mu}^T M \vec{\mu}`, `B^T \vec{\beta}`). *Lines:* 870, 872, 875, 877, 880, 889-891. *Count:* 13+ occurrences. Should be `\top`.
- **[qe-math-004]** — `\mathbf{I}` used for the identity matrix (lines 875, 877, 880); `\mathbf` decoration prohibited.
- **[qe-code-003]** — Three `!pip install` calls placed mid-lecture (line 402-404) rather than at the top. `optax` and `statsmodels` are also installed there.
- **[qe-code-006]** — `optax` (a binary/JAX-companion package) installed without installation notes about Anaconda incompatibility.

### Medium severity
- **[qe-math-004]** — `\vec \mu`, `\vec \theta`, `\vec \beta`, `\vec v` used throughout in narrative and math. *Count:* dozens.
- **[qe-ref-001]** — Author-name narrative citations using parenthetical `{cite}` instead of textual `{cite:t}`. *Count:* 8 occurrences ("Calvo {cite}`Calvo1978`", "Chang {cite}`chang1998credible`", "Cagan {cite}`Cagan`", "Sargent and Wallace's {cite}`sargent1973stability`", etc.).
- **[qe-writing-001]** — Many multi-sentence paragraphs (e.g. 39-54, 56-67).
- **[qe-writing-005]** — Double-backtick quotes ``machine learning``, ``gradient descent``, ``dynamic programming squared`` used in narrative.

### Low severity
- **[qe-math-013 (proposed)]** — Mixed eq-label style: some `$$ … $$ (label)` (line 181, 864) without `eq:` prefix.

## Strengths
- Lecture title in correct Title Case.
- H2/H3 mostly sentence case ("Introduction", "The model", "Model components", "Parameters and variables", "Timing protocol", "A gradient descent algorithm", "Implementation").
- Matrices use `bmatrix` (8 matrix blocks).
- Definitions bolded ("**state**", "**Bellman equations**", "**time inconsistency**", "**machine learning**", "**square summable**").
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- No `\tag`, no `align`-inside-`$$` issues.
- No matplotlib title / figsize / spine violations.

## Recommended actions
1. Replace every `^T` used as transpose with `^\top`.
2. Drop `\mathbf{I}` → plain `I`; drop `\vec` arrows from sequence symbols.
3. Switch narrative `Author {cite}…` to `{cite:t}` form.
4. Move all `!pip install` calls (line 402-404) to the top of the lecture; add note that `optax` requires JAX/non-Anaconda installation.
5. Replace ``\`\`...\`\``` quoting with `**bold**` or `*italic*`.
6. Tighten multi-sentence paragraphs.
