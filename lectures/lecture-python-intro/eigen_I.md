# eigen_I

- **Series:** lecture-python-intro
- **File:** `lectures/eigen_I.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 OK; mostly sentence case; "## The Neumann Series Lemma" (line 861) Title Case (proper noun lemma name). |
| Math         | 9/10  | bmatrix; clean equations; no transpose violations; italic for eigenvalue/eigenvector definitions. |
| Code         | 8/10  | Unicode Greek (`θ`) used; `mpl_toolkits` import is standard with matplotlib; no quantecon-style migration issues. |
| JAX          | out of scope | — |
| Figures      | 5/10  | Many `figsize=` overrides (lines 212, 238, 530, 741, 1032); 7 `ax.set_title` calls outside exercise context; multiple `ax.spines[...].set_color('none')` / `.set_position('zero')` calls. |
| References   | N/A   | no `{cite}` citations |
| Links        | 8/10  | One `{doc}` link present. |
| Admonitions  | 9/10  | `{prf:theorem}`, `{prf:example}` used (qe-admon-004 OK); 3 solutions gated, dropdown, linked. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — `ax.set_title(...)` outside exercise/solution context. *Examples:* lines 226, 231, 266, 278, 543, 547, 551, 1070. *Count:* 7+ occurrences (most are vector-field labels for didactic clarity, but per rule they should move to figure metadata).
- **[qe-fig-007]** — Spines manipulated via `set_color('none')` + `set_position('zero')` to hide the box. *Examples:* lines 136, 138, 219, 221, 245, 247, 537, 539, 614, 616, 744, 746. *Count:* 12 occurrences across multiple figures.

### Medium severity
- **[qe-fig-001]** — `figsize=` overrides on lines 212, 238, 530, 741, 1032. *Count:* 5 occurrences.

### Low severity
- **W3** — "## The Neumann Series Lemma" — "Neumann" is proper noun; acceptable as named lemma.
- **W1** — Some short two-sentence paragraphs.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- bmatrix throughout (M4 OK).
- Italic for definitions (*eigenvalue*, *eigenvector*).
- Equation labels and `{ref}` references.
- Sentence-case section headings (W3 OK).
- `{prf:theorem}` and `{prf:example}` directives (qe-admon-004 OK).
- All solutions gated and dropdown.

## Recommended actions
1. Move `ax.set_title` content to mystnb metadata or `{figure}` captions.
2. Drop the spine-removal calls — keep default matplotlib box per qe-fig-007.
3. Remove `figsize=` overrides.
