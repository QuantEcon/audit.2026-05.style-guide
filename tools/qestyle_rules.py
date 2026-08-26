"""Deterministic checks for the mechanically-detectable ``qe-*`` rules.

Every check returns a list of ``Hit`` records so the audit can quote a line
number for each finding. Rules are implemented from the definitions in
``QuantEcon/action-style-guide/style_checker/rules/``; the seven proposed rules
(``qe-writing-009``, ``qe-math-010``–``qe-math-015``) follow the audit spec §3.

Nothing here scores a lecture — the checks only measure. Scoring stays with the
rubric in ``lectures/spec.md``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from qestyle_lex import INLINE_CODE_RE, Doc, strip_inline

SERIES_DOMAIN = {
    "lecture-python-intro": "intro.quantecon.org",
    "lecture-python-programming": "python-programming.quantecon.org",
    "lecture-python.myst": "python.quantecon.org",
    "lecture-python-advanced.myst": "python-advanced.quantecon.org",
    "lecture-dp": "quantecon.github.io/lecture-dp",
}
QE_SERIES_DOMAINS = [
    "intro.quantecon.org", "python-programming.quantecon.org",
    "python.quantecon.org", "python-advanced.quantecon.org",
    "jax.quantecon.org", "julia.quantecon.org", "stats.quantecon.org",
    "quantecon.github.io/lecture-dp", "python-intro.quantecon.org",
    "dp.quantecon.org", "networks.quantecon.org", "dle.quantecon.org",
]


@dataclass
class Hit:
    rule: str
    line: int
    detail: str


# ---------------------------------------------------------------------------
# Writing
# ---------------------------------------------------------------------------

# Proper nouns and acronyms that may legitimately be capitalised mid-heading.
# Curated from the capitalised-heading-word frequency table over the corpus.
PROPER_NOUNS = {
    # people
    "bellman", "markov", "ramsey", "euler", "stackelberg", "gaussian", "bayes",
    "bayesian", "kalman", "phelps", "riccati", "pareto", "laffer", "keynes",
    "keynesian", "blackwell", "phillips", "wold", "lucas", "gini", "neumann",
    "solow", "hamiltonian", "hamilton", "samuelson", "nash", "dubins", "cagan",
    "sargent", "sims", "hansen", "jagannathan", "jacobi", "newton", "raphson", "taylor",
    "student",                      # Gosset's pen name: "Student-t", "Student's t"
    "cauchy", "schwarz", "hilbert", "banach", "lyapunov", "sylvester", "cholesky",
    "frobenius", "perron", "chebyshev", "bernoulli", "poisson", "cobb", "douglas",
    "koopmans", "cass", "diamond", "arrow", "debreu", "walras", "walrasian",
    "nagel", "rothschild", "stiglitz", "aiyagari", "huggett", "bewley",
    "friedman", "wald", "chernoff", "kullback", "leibler", "shannon", "hopenhayn",
    "prescott", "kydland", "barro", "gordon", "abreu", "chang", "calvo", "mccall",
    "coase", "schelling", "kesten", "zipf", "lorenz", "jensen", "lagrange",
    "lagrangian", "hessian", "jacobian", "laplace", "fourier", "toeplitz",
    "vandermonde", "kronecker", "sherman", "morrison", "woodbury", "harrison",
    "kreps", "muth", "granger", "theil", "tauchen", "rouwenhorst", "sieve",
    "kuhn", "tucker", "karush", "bolzano", "weierstrass", "lipschitz", "borel",
    "lebesgue", "radon", "nikodym", "chapman", "kolmogorov", "wiener", "brownian",
    "ito", "feynman", "kac", "bertrand", "cournot", "stokey", "ljungqvist",
    "atkeson", "hopf", "gorman", "tsyrennikov", "marimon", "mcgrattan", "surico",
    "misspecified", "sz", "morris", "shin", "epstein", "zin", "kihlstrom",
    "mangasarian", "arellano", "eaton", "gersovitz", "dovis", "matsuyama",
    "bhandari", "evans", "sarte", "golosov", "tsyvinski", "werning", "aiyagari",
    "hall", "flavin", "campbell", "deaton", "carroll", "zeldes", "attanasio",
    "rosen", "sherwin", "roth", "shapley", "gale", "monge", "kantorovich",
    "sinkhorn", "hotelling", "ricardo", "malthus", "smith", "mill", "marshall",
    "edgeworth", "slutsky", "roy", "shephard", "hicks", "leontief", "sraffa",
    "dmd", "svd", "var", "vars", "lq", "lqg", "opi", "vfi", "egm", "hjb",
    # places and institutions
    "china", "usa", "us", "uk", "europe", "european", "america", "american",
    "japan", "germany", "france", "argentina", "brazil", "india", "australia",
    "quantecon", "nber", "fred", "imf", "oecd", "worldbank", "penn", "cambridge",
    "chicago", "minnesota", "stanford", "mit",
    # software and formats
    "python", "numpy", "scipy", "pandas", "polars", "matplotlib", "numba",
    "jax", "jupyter", "anaconda", "conda", "notebook", "notebooks", "github",
    "git", "latex", "myst", "markdown", "html", "pdf", "csv", "json", "yaml",
    "sympy", "statsmodels", "sklearn", "pytorch", "tensorflow", "plotly",
    "networkx", "graphviz", "vscode", "linux", "macos", "windows", "unicode",
    "pep", "api", "cpu", "gpu", "tpu", "jit", "llvm", "ipython", "colab",
    "yfinance", "wbgapi", "cvxpy", "quandl", "excel", "openai",
    # month/era style capitals occasionally used in headings
    "covid", "wwii", "gdp", "cpi", "ols", "gls", "mle", "iid", "clt", "lln",
    "ar", "arma", "arima", "garch", "mcmc", "kkt", "sir", "seir", "olg", "dsge",
    "ree", "rbc", "pv", "npv", "cara", "crra", "ces", "hank", "tank",
    # surnames and place names surfaced while verifying qe-writing-006
    "schmidt", "gram", "smirnov", "pearson", "neyman", "metropolis",
    "hastings", "kingdom", "states", "united", "nations", "york",
    "britain", "kong", "korea", "zealand", "africa", "asia", "latin",
    "east", "west", "north", "south", "world", "war", "great",
    "depression", "revolution", "french", "german", "japanese",
    "chinese", "british", "spanish", "italian", "dutch", "russian",
}
# Words that are commonly capitalised in these headings but are not proper nouns.
# Kept explicit so the check is transparent rather than dictionary-driven.
STOP_SMALL = {"a", "an", "the", "of", "in", "on", "to", "for", "and", "or",
              "with", "by", "at", "as", "from", "vs", "via", "is", "it"}

# Common nouns observed capitalised mid-sentence in this corpus. ``qe-writing-004``
# fires only on this curated set, so the check cannot mistake an unlisted surname
# for a style violation.
COMMON_NOUNS = {
    "model", "models", "function", "functions", "problem", "problems", "example",
    "examples", "equation", "equations", "operator", "operators", "iteration",
    "iterations", "data", "optimal", "policy", "policies", "distribution",
    "distributions", "inequality", "value", "values", "code", "economy",
    "decision", "state", "states", "features", "conditions", "programming",
    "process", "processes", "algorithm", "algorithms", "implementation",
    "income", "method", "methods", "approach", "horizon", "linear", "case",
    "cases", "equilibrium", "equilibria", "dynamics", "rule", "rules",
    "representation", "representations", "pricing", "grid", "theory",
    "properties", "property", "difference", "household", "households", "matrix",
    "matrices", "results", "result", "rate", "rates", "theorem", "variables",
    "variable", "growth", "remarks", "comparison", "version", "errors", "error",
    "application", "applications", "initial", "decomposition", "interpretation",
    "price", "prices", "calculations", "operations", "types", "type",
    "libraries", "classes", "class", "point", "points", "parameters",
    "parameter", "capital", "average", "constant", "component", "components",
    "solution", "solutions", "probabilities", "probability", "expectations",
    "expectation", "wealth", "eigenvalues", "eigenvalue", "dynamic", "path",
    "paths", "order", "supply", "demand", "curves", "curve", "statics",
    "residual", "sample", "samples", "chain", "chains", "numbers", "number",
    "multiplier", "interest", "series", "sources", "syntax", "content", "loops",
    "loop", "plots", "plot", "infinite", "ratio", "shocks", "shock", "moments",
    "means", "mean", "stationary", "stationarity", "savings", "simple",
    "implications", "response", "duopoly", "primitives", "asset", "assets",
    "kernel", "transition", "outcomes", "outcome", "assumptions", "assumption",
    "critique", "law", "laws", "utility", "consumption", "output", "labor",
    "labour", "welfare", "firm", "firms", "agent", "agents", "consumer",
    "consumers", "producer", "market", "markets", "money", "inflation",
    "unemployment", "tax", "taxes", "debt", "bond", "bonds", "portfolio",
    "risk", "return", "returns", "investment", "savings", "discount", "budget",
    "constraint", "constraints", "objective", "control", "controls", "action",
    "actions", "reward", "rewards", "horizon", "step", "steps", "stage",
    "stages", "period", "periods", "time", "space", "spaces", "set", "sets",
    "vector", "vectors", "scalar", "sequence", "sequences", "series",
    "convergence", "stability", "existence", "uniqueness", "simulation",
    "simulations", "estimation", "estimate", "estimates", "prediction",
    "forecast", "forecasts", "likelihood", "posterior", "prior", "priors",
    "density", "densities", "moment", "variance", "covariance", "correlation",
    "regression", "residuals", "shock", "innovation", "innovations",
}


def _heading_words(title: str):
    t = re.sub(r"`[^`]*`", " ", title)
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\{[^}]*\}", " ", t)          # {ref}`...` targets, anchors
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return t


def _is_proper(word: str) -> bool:
    """Allowlist lookup that tolerates possessives and hyphenated surnames.

    ``Newton's`` and ``Gram-Schmidt`` are proper nouns even though neither string
    is in the set: the first carries a possessive, the second is two names.
    """
    if re.search(r"['\u2019]s$", word):
        return True                 # a possessive in a heading names someone
    lw = re.sub(r"['\u2019]s?$", "", word.lower())
    if lw in PROPER_NOUNS or lw in STOP_SMALL:
        return True
    parts = [x for x in re.split(r"[-\u2013\u2014]", lw) if x]
    # A single letter in a hyphenated name is a mathematical label, not a word that
    # should have been lowercased: ``Student-t``, ``F-test``, ``p-value``. Requiring it
    # to be allowlisted would mean listing every letter.
    return len(parts) > 1 and all(
        len(x) == 1 or x in PROPER_NOUNS or x in STOP_SMALL for x in parts)


def check_writing_006(doc: Doc):
    """H2+ headings must be sentence case; the H1 lecture title is Title Case."""
    hits = []
    for no, level, title in doc.headings():
        t = _heading_words(title)
        if level < 2:
            # The rule's other half: the lecture title itself should be Title Case.
            words = re.findall(r"[A-Za-z][A-Za-z'\u2019\-]*", t)
            content = [w for w in words[1:]
                       if w.lower() not in STOP_SMALL and not _is_proper(w)]
            if len(content) >= 2 and all(w.islower() for w in content):
                hits.append(Hit("qe-writing-006", no,
                                f"H1 lecture title not Title Case: {title!r}"))
            continue
        # A colon or a spaced dash starts a new sub-phrase, so its next word is
        # allowed a capital; a hyphen inside a word does not.
        segments = re.split(r"[:\u2014\u2013]\s+|\s[-\u2013\u2014]\s", t)
        offenders = []
        for seg in segments:
            words = re.findall(r"[A-Za-z][A-Za-z'\u2019\-]*", seg)
            for w in words[1:]:
                if _is_proper(w) or w.isupper():
                    continue
                if re.fullmatch(r"[A-Z][a-z'\u2019]+(?:[-\u2013][A-Za-z][a-z'\u2019]*)*", w):
                    offenders.append(w)
        if offenders:
            hits.append(Hit("qe-writing-006", no,
                            f"H{level} Title Case: {title!r} ({', '.join(offenders[:4])})"))
    return hits


# Abbreviations whose full stop does not end a sentence.
ABBREV = {"e.g", "i.e", "cf", "vs", "etc", "al", "fig", "eq", "sec", "ch", "no",
          "approx", "resp", "viz", "mr", "mrs", "ms", "dr", "prof", "st", "vol",
          "pp", "ed", "eds", "inc", "ltd", "jr", "sr", "i.i.d", "ie", "eg"}
SENT_END = re.compile(r"([.!?])[\"'’)\]]*\s+(?=[A-Z(\[])")


def _paragraph_blocks(doc: Doc):
    """Narrative paragraph blocks: (first_line, [lines]) between blank lines."""
    blocks, cur, start = [], [], None
    for l in doc.lines:
        if l.kind != "text":
            if cur:
                blocks.append((start, cur))
                cur, start = [], None
            continue
        s = l.raw.strip()
        if not s:
            if cur:
                blocks.append((start, cur))
                cur, start = [], None
            continue
        # Headings, list items, tables, targets and directive-ish lines are not prose.
        if (s.startswith("#") or l.in_table or re.match(r"^([-*+]|\d+[.)])\s", s)
                or re.match(r"^\(.+\)=$", s) or s.startswith(">")
                or re.match(r"^:\w[\w-]*:", s) or s.startswith("%")
                or re.match(r"^\|", s)):
            if cur:
                blocks.append((start, cur))
                cur, start = [], None
            continue
        if start is None:
            start = l.no
        cur.append(l.raw)
    if cur:
        blocks.append((start, cur))
    return blocks


def _count_sentences(text: str) -> int:
    t = strip_inline(text)
    t = re.sub(r"\d\.\d", "0 0", t)                 # decimals
    t = re.sub(r"\{[a-z:]+\}`[^`]*`", "X", t)       # roles
    t = re.sub(r"\[[^\]]*\]\([^)]*\)", "X", t)      # links
    t = t.strip()
    if not t:
        return 0
    n = 1
    for m in SENT_END.finditer(t):
        # Reject boundaries that are really abbreviations or initials.
        before = t[:m.start()]
        tok = re.search(r"([A-Za-z.]+)$", before)
        word = tok.group(1).lower().rstrip(".") if tok else ""
        if word in ABBREV or (len(word) == 1 and word.isalpha()):
            continue
        n += 1
    return n


def check_writing_001(doc: Doc):
    """One sentence per paragraph block."""
    hits = []
    for start, lines in _paragraph_blocks(doc):
        n = _count_sentences(" ".join(lines))
        if n >= 2:
            hits.append(Hit("qe-writing-001", start, f"{n} sentences in one paragraph"))
    return hits


def check_writing_004(doc: Doc):
    """No unnecessary capitalisation of common nouns in narrative text."""
    hits = []
    for l in doc.lines:
        if l.kind != "text" or l.in_table:
            continue
        s = l.raw
        if s.strip().startswith("#") or re.match(r"^\s*([-*+]|\d+[.)])\s", s):
            continue
        s = strip_inline(s)
        # Only mid-sentence positions: a lowercase word (or comma) must precede.
        for m in re.finditer(r"(?<=[a-z,])\s+([A-Z][a-z]+)\b", s):
            w = m.group(1)
            if w.lower() in COMMON_NOUNS and w.lower() not in PROPER_NOUNS:
                hits.append(Hit("qe-writing-004", l.no, f"mid-sentence {w!r}"))
    return hits


def check_writing_008(doc: Doc):
    """Multiple consecutive spaces between words in narrative text."""
    hits = []
    for l in doc.lines:
        if l.kind != "text" or l.in_table:
            continue
        s = doc.masked.get(l.no, l.raw)
        if re.match(r"^\s*([-*+]|\d+\.)\s", s):   # list markers use alignment
            s = re.sub(r"^\s*([-*+]|\d+\.)\s+", "", s)
        s = s.lstrip()
        for m in re.finditer(r"\S(  +)\S", s):
            hits.append(Hit("qe-writing-008", l.no, f"{len(m.group(1))} spaces"))
    return hits


def check_writing_009(doc: Doc):
    """(proposed) Write IID, not i.i.d. or iid."""
    hits = []
    pat = re.compile(r"\bi\.i\.d\.?|\biid\b|\bI\.I\.D\.", re.IGNORECASE)
    anchor = re.compile(r"^\s*\([A-Za-z0-9_:.\-]+\)=\s*$")
    for l in doc.lines:
        if l.kind not in ("text", "math", "code"):
            continue
        if anchor.match(l.raw):
            continue                    # a label definition, not prose
        # Blank inline code so a role target such as {ref}`IID <iid-theorem>`
        # is judged on its visible text, not on its link target.
        s = INLINE_CODE_RE.sub(lambda m: "\x00" * len(m.group(0)), l.raw)
        for m in pat.finditer(s):
            if m.group(0) == "IID":
                continue
            hits.append(Hit("qe-writing-009", l.no, m.group(0)))
    return hits


# ---------------------------------------------------------------------------
# Math
# ---------------------------------------------------------------------------

GREEK_CMDS = (r"\\(?:alpha|beta|gamma|delta|epsilon|varepsilon|zeta|eta|theta|"
              r"vartheta|iota|kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|upsilon|"
              r"phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|"
              r"Upsilon|Phi|Psi|Omega)")


def _math_spans(doc: Doc):
    """(line_no, math_source) for every display-math line and inline-math span.

    Inline spans come from the lexer, which resolves them across line breaks.
    """
    for l in doc.lines:
        if l.kind == "math":
            yield l.no, l.raw
    for no, src in doc.inline_spans:
        yield no, src


GREEK_UNICODE = "αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΥΦΨΩ"


def check_math_001(doc: Doc):
    """LaTeX commands belong inside math; unicode Greek does not."""
    hits = []
    for l in doc.lines:
        if l.kind != "text":
            continue
        s = doc.masked.get(l.no, l.raw)
        for m in re.finditer(GREEK_CMDS, s):
            hits.append(Hit("qe-math-001", l.no,
                            f"LaTeX `{m.group(0)}` outside math delimiters"))
    for no, src in _math_spans(doc):
        for m in re.finditer(f"[{GREEK_UNICODE}]", src):
            hits.append(Hit("qe-math-001", no,
                            f"unicode `{m.group(0)}` inside a math environment"))
    return hits


# Commands that follow a superscript in a relation, not a matrix product. Used to
# tell ``Q^TQ`` (a transpose) from ``Y^T \sim N(m,C)`` (a data history through T).
NOT_A_PRODUCT = (
    r"sim|simeq|approx|leq|geq|le|ge|neq|equiv|in|notin|to|rightarrow|Rightarrow|"
    r"leftarrow|mapsto|quad|qquad|ldots|cdots|dots|right|left|big|Big|bigg|Bigg|"
    r"text|mathrm|label|end|begin|forall|exists|mid|implies|iff|sum|prod|int"
)
# A decorated group whose closing brace can carry a transpose: \hat{X}^\top etc.
DECORATED = r"\\(?:hat|tilde|bar|vec|widehat|widetilde|mathbf|boldsymbol|check|dot)\{[^{}]*\}"

# ``\begin{...}``, ``\left`` and the ``\big`` family open a group, so a factor really does
# follow them — ``\end{bmatrix}' \begin{bmatrix}`` is a transpose. Their closing
# counterparts do not, and are named explicitly.
NOT_A_PRODUCT_PRIME = "|".join(
    [t for t in NOT_A_PRODUCT.split("|")
     if t not in {"begin", "left", "big", "Big", "bigg", "Bigg"}]
    + ["bigr", "Bigr", "biggr", "Biggr", "bigm", "Bigm"])
# A prime on a closing delimiter: ``(A+B)'``, ``\end{bmatrix}'``, ``[0,1,0,0]'``.
# Deliberately NOT extended to ``^\prime``: a ``}`` before it is usually a subscript's
# closing brace, not a transposed group, so ``Q_{r}^\prime`` — next period's Q in
# ``mccall_q`` — would falsely signal that the file uses primes for transposes.
DELIM_PRIME = re.compile(r"(?:\)|\}|\])'(?!')")
# A prime on the repeat of the symbol just before it: ``CC'``, ``U_t U_t'``.
REPEATED_PRIME = re.compile(r"(?<![A-Za-z0-9\\])([A-Za-z])(?:_\{[^}]*\}|_[A-Za-z0-9])?"
                            r"\s*\1(?:_\{[^}]*\}|_[A-Za-z0-9])?'(?!')")
# Some lectures say outright that the prime is not a transpose — ``var_dmd`` line 75,
# "here $'$ is part of the name of the matrix $X'$ and does not indicate matrix
# transposition", and ``arellano`` line 147, "a prime denotes a next period value". An
# author's stated convention beats any heuristic, so a declaration switches the
# bare-prime branches off for that lecture. Three lectures in the corpus declare one.
PRIME_NOT_TRANSPOSE = re.compile(
    r"(?:'|\bprime\b|\\prime)[^.\n]{0,120}?"
    r"(?:not\s+(?:indicate|denote|mean)\w*\s+(?:a\s+)?(?:matrix\s+)?transpos"
    r"|part\s+of\s+the\s+name"
    r"|denotes?\s+(?:a\s+)?next[- ]period)", re.IGNORECASE)


# The factor a transpose is juxtaposed with: ``x_t' R x_t``, ``B'\lambda``.
FOLLOWING_FACTOR = re.compile(r"\s*(?:[A-Za-z\[]|\\(?!(?:" + NOT_A_PRODUCT_PRIME + r")\b)[A-Za-z]+)")


def check_math_002(doc: Doc):
    """Transpose must be ``\\top``, not ``\'``, ``^T`` or ``\\prime``."""
    hits = []
    # An apostrophe is transpose rather than a derivative when the base looks like
    # a matrix or an indexed vector, and it is not applied to an argument. That
    # last condition keeps ``u'(c)`` and ``f'(x)`` out of the count.
    prime = re.compile(
        r"(?:[A-Z](?:_\{[^}]*\}|_[A-Za-z0-9])?"          # A, A_t, A_{t+1}
        r"|[A-Za-z](?:_\{[^}]*\}|_[A-Za-z0-9])"          # x_t, u_{t+1}
        r"|\}|\\top)'(?!'|\s*\()")
    # A closing parenthesis is a transpose whatever follows it: ``(A - B)'(C - D)`` is a
    # quadratic form, not a derivative, so the argument guard does not apply to it. This
    # is the same "the base decides" split ``lprime`` uses.
    prime_paren = re.compile(r"\)'(?!')")
    # The one exception: a parenthesised *function name* — ``(v^*)'(x)``, ``(p^*)'(s)`` —
    # is a derivative, so those keep the argument guard. Six sites corpus-wide.
    fn_paren = re.compile(r"\(\s*\\?[A-Za-z][A-Za-z0-9]*"
                          r"(?:\^\{?\*\}?|_\{[^}]*\}|_[A-Za-z0-9])*\s*(\)')"
                          r"(?=\s*(?:\(|\\left\s*\())")
    # Lowercase vectors juxtaposed with another symbol: c'x, b'y.
    prime_vec = re.compile(r"(?<![A-Za-z0-9\\])([a-z])'(?!')"
                           r"(?=\s*(?:[A-Za-z]|\\(?!(?:" + NOT_A_PRODUCT + r")\b)[A-Za-z]+))")
    # ``^T`` is ambiguous in this corpus (terminal date, summation limit, data
    # history), so it counts only where the base is a matrix-like symbol AND the
    # superscript is followed by a factor rather than a relation.
    supT = re.compile(
        r"(?:(?<![A-Za-z0-9\\])[A-Z]|" + DECORATED + r")"
        r"\^\{?T\}?"
        r"(?=\s*(?:[A-Za-z(\[]|\\(?!(?:" + NOT_A_PRODUCT + r")\b)[A-Za-z]+))")
    # Explicit alternation, not ``\{?...\}?``: with an optional brace the engine
    # backtracks, lets the brace go unconsumed, and the lookahead then sees ``}``
    # instead of ``(`` — so ``u^{\prime}(c)`` defeated the guard while ``u^\prime(c)``
    # obeyed it.
    # ``^\prime`` carried no guard, so every ``u^\prime(c)`` derivative counted as a
    # transpose. But the guard can only apply to a *function-like* base: in this corpus
    # a primed lowercase letter followed by an argument is a derivative, while
    # ``C C^\prime (A^o)^\tau``, ``\mu^\prime_{t+1}`` and ``[0,1,0,0]^\prime`` are
    # transposes that happen to be followed by a factor. So the base decides.
    #
    # The brace is spelled out rather than written ``\{?...\}?``: with an optional brace
    # the engine backtracks, leaves it unconsumed, and the lookahead sees ``}`` instead
    # of ``(`` — which let ``u^{\prime}(c)`` through while ``u^\prime(c)`` was caught.
    PRIME_SUP = r"\^(?:\{\s*\\prime\s*\}|\\prime)"
    lprime = re.compile(
        # A command, a capital, or a closing delimiter: a transpose either way.
        r"(?:\\[A-Za-z]+|[A-Z]|\)|\}|\])(?:_\{[^}]*\}|_[A-Za-z0-9])?"
        + PRIME_SUP
        + r"|"
        # A plain lowercase name: a following argument makes it a derivative.
        + r"(?<![A-Za-z0-9\\])[a-z](?:_\{[^}]*\}|_[A-Za-z0-9])?"
        + PRIME_SUP
        + r"(?!\s*(?:\(|\\left\s*\())")
    # ``\prime`` spelled as a bare apostrophe *inside* the superscript group: ``C^{'}``,
    # ``U_a^{'}``, ``(A^{o'})``. No branch above reaches these — the character before the
    # ``'`` is ``{`` or a bare superscript letter, and DECORATED covers only \hat/\bar
    # commands. Unguarded the shape is 86 % false here (``A^{'}`` is an event complement in
    # util_rand_resp, ``P^{n'}`` indexes a second agent), so it carries the same guards the
    # other branches use: juxtaposition with a following factor, and for a lowercase base a
    # following ``(`` is an argument. ``^{''}`` never matches, so second derivatives stay out.
    SUP_PRIME = r"\^\{[A-Za-z0-9]{0,2}'\}"
    SUB = r"(?:_\{[^{}]*\}|_[A-Za-z0-9])?"
    FACTOR = r"(?=\s*(?:[A-Za-z(\[]|\\(?!(?:" + NOT_A_PRODUCT + r")\b)[A-Za-z]+))"
    FACTOR_NOARG = r"(?=\s*(?:[A-Za-z\[]|\\(?!(?:" + NOT_A_PRODUCT + r")\b)[A-Za-z]+))"
    sup_prime = re.compile(
        r"(?:\\[A-Za-z]+|(?<![A-Za-z0-9\\])[A-Z]|\)|\}|\])" + SUB + SUP_PRIME + FACTOR
        + r"|"
        + r"(?<![A-Za-z0-9\\])[a-z]" + SUB + SUP_PRIME + FACTOR_NOARG
        + r"|"
        + r"(?:\\[A-Za-z]+|(?<![A-Za-z0-9\\])[A-Z])" + SUB + SUP_PRIME + r"(?=\)\s*\^)")
    # A bare apostrophe is ambiguous in this corpus: a transpose in the LQ lectures, a
    # *next-period state* in the dynamic-programming ones — ``arellano`` says so outright
    # at line 147, "a prime denotes a next period value". Three forms cannot be anything
    # but a transpose:
    #   * a prime on a closing delimiter — ``(A+B)'``, ``\end{bmatrix}'``, ``[0,1]'``;
    #   * a prime juxtaposed with the factor that follows it — ``x_t' R x_t``;
    #   * a prime on the repeat of the symbol before it — ``CC'``, ``U_t U_t'``.
    # A lecture writing any of them uses the apostrophe as a transpose, so the rest of its
    # apostrophes count too. A lecture writing none of them uses it for a continuation
    # state, and none of its apostrophes are transposes. The patterns themselves are not
    # narrowed; only the two bare-apostrophe branches are gated.
    # ``^\prime`` carries the same ambiguity as the bare apostrophe — ``\pi^{\prime}`` is
    # next period's belief in ``navy_captain``, whose line 633 defines it as the posterior
    # after one more draw — so it is gated on the same evidence, and can also supply it.
    spans = list(_math_spans(doc))
    declared = bool(PRIME_NOT_TRANSPOSE.search(
        "\n".join(l.raw for l in doc.lines if l.kind == "text")))
    evident = not declared and any(
        DELIM_PRIME.search(src) or REPEATED_PRIME.search(src)
        or any(FOLLOWING_FACTOR.match(src, m.end())
               for m in list(prime.finditer(src)) + list(lprime.finditer(src)))
        for _, src in spans)
    for no, src in spans:
        if evident:
            for m in prime.finditer(src):
                hits.append(Hit("qe-math-002", no, f"apostrophe transpose `{m.group(0)}`"))
            for m in prime_vec.finditer(src):
                hits.append(Hit("qe-math-002", no, f"apostrophe transpose `{m.group(0)}`"))
            deriv = {m.start(1) for m in fn_paren.finditer(src)}
            for m in prime_paren.finditer(src):
                if m.start() in deriv:
                    continue
                hits.append(Hit("qe-math-002", no, f"apostrophe transpose `{m.group(0)}`"))
            for m in lprime.finditer(src):
                hits.append(Hit("qe-math-002", no, r"\prime transpose"))
        for m in supT.finditer(src):
            hits.append(Hit("qe-math-002", no, f"`^T` transpose in `{m.group(0)}`"))
        for m in sup_prime.finditer(src):
            hits.append(Hit("qe-math-002", no, f"apostrophe transpose `{m.group(0)}`"))
    return hits


