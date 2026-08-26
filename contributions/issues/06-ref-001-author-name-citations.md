# `qe-ref-001`: the rule needs to say what "narrative citation" means

**Repo:** `action-style-guide` · **Rule:** `qe-ref-001` (citation style, `{cite}` vs `{cite:t}`)
**Status:** a rule-definition question, not a bug report. Measured against the 348-lecture
corpus at the 2026-08 snapshot.

## What we found

`qe-ref-001` asks for `{cite:t}` where the author's name is part of the sentence, and plain
`{cite}` otherwise. Our checker approximates "part of the sentence" with a lead-word list —
the citation counts as narrative when it follows `by`, `of`, `in`, `to`, `from`, `following`,
`see`, `and`, `with`, `per`, `after`, `via`, a sentence start, or a full stop.

Instrumenting all **1,381** `{cite}` roles in the corpus buckets them as:

| bucket | count |
|---|---:|
| no lead word — not examined | 796 |
| exempted as parenthetical | 290 |
| flagged by lead word | 277 |
| flagged by trailing verb | 18 |

Of the 796 unexamined, the token immediately before the citation is **a capitalised surname
that also appears in the citation key** at **299** of them. All 62 distinct matched tokens are
surnames — Chang 30, Calvo 26, BEGS 24, Stokey 23, Barro 21, Hall 18, Cagan 15, Sargent 9,
Friedman 9 — with no common-word coincidences. These read exactly like the rule's own ❌ shape:

- `Sargent {cite}`sargent91_equilibrium` proposed a way to compute an equilibrium`
- `Hamilton {cite}`Hamilton2005` estimated the stochastic matrix`
- `Following Calvo {cite}`Calvo1978`, we assume that the government chooses…`

The last one is a direct inversion of the rule's ✅ example, `Following {cite:t}`Sargent1987`,
we adopt…`.

## Why we have not changed our checker

Extending it to catch author-name-in-prose moves `qe-ref-001` from 298 occurrences across 110
lectures to **648 across 163** — a 117 % increase, with 53 lectures acquiring a References
finding they did not have. That is a large enough swing that it should follow a decision about
the rule, not precede one.

More importantly, **151 of the 293 additions turn on a question the rule does not answer.**
They are citations that end a clause:

> `…in the spirit of Hall {cite}`Hall1978`.`

Is that narrative — the author's name is in the sentence, so `{cite:t}` — or is it the
parenthetical case the rule exempts, because the citation itself sits at the end as a
reference? Our checker currently exempts it. A reasonable reading says it should not. We do
not think an audit should decide that on the style guide's behalf.

## What would settle it

One sentence in `references.md` saying which of these is wanted:

1. **Name in the sentence wins.** Any citation whose immediately preceding token is an author
   surname takes `{cite:t}`, wherever it sits. (+293 findings here.)
2. **Position wins.** A citation ending a clause is parenthetical regardless of what precedes
   it; `{cite:t}` is for citations in subject or object position. (+142 findings here.)

Either is mechanically checkable and we will implement whichever is chosen. What is not
checkable is the current text, which leaves the commonest case in the corpus undetermined.

## A corpus bug found on the way

Four lines carry a stray `)` immediately after a citation role, which also happens to trip our
parenthetical exemption and suppress a real detection:

- `lecture-python-advanced.myst/tax_smoothing_1.md:41`
- `lecture-python-advanced.myst/tax_smoothing_2.md:32`
- `lecture-python-advanced.myst/tax_smoothing_3.md` (the `barro2003religion` citation)

Each is mirrored in `lecture-dp`, so eight sites in all. These are prose typos in the lectures
rather than a style question, and are worth fixing on their own.
