# Detector verification

**All 41 checks have now been sampled.** Every check in `qestyle_rules.py` was reviewed
adversarially against the real corpus before its counts were published: for each rule, at least ten flagged occurrences were
opened in the lecture source and judged against the canonical rule text, and the corpus
was probed for forms the check might miss. Where a rule's total reach was small enough,
every hit in the corpus was read rather than a sample. The table records the verdict *before* fixes
and what the fix was, because the false positives are the interesting part — a wrong
count is worse than a missing one when the number ends up in a published report.

Verified against the 2026-08 snapshot (`lectures/data/snapshot.json`).

| Rule | Verdict before fix | FP / TP sampled | What was wrong, and the fix |
|------|--------------------|-----------------|------------------------------|
| `qe-writing-006` | needs-fix | 52 / 40 | Possessives (`Newton's`) and hyphenated surnames (`Gram-Schmidt`, `Metropolis-Hastings`) defeated the proper-noun lookup; country names were missing. Added `_is_proper()` (strips possessives, splits hyphens, treats any `X's` as a name) and extended the list. Also added the rule's other half — an H1 that is *not* Title Case.. **A later review found two residual false-positive shapes:** `_is_proper` required *every* hyphen-part to be allowlisted, so `Student-t` failed on the bare `t`, and `jagannathan` was missing while `hansen` was present. A single letter in a hyphenated name is a mathematical label, not a word that should have been lowercased, so single-letter parts are now accepted — which also covers `F-test` and `p-value` — and both surnames were added. Removed exactly 3 occurrences (`qe-writing-006` 1, `qe-fig-004` 2: the `Student-t` heading and caption in `mcmc`, the `Hansen-Jagannathan` caption in `doubts_or_variability`) with no collateral: `First-Order Conditions`, `Back-of-the-Envelope Calculations` and `Multi-Step-Forward` are still flagged |
| `qe-writing-008` | broken | 12 / 28 | Masking inline code and maths with single spaces manufactured double spaces out of correctly-spaced prose. The lexer now masks with NUL, and cross-line inline maths is resolved before masking. |
| `qe-writing-009` | needs-fix | 3 / 12 | Fired on MyST anchor definitions (`(iid-theorem)=`) and on role targets (``{ref}`IID <iid-theorem>` ``). Anchors are skipped and inline code is masked. |
| `qe-writing-001` | added after | — | Not present at review time; added as a paragraph-block sentence counter with an abbreviation list. |
| `qe-writing-004` | added after | — | Not present at review time; added, firing only on a curated common-noun list so an unlisted surname cannot be mistaken for a violation. |
| `qe-math-001` | added after | — | Not present at review time; added. Its first form of false positive — inline maths spanning a line break — is fixed in the lexer. |
| `qe-math-002` | broken, and later **still false at scale** | 22 / 14 | The `^T` branch was ~88 % false: summation limits (`\sum_{t=0}^T`), terminal dates, data histories (`Y^T`), discount factors (`\delta^T`). It now requires a matrix-like base *and* a following factor rather than a relation. The apostrophe branch missed lowercase vectors (`c'x`, `x_t'`), now covered. **A later review found three more false-positive classes, all from guards that one branch had and the others did not:** `^\prime` carried no guard at all, so every `u^\prime(c)` derivative counted (49 occurrences); `prime_vec` had no relation guard, so `\sum_{w' \in W}`, `\max_{a' \in \Gamma}` and `\sum_{s' \in S}` counted as transposes (109); and neither apostrophe branch excluded a *double* prime, so second derivatives `H''(p)`, `W''(\hat I)`, `S''(\bar R)` counted (23). Occurrences 2,129 → 1,865, reach 97 → 93; 264 removed, 0 added. |
| `qe-math-003` | sound | 1 / 12 | One false positive: `\left\{\begin{array}{ll}…\right.` is a case distinction. Now excluded. |
| `qe-math-004` | needs-fix | 4 / 11 | Indicator functions (`\mathbf{1}\{X_t = x\}`) are not vectors, and the legacy `{\bf …}` spelling was missed. Both fixed; the indicator guard looks at the next source line too. |
| `qe-math-005` | broken | 1 / 0 | Matched matrix-by-elements notation and missed the real violation, which is written with parentheses (`(k_t)_{t \geq 0}`). Rewritten. |
| `qe-math-006` | needs-fix | 0 / 0 | Reported nothing, because there is no `align` inside `$$` anywhere in the corpus — which is itself the finding that withdrew the previous pass's headline build-risk claim. Now also reports bare top-level amsmath blocks, with distinct wording and non-Critical severity. |
| `qe-math-007` | sound | 0 / 0 | Extended to `\label{}` and `\eqno`, which MyST also does not resolve. |
| `qe-math-008` | broken | 8 / 8 | Every hit was an indicator function; genuine ones vectors written `\mathbf 1` were missed. Rewritten to detect ones-vector usage in any spelling and report only the *unexplained* case, leaving the bold spelling to `qe-math-004`. |
| `qe-math-010` *(proposed)* | needs-fix, then **undercounting** | 207 / 24 | Double-counted `\mathbb E` in two branches, and the bare-`E` branch fired on `E` as a matrix name. Branches now mask each other, and the bare-letter branch is gated on the lecture actually applying `E` as an operator. **A later review found the opposite failure:** `[PEV]\b` never fires before a subscript, because `_` is a word character — so `\mathbb E_t`, the corpus's usual conditional expectation, was invisible. Now `[PEV](?![A-Za-z])`, which still rejects `\mathbb Exp`. The Roman branch also missed `\textrm{…}`, `{\rm …}` and the name `Prob` while catching `\mathrm{…}` and `\Prob` — same notation, same rule — so those were added. Reach 105 → 117, occurrences 1,167 → 1,396; 232 hits added, all corroborated against their own source line, 0 false positives found. |
| `qe-math-011` *(proposed)* | broken, then **undercounting** | 79 / 18 | `\mathcal{G}` and `\mathcal{B}` are sigma-algebras, not distributions. Restricted to `N`/`U` *and* to a distribution context (after `\sim`, or applied to a parameter list). **A later review found that gate misfiring on one spelling:** the bare-`\mathcal` alternative did not consume the closing brace, so `{\mathcal N}(0,1)` presented the gate with `}` and was refused, while `{\cal N}(0,1)` and `\mathcal{N}(0,1)` passed. A brace-wrapped alternative now mirrors the `\cal` one. Reach 24 → 34, occurrences 86 → 140; 54 hits added, 0 false positives found. |
| `qe-math-012` *(proposed)* | broken | 18 / 5 | Fired on `\operatorname*`, on a standalone `$*$` naming the symbol, and on convolution notation. All three excluded. |
| `qe-math-013` *(proposed)* | broken | 16 / 20 | "equation (44) of {cite}`BEGS1`" is a reference into someone else's paper, where a number is the only citable thing. External-source references are now skipped. |
| `qe-code-002` | broken | 22 / 12 | `alpha=` in a drawing call is matplotlib's opacity; capitalised Greek (`Sigma`, `Psi`, `Gamma`) was missed entirely. Opacity is judged per cell (the kwarg is often on a continuation line) and capitalised forms were added. |
| `qe-code-003` | broken | 24 / 5 | Imports were read from the whole code text, so docstring prose ("from the urn without replacement") and a `{code-block} java` sample were reported as uninstalled dependencies. Now per-cell, Python-only, skipping `no-execute` cells and modules the lecture writes itself; and every install cell is position-checked, not only the first. |
| `qe-code-004` | needs-fix | 3 / 22 | Missed `from time import time` usage, `timeit.default_timer` and the `%time` magic. Added. |
| `qe-code-005` | needs-fix | 0 / 10 | Only caught `%timeit`, not the hand-rolled benchmark loop the rule's own example shows. Added a cell-level check for a timing read inside a loop that accumulates or averages. |
| `qe-code-006` | sound | 0 / 0 | Hardened anyway: package detection now reads real code only, and the warning must actually name the package. |
| `qe-fig-001` | needs-fix | 5 / 28 | Counted *reads* of `rcParams` and `style.use('default')` (a reset), and missed `rcParams.update(...)`. Now only writes count. |
| `qe-fig-002` | needs-fix | 36 / 20 | Flagged screenshots and photographs — a terminal capture or a photo of a GPU cannot be code-generated. Those asset families are excluded. |
| `qe-fig-003` | needs-fix | 0 / 15 | Missed `ax.set(title=…)` and `ax.title.set_text(…)`, ~73 lines corpus-wide. Added; the exercise/solution exemption was already correct. |
| `qe-fig-004` | broken | 70 / 60 | Tokenised LaTeX into words, so `$\bar\pi_t$` counted as five; split hyphenated compounds; and repeated the possessive bug. Maths is masked, compounds are one token, and the proper-noun test now routes through `_is_proper()`. |
| `qe-fig-005` | needs-fix | 99 / 15 | Counted cells that only *define* a plotting helper. A cell renders a figure only if a plotting or render call sits at column zero; `_strip_py` also had to stop collapsing docstrings, which was pulling indented code to column zero. (Reach had already been extended during development from `{figure}` directives to code-cell `mystnb.figure.name` metadata, where most QuantEcon figures live — 44 lectures to 293.) |
| `qe-fig-006` | needs-fix | 7 / 12 | `Im` for the imaginary part is correctly capitalised, and a hyphenated first word (`Taylor-rule`) defeated the proper-noun lookup. |
| `qe-fig-007` | needs-fix | 25 / 12 | `spines['bottom'].set_position(('data', 0))` moves an axis; it does not remove the box. Only removal counts now. |
| `qe-fig-008` | broken | 149 / 15 | A `plot(...)` call spanning several lines was judged on its first line, so `linewidth=2` two lines down was missed. The check now assembles the whole argument list by balancing parentheses. |
| `qe-fig-010` | sound | 0 / 4 | — |
| `qe-link-001` | needs-fix | 2 / 21 | A PDF under `/_static/` is a downloadable asset, not a sibling lecture. Asset paths are skipped. |
| `qe-link-002` | needs-fix | 0 / 25 | Missed hosts that occur in the corpus. Added `python-intro`, `dp`, `networks` and `dle` to the known series domains. |
| `qe-ref-001` | broken, and the fix was **dead code** | 11 / 29 | `and` was treated as an author-position verb, so a list of parenthetical citations was flagged twice over. Removed, list contexts (`include`, `see`) exempted, and findings de-duplicated to one per citation site. **A later review found the exemption never fired.** It tested `s[:m.start() + 1]`, but `NARRATIVE_LEAD` *consumes* the cue word — for `"…reading, see {cite}`x`"` the slice was `'…reading, s'`, so `see\s*$` could not match, and the exemption only worked via the `[.!?]\s+` alternative. Now tested against `s[:m.start()] + m.group(0)` minus the role, which includes the cue. Removed 16 occurrences across 5 lectures, 0 added; every one read as a genuine `see {cite}` reference pointer (`estspec.md:51`, `lqcontrol.md:262` "See {cite}`HansenSargent2008` for details", the two `knowing_forecasts_of_others` footnotes). |
| `qe-fig-009` | broken | 13 / 0 | Counted `:scale:`, which is relative to the image's own pixel size — a screenshot at `:scale: 50` says nothing about how wide it renders, and every one of the 13 hits was a scaled-down screenshot. Restricted to `:width:` as a percentage, which *is* a share of the text width. The corpus has exactly one such value (`100%`), so the rule is now correctly silent. |
| `qe-fig-011` | sound | 0 / 0 | Exhaustively checked: the only nestings in the corpus are `{image}` inside `{prf:example}`, which is what the rule asks for. |
| `qe-admon-001` | broken | 4 / 0 | Counted plain ```` ```python ```` display blocks, which are shown rather than run. The rule is about *executable* cells, so the check now requires a `{code-cell}`. All four hits were display blocks. |
| `qe-admon-002` | sound | 0 / 1 | The single hit is genuine — a `:::{solution-start}` colon fence with no `:class: dropdown`. |
| `qe-admon-003` | sound | 0 / 2 | Both hits read in source and confirmed: `python_by_example.md` has two `{exercise-start}` fences that are never closed. |
| `qe-admon-004` | sound | 0 / 0 | Exhaustively checked: all 244 proof-family directives in the corpus carry the `prf:` prefix. A genuine clean result, not a dead check. |
| `qe-admon-005` | sound | 0 / 0 | Zero hits confirmed live rather than dead — a synthetic solution label with no matching exercise does fire the check. |

## Lexer bugs found along the way

Most false counts turned out to be structural rather than regex errors. Each of these
would have corrupted several rules at once:

1. **`{math}` directive bodies were typed as code.** 1,783 blocks across 172 lectures —
   every math rule was blind to them and every code rule was reading LaTeX. This alone
   moved `qe-math-002` in `lqcontrol` from 11 hits to 61.
2. **Display math closed at the end of a content line** (`… p}$$`) left the `$$` state
   machine inverted, so the rest of the lecture was typed as the wrong region.
3. **Blockquoted display math** (`> $$`) did the same.
4. **Inline maths spanning a line break** (`$N(0,\n\sigma^2)$`) was invisible, so its
   LaTeX looked like narrative text.
5. **Gated `{exercise-start}` treated as a container.** It is a marker: its fence closes
   immediately and `{exercise-end}` is a separate fence. Treating it as a container made
   every later directive look nested, and made `in_exercise` far too broad — which
   suppressed real `qe-fig-003` findings and invented `qe-admon-003` ones.
6. **HTML comments were scanned.** Commented-out prose and maths never reach the page.
8. **A `{code-cell}`'s YAML metadata block was typed as Python.** A cell may open with a
   `---` … `---` mystnb block, and its body is options, not code:
   `caption: Inflation spectra $f_{\pi\pi}(\omega,t)$` was scanned as Python and counted
   as a spelled-out Greek variable. The `:key: value` option spelling was already typed
   `option`; the block spelling was not. Fixed with a three-state flag while a code fence
   is open. `qe-code-002` lost 41 occurrences across 13 lectures, reach 49 → 38, and no
   other rule moved — every removal a `caption:` or `name:` line, with real code on
   neighbouring lines kept (`robust_permanent_income` 5 → 3, `var_subsets` 38 → 37).

   Note what this does *not* fix: a caption's mathematics is now in an `option` region, and
   no math rule reads those. Six captions in that one lecture write a bare `E(...)` where
   the prose writes `\mathbb{E}`. Whether the math rules should read caption text is a
   scope question, not a bug, and is unresolved.
7. **An inline-code span could run across a paragraph break.** `STREAM_CODE_RE` was
   written `` (`+)((?:[^`]|\n(?!\s*\n))*?)\1 `` — but `` [^`] `` matches a newline
   itself, so the `\n(?!\s*\n)` guard beside it was dead code and an unbalanced
   backtick paired with one hundreds of lines away. One stray `` `shock' `` at
   `five_preferences.md:166` — a backtick closed with a typographic apostrophe — masked
   **381 of that file's 798 narrative lines**, leaving 18 inline math spans where there
   are 318. Fixed to `` [^`\n] ``, so a newline is only ever consumed through the
   guarded alternative and a span still spans one line break but never a blank line.
   Corpus effect: `qe-writing-008` +79 occurrences, `qe-math-011` +2, `qe-math-001` +1,
   `qe-math-010` +1 — all in that one file, all real, all previously invisible. Three
   lectures have odd narrative backtick parity; only this one lost lines to it.

## Known limitations, accepted deliberately

Not every gap found is worth closing. These are left in, because closing them would trade a
measured undercount for an unmeasured false-positive rate — and the false-positive rate is
the number this audit's credibility rests on.

- **`qe-math-010`'s bare-letter branch requires a delimiter.** It counts `E[…]`, `E_t(…)`,
  `E\{…\}` but not `E_0 \sum` or `E \tilde\theta_t^2`, so a lecture that writes every
  expectation without brackets is undercounted. Loosening it would have to treat a lone `E`
  as an operator, and in this corpus `E` is very often a matrix. The same pattern computes
  the `e_is_operator` gate, so in a file where *every* expectation is delimiter-free the
  branch switches off entirely — `tax_smoothing_1` (lines 70, 203, 354) and
  `tax_smoothing_2` (122) are the known instances, both scoring 0 on the branch. The
  explicit-notation branches (`\mathbb E`, Roman spellings) are unaffected and do fire
  there.
- **`qe-ref-001` cannot see a bare author-year reference.** A reference written as plain
  prose — "Rosen and Topel (1988)" with no `{cite}` role — is invisible to a check that
  looks at roles. `match_transport` (1421) and `smoothing` (761, 791) score a clean
  References mark while containing exactly that.
- **`:load:` code cells are outside the scanner's reach.** A cell that executes a file from
  `_static/lecture_specific/` has no source in the lecture, so no `qe-code-*` or `qe-fig-*`
  rule can inspect it. `rob_markov_perf` (453) loads the non-robust MPE that every
  comparison in that lecture is measured against.
- **`qe-writing-006` depends on a curated noun list.** Any surname absent from
  `PROPER_NOUNS` reads as a lowercase word that should have been capitalised, and
  `_is_proper` requires *every* hyphen-part to be known — so `Rosen-Topel` fails on its
  second half. Two false positives are known in `hs_recursive_models` (1695, 1892).

Each of these is a reason to read the cited lines before trusting a category score, not a
reason to distrust the corpus totals.

- **`qe-math-002`: the primed next-period state is now handled per lecture.** The
  apostrophe is genuinely ambiguous in this corpus — a transpose in the LQ lectures, a
  continuation state in the dynamic-programming ones, and `arellano.md:147` says so
  outright: "a prime denotes a next period value". No pattern can separate them at the
  occurrence level, so the check now decides per *file*. Three forms cannot be anything
  but a transpose: a prime on a closing delimiter (`(A+B)'`, `\end{bmatrix}'`), a prime
  juxtaposed with the factor that follows it (`x_t' R x_t`), and a prime on the repeat of
  the symbol before it (`CC'`, `U_t U_t'`). A lecture writing any of them uses the
  apostrophe as a transpose, so the rest of its apostrophes count; a lecture writing none
  of them does not, and none of its apostrophes count. Removed 242 occurrences across 13
  lectures — `atkeson_1991` 71 (Math 5.0 → 9.5, HIGH → LOW), `tsyrennikov_2013` 50,
  `arellano` 31, `repeat_mh` 25 — with 0 added and all eight canary transposes intact.
  **The first version of this gate covered only the bare-apostrophe branches**, so the
  same next-period-state class survived in the `^\prime` spelling: `navy_captain` scored
  6 on `\pi^{\prime}` and `z^{\prime}` in a file whose line 633 *defines* the prime as
  the posterior after one more draw, and whose `\top` and `^T` counts are both zero.
  `lprime` is now gated on the same flag and can also supply evidence for it. −8, and
  the 230 legitimate `^\prime` hits in eight other files are untouched because those
  files carry bare-apostrophe evidence.
  Not extended: a `^\prime` on a `}` as *evidence*. A brace before it is usually a
  subscript's closing brace rather than a transposed group, so `Q_{r}^\prime` — next
  period's Q in `mccall_q` — falsely switched that file's branches back on and added a
  hit. Measured, reverted, and left as a comment on `DELIM_PRIME`.
- **The three `qe-math-002` branches still double-count the same site.** `x_t' R x_t` is
  reported once by the `prime` branch for `x_t'` and again by `prime_vec` for `t'`.
  `check_math_010` solved the same problem by having its branches mask each other after
  each pass; `check_math_002` should do the same.

- **`qe-ref-001` treats a line-initial citation as sentence-initial.** The check runs per
  source line, so `^\s*\{cite\}` fires on a wrapped paragraph continuation. 167 citations
  are line-initial across 80 lectures; for 90 the previous line does not end a sentence.
  Not fixed, and deliberately: many of those 90 are *correct* findings reached by the wrong
  mechanism — `chang_ramsey.md:581` wraps mid-sentence after "the insights of Kydland and
  Prescott", so the citation genuinely wants `{cite:t}`. Repairing the line-break heuristic
  alone would delete them. The real fix is author-name detection, which is the upstream
  definition question in `contributions/issues/06-…`.

### The `qe-math-002` evidence pass disagreed with its own counting pass

`os_time_iter` scored 8 findings, all of them `u'` — the derivative of utility, composed
with a policy as `(u' \circ \sigma^*)`. Its whole Math score rested on them.

The per-file evidence gate asks whether a lecture uses the apostrophe as a transpose at all.
One of its signals is `)'` on a closing delimiter. `os_time_iter`'s only such site is
`(v^*)'(x)` at line 109 — which is precisely the shape `fn_paren` exists to exempt, because
a parenthesised *function name* applied to an argument is a derivative. The counting pass
applied that exemption; the evidence pass did not. So the gate opened on a site the counter
would have thrown away, and every ordinary derivative prime in the file was then counted.

The two passes now share the exemption. 16 occurrences removed — `os_time_iter` in both the
series that carry it — reach 66 → 64, nothing added, and all nine canary lectures unchanged.

The general lesson, which cost two other bugs today: **when a check has an evidence phase and
a counting phase, they have to agree about what the evidence is.** A signal the counter
rejects must not be allowed to unlock the counter.

### `qe-math-011` flagged the null space as a distribution

All 8 hits in `svd_intro` were `{\mathcal N}(X)`, the null space of a matrix, and line 129
says so outright: *"let ${\mathcal C}$ denote a column space, ${\mathcal N}$ denote a null
space, and ${\mathcal R}$ denote a row space"*. The `DIST_AFTER` gate accepted any `(` as a
parameter list, so an operator applied to a matrix looked like a law applied to parameters.

A declaration override was available — the mechanism `qe-math-002` uses — but the data
suggested something better. Splitting every hit in the corpus by argument shape is a clean
partition: all 8 comma-less arguments are `svd_intro`'s null space, and all 134 genuine
distribution sites carry a comma (`{\cal N}(0,I)`, `\mathcal N(\mu, \sigma^2)`). So a
parameter list now has to have more than one parameter. A name introduced by `\sim` needs no
parameters at all and is unaffected.

That generalises where a declaration would not: any lecture using `\mathcal N` for a null
space is now handled, whether or not it says so. 8 removed, reach 35 → 34, nothing added.

### `qe-code-002` counted other people's parameter names

`qe.LQ(Q, R, A, B, C, beta=β, T=T)` was reported as a spelled-out Greek variable. It is a
keyword argument of QuantEcon.py's `LQ`, and the author cannot rename it — they are already
passing `β`, having complied with the rule for their own variable. The same shape appears as
`qe.LQMarkov(..., beta=β)` and `qe.tauchen(rho=ρ, sigma=ν)`.

The reviewer's diagnosis of the *mechanism* was wrong, and checking it was what found the
real one. It blamed the imported-name exemption being switched off by its own `=` guard, but
in `lqcontrol` `beta` is never imported — `LQ` is. The exemption was not misfiring; it simply
did not apply, and no rule covered the case. Applying the reviewer's fix as described changed
nothing at all: 0 files, measured.

The exemption is therefore **callee-based**: a Greek name used as a keyword argument is
exempt when the enclosing callee is an imported name. A lecture's own `def f(alpha=0.5)` is
still its own naming choice and still counts. Removed 99 occurrences across 42 lectures,
reach 85 → 49, with `likelihood_ratio_process.md:541`'s real `beta = np.array(...)` intact.

The callee lookup is per line, so a keyword argument on a continuation line of a multi-line
call has no visible `(` and is not exempted — `dyn_stack` keeps 1 of its 4 hits for that
reason. That is the conservative direction (a retained false positive, not a lost finding),
and it is the fourth instance of the single-line/multi-line hazard recorded here.

### `qe-code-003` could not see the install cell it asks about

`_python_blocks` dropped every non-executing cell, on the reasoning that illustrative code
is not a dependency. But `!pip install jax` under `:tags: [skip-execution]` is the standard
idiom in the GPU lectures — the cell is skipped *because the build image already has the
package* — so the rule reported "no install cell" for the three lectures that use it
(`two_computation`, `ak_aiyagari`, `back_prop`).

Getting this right took two corrections, and both are worth recording because each was a
new false positive rather than a miss:

1. Including skipped cells made the rule then demand `hide-output` on them. A cell that
   never runs has no output to hide, so that requirement is now waived for
   `skip-execution` / `no-execute`.
2. Including *all* non-executing cells pulled in `:class: no-execute` blocks, and
   `getting_started` — the installation tutorial — uses those to show the reader how to
   install QuantEcon.py. The rule reported them as install cells "not near the top" of a
   585-line file. They are not this lecture's dependencies at all.

So the two spellings are now distinguished, because they mean different things:
`skip-execution` on a `{code-cell}` is *this lecture's* install, deferred; `no-execute` on a
`{code-block}` is example code for the reader. Only the first is ever an install cell.
Result: 3 occurrences removed, reach 32 → 29, nothing added, no other rule moved.

### `qe-code-002` was reading docstring prose as code

`check_code_002` called `_strip_py(l.raw)` **one line at a time**. The docstring regexes are
multi-line, so an *interior* line of a triple-quoted string carries no quote characters and
stripping it in isolation masks nothing — the English and LaTeX inside numpydoc prose was
being counted as spelled-out Greek variables. All 11 hits in `von_neumann_model` were of that
kind, in a lecture whose code already uses `α`, `β` and `γ` correctly; `samuelson` was flagged
for `Y_t = \alpha (1 + \beta) Y_{t-1}` written inside a docstring.

`check_code_003` in the same file had always stripped per cell. This now matches it, mapping
the stripped body back onto line numbers — safe because `_strip_py` preserves line structure,
which is itself a fix from an earlier pass. Removed 28 occurrences across 9 lectures, reach
89 → 85, and no other rule moved. `sargent_surico` went 89 → 87, keeping its real code hits
(`def lucas_filter(x, beta=0.95)`).

Worth noticing that this is the third distinct bug caused by looking at one line where the
construct spans several — the others being the display-math state machine and the
unbalanced-backtick masking. When a check consults `l.raw`, ask what the enclosing cell or
paragraph looks like first.

### An author's stated convention beats the heuristic

`var_dmd` scored 28 `qe-math-002` findings and line 75 says, in prose, *"here $'$ is part of
the name of the matrix $X'$ and does not indicate matrix transposition"*. Line 120 settles
it beyond argument — `\hat A = X' X^\top (X X^\top)^{-1}` uses the prime as a name and
`\top` as the transpose on one line — and the file uses `\top` 92 times.

The per-file evidence gate could not see this: `FOLLOWING_FACTOR` cannot tell a transposed
matrix in a product from a prime-*named* matrix in a product, so `X' X^+` at line 97 read as
evidence. A ratio test would have been the wrong instrument — `linear_algebra` has 114 prime
hits against a single `\top` and its primes really are violations.

So a *declaration* now overrides the heuristic. `PRIME_NOT_TRANSPOSE` looks for the author
saying it: "does not indicate … transpose", "part of the name", "denotes a next period".
Three lectures in the corpus declare one — `var_dmd`, `arellano` and `opt_tax_recur` — and
the last two were already handled by the evidence rule. Effect: `var_dmd` 28 → 0, and not
one other file moved.

### `qe-code-002` and imported names

A name the lecture *imports* is not a variable it chose to spell out: `from scipy.stats
import beta` binds a distribution, `from sympy import Lambda` binds a class, and renaming
either to `β`/`Λ` breaks the import and means something else. This was reported six separate
times before being fixed. Names bound by an `import` in the file are now exempt: **105
occurrences removed across 21 lectures**, reach 106 → 88. Sampled across `lln_clt`,
`bayes_intro`, `scipy`, `imp_sample` and `equalizing_difference` — every one a library call,
and several of those files already use `β`/`γ` correctly for their own variables.

The reviewer argued the exemption "cannot produce a false negative". At *name* scope that is
true; at *file* scope it is not, and the corpus contains exactly one counterexample:
`likelihood_ratio_process.md:541` writes `beta = np.array(...)` for a type-II error
probability, shadowing the import with a variable that genuinely should be `β`. The
exemption therefore does not apply on a line that *assigns* the name, which keeps that one
finding. 105 false positives out of, 1 true positive kept.

### Two fixes that were verified, then rejected

Both came from reviewer doubts, both reproduced exactly, and both were rejected because
they fail the both-directions test. Recording them so they are not re-proposed, and so a
narrower version has somewhere to start.

- **`qe-writing-004` on markdown link labels and quoted titles.** 60 of its 64 removals are
  correct — a label reproducing a lecture or book title is not the author's capitalisation.
  But 4 occurrences on 3 lines are genuine: `[Envelope Theorem](…/Envelope_theorem)` in
  `os.md:501`, `[Pareto Distribution]` in `mle.md:298`, `[Gershgorin Circle Theorem]` in
  `eigen_II.md:457`. In each the linked article's own title is lowercase — Wikipedia slugs
  preserve case, and the same set contains genuinely Title-Case slugs like
  `Golden_Rule_savings_rate` — and the corpus writes the same term lowercase elsewhere
  ("envelope theorem" 10×, including `os_time_iter.md:113` linking the *same URL* with a
  lowercase label). That is the rule's own *inconsistent capitalisation* bullet. A patch
  that exempts link labels must first distinguish a reproduced title from an author's own
  words, and the URL slug is the available signal.
- **`qe-writing-004` on "Example N" as a section reference.** The mechanics were clean —
  71 removed, 0 added, no offset or backtracking trap — but the premise is wrong. The
  claim is that `<capitalised common noun> <number>` names a labelled item and is never
  the rule's business. The corpus disagrees: `var_dmd.md` writes "Representation 3"
  capitalised 8 times and "representation 3" lowercase 8 times for the *same three
  headings*, three lines apart. That is precisely the inconsistency the rule exists to
  find, so the 71 removals include real findings.

### The build's warnings: 478 down to 23

Almost all of them were one thing. Reviewer prose and the detectors' own sample text quote
MyST roles from the corpus — `` {cite}`Hall1978` ``, `` {eq}`label` ``, `` {doc}`ifp_egm` ``
— and left bare, Sphinx tries to resolve every one against a book that does not contain the
cited work. 615 such roles across the 348 reports produced 478 of the build's warnings, and
the count grew with every batch of overlays (263 → 309 → 391 → 478), heading for roughly 700
at full coverage. At that level the build stops being a usable signal for a real problem.

`escape_roles()` in `qestyle_draft.py` now wraps them as literal spans at every point prose
reaches a report — mechanical sample text, reviewer finding detail, strengths, actions and
rule titles — and `qestyle_report.py` does the same for the titles it splices into the series
tables. Build warnings: **478 → 23**.

Two things had to be right, and neither is obvious:

- **The space padding is load-bearing.** ``` ``{doc}`x``` ``` closes on a run of three
  backticks and does not parse as a code span. `` `` {doc}`x` `` `` does. The hand-written
  prose in `intro.md` already used the padded form, which is the clue.
- **One dangling backtick was upstream, not a rendering problem.** `qe-ref-001`'s detail
  quoted `m.group(0)`, and that match *ends* in a backtick, so the sample carried a stray one
  that no escaping could close. Fixed in the detector.

Worth recording how the measurement went wrong twice, because the same trap is easy to fall
into again: the first count treated the escaped form as unescaped — the padding space defeats
a `` (?<!`) `` lookbehind — which made a working fix look like it had done nothing. The
warning count is the only ground truth here.

The 23 that remain are hand-written prose quoting examples in `intro.md`, `appendix.md` and
`cross_product_trick`'s malformed `eq:Kalman102}` target, plus three `mcmc` theorem labels
that genuinely do not exist in this book. That is the "few dozen standing" level the runbook
describes, and a new warning is now visible against it.

## Reproducing this

```bash
cd tools
python3 - <<'PY'
import sys, glob; sys.path.insert(0, '.')
from qestyle_lex import lex
from qestyle_rules import CHECKS
rule = 'qe-fig-003'
for f in glob.glob('/path/to/quantecon/lecture-python.myst/lectures/*.md'):
    for h in CHECKS[rule](lex(f, 'lecture-python.myst')):
        print(f"{f}:{h.line}: {h.detail}")
PY
```

Then open each cited line and judge it against
`action-style-guide/style_checker/rules/`. A rule is only as good as the sample someone
actually read.
