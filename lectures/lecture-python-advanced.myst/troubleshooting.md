# Style Audit — troubleshooting

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/troubleshooting.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | Mostly compliant; a few short multi-sentence paragraphs and a chatty phrasing. |
| Math         | N/A   | no math content |
| Code         | N/A   | no executable code cells |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | One static `{image}` directive of the launch button; appropriate use. |
| References   | N/A   | no citations |
| Links        | 7/10  | One raw `python-programming.quantecon.org` URL should use `{doc}`. |
| Admonitions  | N/A   | only `raw` and `image` directives |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-link-002]** — Raw `python-programming.quantecon.org/getting_started.html` URL should use `{doc}\`programming:getting_started\``. *Example:* `lectures/troubleshooting.md:32`. *Count:* 1 occurrence.

### Low severity
- **[qe-writing-001]** — Several short paragraphs run two sentences instead of being split. *Example:* `lectures/troubleshooting.md:34`. *Count:* ~3 occurrences.

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case section headings (qe-writing-006).
- Concise reader-friendly tone (qe-writing-002).

## Recommended actions
1. Replace the raw `python-programming.quantecon.org` URL with `{doc}\`programming:getting_started\`` (qe-link-002).
2. Split the few two-sentence paragraphs into one-sentence units (qe-writing-001).