def check_math_003(doc: Doc):
    """Matrices must use ``bmatrix``, not pmatrix/vmatrix/Bmatrix/array."""
    hits = []
    envs = re.compile(r"\\begin\{(pmatrix|vmatrix|Vmatrix|Bmatrix|matrix|smallmatrix)\}")
    arr = re.compile(r"\\begin\{array\}")
    # ``\left\{ \begin{array}{ll} ... \right.`` is a case distinction, not a matrix.
    cases = re.compile(r"\\left\\?\{\s*\\begin\{array\}")
    for no, src in _math_spans(doc):
        for m in envs.finditer(src):
            hits.append(Hit("qe-math-003", no, f"{m.group(1)} environment"))
        case_starts = {m.end() - len("\\begin{array}") for m in cases.finditer(src)}
        for m in arr.finditer(src):
            if m.start() in case_starts:
                continue
            hits.append(Hit("qe-math-003", no, "array used as matrix"))
    return hits


def check_math_004(doc: Doc):
    """No bold face for matrices or vectors."""
    hits = []
    pat = re.compile(r"\\(mathbf|boldsymbol|bm|pmb)\b|\{\s*\\bf\b")
    # A bold one applied to a condition or a set is an indicator function, which
    # the rule does not cover; a standalone bold one is a vector of ones.
    # The brace may sit on the next source line (``\mathbf{1}`` then
    # ``\left\{ … \right\}``), so each span is matched against itself plus the
    # following one.
    indicator = re.compile(r"(?:\\(?:mathbf|bm|boldsymbol)\s*\{?1\}?|\{\s*\\bf\s*1\s*\})"
                           r"\s*(?:\\left)?\s*(?:\\?\{|_)")
    spans = list(_math_spans(doc))
    for i, (no, src) in enumerate(spans):
        nxt = spans[i + 1][1] if i + 1 < len(spans) else ""
        skip = {m.start() for m in indicator.finditer(src + " " + nxt)}
        for m in pat.finditer(src):
            if m.start() in skip:
                continue
            hits.append(Hit("qe-math-004", no, m.group(0).strip()))
    return hits


