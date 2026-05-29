# Style Audit — troubleshooting

- **Series:** lecture-python-programming
- **File:** `lectures/troubleshooting.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10| Two H2 section headings in Title Case; otherwise clean. |
| Math         | N/A   | No math content. |
| Code         | N/A   | No code cells. |
| JAX          | out of scope | — |
| Figures      | 8/10  | One `{image}` directive at line 52 — no caption, but used appropriately for a screenshot. |
| References   | N/A   | No citations. |
| Links        | 9/10  | Uses `{doc}` for `getting_started` cross-reference correctly; remaining links are external (quantecon.org, github.com) which are appropriate for an issue-reporting page. |
| Admonitions  | N/A   | No admonitions beyond the standard raw header. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Two H2 section headings use Title Case instead of sentence case. *Examples:* line 25 `## Fixing Your Local Environment`, line 61 `## Reporting an Issue`. *Count:* 2 occurrences.

### Low severity
- **[qe-fig-004]** — The `{image}` directive at line 52 has no caption (just an empty body); for a launch-icon screenshot this is acceptable but could be made explicit.

## Strengths
- Lecture title "Troubleshooting" is correctly Title Case per qe-writing-006.
- One-sentence paragraphs throughout per qe-writing-001.
- Uses `{doc}` link for `getting_started` (qe-link-002 compliant, intra-series).
- No code or math to violate qe-code-* / qe-math-* rules.

## Recommended actions
1. Rename H2s to sentence case: "Fixing your local environment", "Reporting an issue".
