# troubleshooting

- **Series:** lecture-python-intro
- **File:** `lectures/troubleshooting.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title Case H1, sentence-case H2s, one-sentence paragraphs throughout. |
| Math         | N/A   | no math content |
| Code         | N/A   | no executable code cells |
| JAX          | out of scope | — |
| Figures      | 7/10  | uses `{image}` directive once (line 52); fine for PDF; no `:alt:` text. |
| References   | N/A   | no citations |
| Links        | 7/10  | direct URL to `python-programming.quantecon.org/getting_started.html` (line 32) instead of `{doc}` link. |
| Admonitions  | N/A   | only a `{raw} html` and `{image}` block |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-link-002]** — Cross-series URL written as direct link instead of `{doc}` reference. *Example:* `lectures/troubleshooting.md:32` (`[this lecture](https://python-programming.quantecon.org/getting_started.html)`). *Count:* 1 occurrence.

### Low severity
- **[qe-writing-001]** — A few paragraphs combine two sentences (lines 65–66: "Please be as specific…" + "Tell us where…"). Minor.
- **[qe-fig-011]** — `{image}` directive used (line 52) — correct choice over `{figure}` for a non-cross-referenced launch icon.

## Strengths
- Headings comply with W2/W3.
- Generally one-sentence paragraphs.
- Correct use of `{image}` directive (not `{figure}`) for a static icon.

## Recommended actions
1. Replace the direct URL on line 32 with `{doc}\`programming:getting_started\`` per qe-link-002.
2. Split the two-sentence paragraph in the "Reporting an issue" section.