def check_math_005(doc: Doc):
    """Sequences use curly brackets — not square brackets or parentheses."""
    hits = []
    # Require an explicit index range so matrix-by-elements notation
    # (``[f_{ij}]_{i \in ...}``) is not mistaken for a sequence.
    square = re.compile(r"\[\s*\\?[A-Za-z][A-Za-z0-9]*_\{?[a-z]\}?\s*\]\s*"
                        r"_\{?[a-z]\s*(?:=|\\geq|\\ge|\\in)")
    paren = re.compile(r"(?<![A-Za-z0-9\\])\(\s*\\?[A-Za-z][A-Za-z0-9]*_\{?[a-z]\}?\s*\)\s*"
                       r"_\{?[a-z]\s*(?:=|\\geq|\\ge|\\in)")
    prose = doc.narrative_text().lower()
    for no, src in _math_spans(doc):
        if "matrix" in src.lower():
            continue
        for _ in square.finditer(src):
            hits.append(Hit("qe-math-005", no, "square-bracket sequence"))
        for _ in paren.finditer(src):
            hits.append(Hit("qe-math-005", no, "parenthesised sequence"))
    return hits


# Only the multi-line alignment environments — the ones this rule is about. A bare
# ``\begin{equation}`` is a different (and much smaller) convention question.
BARE_DISPLAY_ENVS = {"align", "align*", "alignat", "alignat*", "gather", "gather*",
                     "multline", "multline*", "flalign", "flalign*", "eqnarray",
                     "eqnarray*"}


