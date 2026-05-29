# Style Audit — long_run_growth

- **Series:** lecture-python-intro
- **File:** `lectures/long_run_growth.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2/H3 OK (proper nouns retained); some multi-sentence paragraphs. |
| Math         | N/A   | virtually no math content |
| Code         | 8/10  | Standard Anaconda imports only; `alpha=` matplotlib kwarg only. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 275, 359, 420; 1 `{figure}` directive without `:name:`; no `ax.set_title` violations. |
| References   | 4/10  | 4 `{cite}` usages, **all in-text** (e.g. "Adam Tooze's account... see chapter 1 of {cite}", "Chapter 1 of {cite}", "figure from chapter 1 of {cite}") — all should be `{cite:t}`. |
| Links        | 9/10  | `{doc}` cross-references used (2 occurrences). |
| Admonitions  | N/A   | no exercises / solutions |

## Issues

### Critical
_None found._

### High severity
- **[qe-ref-001]** — All 4 in-text `{cite}` usages should be `{cite:t}`. *Examples:* line 29 ("see chapter 1 of {cite}\`Tooze_2014\`"), 40 ("Chapter 1 of {cite}\`Tooze_2014\`"), 504 ("figure from chapter 1 of {cite}\`Tooze_2014\`"). *Count:* 4 occurrences. **Systemic for this lecture.**

### Medium severity
- **W1** — Several multi-sentence paragraphs (lines 29–31, 40–43, 46–48).
- **[qe-fig-001]** — `figsize=` overrides on lines 275, 359, 420. *Count:* 3 occurrences.

### Low severity
- **W7** — Capitalized phrases mid-text like "American century" / "Industrial Revolution" — proper-noun-like; debatable but acceptable.
- **[qe-fig-005]** — One `{figure}` directive present but no `:name:` field for cross-referencing.

## Strengths
- Section headings comply with W3 (proper nouns capitalized: United Kingdom, US, UK, China).
- Clean prose; one-sentence paragraphs in most sections.
- `{doc}` cross-references used (qe-link-002 OK).

## Recommended actions
1. Convert all 4 in-text `{cite}` usages to `{cite:t}`.
2. Remove `figsize=` overrides.
3. Add `:name:` to the `{figure}` directive.
4. Split multi-sentence paragraphs in Overview.
