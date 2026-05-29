# black_litterman

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/black_litterman.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 5.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title in Title Case; sentence-case headings; some long compound paragraphs. |
| Math         | 2/10  | Heavy `\mathcal{N}` use; primes as transpose; bold zero vector. |
| Code         | 5/10  | 16 spelled-Greek assignments; no install cell (uses numpy/scipy only — OK). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 4/10  | `ax.set_title` used 3 times; 7 `figsize=`; 4 `set_xlabel` with capitalised labels (e.g. "Mean"). |
| References   | 8/10  | 6 `{cite}` used; never `{cite:t}` despite narrative author usage. |
| Links        | 6/10  | Two raw `python-advanced.quantecon.org` URLs. |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-011 (proposed)]** — `\mathcal{N}` used systematically as Normal distribution. *Example:* `lectures/black_litterman.md:518`. *Count:* 16 occurrences.
- **[qe-math-002]** — Prime `'` used as transpose. *Example:* `w'(\vec r - r_f 1)`, `C' w`, ~28 inline-math primes used as transpose. *Count:* ~28 occurrences.
- **[qe-fig-003]** — `ax.set_title` used 3 times to embed titles in matplotlib. *Count:* 3 occurrences.
- **[qe-fig-006]** — `set_xlabel("Mean")` and similar Title-Case axis labels. *Count:* 4 occurrences.

### Medium severity
- **[qe-math-004]** — Bold used for vectors/matrices. *Example:* `lectures/black_litterman.md:518`, `:592`, `:812`, `:831`. *Count:* 4 occurrences.
- **[qe-link-002]** — Raw `python-advanced.quantecon.org` URLs for sibling-series references. *Example:* `lectures/black_litterman.md:30`, `:38`. *Count:* 2 occurrences.
- **[qe-code-002]** — Spelled Greek (`alpha`, `beta`, `gamma`, `delta`) heavily used in code (16 assignments).
- **[qe-fig-001]** — 7 `figsize=` settings without justification.

### Low severity
- **[qe-writing-005]** — `**Black-Litterman**`, `**robust portfolio choice**` bold-as-emphasis use is borderline definitional.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.

## Strengths
- `\mathbb{E}` used (mixed with bare) (qe-math-010, proposed).
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- Consistent `{cite}` usage for references.

## Recommended actions
1. Replace `\mathcal{N}` with `N` for the Normal distribution (qe-math-011, proposed).
2. Replace prime `'` with `^\top` for transpose throughout (qe-math-002).
3. Remove `ax.set_title` calls; move titles to mystnb figure metadata (qe-fig-003).
4. Lowercase axis labels (qe-fig-006).
5. Remove `\mathbf{0}` for zero vector — use plain `0` (qe-math-004).
6. Convert raw `python-advanced.quantecon.org` URLs to markdown links to same-series docs (qe-link-001).
