# networks

- **Series:** lecture-python-intro
- **File:** `lectures/networks.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 OK; H2/H3 mostly sentence case; "### Example: Aircraft Exports" / "### Example: A Markov Chain" Title Case (H3). |
| Math         | 5/10  | Uses `\begin{pmatrix}` (M4 violation) throughout for matrices; `\mathbf{1}` used (M3 violation); `\top` for transpose correct. |
| Code         | 8/10  | `!pip install quantecon` at top with `hide-output` (qe-code-003 OK); standard Anaconda otherwise. |
| JAX          | out of scope | — |
| Figures      | 7/10  | `figsize=` on lines 117, 430; 3 `{figure}` directives all with `:name:` (qe-fig-005 OK); no `ax.set_title` violations. |
| References   | 7/10  | 10 `{cite}` usages; 2 are in-text ("found in {cite}", "by {cite}\`newman2018networks\`") — should be `{cite:t}`. |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | `{prf:theorem}`, `{prf:example}` used (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
- **M4** — Matrices use `\begin{pmatrix}` instead of `\begin{bmatrix}` throughout. *Examples:* lines 549, 605, 617. *Count:* 3+ matrix displays.

### Medium severity
- **M3** — Uses `\mathbf 1` (lines 1034, 1037) and `\mathbf{1}` (line 1049) for ones vector instead of `\mathbb{1}`. *Count:* 3 occurrences.
- **W3** — "### Example: Aircraft Exports" (line 85), "### Example: A Markov Chain" (160) use Title Case.
- **[qe-ref-001]** — In-text citations should use `{cite:t}`. *Examples:* `lectures/networks.md:688` ("found in {cite}\`sargent2022economic\`"), 1149 ("by {cite}\`newman2018networks\`, {cite}\`menczer2020first\`..."). *Count:* 2 sentences.

### Low severity
- **W1** — A few short two-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` on lines 117, 430. *Count:* 2 occurrences.

## Strengths
- Transpose `^\top` used (M2 OK).
- Section headings mostly sentence case.
- Bold for definitions (**nodes**, **vertices**, **edges**, **links**).
- Equation labels and references used.
- 3 `{figure}` directives all with `:name:` for cross-referencing (qe-fig-005 OK).
- `{prf:theorem}`, `{prf:example}` directives (qe-admon-004 OK).
- `quantecon` install at top with `hide-output` (qe-code-003 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Convert all `\begin{pmatrix}` to `\begin{bmatrix}` per M4.
2. Replace `\mathbf 1`/`\mathbf{1}` with `\mathbb{1}` per M3.
3. Convert example H3 headings to sentence case.
4. Convert in-text `{cite}` on lines 688, 1149 to `{cite:t}`.
5. Remove `figsize=` overrides.