def check_math_006(doc: Doc):
    """``align`` inside ``$$`` breaks the PDF build; use ``aligned``.

    Two distinct shapes are reported, with different wording so the audit can
    separate them: a multi-line environment nested inside ``$$`` (a build risk),
    and a bare top-level amsmath block, which is not nested but goes against the
    corpus convention of ``$$ … \\begin{aligned} … $$``.
    """
    hits = []
    pat = re.compile(r"\\begin\{(align|alignat|gather|multline|flalign)(\*?)\}")
    for start, end, delim, body in doc.math_blocks:
        if delim == "$$":
            for m in pat.finditer(body):
                hits.append(Hit("qe-math-006", start,
                                f"\\begin{{{m.group(1)}{m.group(2)}}} inside $$ "
                                f"(build risk)"))
        elif delim in BARE_DISPLAY_ENVS:
            hits.append(Hit("qe-math-006", start,
                            f"bare \\begin{{{delim}}} display block; the corpus "
                            f"convention is $$ … \\begin{{aligned}} … $$"))
    return hits


def check_math_007(doc: Doc):
    """No manual ``\\tag`` numbering."""
    hits = []
    pat = re.compile(r"\\tag\*?\{|\\eqno|\\label\{")
    for no, src in _math_spans(doc):
        for m in pat.finditer(src):
            hits.append(Hit("qe-math-007", no,
                            f"{m.group(0)} — use $$ … $$ (label) numbering"))
    return hits


def check_math_008(doc: Doc):
    """A ones vector must be explained where it is introduced.

    ``\\mathbb{1}\\{X_t = x\\}`` is an indicator function, not a ones vector, so an
    argument immediately after the symbol takes the occurrence out of scope.
    """
    hits = []
    ones = re.compile(r"\\(?:mathbb|mathbf|bm|boldsymbol)\s*\{?\s*1\s*\}?"
                      r"|\{\s*\\bf\s*1\s*\}")
    indicator = re.compile(r"^\s*(?:\\left)?\s*(?:\\?\{|\[|\(|_\s*\{?[A-Za-z\\])")
    uses = []
    for no, src in _math_spans(doc):
        for m in ones.finditer(src):
            if indicator.match(src[m.end():]):
                continue
            uses.append((no, m.group(0).strip()))
    if not uses:
        return hits
    prose = doc.narrative_text().lower()
    if re.search(r"(vector|matrix)\s+of\s+ones|ones\s+vector|vector\s+of\s+1"
                 r"|column\s+vector\s+of\s+ones", prose):
        return hits
    hits.append(Hit("qe-math-008", uses[0][0],
                    f"ones vector `{uses[0][1]}` used {len(uses)}x with no "
                    f"'vector of ones' explanation in the prose"))
    return hits


def check_math_010(doc: Doc):
    """(proposed) Blackboard P/E/V with braces for probability, expectation, variance."""
    hits = []
    # (a) The right symbol, missing its braces.
    # Not ``[PEV]\b``: ``_`` is a word character, so ``\b`` never fires before a
    # subscript and ``\mathbb E_t`` — the corpus's usual conditional expectation —
    # went uncounted. ``(?![A-Za-z])`` still rejects ``\mathbb Exp``.
    bare_mathbb = re.compile(r"\\(?:mathbb|Bbb)\s+[PEV](?![A-Za-z])")
    # (b) A plain letter used as the operator: E[X], E_t(...), P(A).
    #     Only counted where the letter is actually applied to something.
    applied = r"(?:\s*(?:_\{[^}]*\}|_[A-Za-z0-9])?\s*(?:\\left)?\s*(?:\[|\\\{|\())"
    bare_E = re.compile(r"(?<![\\A-Za-z0-9_{])E" + applied)
    # (c) Roman or calligraphic spellings of the same operators.
    ROMAN = r"(?:Var|Cov|Pr|Prob|E|Cor)"
    other = re.compile(r"\\(Pr|Var|Cov|Prob)\b"
                       r"|\\(?:text|textrm|mathrm|operatorname)\s*\{\s*" + ROMAN + r"\s*\}"
                       r"|\{\s*\\rm\s+" + ROMAN + r"\s*\}"
                       r"|\\mathcal\s*\{\s*[EPV]\s*\}")
    spans = list(_math_spans(doc))
    # The bare-letter branch only makes sense in a lecture that really does use E as
    # an operator; otherwise E is far more likely to be a matrix or a variable.
    corpus = " ".join(src for _, src in spans)
    e_is_operator = bool(re.search(r"(?<![\\A-Za-z0-9_{])E\s*(?:_\{[^}]*\}|_[A-Za-z0-9])?"
                                   r"\s*(?:\\left)?\s*(?:\[|\\\{)", corpus))
    for no, src in spans:
        masked = src
        for m in bare_mathbb.finditer(src):
            hits.append(Hit("qe-math-010", no, f"missing braces: `{m.group(0).strip()}`"))
        masked = bare_mathbb.sub(lambda m: " " * len(m.group(0)), masked)
        for m in other.finditer(masked):
            hits.append(Hit("qe-math-010", no, f"non-blackboard `{m.group(0).strip()}`"))
        masked = other.sub(lambda m: " " * len(m.group(0)), masked)
        if e_is_operator:
            for m in bare_E.finditer(masked):
                hits.append(Hit("qe-math-010", no,
                                f"bare expectation `{m.group(0).strip()}`"))
    return hits


# A distribution name is being named when it follows ``\sim`` or is applied to a
# parameter list. ``\mathcal{G}`` elsewhere is a sigma-algebra or a generic set.
DIST_AFTER = re.compile(r"^\s*(?:\\left)?\s*[(\[]")
DIST_BEFORE = re.compile(r"\\(?:sim|thicksim|overset\{[^}]*\}\{\\sim\})\s*"
                         r"(?:\\text\{[^}]*\}\s*)?$")


def check_math_011(doc: Doc):
    """(proposed) Distribution names: plain letters, never \mathcal / \mathbb."""
    hits = []
    pat = re.compile(r"\\mathcal\s*\{\s*(N|U)\s*\}|\{\s*\\cal\s*(N|U)\s*\}"
                     r"|\{\s*\\mathcal\s+(N|U)\s*\}"
                     r"|\\mathbb\s*\{\s*(N|U)\s*\}|\\mathcal\s+(N|U)\b")
    for no, src in _math_spans(doc):
        for m in pat.finditer(src):
            before, after = src[:m.start()], src[m.end():]
            if not (DIST_BEFORE.search(before) or DIST_AFTER.match(after)):
                continue        # not being used as a distribution name here
            hits.append(Hit("qe-math-011", no,
                            f"decorated distribution `{m.group(0).strip()}`"))
    return hits


