# ifp_egm_transient_shocks

- **Series:** lecture-dp
- **File:** `lectures/ifp_egm_transient_shocks.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×9; `qe-writing-003` ×2; `qe-writing-002` ×4, +1 more. |
| Math         | 9.5/10 | `qe-math-009` ×1. |
| Code         | 7.5/10 | `qe-code-001` ×4; `qe-code-004` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×7; `qe-fig-003` ×3; `qe-fig-008` ×10, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 6. *Lines:* 590, 592, 595, 598, 601, 604. *Example:* time.time(.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 365, 616, 631, 795, 933, 982, 1048. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 368, 369, 618, 619, 656, 658, 937, 944, 994, 1068. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 59, 69, 174, 189, 377, 384, 814, 821, 894. *Example:* H2 Title Case: 'The Household Problem' (Household, Problem).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 656, 842, 848, 862. *Example:* line 656 writes `+ y_bar(k) , label=label` with a space before the comma (E203); line 842 writes `jnp.arange(1, n+1)` unspaced while line 843 directly below writes `(n + 1) / n` spaced; line 848 writes `p: float=0.01`, which needs spaces around `=` on an annotated parameter (E252), where 514 in the same file gets it right; line 862 leaves trailing whitespace after `return wealth_top / wealth_total` (W291, also at 309, 473, 638-639).
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 805, 940, 947. *Example:* .set(xlabel='assets', title=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 34, 104, 616, 816. *Example:* line 34 reads 'we continue extend the IFP' - a verb is missing; line 104 ends 'where $a_y, b_y$ are positive constants' with no full stop and a trailing space; line 816 has 'Lets'' for 'Let's' plus four words of padding ('some standard measures of this phenomenon'). The fourth is duplication: the figure cell at 616-623 is byte-identical to the one at 365-373, labels included, and both plot `a_vec`/`c_vec` - the NumPy solution from line 358 - so the JAX section's only policy figure is a second printing of the NumPy section's. The prose around it (426-427 repeating 234-235 verbatim, the identical operator docstrings at 268-275 and 436-443, 'Let's road test the EGM code' at both 349 and 544) has the same copy-forward character.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 556, 968. *Example:* lines 556-570 present a verification that cannot work as described. `create_ifp` is defined twice - at 210 with `β=0.96` and again at 401 with `β=0.94` - so `ifp_numpy` (352) and `ifp` (547) are different models, yet 567-568 concludes 'These numbers confirm that we are computing essentially the same policy'. Line 570 then diagnoses the gap as 'mainly due to different Monte Carlo integration outcomes over relatively small samples', which is a specific wrong answer: both constructors draw 100 standard normals from the same seed, and the discount factor is what differs. Second, exercise `ifp_egm_ex1` at 968 says to step `r` through `np.linspace(0, 0.016, 4)` and its own solution at 984 uses `np.linspace(0, 0.04, 4)`, justified by a comment ('With β=0.96, we need R*β < 1, so r < 0.0416') that names a discount factor the model in scope does not have.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 570, 706. *Example:* 2 spaces.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 934. *Example:* figsize=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 99. *Example:* `\mathsf Z` at line 99 for the Markov chain's state support - the one decorative letter left in this file, and the same object the code calls `z_grid`. Plain $Z$ would do, and would also settle the disagreement across the series, where `` {doc}`ifp_egm` `` writes `\mathsf S`/`\mathsf Z` and `` {doc}`ifp_advanced` `` writes `\mathbf S` and `\mathscr C` for the same family of objects.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 1017. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.


## Strengths

- The Monte Carlo step is written into the math before it appears in code: equation `cfequmc` at 248-256 restates `cfequ_ts` with the integral replaced by $\frac{1}{m}\sum_{\ell=1}^m$, and line 258 says each $\eta_\ell$ is a standard normal draw - so `η_draws` in the constructor at 418 is implementing something the reader has already seen defined.
- Every level of the three-deep JAX operator (458-481) carries a one-line docstring naming exactly what it returns, down to the innermost `∫ u'(σ(R s_i + y(z_k, η'), z_k)) φ(η') dη'` at 462 - the nesting is followable without re-deriving it, and the same structure is mirrored by the explicit quadruple loop in the NumPy version at 292-315.
- `y_bar` is honest about being an approximation: the docstring at 638-644 gives the double sum it computes, and the display at 673-675 writes the same thing in math as $\bar y(z) := \sum_{z'} \frac{1}{m}\sum_\ell y(z', \eta_\ell)\Pi(z, z')$ rather than as an idealised expectation, with line 677 saying so in words.
- The lecture reports its own failure and traces it: the wealth distribution is called implausible at 809-811, the Gini and top-share numbers are 'a long way out' at 875, calibration is ruled out as the explanation at 882-887 in favour of a structural impossibility result, and the reader is pointed forward to `` {doc}`ifp_advanced` ``.
- The interest-rate experiment at 903-958 states the limit of what it shows - 'the differences are minor and we cannot increase $r$ much more without violating the stability constraint' - instead of stopping at the direction of the effect.
- Density and CDF conventions are followed and made explicit: line 124 introduces $\phi$ as 'the density of the shock $\eta_t$ (standard normal)' in lowercase, and every subsequent $\phi(\eta')d\eta'$ in 116-117, 147-148 and the code comments at 295 and 473 uses it consistently (qe-math-015 (proposed) clean).

## Recommended actions

1. Give the two model constructors distinct names and reconcile their defaults - `create_ifp` at 210 uses `β=0.96` and the redefinition at 401 uses `β=0.94`. As it stands the NumPy/JAX comparison at 558-564 measures a difference in the discount factor, the conclusion at 567-568 is unsupported, and the explanation offered at 570 (Monte Carlo noise) sends the reader looking in the wrong place. Fixing this also fixes the stale `β=0.96` comment at 983.
2. Make the JAX section's figure plot the JAX result. Lines 616-623 duplicate 365-373 exactly and draw `a_vec`/`c_vec` from the NumPy solve at 358; they should use `c_vec_jax`/`a_vec_jax` from 553, or the cell should go.
3. Delete or fix the dead warm-start in all three loops. `c_init = c_vec; a_init = a_vec` at 927-928, 996-997 and 1066-1067 sits at the end of the loop body, but the next iteration overwrites both at 916-917, 990-991 and 1056-1057 - so the comment 'Use last solution as initial conditions for the policy solver' describes something that never happens, and every solve restarts from consume-everything.
4. Work through the figure debt, the largest mechanical item: mystnb `name`/`caption` metadata on the 7 figure cells (365, 616, 631, 795, 933, 982, 1048), `lw=2` on the 10 default-width line plots (368, 369, 618, 619, 656, 658, 937, 944, 994, 1068), the 3 embedded titles moved into captions (805, 940, 947), and the hand-set `figsize=(12, 4)` dropped at 934 (qe-fig-005 x7, qe-fig-008 x10, qe-fig-003 x3, qe-fig-001 x1).
5. Sentence-case the 8 headings at 59, 174, 189, 377, 384, 814, 821 and 894 ('The household problem', 'NumPy implementation', 'Set up', 'JAX implementation', 'Wealth inequality', 'Measuring inequality', 'Interest rate and inequality') (qe-writing-006 x8).
6. Replace the 6 `time.time()` readings at 590-604 with the `qe.Timer` context manager and move `import time` at 577 into the import cell at 47-55 (qe-code-004 x6).
7. Fix the prose and code slips: 'continue extend' at 34, the missing full stop at 104, 'Lets'' at 816, 'Exercises 1' at 1013, the double spaces at 570 and 706, plus the space before the comma at 656, the `n+1`/`n + 1` mismatch at 842-843, `p: float=0.01` at 848 and trailing whitespace at 862. Leave the apostrophes at 115, 116 and 122 alone - they are derivatives of $u$, not transposes.
