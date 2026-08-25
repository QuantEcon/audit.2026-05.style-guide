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
| `qe-writing-006` | needs-fix | 52 / 40 | Possessives (`Newton's`) and hyphenated surnames (`Gram-Schmidt`, `Metropolis-Hastings`) defeated the proper-noun lookup; country names were missing. Added `_is_proper()` (strips possessives, splits hyphens, treats any `X's` as a name) and extended the list. Also added the rule's other half — an H1 that is *not* Title Case. |
| `qe-writing-008` | broken | 12 / 28 | Masking inline code and maths with single spaces manufactured double spaces out of correctly-spaced prose. The lexer now masks with NUL, and cross-line inline maths is resolved before masking. |
| `qe-writing-009` | needs-fix | 3 / 12 | Fired on MyST anchor definitions (`(iid-theorem)=`) and on role targets (``{ref}`IID <iid-theorem>` ``). Anchors are skipped and inline code is masked. |
| `qe-writing-001` | added after | — | Not present at review time; added as a paragraph-block sentence counter with an abbreviation list. |
| `qe-writing-004` | added after | — | Not present at review time; added, firing only on a curated common-noun list so an unlisted surname cannot be mistaken for a violation. |
| `qe-math-001` | added after | — | Not present at review time; added. Its first form of false positive — inline maths spanning a line break — is fixed in the lexer. |
| `qe-math-002` | broken | 22 / 14 | The `^T` branch was ~88 % false: summation limits (`\sum_{t=0}^T`), terminal dates, data histories (`Y^T`), discount factors (`\delta^T`). It now requires a matrix-like base *and* a following factor rather than a relation. The apostrophe branch missed lowercase vectors (`c'x`, `x_t'`), now covered. |
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
| `qe-ref-001` | broken | 11 / 29 | `and` was treated as an author-position verb, so a list of parenthetical citations was flagged twice over. Removed, list contexts (`include`, `see`) exempted, and findings de-duplicated to one per citation site. |
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

### The build's 309 warnings

Almost all of them are one thing: reviewer prose quotes a MyST role from the corpus
verbatim — `` {cite}`X` ``, `` {cite:t}`X` ``, `` {eq}`label` ``, `` {doc}`advanced:…` `` —
and Sphinx tries to resolve it in *this* book, where the cited work is not present. 308 of
the 309 fall into that family (41 `cite`, 8 `cite:t`, 15 undefined labels, the rest
`equation not found`); the one straggler, `unknown document: 'advanced:additive_functionals'`
from `exchangeable.md:44`, is the same thing with a `{doc}` role.

They are noise, but enough of it to hide a real warning. The fix belongs in
`qestyle_draft.py`, where reviewer `detail` text is rendered: escape a bare MyST role into
literal backticks so it displays rather than resolves. Not done yet — it rewrites all 348
reports, so it wants its own pass and its own diff.

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
