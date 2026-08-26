# hansen_singleton_1982

- **Series:** lecture-python.myst
- **File:** `lectures/hansen_singleton_1982.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-002` ×4; `qe-writing-009` (proposed) ×1; `qe-writing-003` ×1, +1 more. |
| Math         | 5/10  | `qe-math-010` (proposed) ×12; `qe-math-009` ×3. |
| Code         | 7/10  | `qe-code-002` ×2; `qe-code-001` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 12. *Lines:* 168, 188, 211, 239, 245, 376, 378, 568, 600, 841, …. *Example:* bare expectation `E_t[`.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 2. *Lines:* 86, 387. *Example:* lines 85-87 split a conditional expression across three continuation lines at a 9-space indent that matches neither the opening bracket nor a hanging indent (E128), leaving `if "\\" not in c / and "^" not in c and "_" not in c / else c for c in ...` hard to parse; line 387 leaves trailing whitespace inside a docstring. The `data[n_lags - 1 - j : t_obs - 1 - j, :]` spacing at 311, 363 and 368 is correct PEP8 for a slice with compound expressions and is left alone.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 781, 782. *Example:* spelled-out `xi`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 154, 166, 378. *Example:* the letter M carries three jobs and its lowercase carries two more: $M_j$ is the maturity of asset $j$ (124, 131, 151), $M_{t+1}(\theta)$ is the stochastic discount factor (166, 188, 540, 598), $m$ is the number of Euler equations (221, 376, 574) and $m_t(\theta)$ is the moment vector (540, 600) - so `\beta^{M_j}` and $M_{t+1}$ appear in the same display at 151-166 meaning unrelated things. The asset index also switches mid-sentence at 154, from 'asset $j$' to $R^i_{t+1} = (P_{i,t+1}+D_{i,t+1})/P_{i,t}$, and the superscript $i$ then persists (161, 164, 188, 540) while the model is written in $j$. And the information set is $\mathcal{I}_t$ at 328, 330, 332 and 334 but plain $I_t$ at 378.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 50, 182, 330, 1119. *Example:* line 50 is a subordinate clause with no main clause ('Though maximum likelihood estimators ... will be asymptotically more efficient when the distributional assumptions are correctly specified.'), and line 182 is a fragment ending in a comma - 'Just like what we did together in `` {doc}`hansen_singleton_1983` ``,' - whose continuation starts a new paragraph at 184. Lines 328, 330 and 334 state the same requirement three times in four lines: instruments must lie in $\mathcal{I}_t$. Lines 1119 and 1121 each contain a grammatical slip ('So GMM is provides a way', 'more efficient that are the GMM estimators').

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 957. *Example:* figsize=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 420. *Example:* the whole estimator is implemented before the object it minimises is defined: `two_step_gmm` at 420-534 minimises the GMM criterion, forms the optimal weighting matrix and computes the $J$ statistic, and the section that defines $g_T(\theta)$, the criterion `` {eq}`hs82-criterion` ``, the sandwich covariance and $J_T$ only begins at 536. A reader meeting `j_stat`, `j_df` and the two-step weighting at 420-534 has not yet been told what any of them are.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 606. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 741. *Example:* iid.


## Strengths

- The estimator is validated before it is used: a DGP that satisfies the Euler equation by construction (740-785), a single-sample recovery check, then a 500-replication Monte Carlo whose $J$ histogram is compared against the $\chi^2$ density (930-974) - and only then the real data at 976.
- Every display carries a label and is cited where it is used: `hs82-euler` (159) at 156, 170, 176, 180 and 188, `hs82-uncond` and `hs82-instruments` (202, 226) at 247, `hs82-finite-so` (591) at 608 - the lecture never refers to 'the equation above'.
- Every array builder validates its inputs and says why it rejects them (254, 266, 294-297, 343-349, 390-397), including the sample-size-versus-horizon condition that would otherwise fail silently with an empty window.
- The lecture is explicit about where it departs from the paper - the scope note at 52, and the admission at 606-608 that the HAC covariance is 'a modern precaution, not part of the original procedure, which exploits the known MA order directly'.
- Data provenance is fully documented: the FRED and Ken French sources, the builder script in QuantEcon/data-lectures, the substitution of the Ken French return for CRSP and its consequence ('we only want to match the paper qualitatively', 984).
- Code identifiers use `γ` and `β` to match the mathematics (256, 268, 758-759, 790-791), and the multi-period builder documents its timing convention in comments before the loop (351-353).

## Recommended actions

1. Brace the 11 bare expectation operators - `E_t[` and `E[` become `\mathbb{E}_t[` and `\mathbb{E}[` (168, 188, 211, 239, 245, 376, 378, 568, 600, 1044, ...) - the single largest fix in this lecture (qe-math-010 (proposed), proposed).
2. Fix the text-versus-code disagreement at 787: the prose says '700 monthly observations' while the cell at 792-793 generates 5000, and the Monte Carlo at 945 uses 900.
3. Resolve the M/m overloading described above - rename the maturity or the discount factor - and settle on one asset index and one symbol for the information set.
4. Move the implementation cells at 249-534 after '## GMM criterion and asymptotic theory' (536), or move the criterion, weighting matrix and $J$ statistic ahead of the code that computes them.
5. Reconcile the two statements of the disturbance's MA order: line 380 says the number of autocovariances in $S_0$ is determined by $n$, 'the order of the moving average disturbance', while 588 says the disturbance is at most MA($n-1$) - the code uses `ma_order=horizon-1` (906), so 380 is the one to fix.
6. Repair the prose defects: the clauseless sentence at 50, the fragment at 182-184, the triple statement of the instrument-timing requirement at 328-334, and the two grammar slips at 1119 and 1121.
7. Housekeeping: rename `xi` to `ξ` at 781-782 (qe-code-002), sentence-case the figure caption at 932 (qe-fig-004), drop `figsize=` at 957 (qe-fig-001), write 'IID' at 741 (qe-writing-009 (proposed), proposed), and clear the trailing whitespace at 387 and the double space at 606.