def check_math_012(doc: Doc):
    """(proposed) Multiplication uses \cdot or juxtaposition, never ``*``."""
    hits = []
    # A convolution is conventionally written with a star, so exempt lectures that
    # say so rather than flagging their notation.
    if re.search(r"convolution", doc.narrative_text(), re.IGNORECASE):
        return hits
    for no, src in _math_spans(doc):
        s = re.sub(r"\\(?:begin|end)\{[A-Za-z]+\*\}", " ", src)
        s = re.sub(r"\\operatorname\s*\*", " ", s)
        s = re.sub(r"\\(?:argmin|argmax|sup|inf|max|min|lim)\s*\*", " ", s)
        s = re.sub(r"\^\s*\{[^}]*\*[^}]*\}", " ", s)
        s = re.sub(r"\^\s*\*", " ", s)
        s = re.sub(r"_\s*\{[^}]*\*[^}]*\}", " ", s)
        s = re.sub(r"_\s*\*", " ", s)
        s = re.sub(r"\\ast", " ", s)
        for m in re.finditer(r"(?<!\\)\*", s):
            # Require an operand on both sides: a lone ``$*$`` is naming the symbol.
            left, right = s[:m.start()].strip(), s[m.end():].strip()
            if not left or not right:
                continue
            if not re.search(r"[A-Za-z0-9)\}\]]$", left):
                continue
            if not re.match(r"[A-Za-z0-9(\\{\[]", right):
                continue
            hits.append(Hit("qe-math-012", no, "* as multiplication"))
    return hits


def check_math_013(doc: Doc):
    """(proposed) Reference equations with {eq}`label`, not "equation (3)"."""
    hits = []
    pat = re.compile(r"\b(?:equations?|eqs?\.|formulas?)\s*\(\d+\)|"
                     r"\bsee\s+\(\d+\)|\bin\s+\(\d+\)\s+above", re.IGNORECASE)
    broken = re.compile(r"\{eq\}`[^`]*\}|\{eq\}`[^`\n]*(?<!`)$")
    # "equation (44) of {cite}`BEGS1`" points into someone else's paper, where a
    # numeric reference is the only thing that can be cited.
    external = re.compile(r"\{cite(?::[a-z]+)?\}|\\cite|\bof\s+(?:the\s+)?"
                          r"(?:paper|book|article|text)\b|\bin\s+the\s+paper\b"
                          r"|\btheir\s+notation\b", re.IGNORECASE)
    for l in doc.lines:
        if l.kind != "text":
            continue
        s = doc.masked.get(l.no, l.raw)
        if external.search(l.raw):
            continue
        for m in pat.finditer(s):
            hits.append(Hit("qe-math-013", l.no, f"manual reference {m.group(0)!a}"))
        for m in broken.finditer(l.raw):
            hits.append(Hit("qe-math-013", l.no, f"malformed {{eq}} reference `{m.group(0)[:40]}`"))
    return hits


# ---------------------------------------------------------------------------
# Code
# ---------------------------------------------------------------------------

GREEK_WORDS = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta",
               "theta", "iota", "kappa", "mu", "nu", "xi", "rho", "sigma",
               "tau", "upsilon", "phi", "chi", "psi", "omega",
               # capitalised forms name matrices and should also be unicode
               "Gamma", "Delta", "Theta", "Lambda", "Xi", "Sigma", "Upsilon",
               "Phi", "Psi", "Omega"]
GREEK_RE = re.compile(r"(?<![\w.])(" + "|".join(GREEK_WORDS) + r")(?![\w])")

# ``alpha=`` in a drawing call is matplotlib's opacity, not a model parameter.
STYLE_KWARG = re.compile(
    r"\b(?:color|facecolor|edgecolor|lw|linewidth|ls|linestyle|label|marker|"
    r"markersize|cmap|zorder|hatch|antialiased|capsize|elinewidth|va|ha)\s*=")

ANACONDA = {
    "numpy", "np", "scipy", "pandas", "pd", "matplotlib", "mpl", "sympy",
    "statsmodels", "sklearn", "seaborn", "numba", "math", "random", "time",
    "itertools", "functools", "collections", "os", "sys", "re", "json", "csv",
    "datetime", "typing", "dataclasses", "warnings", "copy", "pickle",
    "urllib", "requests", "pathlib", "abc", "operator", "string", "textwrap",
    "networkx", "nx", "numexpr", "cython", "PIL", "IPython", "tqdm", "bs4",
    "sqlite3", "subprocess", "io", "gc", "inspect", "enum", "fractions",
    "decimal", "statistics", "heapq", "bisect", "array", "struct", "hashlib",
    "unittest", "pprint", "contextlib", "importlib", "traceback", "shutil",
    "glob", "tempfile", "zipfile", "tarfile", "threading", "multiprocessing",
    "concurrent", "asyncio", "queue", "logging", "argparse", "configparser",
    "platform", "getpass", "uuid", "secrets", "base64", "binascii", "codecs",
    "locale", "gettext", "calendar", "zoneinfo", "__future__",
    "mpl_toolkits", "pylab", "cmath", "cProfile", "timeit", "doctest",
}
BINARY_PKGS = {"graphviz", "pygraphviz", "pydot"}
PY_LANGS = {"", "python", "python3", "ipython", "ipython3", "py"}


def _code_cells(doc: Doc):
    """Group consecutive code lines into cells: (first_line, [lines])."""
    cells, cur, start = [], [], None
    for l in doc.lines:
        if l.kind == "code":
            if start is None:
                start = l.no
            cur.append(l.raw)
        else:
            if cur:
                cells.append((start, cur))
            cur, start = [], None
    if cur:
        cells.append((start, cur))
    return cells


def _python_blocks(doc: Doc, include_skipped: bool = False):
    """Directive blocks whose body is Python: (start_line, options, body_text).

    A ``{code-block} java`` sample is not this lecture's Python, and treating it as
    such made ``qe-code-003`` report ``java`` as an uninstalled dependency.

    Non-executing cells are dropped by default: their *imports* are not dependencies.
    But the two spellings mean different things, and only one of them is ever the
    lecture's own install cell:

    * ``:tags: [skip-execution]`` on a ``{code-cell}`` means "this is my install, the
      build image already has the package" — ``!pip install jax`` in the GPU lectures.
      ``include_skipped`` brings these back, because otherwise the very cell
      ``qe-code-003`` is asking about is invisible to it.
    * ``:class: no-execute`` on a ``{code-block}`` means "example code for the reader".
      ``getting_started`` shows the reader how to install QuantEcon.py that way, and
      counting it as this lecture's install cell reports it as "not near the top" —
      which is the false positive the first version of this fix introduced.
    """
    out = []
    for start, end, name, arg, opts, body in doc.blocks:
        if name not in ("code-cell", "code", "code-block", "sourcecode"):
            continue
        info = (arg or "").strip()
        lang = info.split()[0].lower() if info else ""
        if lang not in PY_LANGS:
            continue
        if "no-execute" in str(opts.get("class", "")):
            continue        # example code for the reader, never a dependency
        if not include_skipped and "skip-execution" in opts.get("__raw__", ""):
            continue        # not executed here, so not a dependency of this lecture
        out.append((start, opts, "\n".join(body)))
    return out


def _strip_py(src: str) -> str:
    """Drop comments and string literals so identifier checks stay on identifiers.

    Line structure is preserved — a docstring is replaced by the same number of
    newlines, not by a space. Collapsing it would pull indented code up to column
    zero, which made an indented ``plt.show()`` look top-level.
    """
    def blank(m):
        return "\n" * m.group(0).count("\n")

    src = re.sub(r'"""(?:.|\n)*?"""', blank, src)
    src = re.sub(r"'''(?:.|\n)*?'''", blank, src)
    src = re.sub(r'"[^"\n]*"', " ", src)
    src = re.sub(r"'[^'\n]*'", " ", src)
    src = re.sub(r"#[^\n]*", " ", src)
    return src


def _enclosing_callee(s: str, pos: int) -> str:
    """The name whose argument list contains *pos*, or "" if pos is not in a call."""
    depth = 0
    for i in range(pos - 1, -1, -1):
        c = s[i]
        if c == ")":
            depth += 1
        elif c == "(":
            if depth == 0:
                m = re.search(r"([A-Za-z_][\w.]*)\s*$", s[:i])
                return m.group(1) if m else ""
            depth -= 1
    return ""


def check_code_002(doc: Doc):
    """Unicode Greek letters in code, not spelled-out names."""
    hits = []
    # ``alpha=`` is matplotlib's opacity wherever a cell draws, and the kwarg is
    # often on a continuation line, so the judgement is made per cell.
    drawing_lines = set()
    for start, lines in _code_cells(doc):
        if PLOT_CALL.search(_strip_py("\n".join(lines))):
            drawing_lines.update(range(start, start + len(lines)))
    # A name the lecture *imports* is not a variable it chose to spell out — ``from math
    # import gamma`` binds the gamma function, and renaming it to ``γ`` breaks the import
    # and means something else. Six lectures were flagged for exactly this. Collecting the
    # bound names cannot cause a false negative: a spelled-out Greek *variable* is never
    # also an imported name.
    imported = set()
    for l in doc.lines:
        if l.kind != "code":
            continue
        for m in re.finditer(r"^\s*(?:from\s+[\w.]+\s+)?import\s+(.+)$", l.raw):
            for part in m.group(1).split(","):
                toks = part.strip().split()
                if not toks:
                    continue
                imported.add(toks[0].rsplit(".", 1)[-1])
                if len(toks) == 3 and toks[1] == "as":      # ``import quantecon as qe``
                    imported.add(toks[2])
    # ``_strip_py`` must see a whole cell: the docstring regexes are multi-line, so an
    # *interior* line of a triple-quoted string carries no quote characters and stripping
    # it alone masks nothing. All 11 hits in ``von_neumann_model`` were English words in
    # numpydoc prose, in a lecture whose code already uses ``α``/``β``/``γ``.
    # ``check_code_003`` already strips per cell; this now matches it. ``_strip_py``
    # preserves line structure, so the stripped body lines up with the raw one.
    masked_code = {}
    for start, lines in _code_cells(doc):
        for off, ml in enumerate(_strip_py("\n".join(lines)).split("\n")):
            masked_code[start + off] = ml
    for l in doc.lines:
        if l.kind != "code":
            continue
        s = masked_code.get(l.no, _strip_py(l.raw))
        drawing = l.no in drawing_lines or bool(STYLE_KWARG.search(s))
        for m in GREEK_RE.finditer(s):
            word = m.group(1)
            if word == "alpha" and drawing and re.match(r"\s*=", s[m.end():]):
                continue
            # ...unless this line *assigns* it, in which case the lecture has shadowed the
            # import with a variable of its own and the rule does apply:
            # ``likelihood_ratio_process.md:541`` writes ``beta = np.array(...)`` for a
            # type-II error probability, the one such site in the corpus.
            assigned = bool(re.match(r"\s*=(?!=)", s[m.end():]))
            # A keyword argument names a parameter of somebody else's callable, which the
            # author cannot rename: ``qe.LQ(Q, R, A, B, C, beta=β, T=T)`` in ``lqcontrol``
            # already uses ``β`` for its own variable and passes it to LQ's ``beta=``.
            # Exempt only when the callee is imported — a lecture's own
            # ``def f(alpha=0.5)`` is still its own naming choice, and so is counted.
            if assigned:
                callee = _enclosing_callee(s, m.start())
                if callee and (callee in imported
                               or callee.split(".")[0] in imported):
                    continue
            # An imported name used as a value is the library object, not a variable the
            # lecture chose to spell out — unless a statement-level assignment shadows it,
            # as ``likelihood_ratio_process.md:541`` does with ``beta = np.array(...)``.
            if word in imported and not (
                    assigned and re.fullmatch(r"\s*", s[:m.start()])):
                continue
            hits.append(Hit("qe-code-002", l.no, f"spelled-out `{word}`"))
    return hits


