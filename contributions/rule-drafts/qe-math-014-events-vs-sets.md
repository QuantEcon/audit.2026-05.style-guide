# `qe-math-014` — Braces `\{…\}` for events; parentheses `(…)` for sets when using `\mathbb{P}`

**Target file:** `style_checker/rules/math-rules.md`
**Style-guide source:** [`math.md` § Probability, expectation, and variance](https://github.com/QuantEcon/QuantEcon.manual/blob/main/manual/styleguide/math.md)

> ⚠️ **Weaker-evidence proposal.** Documented in the style guide but with limited corpus evidence; included for completeness. The team may prefer to defer this or fold its check into `qe-math-010` rather than create a separate rule.

---

## Rule entry (ready to append to `math-rules.md`)

```markdown
### Rule: qe-math-014
**Type:** style  
**Title:** Braces for events, parentheses for sets with \mathbb{P}

**Description:**  
When writing probability using `\mathbb{P}`:
- Use **curly braces** `\{...\}` for events (logical conditions on random variables)
- Use **parentheses** `(...)` for sets (subsets of the sample space named by a symbol)

**Check for:**
- `\mathbb{P}(X = x)` — event written with parentheses (should be `\mathbb{P}\{X = x\}`)
- `\mathbb{P}\{B\}` where $B$ is a named set — should be `\mathbb{P}(B)`

**Guidance:**  
This is a judgment call that requires understanding whether the argument is an event (a logical condition) or a set (a named subset). Both forms are syntactically valid; the rule is about semantic appropriateness.

**Examples:**
```markdown
<!-- ✅ Correct -->
$\mathbb{P}\{X = 5\}$         (event — logical condition)
$\mathbb{P}\{X \leq x\}$       (event)
$\mathbb{P}\{X \in A\}$        (event — membership)
$\mathbb{P}(B)$                (set — named subset)
$\mathbb{P}(A \cap B)$         (set — intersection)

<!-- ❌ Incorrect -->
$\mathbb{P}(X = 5)$            (event written with parens)
$\mathbb{P}\{B\}$              (named set written with braces)
```
```

---

## Rationale (for issue / PR body, not for the rules file)

**Style-guide quote** (`math.md`):
> Use `\mathbb{P}` for probability, with braces `\{...\}` for events and parentheses `(...)` for sets:
> 
> `$\mathbb{P}\{X = 5\}$, $\mathbb{P}\{X \leq x\}$, $\mathbb{P}(B)$`

**Corpus evidence (May 2026 audit):** Limited. The rule was documented in the audit spec (under provisional ID `qe-math-A2`) but few clean violations were tallied in the corpus.

**Recommendation:** Three options for the team:

1. **Defer** — wait until evidence accumulates from a future audit before formalising.
2. **Fold into `qe-math-010`** — the parent rule already covers `\mathbb{P}` usage; this can be a sub-rule mentioned in `qe-math-010`'s description rather than a separate rule.
3. **Add as `style` type** — explicitly judgment-based, no auto-fix, just flag for human review.

**Why judgment:** Distinguishing "event" (logical condition) from "set" (named subset) requires reading the surrounding text. Not a Phase 4.3 candidate.
