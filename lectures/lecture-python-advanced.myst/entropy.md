# entropy

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/entropy.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 5.9 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Sentence-case headings; some long compound paragraphs. |
| Math         | 4/10  | Repeated `'` for transpose, `{\cal N}`/`{\mathcal N}` for Normal, bare `E_t`. |
| Code         | N/A   | no executable code cells |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 4 `{figure}` directives reference static images (entropy_*.jpg, MyGraph5.png); 4 figures correctly have `:name:` fields (one is bare `fig1`). |
| References   | 8/10  | 10 `{cite}` used; never `{cite:t}`. |
| Links        | 6/10  | Two raw `python-advanced.quantecon.org` URLs (L33, L34). |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Prime `'` used systematically for transpose. *Example:* `lectures/entropy.md:269`, `:279`, `:296`, `:330`, `:441`. *Count:* ~9 occurrences.

### Medium severity
- **[qe-math-011 (proposed)]** — `{\cal N}` and `{\mathcal N}` used as Normal distribution. *Example:* `lectures/entropy.md:256`, `:323`. *Count:* 4 occurrences.
- **[qe-math-010 (proposed)]** — Bare `E_t` and `E` for expectation. *Example:* `lectures/entropy.md:362`-`366`, `:382`, `:394`, `:441`. *Count:* ~6 occurrences.
- **[qe-writing-005]** — `**Claim**`, `**Proof**`, `**Problem:**`, `**Extension**`, `**uncertainty**` used as labels rather than definitions.
- **[qe-link-002]** — Two raw `python-advanced.quantecon.org` URLs for sibling-series references (`five_preferences.html`, `robustness.html`). *Example:* `lectures/entropy.md:33`, `:34`. *Count:* 2 occurrences (these should be `{doc}` or markdown `[](five_preferences)`).
- **[qe-fig-002]** — 4 `{figure}` directives reference static image files which could be code-generated.
- **[qe-fig-005]** — Figure name `fig1` is non-descriptive.

### Low severity
- **[qe-writing-001]** — Some paragraphs run two to three sentences (e.g. L40-44, L131-138).

## Strengths
- Equation labels via `$$ ... $$ (label)` and `{eq}` references (qe-math-007).
- Title in Title Case (qe-writing-006); sentence-case headings (qe-writing-006).
- Sequences in curly brackets (qe-math-005).
- Most `{figure}` directives have `:name:` fields (rare in this series — qe-fig-005).

## Recommended actions
1. Replace `'` with `^\top` throughout (qe-math-002).
2. Replace `{\cal N}` / `{\mathcal N}` with `N` (qe-math-011, proposed).
3. Replace bare `E` / `E_t` with `\mathbb{E}` / `\mathbb{E}_t` (qe-math-010, proposed).
4. Use italics for *Claim*, *Proof*, *Problem*, *Extension* labels (qe-writing-005).
5. Convert sibling-series URLs to markdown links (qe-link-001).
6. Replace generic `fig1` name with descriptive `fig-...` (qe-fig-005).
