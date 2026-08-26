# intro_supply_demand

- **Series:** lecture-python-intro
- **File:** `lectures/intro_supply_demand.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-002` ×6; `qe-writing-004` ×2; `qe-writing-003` ×2, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×2; `qe-fig-004` ×2; `qe-fig-008` ×12. |
| References   | N/A   | no citations in this lecture. |
| Links        | 8/10  | `qe-link-002` ×4. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 114, 243, 407, 408, 409, 410. *Example:* inline comments separated from the code by a single space where PEP8 asks for two - `consumers = range(1, 11) # consumers 1,..., 10` (114), the same at 243, and the four field comments in the `Market` namedtuple declaration (407-410).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 183, 209, 301, 349, 448, 449, 490, 556, 634, 755, …. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 36, 136, 144, 402, 853, 898. *Example:* four sentences of 33-47 words (36, 136 at 47 words, 144 at 43, 402) and two copies of a sentence that has lost its main verb: "Our [SciPy] lecture has a section on [Optimization] is a useful resource to find out more" (853-855, repeated verbatim at 898-900).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 53, 87, 390, 642, 678, 700, 703. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 197, 285. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 747, 832. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 4. *Lines:* 853, 854, 898, 899. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 260, 461. *Example:* the `prf:example` block at 260-283 is not an example: it opens with a \$10/\$20 illustration but then carries the general definition of the inverse supply curve (272-274), the formula for total producer surplus (267-270) and a forward reference to a figure that lives outside the block ("We show an example below", 276; "The shaded area is...", 282, with the figure at 285); and the lecture has two sections called "Consumer surplus" (H2 at 63, H3 at 461) and two called "Producer surplus" (H2 at 227, H3 at 528), so the table of contents gives the reader no way to tell the discrete/continuous treatment from the affine-model treatment.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 414, 899. *Example:* mid-sentence 'Market'.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 247. *Example:* the discrete producer figure plots willingness to sell only, while its consumer counterpart at 118-120 overlays the surplus in orange on top of the black paid-portion; producer surplus $\max\{p - v_i, 0\}$ is defined at 258 and never shown for the discrete case, and the figure does not even mark the price line.


## Strengths

- The discrete-then-continuous pairing is genuinely well built: each concept gets a bar chart of ten agents and then the matching shaded-area figure, and every one of those figures has a caption and a `name`.
- The two surplus definitions carry equation labels (`eq:cstm_spls` at 472, `eq:pdcr_spls` at 538) and both are cited by `{eq}` when the integral is evaluated (521, 588); the welfare/equilibrium punchline is made by pointing `` {eq}`eq:equilib_q` `` back at `` {eq}`eq:old1` `` (678).
- Parameters are held in a `namedtuple` with a `create_market` factory (407-418), so the four exercises can redefine `inverse_demand`/`inverse_supply` without touching the parameter set.
- Differentials are written `\mathrm{d} x` rather than italic `dx` in the main exposition (471, 537, 646), which is the correct upright form.
- The `{seealso}` and `{note}` admonitions carry the digressions - the multiple-goods forward pointer at 23, the meaning of "affine" at 380 - keeping the main line of argument clean.

## Recommended actions

1. Repair the two broken `{seealso}` sentences at 853-855 and 898-900 ("has a section on X is a useful resource") and break the four 33-47 word sentences at 36, 136, 144 and 402.
2. Move the general material out of the `prf:example` at 260-283 - the inverse supply curve definition and the total-surplus formula belong in the body, with only the \$10/\$20 illustration left inside.
3. Rename the duplicated section headings so the H3 pair at 461 and 528 is distinguishable from the H2 pair at 63 and 227 (for example "Consumer surplus in the affine model").
4. Convert the four raw `python-programming.quantecon.org` URLs (853, 854, 898, 899) to `{doc}` cross-series references.
5. Set `lw=2` on the twelve curve plots and add `mystnb: figure: caption/name` metadata to the two exercise figures at 747 and 832 so they can be captioned like the rest.
6. Show producer surplus on the discrete producer figure (247) the way the consumer figure does at 118-120, and add the price line.
7. Make the differentials consistent - lines 603, 777 and 796 write `dx` while the surrounding equations write `\mathrm{d} x` - lower-case 'Market' at 414 and 899, drop the trailing period from the heading at 140, and separate the inline comments listed above by two spaces.
