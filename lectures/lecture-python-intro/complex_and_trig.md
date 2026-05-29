# Style Audit — complex_and_trig

- **Series:** lecture-python-intro
- **File:** `lectures/complex_and_trig.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.7 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Multiple Title Case H2/H3 violations; "## Note: we choose the solution near 0" is mid-content heading. |
| Math         | 7/10  | Generally clean; uses `aligned`; equations not labeled; no transpose needed. |
| Code         | 8/10  | Unicode Greek (`π`, `ω`, `θ`) used in code (qe-code-002 OK); minor `lambda` Python keyword usage (not a violation). |
| JAX          | out of scope | — |
| Figures      | 5/10  | `figsize=` on 3 lines (98, 133, 333); `ax.set_title("Trigonometry of complex numbers", ...)` on line 143 outside exercise context; spines `set_visible(False)` violations. |
| References   | 6/10  | "Samuelson (1939) {cite}\`Samuelson1939\`" (line 34) is manual year + citation — should be `{cite:t}\`Samuelson1939\`` only. |
| Links        | N/A   | no cross-series links |
| Admonitions  | 8/10  | Solutions use `:class: dropdown` + exercise labels; gated form (qe-admon-001 OK); `{prf:theorem}` used for de Moivre's theorem (qe-admon-004 OK). |

## Issues

### Critical
_None found._

### High severity
- **W3** — Systematic Title Case in subsection headings. *Examples:* "### Complex Numbers" (44), "### An Example" (104), "## De Moivre's Theorem" (160), "## Applications of de Moivre's Theorem" (178), "### Example 1/2/3" (180, 205, 231), "### Trigonometric Identities" (358), "### Trigonometric Integrals" (421), "### Exercises" (486). *Count:* 8+ headings.
- **[qe-fig-007]** — Spines hidden with `ax.spines['top'/'right'].set_visible(False)` — see lines around the figure on line 143; 3 spine-removal calls.
- **[qe-ref-001]** — Manual "Author (Year)" + `{cite}` pattern. *Example:* `lectures/complex_and_trig.md:34` ("Samuelson (1939) {cite}\`Samuelson1939\`"). *Count:* 1 occurrence.

### Medium severity
- **W3** — "## Note: we choose the solution near 0" (line 306) used as section heading where it appears to be a code comment.
- **W7** — "de Moivre's theorem" capitalized inconsistently: "## De Moivre's Theorem" vs "de Moivre's theorem states that:" (line 162).
- **[qe-fig-001]** — `figsize=` overrides on lines 98, 133, 333. *Count:* 3 occurrences.
- **[qe-fig-003]** — `ax.set_title("Trigonometry of complex numbers", ...)` on line 143 outside any exercise/solution context.

### Low severity
- **W1** — Some longer paragraphs (lines 33–36, 38–41).
- **[qe-fig-005]** — No figures have a `:name:` field.

## Strengths
- H1 title in Title Case (W2 OK).
- `aligned` inside `$$` (M12 OK).
- Bold for definitions ("**real part**", "**imaginary part**", "**modulus**").
- Unicode Greek in code (qe-code-002 OK).
- `{prf:theorem}` for de Moivre (qe-admon-004 OK).

## Recommended actions
1. Convert all H2/H3 headings to sentence case per qe-writing-006.
2. Convert "Samuelson (1939) {cite}" → `{cite:t}` form.
3. Remove `ax.spines[...].set_visible(False)` calls per qe-fig-007.
4. Remove `ax.set_title` outside exercise context (line 143).
5. Remove `figsize=` overrides on lines 98, 133, 333.
