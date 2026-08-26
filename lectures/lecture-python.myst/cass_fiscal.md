# cass_fiscal

- **Series:** lecture-python.myst
- **File:** `lectures/cass_fiscal.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×12; `qe-writing-001` ×3; `qe-writing-005` ×3, +4 more. |
| Math         | 9/10  | `qe-math-001` ×1. |
| Code         | 7.5/10 | `qe-code-001` ×4; `qe-code-003` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×10; `qe-fig-005` ×6; `qe-fig-008` ×11, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 9. *Lines:* 828, 875, 910, 978, 1057, 1386, 1653, 1708, 1734. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 10. *Lines:* 774, 779, 786, 792, 798, 1022, 1028, 1034, 1043, 1048. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 809, 900, 1054, 1383, 1631, 1686. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 11. *Lines:* 772, 777, 784, 790, 796, 1020, 1026, 1027, 1032, 1039, …. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 12. *Lines:* 39, 112, 169, 232, 275, 283, 331, 598, 1208, 1525, …. *Example:* H2 Title Case: 'The Economy' (Economy).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 56. *Lines:* 18, 20, 22, 24, 32, 34, 75, 87, 102, 125, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 313, 420, 969, 1395. *Example:* 74 code lines carry trailing whitespace (313, 420, 473, 531-533, 578, 620, 679, 716, 819-820, 831, 860, 905-906, 914-915, 922-924, 927-929, 933, 954, 968, 987-989, 995, 1015, 1023, 1029, 1039, 1065-1067, 1114-1116, 1150, 1153-1155, 1190-1191, 1225, 1228, 1232, 1239, 1373-1374, 1379, 1394-1395, 1409-1410, 1420, 1423-1425, 1441-1442, 1474-1475, 1641, 1656-1657, 1696, 1711, 1729, 1733, 1738); ten lines exceed 79 characters, the worst being 122 at line 1395 (`fig.legend(...)` with six keyword arguments on one line), 94 at 969 and 970, and 93 at 345; and the `namedtuple` continuation at 314 is indented to column 13 under a paren opened at column 22.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['mpmath'].
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 1. *Lines:* 1771. *Example:* LaTeX `\mu` outside math delimiters.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 1173, 1585, 1614. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 24, 65, 236. *Example:* line 24 is a 44-word sentence that also contains "with an sequences of several distorting flat-rate taxes"; lines 64-65 end one line with "to represent it as" and begin the next with "as", so the word is duplicated across the break; line 236 reads "Let $U_1 = \frac{\partial U}{\partial c}, U_2 = \ldots = -\frac{\partial U}{\partial n}.$, we can derive FOC from the Lagrangian" - a full stop inside the math followed by a comma, and a "Let ..., we can derive" construction with no main clause.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 302, 1101, 1609. *Example:* the note at 302-306 asks the reader to accept growth machinery 1200 lines before it is explained ("we include routines to handle the growth component, which will be discussed further in the section `` {ref}`growth_model` ``... to avoid code duplication"), so `μ_t=1`, `μ_ss=None` and `A_path=None` appear in every signature from 342 onward with no meaning attached; then line 1609 tells the reader the growth section's routines are "in the section `` {ref}`cass_fiscal_shooting` ``", which is not where a growth routine is - it is where the ordinary routines were pre-loaded with the growth arguments. Lines 1101-1103 are unreadable as written: "a foreseen in-" ends one line and "crease in $\tau_{ct}$" begins the next, and the parenthetical "(i.e., a decrease in $(1+\tau_{ct})$ $(1+\tau_{ct+1})$)" has lost the operator between the two factors.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 164, 405, 1094. *Example:* the definition at 164-166 bolds four separate phrases in one sentence, articles included - **budget-feasible government policy**, **a feasible allocation**, **a price system** on top of the term being defined - so more of the sentence is bold than is not. The eight quantity labels at 405-501 (*Price:*, *Capital rental rate*, *Labor rental rate:*, *Gross one-period return on capital:*, *One-period discount factor:*, *Net one-period rate of interest:*) use italic as pseudo-headings. And the six experiment headers at 1094, 1141, 1177, 1364, 1400 and 1414 are bold pseudo-headings, while the growth section's equivalents at 1625 and 1682 are real H4s - the same structural element formatted two different ways in one file.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 600. *Example:* the shooting algorithm is stated as six steps (600-612) whose whole content is a search over $c_0$ - "Compute the difference $\hat k_S - \bar k$... adjust $c_0$ and repeat", "Adjust $c_0$ iteratively using the bisection method" - and the family of candidate capital paths that bracket $\bar k$, some diverging up and some crashing to zero, is never plotted. That figure is the one that makes shooting comprehensible, and it is also what would show the reader why `mpmath` is needed at all (line 300: "in cases where the solution diverges due to numerical instability"). All six figures in the lecture are post-solution transition panels.


## Strengths

- Two independent solution methods are implemented for the same model - the shooting algorithm (616-700) and residual minimisation (1225-1341) - and the exercises ask the reader to replicate all four experiments with the second method, so the agreement between them is demonstrated rather than claimed.
- Every equilibrium object gets its own labelled equation and a matching one-line implementation, in order: $q_t$ at `` {eq}`eq:equil_q` `` then `compute_q_path`, $\eta_t$ then `compute_η_path`, $w_t$ then `compute_w_path`, $\bar R$ at `` {eq}`eq:gross_rate` `` then `compute_R_bar`, $r_{t,t+s}$ then `compute_rts_path` (405-537).
- The no-arbitrage restriction is derived rather than imposed: 174-201 rearranges the household budget constraint to isolate the coefficient on $k_t$, then argues both directions (buy unlimited capital if positive, short-sell synthetic capital if negative) before concluding the coefficient must vanish.
- Each experiment's economics is narrated as a dated sequence with the mechanism at each date - the $\tau_c$ experiment at 1123-1137 walks through $t=0$ (anticipatory jump and consumption binge), $t \in (0, T)$ (falling capital raising $\bar R$), $t = T$ (the jump depressing $\bar R$ below 1) and $t > T$ (austerity and gradual recovery).
- The growth extension reuses the whole apparatus by rescaling to effective labour units (1525-1607), and each modified equation is presented explicitly as "the counterpart to" its constant-technology original (`` {eq}`eq:feasi_capital` `` → `` {eq}`eq:feasi_mod` ``, `` {eq}`eq:diff_second` `` → `` {eq}`eq:diff_mod` ``, `` {eq}`eq:consume_R` `` → its modified form).

## Recommended actions

1. Fix the two equation labels written without the required space - `$$(eq:no_arb_firms)` at line 230 and `$$(eq:euler_house)` at line 360 - the other 28 labels in the file all use `$$ (label)`, and both of these are cited (`eq:no_arb_firms` at 279 and 352, `eq:euler_house` at 1096 and 1101), so as written those four references are at risk of not resolving.
2. Remove the stray `$` after `1.025` on lines 1770 and 1771: it leaves the math-span parity odd on both lines, which swallows " at t=10" and " at t=0" into mathematics and is the actual cause of the qe-math-001 finding reported at 1771.
3. Sentence-case the twelve Title Case headings at 39, 112, 138, 169, 232, 275, 283, 331, 598, 1208, 1525 and 1583 (qe-writing-006, 12 occurrences) and collapse the 56 multiple-space runs (qe-writing-008, 56 occurrences).
4. Move the ten embedded matplotlib titles into figure captions (774, 779, 786, 792, 798, 1022, 1028, 1034, 1043, 1048), add `mystnb: figure: caption/name` metadata to the six code-cell figures at 809, 900, 1054, 1383, 1631 and 1686, and set `lw=2` on the eleven plot calls at 772, 777, 784, 790, 796, 1020, 1026, 1027, 1032, 1039 and the eleventh (qe-fig-003 10, qe-fig-005 6, qe-fig-008 11 occurrences).
5. Add a `!pip install mpmath` cell with `tags: [hide-output]` near the top - `mp` and `mpf` are genuinely used at 649-658 and `mpmath` is not in Anaconda (qe-code-003).
6. Add a figure showing the shooting search itself: several candidate $c_0$ guesses and the capital paths they generate, bracketing $\bar k$.
7. Sweep the prose and code hygiene: drop the nine `figsize=` overrides at 828, 875, 910, 978, 1057, 1386, 1653, 1708 and 1734 (qe-fig-001, 9 occurrences), split the three two-sentence paragraphs at 1173, 1585 and 1614 (qe-writing-001), strip the 74 trailing-whitespace lines, wrap the ten over-length lines, and fix "hßousehold" (125), "as\nas" (64-65), "an sequences" (24), "proceeds follows" (1246) and "In this this sequel" (1811).