def check_code_003(doc: Doc):
    """Non-Anaconda packages installed near the top, with hide-output."""
    hits = []
    blocks = _python_blocks(doc)
    # Modules the lecture writes itself are not installable packages.
    local = set()
    for _, _, body in blocks:
        for m in re.finditer(r"%%(?:writefile|file)\s+(\S+)", body):
            name = m.group(1).rsplit("/", 1)[-1]
            local.add(name[:-3] if name.endswith(".py") else name)

    imported = set()
    for _, _, body in blocks:
        for m in re.finditer(
            r"^[ \t]*(?:import|from)[ \t]+([A-Za-z_][\w.]*)"
            r"(?=[ \t]*(?:$|[,;]|as[ \t]|import[ \t]))",
            _strip_py(body), re.M,
        ):
            imported.add(m.group(1).split(".")[0])
    extra = {i for i in imported if i not in ANACONDA and i not in local}

    installs = []          # (line, packages, options)
    for start, opts, body in _python_blocks(doc, include_skipped=True):
        for m in re.finditer(r"!\s*(?:pip|conda)\s+install\s+([^\n]*)", body):
            pkgs = {w for w in re.split(r"\s+", m.group(1))
                    if w and not w.startswith("-")}
            installs.append((start, pkgs, opts))

    installed = set().union(*(p for _, p, _ in installs)) if installs else set()
    missing = {e for e in extra
               if not any(e.lower() in p.lower() for p in installed)}
    if missing:
        hits.append(Hit("qe-code-003", installs[0][0] if installs else 1,
                        f"non-Anaconda import with no install cell: "
                        f"{sorted(missing)[:5]}"))
    # "Near the top" = within the first fifth of the file, or the first 80 lines.
    limit = max(80, int(doc.n_lines * 0.2))
    for line, pkgs, opts in installs:
        if line > limit:
            hits.append(Hit("qe-code-003", line,
                            f"install cell at line {line} of {doc.n_lines} "
                            f"(not near the top)"))
        tags = str(opts.get("tags", "")) + opts.get("__raw__", "")
        # A cell tagged ``skip-execution`` never runs, so it has no output to hide and
        # ``hide-output`` would be noise. Asking for it there is the false positive the
        # first version of this fix introduced.
        if "hide-output" not in tags and "skip-execution" not in tags \
                and "no-execute" not in tags:
            hits.append(Hit("qe-code-003", line,
                            "install cell missing the hide-output tag"))
    return hits


def check_code_004(doc: Doc):
    """Use qe.Timer instead of manual timing."""
    hits = []
    code = doc.code_text()
    bare_time = bool(re.search(r"from\s+time\s+import\s+[^\n]*\btime\b", code))
    pat = re.compile(
        r"time\.(?:time|perf_counter|process_time|monotonic)\s*\("
        r"|timeit\.default_timer\s*\("
        r"|\bqe\.(?:tic|toc)\b"
        r"|(?<![\w.])(?:tic|toc|tac)\s*\(\s*\)"
        r"|^\s*%{1,2}time\b(?!it)")
    for l in doc.lines:
        if l.kind != "code":
            continue
        s = _strip_py(l.raw)
        for m in pat.finditer(s):
            hits.append(Hit("qe-code-004", l.no, m.group(0).strip()))
        if bare_time:
            for _ in re.finditer(r"(?<![\w.])time\s*\(\s*\)", s):
                hits.append(Hit("qe-code-004", l.no, "bare time() reading"))
    return hits


def check_code_005(doc: Doc):
    """Use qe.timeit instead of %timeit or a hand-rolled benchmark loop."""
    hits = []
    for l in doc.lines:
        if l.kind != "code":
            continue
        for m in re.finditer(r"^\s*%{1,2}timeit\b", l.raw):
            hits.append(Hit("qe-code-005", l.no, m.group(0).strip()))
    # A timing read inside a loop that accumulates or averages is a benchmark.
    code = doc.code_text()
    bare_time = bool(re.search(r"from\s+time\s+import\s+[^\n]*\btime\b", code))
    read = (r"time\.(?:time|perf_counter|monotonic)\s*\(|timeit\.default_timer\s*\("
            + (r"|(?<![\w.])time\s*\(\s*\)" if bare_time else ""))
    for start, lines in _code_cells(doc):
        body = _strip_py("\n".join(lines))
        if not re.search(r"^\s*(?:for|while)\b", body, re.M):
            continue
        if not re.search(read, body):
            continue
        accumulates = re.search(
            r"\w*(?:time|times|elapsed|secs|seconds)\w*\s*\.append\s*\(", body)
        averages = re.search(r"/\s*(?:len\s*\(|\d+\s*$)", body, re.M)
        if accumulates or averages:
            hits.append(Hit("qe-code-005", start,
                            "hand-rolled benchmark loop — use qe.timeit"))
    return hits


def check_code_006(doc: Doc):
    """Binary packages need an installation warning admonition."""
    hits = []
    code = " ".join(_strip_py(b) for _, _, b in _python_blocks(doc)).lower()
    used = {p for p in BINARY_PKGS if re.search(rf"(?<![\w.]){p}\b", code)}
    if not used:
        return hits
    has_warning = False
    for start, end, name, arg, opts, body in doc.blocks:
        if name not in ("admonition", "warning"):
            continue
        text = ((arg or "") + " " + "\n".join(body)).lower()
        if any(p in text for p in used):
            has_warning = True
    if not has_warning:
        hits.append(Hit("qe-code-006", 1,
                        f"binary package {sorted(used)} with no warning admonition"))
    return hits


def check_fig_001(doc: Doc):
    """Do not set figure size unless necessary."""
    hits = []
    for l in doc.lines:
        if l.kind != "code":
            continue
        for _ in re.finditer(r"\bfigsize\s*=", l.raw):
            hits.append(Hit("qe-fig-001", l.no, "figsize="))
        # Only a write counts. ``plt.rcParams['axes.prop_cycle']`` is a read, and
        # ``style.use('default')`` restores the default rather than overriding it.
        for m in re.finditer(
            r"rcParams\s*\[[^\]]*\]\s*=|rcParams\.update\s*\("
            r"|\b(?:plt|mpl|matplotlib)\.rc\s*\("
            r"|\b(?:sns|seaborn)\.set(?:_style|_theme|_context)?\s*\("
            r"|plt\.style\.use\s*\(\s*(?![\"']?(?:default|classic))", l.raw):
            hits.append(Hit("qe-fig-001", l.no, "style override"))
    return hits


# Asset families that are screenshots, photographs or diagrams rather than plots.
# ``qe-fig-002`` asks for code-generated *figures*; it does not ask a lecture to
# draw a photograph of a GPU.
NOT_A_PLOT = re.compile(
    r"logo|screenshot|screen[_-]|/getting_started/|/workspace/|/troubleshooting/"
    r"|/need_for_speed/|/parallelization/|/python_by_example/|/about_py/"
    r"|/debugging/|/jupyter|jp_demo|htop|geforce|nvidia|vscode|anaconda"
    r"|qe-menubar|favicon", re.IGNORECASE)


def check_fig_002(doc: Doc):
    """Prefer code-generated figures over static images."""
    hits = []
    img = re.compile(r"\.(?:png|jpg|jpeg|gif|svg|pdf)\b", re.IGNORECASE)
    for l in doc.lines:
        if l.kind not in ("text", "fence", "option"):
            continue
        if NOT_A_PLOT.search(l.raw):
            continue        # a screenshot or photograph, which code cannot generate
        m = img.search(l.raw)
        if m and (re.search(r"\{(?:figure|image)\}", l.raw) or re.search(r"!\[[^\]]*\]\(", l.raw)
                  or l.kind == "fence"):
            hits.append(Hit("qe-fig-002", l.no, f"static image {m.group(0)}"))
    return hits


def check_fig_003(doc: Doc):
    """No embedded matplotlib titles outside exercises/solutions."""
    hits = []
    pat = re.compile(r"\.(?:set_title|suptitle)\s*\(|\bplt\.title\s*\("
                     r"|\.set\(\s*[^)]*\btitle\s*=|\.title\.set_text\s*\(")
    for l in doc.lines:
        if l.kind != "code" or l.in_exercise:
            continue
        for m in pat.finditer(l.raw):
            hits.append(Hit("qe-fig-003", l.no, m.group(0).strip("(")))
    return hits


def check_fig_004(doc: Doc):
    """Figure captions: sentence case, 6 words or fewer."""
    hits = []
    captions = []
    for no, name, arg, opts, marker in doc.directives:
        cap = opts.get("caption") or ""
        if name in ("figure", "image") and cap:
            captions.append((no, cap))
        elif name == "code-cell" and cap and "figure:" in opts.get("__raw__", ""):
            captions.append((no, cap))
    for no, cap in captions:
        if cap.strip() in ("|", ">", "|-", ">-"):
            continue        # a YAML block scalar; the body is not in the options
        # Inline maths is one token however many LaTeX commands it contains, and a
        # hyphenated compound is one word.
        text = re.sub(r"\$[^$]*\$", " x ", cap).replace("\\n", " ")
        words = re.findall(r"[A-Za-z][A-Za-z'’\-–]*", text)
        if len(words) > 6:
            hits.append(Hit("qe-fig-004", no, f"caption of {len(words)} words"))
        offenders = [w for w in words[1:]
                     if re.fullmatch(r"[A-Z][a-z'’]+(?:[-–][A-Za-z][a-z'’]*)*", w)
                     and not _is_proper(w)]
        if offenders:
            hits.append(Hit("qe-fig-004", no,
                            f"Title Case caption ({', '.join(offenders[:3])})"))
    return hits


