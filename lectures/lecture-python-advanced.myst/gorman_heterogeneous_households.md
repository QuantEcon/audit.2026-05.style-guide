# gorman_heterogeneous_households

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/gorman_heterogeneous_households.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-001` ×6; `qe-writing-009` (proposed) ×5; `qe-writing-003` ×3, +3 more. |
| Math         | 8/10  | `qe-math-002` ×1; `qe-math-009` ×3. |
| Code         | 6.5/10 | `qe-code-001` ×8; `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×5; `qe-fig-003` ×2; `qe-fig-004` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 747, 772, 1271, 1375, 1747, 1925, 1936, 2198. *Example:* continuation lines are indented to a fixed offset rather than to the opening delimiter, in five places and never the same offset twice: 1271-1272 (`lq.compute_sequence(x0_full, ` then 24 spaces), 1375-1376 (16 spaces against a paren at column 35), 1747-1748 (20 spaces), 1925-1926 and 1933-1934 (8 and 12 spaces), 2055-2060 (12), 2184-2191 (16). Blank-line spacing around top-level definitions is also inconsistent: 747 puts one blank line between `doublej2` and `heter` where PEP8 asks for two, and `_pct` at 2198 is defined in the middle of a script cell with one blank line on each side. 772 and 858 use `##` to head a block comment (E266), and 772 also carries trailing whitespace, as do 64 other lines in the file. 1936 is an f-string with no placeholder, `set_title(f'Average of Individual Household Endowments')`. Inside the same figure, `fontsize=20` is set on three axis labels (2214, 2215, 2221, 2227) and omitted on two others (2220, 2226), and 2209 writes `figsize=(14,  6)` with a double space.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 1762, 1879, 1922, 2052, 2209. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 1759, 1847, 1905, 2038, 2166. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 1048. *Example:* `^T` transpose in `R^T`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 6. *Lines:* 250, 1297, 1462, 1474, 1522, 1990. *Example:* 2 sentences in one paragraph.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 308. *Example:* H2 Title Case: 'Dynamic, Stochastic Economy' (Stochastic, Economy).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 42. *Lines:* 32, 35, 39, 53, 58, 61, 67, 72, 76, 80, …. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 5. *Lines:* 326, 1327, 1508, 1523, 1553. *Example:* i.i.d..

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 1270, 1374. *Example:* spelled-out `beta`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 1927, 1936. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 1764, 1768. *Example:* plot() without lw=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 405, 995, 1995. *Example:* $\alpha$ and $\beta$ are already spoken for by the model - $\alpha_j$ is household $j$'s mean endowment (1478, 1490, 1496) and $\beta$ is the discount factor from 314 onward - and 1995 reuses both as the two shape parameters of the redistribution function, $\tau(j; J, \alpha, \beta) = \alpha [g(j;J)]^\beta$, so 2000-2001 has to gloss "$\alpha > 0$ controls the overall magnitude of redistribution" and "$\beta$ controls the progressivity" about symbols the reader has been holding two other meanings for since the Overview; the code avoids the collision by renaming them `red_α` and `red_β` (2043-2044), which is what the mathematics could have done too. The information set is written `\mathcal{J}_0` at 405, 639 and 934 where a plain $J_0$ would read as easily - and $J$ is already the household count (316), so the calligraphic form is carrying the disambiguation that a different letter would carry better.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 72, 723. *Example:* 72 is a 60-word sentence that states the lecture's whole method in one breath ("In a little more detail, when conditions for Gorman aggregation of preferences are satisfied, we can compute a competitive equilibrium of a heterogeneous-household economy in two steps: solve a representative-agent linear-quadratic planning problem for aggregates, then recover household allocations via a sharing-formula that makes each household's consumption a household-specific constant share of aggregate consumption") and is immediately followed by a bullet that continues it grammatically, so the sentence and its qualification are split across two blocks. 723 puts its subordinate clause first and its subject last, so the sentence has to be read twice: "Because the deviation term $\tilde{\chi}_{jt}$ depends on it through the inverse canonical representation, the augmented state includes household $j$'s own lagged durable stock $h_{j,t-1}$" - "it" refers forward to the noun at the end of the sentence.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 1903, 1983, 2245. *Example:* three claims are not supported by the cells that follow them. (a) 1903 says "Next, we examine whether the household consumption and endowment paths generated by the simulation obey the Gorman sharing rule", and the cell builds exactly the two panels that check would need - `c_panel` and `d_panel`, the cross-sectional deviations from the mean (1909-1910) - then asserts their shapes match (1911) and never uses them again: the figure plots the aggregate endowment and the mean across households (1913-1942), and 1945 concludes only that "the average of individual household endowments tracks the aggregate endowment process". The sharing rule is never tested. (b) 1981-1988 says the redistribution will "Lower the weights for low-$j$ types", "Increase the weights for high-$j$ types" and "Leave middle-$j$ types relatively unaffected" through a smooth transformation whose progressivity is governed by $\beta$ (2001), and both cells then set `red_β = 0.0` (2044, 2173). With $\beta = 0$, `dist_from_median ** β` is 1 for every household, so $\tau_j = \alpha = 0.8$ uniformly and the scheme becomes a flat shrinkage of every weight toward $1/J$ - the middle is affected exactly as much as the tails, and the design the four bullets describe is switched off. (c) 2245-2247 reads the last figure as showing "a striking reduction in income and consumption inequality after redistribution" and invites the reader to "notice how insurance smooths consumption relative to income", but the figure has three panels - $y^{pre}$, $y^{post}$, $c^{post}$ (2211-2227) - and no $c^{pre}$: the pre-redistribution consumption percentiles are computed at 2206 and never plotted, so neither the consumption-inequality comparison nor the consumption-against-income comparison is on the page.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 158. *Example:* caption of 7 words.


