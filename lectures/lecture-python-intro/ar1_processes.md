# ar1_processes

- **Series:** lecture-python-intro
- **File:** `lectures/ar1_processes.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-001` ×3; `qe-writing-009` (proposed) ×1; `qe-writing-005` ×1, +3 more. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×2. |
| Code         | 6/10  | `qe-code-002` ×21; `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×6; `qe-fig-008` ×9; `qe-fig-001` ×1. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 21. *Lines:* 166, 180, 182, 210, 211, 213, 216, 230, 265, 267, …. *Example:* spelled-out `mu`.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 171, 209, 228, 263, 407, 623. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 9. *Lines:* 182, 215, 436, 437, 530, 531, 633, 634, 635. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 372. *Example:* missing braces: `\mathbb E`.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 46, 186, 540. *Example:* line 46 `#set default figure size` has no space after the hash; line 186 `ax.legend(bbox_to_anchor=[1.05,1],loc=2,borderaxespad=1)` omits the space after every comma; line 540 `parameter_pairs= (2, 2), ...` has a space after `=` but not before.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 465, 488, 568. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 46. *Example:* style override.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 335. *Example:* `` {cite} `` in narrative flow: 'by `` {cite} ``'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 447. *Example:* exercise ar1p_ex2 (lines 447-490) asks the reader to build a kernel density estimator and test it on three beta distributions; nothing connects it to AR(1) processes, and its real purpose - supplying the KDE class that exercise ar1p_ex3 needs at line 628 - is never stated.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 288. *Example:* line 288 is a definition sentence - 'A stationary distribution is a distribution that is a "fixed point" of the update rule' - with the defined term left unbolded, four lines before the same lecture correctly bolds **stationary** at line 292.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 310. *Example:* the Ergodicity section (lines 310-359) asserts that time-series averages converge to expectations under the stationary distribution and never plots it, although the neighbouring stability claims each get a figure (lines 171, 209, 228, 263).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 369. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 561. *Example:* iid.


## Strengths

- Every labelled display equation is actually used: can_ar1, ar1_ma, dyn_tm, mu_sig_star and ar1_ergo are each cited later with `` {eq} ``, so no label is dead weight.
- The stability argument is built visually in four steps - the ten-period density sequence at line 171, the forty-period sequence at line 209, the same sequence from a different initial condition at line 228, then the analytical limit psi-star overlaid on it at line 263.
- Side remarks are parked in parenthetical one-line paragraphs (lines 74-75, 150, 203, 303-304) rather than being spliced into the main argument.
- All three exercises use gated {exercise} / {solution-start} ... {solution-end} syntax with `:class: dropdown`, so solutions are hidden by default.

## Recommended actions

1. Rename the spelled-out Greek variables in the first half of the lecture - `mu`, `mu_star`, `std_star` at lines 166, 180-184, 211-217, 267-268 - to the Unicode forms already used in the second half at lines 604-635 (`mu`, `psi`); the lecture currently spells the same quantity two different ways (qe-code-002, 12 occurrences).
2. Fix the dropped terms in the backward-iteration display: line 97 should read `a^3 X_{t-3} + a^2 b + a^2 c W_{t-2} + a b + a c W_{t-1} + b + c W_t` - the `a b` and `a c W_{t-1}` terms produced by the previous substitution are missing.
3. Add mystnb figure metadata (`mystnb: figure: name/caption`) to the seven plotting cells at lines 171, 209, 228, 263, 407, 523 and 623 so the figures are nameable and cross-referenceable (qe-fig-005, 7 occurrences).
4. Set `lw=2` on the nine `ax.plot` calls at lines 182, 215, 436, 437, 530, 531, 633, 634 and 635 (qe-fig-008, 9 occurrences).
5. Bold the defined term at line 288 and give the Ergodicity section (line 310) a figure showing a running time average converging to mu-star, so the one unillustrated claim in the lecture is illustrated like the rest.
6. Fix the PEP8 spacing at lines 46, 186 and 540, and make the plot labels at lines 633-635 raw strings (`label=r"$\psi_t$"`) - as written the backslash is an invalid escape sequence.
7. Sweep the remaining single-instance mechanical items: brace `\mathbb E` at line 372 (qe-math-010 (proposed)), `iid` to `IID` at line 561 (qe-writing-009 (proposed)), the mid-narrative `{cite}` at line 335 (qe-ref-001), the double space at line 369 (qe-writing-008), the figsize override at line 46 (qe-fig-001), and split the two-sentence paragraphs at lines 465, 488 and 568 (qe-writing-001).
