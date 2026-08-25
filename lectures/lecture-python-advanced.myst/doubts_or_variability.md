# doubts_or_variability

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/doubts_or_variability.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×9; `qe-writing-002` ×8; `qe-writing-001` ×4, +2 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×128; `qe-math-011` (proposed) ×24; `qe-math-004` ×6, +2 more. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-004` ×1; `qe-fig-001` ×9. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 9. *Lines:* 363, 1182, 1276, 1346, 1453, 1785, 1899, 1951, 2107. *Example:* figsize=.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 2537. *Example:* apostrophe transpose `W'`.
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 6. *Lines:* 265, 270, 2193, 2195, 2206. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 128. *Lines:* 173, 191, 219, 225, 227, 235, 242, 249, 257, 265, …. *Example:* bare expectation `E_t(`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 24. *Lines:* 441, 459, 918, 975, 977, 2282, 2590, 2606, 2633, 2647, …. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 8. *Lines:* 51, 85, 89, 93, 110, 508, 1013, 1924. *Example:* eight sentences run past 34 words, and the long ones stack up in the Overview where the reader has least context: 51-52 (37), 85 (34), 89 (39), 93 (39) and 110 (36) are five of the first twenty prose lines; 508-509 is 38 words listing three citations inside a subordinate clause; 1013 is 43 words that name three value functions in one breath; 1924 is 36.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 9. *Lines:* 438, 452, 512, 518, 525, 532, 593, 619, 706. *Example:* nine terms are introduced in italic where the rule asks for bold: the two consumption specifications *geometric-random-walk* (438) and *geometric-trend-stationary* (452), the four agent types at 512, 518, 525 and 532 (each italic label heading its own defining bullet list), the *type I recursion* (593), the *risk-sensitive recursion* (619) and the *multiplier* preference ordering at 706 - the last one is definitional in the same sentence ("is defined by") and the same word is correctly bolded at 506, which shows the file knows the convention.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 141, 152, 1342. *Example:* trailing whitespace on three code lines - `T = 235  ` (141), `R_mean = np.array([...])  ` (152) and `w_star = w_from_θ(θ_star, "rw") ` (1342) - PEP8 W291; these are the only PEP8 marks in an otherwise clean set of cells.
- **[qe-math-014 (proposed)]** *(reviewer)* — Braces \{…\} for events, parentheses (…) for sets. *Count:* 4. *Lines:* 1068, 1070, 2906, 2916. *Example:* the detection-error probabilities are written with parentheses round events - `p_A = \Pr_A(L_T < 0)` (1068), `p_B = \Pr_B(L_T > 0)` (1070) and the same two again at 2906 and 2916 - where `\{L_T < 0\}` is an event and the proposed convention reserves parentheses for sets.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 2352, 2582, 2778, 3115. *Example:* 2 sentences in one paragraph.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 3. *Lines:* 984, 2861, 3013. *Example:* iid.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 339. *Example:* Title Case caption (Hansen-Jagannathan).
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 52. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 502. *Example:* the 780 lines from 403 to 1180 carry no figure at all, and the passage that most needs one is the four-agent taxonomy at 502-558: four bullet lists of parameters followed by two prose sentences (541, 543) asserting which types are observationally equivalent to which, in what sense, and for which objects - a small table (type, parameters, penalty vs constraint, equivalence) or a diagram of the equivalences would carry the whole section, which the rest of the lecture then depends on.


## Strengths

- All eleven exercises use `{exercise}` with a labelled `{solution-start}` / `{solution-end}` pair and `:class: dropdown`, and the body of the lecture hands work to them by label at the point it skips a step - line 619 says "{ref}`Exercise 3 <dov_ex3>` asks you to verify this step" instead of leaving a gap.
- Every generated figure carries `mystnb: figure: caption/name` metadata with a stable naming scheme (`fig-bhs-1` through `fig-bhs-6`, plus `fig-bhs-fear`, `fig-bhs-sdf-decomp`, `fig-bhs-contour`), so the figures are addressable even though the prose does not yet use `{numref}`.
- The two consumption models are carried as parallel dictionaries (`rw` and `ts` at 144-145) and every later computation indexes both through the same code path - e.g. `θ_rw_from_η` / `θ_ts_from_η` at 1862-1866 - so the random-walk and trend-stationary results cannot drift apart.
- Historical and naming asides are parked in `{note}` blocks (42-48, 59-62, 505-510) rather than spliced into the argument, which keeps the main line of the Overview readable despite the density of citations.
- The FRED data pipeline at 2024-2061 is commented step by step (nominal components, deflate, per-capita, log, restrict to 1948Q1-2006Q4) so the 235-quarter sample used everywhere else in the lecture is reproducible rather than asserted.
- Code uses Unicode Greek throughout (`β`, `γ`, `θ`, `η`, `σ_ε`, `Σ_R`) and writes exponentiation as `**` without spaces, matching both the mathematics and the code rules.

## Recommended actions

1. Brace the expectation and probability operators - 128 occurrences of bare `E_t(`, `E[`, `\Pr` and friends starting at 173, 191, 219, 225, 227, 235, 242, 249, 257, 265 - as `\mathbb{E}` / `\mathbb{P}`; at 128 hits this is by far the largest fix in the file and the reason Math scores 3/10 (qe-math-010 (proposed), proposed).
2. Replace the 24 `\mathcal{N}` distribution names with plain `N` at 441, 459, 918, 975, 977, 2282, 2590, 2606, 2633, 2647 and 14 more (qe-math-011 (proposed), proposed).
3. Bold the nine definitions listed above and keep italic for the genuine emphases the lecture already has (*puzzles* 66, *misspecification* 100, *worst-case* 900, *twice* 1617, *variability* / *doubts* 2162).
4. Add a table or diagram of the four agent types near 502 giving each one's parameters and its equivalence class, and reference the figures by `{numref}` - the file names ten figures and cites none of them, so the prose still says "the following figure" (1327) and "the left panel" (1329) where a numbered reference would do.
5. Write the four detection-error probabilities as events in braces - `\Pr_A\{L_T < 0\}` at 1068 and 2906, `\Pr_B\{L_T > 0\}` at 1070 and 2916 (qe-math-014 (proposed), proposed).
6. Drop the nine `figsize=` overrides at 363, 1182, 1276, 1346, 1453, 1785, 1899, 1951 and 2107 and let the theme set figure size (qe-fig-001, 9 occurrences).
7. Sweep the small items: `\mathbf{1}` at 265, 270, 2193, 2195 and 2206 should be `\mathbb{1}` with the ones-vector convention spelled out where it first appears, as `math.md` asks (qe-math-004, qe-math-008; 6 occurrences); `iid` to `IID` at 984, 2861, 3013 (qe-writing-009 (proposed), proposed); the apostrophe transpose `W'` at 2537 to `W^\top` (qe-math-002); split the two-sentence paragraphs at 2352, 2582, 2778 and 3115 (qe-writing-001); and strip the trailing whitespace on 38 lines, including the three code lines at 141, 152 and 1342.
