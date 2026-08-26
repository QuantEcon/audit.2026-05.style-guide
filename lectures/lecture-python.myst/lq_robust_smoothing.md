# lq_robust_smoothing

- **Series:** lecture-python.myst
- **File:** `lectures/lq_robust_smoothing.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×6; `qe-writing-002` ×4; `qe-writing-003` ×1, +1 more. |
| Math         | 7.5/10 | `qe-math-003` ×9. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×2; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 9. *Lines:* 105, 107, 108, 110, 111, 133, 136, 222, 469. *Example:* pmatrix environment.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 6. *Lines:* 189, 622, 768, 862, 1036, 1048. *Example:* bold is used for emphasis in places the lecture elsewhere italicises, and the clearest evidence is internal: line 491 writes *more persistent* in italic and line 1036 writes **more persistent** in bold, the same two words making the same point. The other five are **conditional means** (189), the whole bolded sentence at 622, the bolded question at 862, and **high-frequency** / **Low-frequency** (768, 772) and **do** (1048). The lecture's genuine definitions are bolded correctly and abundantly (75-77, 187, 191, 203, 292, 433, 473, 864, 866), and its emphases are italicised correctly eighteen times, so this is drift rather than a missing convention.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 889, 899, 906. *Example:* three one-line docstrings are written as padded single-quoted strings rather than triple-quoted (PEP 257, referenced by PEP 8): `"Simulate n_paths draws of μ_{t+1} = ζ μ_t + α w_{t+1} from μ_0 = 0."` (889), and likewise 899 and 906. The other three docstrings in the lecture (690-693, 698-701, 1178-1184) use triple quotes, so the file is inconsistent with itself; the same three functions are copied into lq_robust_bewley.md, where they have the same problem. No other PEP8 deviation was found - no long lines, no trailing whitespace, and the arithmetic spacing is correct throughout.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 834, 840. *Example:* .set_title.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 227, 318, 599, 1124. *Example:* line 227 is a 70-word semicolon chain that defines ten symbols in a single sentence ($^*$, $c$, $s$, $h$, $k$, $i$, $d$, $b$, $\gamma$, $w^*$, $v^*$) - the lecture uses bulleted lists for exactly this job at 74-78 and 148-152, so the list form is available and preferred; line 318 packs the special case, two identities and a marginal-propensity result into 50 words; line 599 runs to 48 words with two subordinated 'as in locus' clauses; and line 1124 in the exercise solution leaves a working step in the text - '$\hat\beta - 1 = -\delta + u/\delta \cdot \beta/\beta$, more directly $\hat\beta-1+u = (u-\delta^2)/\delta$' - where the first expression multiplies by $\beta/\beta$ and is then abandoned.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 823. *Example:* figsize=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 154. *Example:* the note at 147-155 tells the reader that '`` {doc}`robust_permanent_income` `` writes the same object as $\theta^2$', where the object is $\alpha^2$ - but $\theta$ is not introduced until line 229, where it is the *penalty* parameter of the robust Bellman equation, related to $\sigma$ by $\sigma = -\theta^{-1}$ at 236. So $\theta$ carries two unrelated meanings in the lecture and the reader meets the second one first. This matters more than usual here because the lecture opens with a note (74-78) devoted to freeing up symbols so that $\sigma$ can be the robustness parameter.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 717. *Example:* the collision of the two Riccati roots is the subject of a `{note}` (650-656) and of the whole of exercise 2 (1101-1150), and it is never drawn. It appears only as a four-row printed table of root pairs (717-724) and, in the exercise, as a printed string of '+' and '-' characters (1145). A plot of the two roots of `` {eq}`eq:rcs-riccati` `` against $\sigma$ over $(\underline\sigma, 0]$, with the branch point marked, would show the double root, the sign flip and the breakdown point in one frame - and this is a lecture with four well-captioned figures elsewhere, so the omission stands out.


## Strengths

- The lecture opens by declaring exactly the three notational departures it makes from its two prerequisites - $v_{t+1}$ for the distortion, $\eta_i$ instead of $\sigma_i$ so that $\sigma$ is free, and $a_t$ for net assets instead of $b_t$ for debt (74-78) - which is the single most useful thing a third lecture in a sequence can do.
- The organising role of $\alpha^2$ is stated and then honoured: the note at 147-155 lists the three different things the same scalar measures across the three lectures, and every subsequent result - the locus `` {eq}`eq:rcs-oe` ``, the persistence `` {eq}`eq:rcs-zeta` ``, the breakdown point `` {eq}`eq:rcs-breakdown` `` and the spectrum `` {eq}`eq:rcs-spectrum` `` - depends on $\sigma$ only through $\sigma\alpha^2$.
- The two observational-equivalence theorems are not left as a confusing pair: 579-599 explains that they hold *different* agents fixed, works through what each one implies for the drift of expected consumption, and states plainly that the economics is the same in both.
- The closed-form solution earns its keep three times over: the discriminant of `` {eq}`eq:rcs-riccati` `` is shown to be a perfect square (632-644), which yields both roots exactly, explains why a distance-based numerical root selector silently switches branches (650-656), and locates the breakdown point as the point where the two roots coincide (674-678).
- The breakdown point and the detection error probability are presented as two different kinds of bound - a hard mathematical limit and a soft statistical one - and the lecture then reports how they actually interact in this calibration, including the caveat that their near-coincidence at $T = 40$ 'is a property of this calibration and of $T = 40$, not a theorem' (984).
- Probability events are written the way the proposed qe-math-014 (proposed) asks, with braces: $\mathbb{P}\{\text{prefer approximating} \mid \text{worst-case is true}\}$ (869-870).

## Recommended actions

1. Convert the nine `pmatrix` environments to `bmatrix` (105, 107, 108, 110, 111, 133, 136, 222, 469) - this is the only mechanical math violation in the lecture (qe-math-003, 9 occurrences).
2. Turn the symbol glossary at 227 into a bulleted list, matching the notes at 74-78 and 148-152, and split the long sentences at 318 and 599.
3. Give $\theta$ one meaning: either drop the $\theta^2$ aside at 154 or move it after 236, where $\theta$ has been defined as the penalty parameter.
4. Add a figure of the two Riccati roots against $\sigma$ over the admissible range, with the double root at $\underline\sigma$ marked - the note at 650 and exercise 2 both turn on a picture that is never drawn.
5. Change the six emphasis-bolds to italic (189, 622, 768, 772, 862, 1036, 1048); note that 1036 and 491 currently mark up the identical phrase two different ways.
6. Settle the marginal-utility subscript: the lecture writes $\mu_{st}$, $\mu_{s,t+1}$ and $\mu_{s,t-1}$ (285-297, 372, 386, 855) - pick one convention, and apply the same choice in lq_robust_bewley.md, which inherits the mixture.
7. Remove the two `set_title` calls at 834 and 840 in favour of the cell's mystnb caption (qe-fig-003, 2 occurrences), drop `figsize=(11, 4)` at 823 unless the two-panel aspect is deliberate (qe-fig-001), and give the three one-line docstrings at 889, 899 and 906 triple quotes.