# A code cell renders a figure if it calls one of these.
PLOT_CALL = re.compile(
    r"\.(?:plot|bar|barh|scatter|hist|hist2d|imshow|contour|contourf|pcolor|"
    r"pcolormesh|stackplot|fill_between|fill_betweenx|step|stem|boxplot|violinplot|"
    r"pie|errorbar|hexbin|matshow|spy|quiver|streamplot|plot_surface|plot_wireframe|"
    r"semilogx|semilogy|loglog|axhline|axvline|axline)\s*\(|"
    r"\bplt\.show\s*\(|\bsns\.\w+\s*\(|\bfig\.show\s*\("
)


def _cell_makes_figure(body) -> bool:
    """Does this cell actually render a figure?

    A cell whose plotting all happens inside a ``def`` renders nothing by itself —
    the figure appears where the helper is called. So the plotting call, or a
    render call, has to sit at column zero.
    """
    src = _strip_py("\n".join(body) if isinstance(body, list) else body)
    if not PLOT_CALL.search(src):
        return False
    for line in src.split("\n"):
        if not line[:1].strip():
            continue            # indented: inside a def, a loop or a with-block
        if PLOT_CALL.search(line):
            return True
    return False


def check_fig_005(doc: Doc):
    """Every figure needs a descriptive name for numref cross-referencing.

    Covers both ``{figure}``/``{image}`` directives and the far more common
    code-cell figures, whose name lives in ``mystnb.figure.name`` metadata.
    """
    hits = []
    for no, name, arg, opts, marker in doc.directives:
        if name not in ("figure", "image"):
            continue
        nm = opts.get("name")
        if not nm:
            hits.append(Hit("qe-fig-005", no, f"{{{name}}} without :name:"))
        elif re.fullmatch(r"fig(?:ure)?[-_:]?\d*", nm.strip(), re.IGNORECASE):
            hits.append(Hit("qe-fig-005", no, f"non-descriptive name `{nm}`"))
    for start, end, name, arg, opts, body in doc.blocks:
        if name != "code-cell" or not _cell_makes_figure(body):
            continue
        raw = opts.get("__raw__", "")
        if "figure:" not in raw:
            hits.append(Hit("qe-fig-005", start,
                            "code-cell figure without mystnb figure metadata"))
        elif not re.search(r"^\s*name:\s*\S", raw, re.M):
            hits.append(Hit("qe-fig-005", start, "mystnb figure without name:"))
        else:
            nm = re.search(r"^\s*name:\s*(\S+)", raw, re.M).group(1)
            if re.fullmatch(r"fig(?:ure)?[-_:]?\d*", nm, re.IGNORECASE):
                hits.append(Hit("qe-fig-005", start, f"non-descriptive name `{nm}`"))
    return hits


def check_fig_006(doc: Doc):
    """Axis labels should be lowercase."""
    hits = []
    pat = re.compile(r"(?:set_(?:x|y|z)label|(?:plt|ax)\.(?:x|y)label)\s*\(\s*"
                     r"(?:[rf]?['\"])([^'\"]{1,60})['\"]")
    for l in doc.lines:
        if l.kind != "code":
            continue
        for m in pat.finditer(l.raw):
            label = m.group(1).strip()
            core = re.sub(r"^\$+|\\[A-Za-z]+", "", label).strip()
            if not core or not core[0].isalpha():
                continue
            if core.isupper():          # GDP, CPI — legitimate acronym
                continue
            if re.match(r"^[A-Z][a-z]", core) and core.split()[0].lower() not in PROPER_NOUNS:
                hits.append(Hit("qe-fig-006", l.no, f"axis label `{label}`"))
    return hits


def check_fig_007(doc: Doc):
    """Keep the figure box — do not remove spines."""
    hits = []
    pat = re.compile(r"spines\s*(?:\[|\.)[^\n]*(?:set_visible\s*\(\s*False|set_color\s*\(\s*['\"]none)|despine\s*\(|set_frame_on\s*\(\s*False")
    for l in doc.lines:
        if l.kind != "code":
            continue
        if re.search(r"spines", l.raw) and not re.search(r"set_visible\s*\(\s*False|despine|"
                                                        r"set_color\s*\(\s*['\"]none", l.raw):
            continue
        for m in pat.finditer(l.raw):
            hits.append(Hit("qe-fig-007", l.no, "spine removal"))
    return hits


def check_fig_008(doc: Doc):
    """Line charts should use lw=2.

    A ``plot(...)`` call often spans several source lines, so the whole argument
    list has to be assembled before deciding whether ``lw=`` is there.
    """
    hits = []
    pat = re.compile(r"\b(?:ax\d?|axes?\[[^\]]*\]|axs?\[[^\]]*\]|plt|ax)\.plot\s*\(")
    code = [l for l in doc.lines if l.kind == "code"]
    by_no = {l.no: i for i, l in enumerate(code)}
    for i, l in enumerate(code):
        for m in pat.finditer(l.raw):
            # Walk forward until the call's parentheses balance.
            depth, args, j, pos = 0, [], i, m.end() - 1
            while j < len(code) and j - i < 12:
                seg = code[j].raw[pos:] if j == i else code[j].raw
                for ch in seg:
                    if ch == "(":
                        depth += 1
                    elif ch == ")":
                        depth -= 1
                        if depth == 0:
                            break
                    args.append(ch)
                if depth == 0:
                    break
                j += 1
                pos = 0
            call = "".join(args)
            if not re.search(r"\b(?:lw|linewidth)\s*=", call):
                hits.append(Hit("qe-fig-008", l.no, "plot() without lw="))
    return hits


def check_fig_009(doc: Doc):
    """Figures should occupy 80–100% of text width.

    Only ``:width:`` expresses a fraction of the text width. ``:scale:`` is
    relative to the image's own pixel size, so a screenshot at ``:scale: 50``
    says nothing about how wide it renders — counting it measured the wrong
    quantity, and every hit in this corpus was a scaled-down screenshot.
    """
    hits = []
    for no, name, arg, opts, marker in doc.directives:
        if name not in ("figure", "image"):
            continue
        val = (opts.get("width") or "").strip()
        m = re.match(r"^(\d+(?:\.\d+)?)\s*%$", val)
        if not m:
            continue        # an absolute width (px, em) is not a share of the page
        pct = float(m.group(1))
        if pct < 80 or pct > 100:
            hits.append(Hit("qe-fig-009", no, f":width: {val} (outside 80–100%)"))
    return hits


def check_fig_011(doc: Doc):
    """Use the image directive, not figure, when nested inside another directive."""
    hits = []
    for no, marker, name, pmarker, pname in doc.nestings:
        if name == "figure" and pname and pname not in ("only", "tab-set", "tab-item"):
            hits.append(Hit("qe-fig-011", no, f"{{figure}} nested inside {{{pname}}}"))
    return hits


def check_fig_010(doc: Doc):
    """Plotly figures need an {only} latex fallback."""
    hits = []
    code = doc.code_text()
    if not re.search(r"\bimport\s+plotly|from\s+plotly|\bgo\.Figure|plotly\.express", code):
        return hits
    has_only = any(name == "only" and "latex" in arg for _, name, arg, _, _ in doc.directives)
    if not has_only:
        hits.append(Hit("qe-fig-010", 1, "plotly used with no {only} latex directive"))
    return hits


# ---------------------------------------------------------------------------
# Links
# ---------------------------------------------------------------------------

def check_link_001(doc: Doc):
    """Same-series references should be relative markdown links, not full URLs."""
    hits = []
    own = SERIES_DOMAIN.get(doc.series, "")
    if not own:
        return hits
    pat = re.compile(r"\]\(\s*(https?://" + re.escape(own) + r"[^)\s]*)\)")
    asset = re.compile(r"/_static/|/_downloads/|\.(?:pdf|zip|py|ipynb|csv|xlsx|png|jpg)$",
                       re.IGNORECASE)
    for l in doc.lines:
        if l.kind not in ("text", "option"):
            continue
        for m in pat.finditer(l.raw):
            if asset.search(m.group(1)):
                continue        # a downloadable asset, not a sibling lecture
            hits.append(Hit("qe-link-001", l.no, f"full URL to own series ({own})"))
    return hits


def check_link_002(doc: Doc):
    """Cross-series references must use {doc} with an intersphinx prefix."""
    hits = []
    own = SERIES_DOMAIN.get(doc.series, "")
    others = [d for d in QE_SERIES_DOMAINS if d != own]
    pat = re.compile(r"\]\(\s*https?://(" + "|".join(re.escape(d) for d in others) + r")[^)]*\)")
    bare = re.compile(r"(?<!\()\bhttps?://(" + "|".join(re.escape(d) for d in others) + r")/\S+")
    for l in doc.lines:
        if l.kind not in ("text", "option"):
            continue
        for m in pat.finditer(l.raw):
            hits.append(Hit("qe-link-002", l.no, f"raw link to {m.group(1)}"))
        for m in bare.finditer(l.raw):
            if "](" in l.raw[:m.start()][-3:]:
                continue
            hits.append(Hit("qe-link-002", l.no, f"bare URL to {m.group(1)}"))
    return hits


# ---------------------------------------------------------------------------
# References
# ---------------------------------------------------------------------------

NARRATIVE_LEAD = re.compile(
    r"(?:\b(?:by|of|in|to|from|following|see|and|with|per|after|via)\s+|^\s*|"
    r"[.!?]\s+)\{cite\}`", re.IGNORECASE)
NARRATIVE_TRAIL = re.compile(
    r"\{cite\}`[^`]+`\s+(?:show|shows|showed|prove|proves|proved|argue|argues|argued|"
    r"introduce|introduced|study|studies|studied|develop|developed|derive|derived|"
    r"note|notes|noted|find|finds|found|consider|considers|considered)\b",
    re.IGNORECASE)