## Strengths

- The dynamic sharing rule is derived first in a static economy where it can be seen: 130-303 sets up Gorman's compensated demands $c^j = \psi_j(p) + u^j \psi_c(p)$, specialises to the quadratic case where $\psi_j(p) = \chi^j$ (273), solves the aggregate relation for the common term and substitutes (283-292) to get $c^j - \chi^j = (u^j/u^a)(c^a - \chi^a)$ - and 299 then says explicitly that this is {eq}`eq:sharing_rule` "except that goods are indexed by both dates and states in subscripts".
- Aggregation is shown to fail before it is shown to work: 146-148 gives a two-agent Cobb-Douglas example with endowments $(8,3)$ and $(3,8)$, 165-191 computes both utility possibility frontiers along the contract curve and plots them crossing, and 150-154 draws the consequence the rest of the lecture depends on - that with crossing frontiers the equilibrium price cannot be determined independently of the allocation.
- The Pareto weight is not asserted but solved for, and the algebra is laid out in the order the code runs it: the five present values are named and defined (667-685), the budget constraint is written with each term braced by `\underbrace` to its name (692), labour income is replaced using $\ell_{jt} = \mu_j g_t$ (695-698), and the result $\mu_j = (W_k + W_d - W_{c2})/(W_{c1} - W_g)$ (710) is then read back in words - numerator is household wealth, denominator the net cost of a unit of aggregate consumption (713-715).
- The Negishi alternative is put in a `{note}` at 82-92 precisely where a reader would ask why a fixed point is not needed, and the note answers it: Negishi's weights depend on the allocation through marginal utilities of income, so his welfare function requires a fixed point in the weights, while Gorman's conditions let prices and aggregates be computed "*without* resorting to Negishi's fixed point approach".
- The many-household economy is constructed so that aggregation is verifiable rather than assumed: the first $J_a$ households absorb the negative of every idiosyncratic shock (1481-1484), 1487-1497 shows the resulting $\sum_j d_{jt}$ depends only on $\sum_j \alpha_j$ and $d_{a,t}$ once $\sum_j \phi_j = 1$, and the code both normalises $\phi$ to satisfy that (1700) and prints the realised sum as a check (1732).
- The limited-markets result is stated with its assumptions attached and then tested: 920-934 specialises to the one-good constant-return case, notes $R = \gamma_1 + \delta_k = 1/\beta$ and imposes the $\mathcal{J}_0$-measurability restriction that Chapter 12.6 needs, and 1413-1434 then plots the two households' bond positions with their sum and prints $\max_t |\sum_j \hat k_{jt}|$ - the number that decides whether the two-asset implementation is self-financing.
- Notation that could be confused is disambiguated at the point of use: 1312 warns that $\varepsilon^1_t, \varepsilon^2_t$ are innovations in $w_{t+1}$ and "should not be confused with the wage-price sequence $w_{0t}$ in the household budget constraint", and 373 records that $\Pi_h$ here is the $\Pi$ of {cite:t}`HansenSargent2013`.

## Recommended actions

1. Either perform the sharing-rule check the text promises at 1903 - `c_panel` and `d_panel` (1909-1910) are the deviation panels it needs and are currently computed, asserted and discarded - or change 1903 and 1945 to claim only what the figure shows.
2. Add the $c^{pre}$ panel to the last figure (2209-2241): `c_pre_pct` is already computed at 2206, and without it neither claim in 2245-2247 can be read off the page.
3. Reconcile the redistribution scheme with its description: with `red_β = 0.0` (2044, 2173) the transformation at 1993-1996 degenerates to a uniform shrinkage of every weight toward $1/J$, which contradicts bullets 1-3 at 1983-1985 and the reading of $\beta$ at 2001 - pick a positive $\beta$ or describe the flat scheme that is actually run.
4. Rename the redistribution parameters in the mathematics at 1995-2001 so they do not collide with the discount factor $\beta$ (314) and the mean endowments $\alpha_j$ (1478), following what the code already does with `red_α` and `red_β`.
5. Bring `build_gorman_extended`'s signature (1526-1534) into the lecture's own unicode convention - `rho1`, `rho2`, `sigma_a`, `alphas`, `phis`, `sigmas`, `gammas`, `rho_idio`, `rho_pref` are the only spelled-out Greek names in the file, and the call site at 1723-1730 pairs each one with its unicode twin (`rho1=ρ1`, `sigma_a=σ_a`, `alphas=αs`, ...); see the scanner doubt below, since the check currently reports none of them.
6. Align the continuation lines at 1271, 1375, 1747, 1925, 1933, 2055 and 2184 with their opening delimiters, put two blank lines around the definitions at 747 and 2198, drop the `##` block comments at 772 and 858, remove the empty f-string at 1936, and settle the `fontsize` overrides in the figure at 2209-2227 one way or the other.
7. Sweep the mechanical items: the 5 `figsize=` overrides (1762, 1879, 1922, 2052, 2209), `mystnb` figure names on the 5 unnamed figure cells (1759, 1847, 1905, 2038, 2166), the 2 `set_title` calls (1927, 1936) into captions, `lw=2` at 1764 and 1768, the 5 "i.i.d." spellings (326, 1327, 1508, 1523, 1553) to "IID", sentence case for the H2 at 308, the 6 two-sentence paragraphs (250, 1297, 1462, 1474, 1522, 1990), the 42 double spaces and the 65 lines of trailing whitespace.