def check_ref_001(doc: Doc):
    """{cite:t} for in-text author citations, {cite} for parenthetical ones."""
    hits = []
    for l in doc.lines:
        if l.kind != "text":
            continue
        s = l.raw
        # One finding per citation site, whichever pattern spotted it.
        flagged = {}
        for m in NARRATIVE_TRAIL.finditer(s):
            flagged[m.start()] = f"{{cite}} in author position: {m.group(0)[:48].rstrip(chr(96))!r}"
        for m in NARRATIVE_LEAD.finditer(s):
            # A parenthetical citation at the end of a clause is correct.
            after = s[m.end():]
            if re.match(r"[^`]*`\s*[.,;:)]", after):
                continue
            # "include {cite}`a` and {cite}`b`." is a list, not an author position;
            # neither is "see {cite}`x`". The cue word can be the lead word the match
            # itself consumed, so the text tested has to include it — ``s[:m.start()]``
            # cut the cue off and this exemption could only ever fire via the
            # ``[.!?]\s+`` alternative.
            lead = s[:m.start()] + m.group(0)[:-len("{cite}`")]
            if re.search(r"\b(?:include|includes|including|see|e\.g\.|cf\.)\s*$",
                         lead, re.IGNORECASE):
                continue
            flagged.setdefault(m.start(),
                               f"{{cite}} in narrative flow: {m.group(0)[:48].rstrip(chr(96))!r}")
        for pos, detail in sorted(flagged.items()):
            hits.append(Hit("qe-ref-001", l.no, detail))
    return hits


def count_citations(doc: Doc):
    text = doc.narrative_text()
    return len(re.findall(r"\{cite\}`", text)), len(re.findall(r"\{cite:t\}`", text))


# ---------------------------------------------------------------------------
# Admonitions
# ---------------------------------------------------------------------------

PROOF_NAMES = {"theorem", "lemma", "proof", "definition", "corollary",
               "proposition", "assumption", "axiom", "remark", "conjecture",
               "criteria", "algorithm", "observation", "property"}


def check_admon_001(doc: Doc):
    """An exercise containing an *executable* cell must use gated syntax.

    A plain ```` ```python ```` block is displayed, not run, so it does not need
    the gated form — every hit before this distinction was drawn was one of those.
    """
    hits = []
    seen = set()
    for l in doc.lines:
        if l.kind != "code" or "code-cell" not in l.directives:
            continue
        if "exercise" in l.directives and "exercise-start" not in l.directives:
            if "exercise" not in seen:
                hits.append(Hit("qe-admon-001", l.no,
                                "executable cell inside a non-gated {exercise}"))
                seen.add("exercise")
        if "solution" in l.directives and "solution-start" not in l.directives:
            if "solution" not in seen:
                hits.append(Hit("qe-admon-001", l.no,
                                "executable cell inside a non-gated {solution}"))
                seen.add("solution")
    return hits


def check_admon_002(doc: Doc):
    """Solutions default to :class: dropdown."""
    hits = []
    for no, name, arg, opts, marker in doc.directives:
        if name in ("solution", "solution-start"):
            if "dropdown" not in str(opts.get("class", "")):
                hits.append(Hit("qe-admon-002", no, f"{{{name}}} without :class: dropdown"))
    return hits


def check_admon_003(doc: Doc):
    """Nested directives need more ticks than their parent. Critical when equal.

    Two distinct faults land here. A gated ``{exercise-start}`` whose fence is
    never closed silently swallows the rest of the exercise; and a directive
    nested inside another with no extra ticks cannot be closed unambiguously.
    """
    hits = []
    for no, name, ticks in doc.unclosed_gated:
        hits.append(Hit("qe-admon-003", no,
                        f"{{{name}}} fence ({ticks} ticks) is never closed — the "
                        f"directive swallows the rest of the block"))
    for no, marker, name, pmarker, pname in doc.nestings:
        if not pname or pname.endswith(("-start", "-end")):
            continue
        if marker[0] == pmarker[0] and len(marker) >= len(pmarker):
            hits.append(Hit("qe-admon-003", no,
                            f"{{{name}}} ({len(marker)} ticks) inside {{{pname}}} "
                            f"({len(pmarker)} ticks)"))
    return hits


def check_admon_004(doc: Doc):
    """Proof-family directives require the prf: prefix."""
    hits = []
    for no, name, arg, opts, marker in doc.directives:
        if name in PROOF_NAMES:
            hits.append(Hit("qe-admon-004", no, f"{{{name}}} missing prf: prefix"))
    for l in doc.lines:
        if l.kind != "text":
            continue
        for m in re.finditer(r"\{(theorem|lemma|proof|definition|corollary|proposition)\}`", l.raw):
            hits.append(Hit("qe-admon-004", l.no, f"{{{m.group(1)}}} role missing prf:"))
    return hits


def check_admon_005(doc: Doc):
    """Solutions must name the exercise they solve."""
    hits = []
    ex_labels = set()
    for no, name, arg, opts, marker in doc.directives:
        if name in ("exercise", "exercise-start"):
            lab = opts.get("label") or arg.strip()
            if lab:
                ex_labels.add(lab.strip())
    for no, name, arg, opts, marker in doc.directives:
        if name in ("solution", "solution-start"):
            target = arg.strip()
            if not target:
                hits.append(Hit("qe-admon-005", no, f"{{{name}}} with no exercise label"))
            elif ex_labels and target not in ex_labels:
                hits.append(Hit("qe-admon-005", no, f"solution label {target!r} has no exercise"))
    return hits


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

CHECKS = {
    "qe-writing-001": check_writing_001,
    "qe-writing-004": check_writing_004,
    "qe-writing-006": check_writing_006,
    "qe-writing-008": check_writing_008,
    "qe-writing-009": check_writing_009,
    "qe-math-001": check_math_001,
    "qe-math-002": check_math_002,
    "qe-math-003": check_math_003,
    "qe-math-004": check_math_004,
    "qe-math-005": check_math_005,
    "qe-math-006": check_math_006,
    "qe-math-007": check_math_007,
    "qe-math-008": check_math_008,
    "qe-math-010": check_math_010,
    "qe-math-011": check_math_011,
    "qe-math-012": check_math_012,
    "qe-math-013": check_math_013,
    "qe-code-002": check_code_002,
    "qe-code-003": check_code_003,
    "qe-code-004": check_code_004,
    "qe-code-005": check_code_005,
    "qe-code-006": check_code_006,
    "qe-fig-001": check_fig_001,
    "qe-fig-002": check_fig_002,
    "qe-fig-003": check_fig_003,
    "qe-fig-004": check_fig_004,
    "qe-fig-005": check_fig_005,
    "qe-fig-006": check_fig_006,
    "qe-fig-007": check_fig_007,
    "qe-fig-008": check_fig_008,
    "qe-fig-009": check_fig_009,
    "qe-fig-010": check_fig_010,
    "qe-fig-011": check_fig_011,
    "qe-link-001": check_link_001,
    "qe-link-002": check_link_002,
    "qe-ref-001": check_ref_001,
    "qe-admon-001": check_admon_001,
    "qe-admon-002": check_admon_002,
    "qe-admon-003": check_admon_003,
    "qe-admon-004": check_admon_004,
    "qe-admon-005": check_admon_005,
}

# Which audit category each rule scores under.
CATEGORY = {
    "writing": ["qe-writing-001", "qe-writing-004", "qe-writing-006",
                "qe-writing-008", "qe-writing-009"],
    "math": ["qe-math-001", "qe-math-002", "qe-math-003", "qe-math-004", "qe-math-005",
             "qe-math-006", "qe-math-007", "qe-math-008", "qe-math-010",
             "qe-math-011", "qe-math-012", "qe-math-013"],
    "code": ["qe-code-002", "qe-code-003", "qe-code-004", "qe-code-005", "qe-code-006"],
    "figures": ["qe-fig-001", "qe-fig-002", "qe-fig-003", "qe-fig-004",
                "qe-fig-005", "qe-fig-006", "qe-fig-007", "qe-fig-008",
                "qe-fig-009", "qe-fig-010", "qe-fig-011"],
    "references": ["qe-ref-001"],
    "links": ["qe-link-001", "qe-link-002"],
    "admonitions": ["qe-admon-001", "qe-admon-002", "qe-admon-003",
                    "qe-admon-004", "qe-admon-005"],
}

PROPOSED = {"qe-writing-009", "qe-math-010", "qe-math-011", "qe-math-012",
            "qe-math-013", "qe-math-014", "qe-math-015"}

BUILD_RISK = {"qe-math-006", "qe-admon-003"}

# Titles for the proposed rules, which have no entry in the registry yet.
# Source: lectures/spec.md §3.
PROPOSED_TITLES = {
    "qe-writing-009": 'Write "IID" — not "i.i.d." or "iid"',
    "qe-math-010": r"Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces",
    "qe-math-011": r"Distribution names in plain letters, not \mathcal / \mathbb",
    "qe-math-012": r"Multiplication via \cdot or juxtaposition, never *",
    "qe-math-013": "Reference equations via {eq}`label`",
    "qe-math-014": r"Braces \{…\} for events, parentheses (…) for sets",
    "qe-math-015": "Lowercase for densities/PMFs, uppercase for CDFs",
}


def load_rule_titles(rules_dir: str) -> dict:
    """Read ``qe-*`` titles from the action-style-guide rule files."""
    import glob
    import os
    titles = dict(PROPOSED_TITLES)
    for path in sorted(glob.glob(os.path.join(rules_dir, "*-rules.md"))):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for m in re.finditer(
            r"###\s*Rule:\s*(qe-[a-z]+-\d{3})\s*\n(?:.*?\n)?\*\*Title:\*\*\s*(.+)",
            text,
        ):
            titles[m.group(1)] = m.group(2).strip()
    return titles


def run_all(doc: Doc):
    """Run every check; return {rule: [Hit, ...]} with empty results dropped."""
    out = {}
    for rule, fn in CHECKS.items():
        hits = fn(doc)
        if hits:
            out[rule] = hits
    return out
