# Authentic JEE Advanced phrasing (user's instruction, 18-Oct-2026)

Style: authentic JEE Advanced phrasing. Rigorous, precise, objective academic language. Read this before writing
question 1 and again before the review pass. The build script lints some of it (stock phrases, syllabus words).

## Voice
- Formal, impersonal, third person. No "you", "we", "let's", no chatty or hinting words ("nice", "interesting", "easy").
- Complete sentences. Every symbol is introduced before use ("Let ... be ...", "Consider ...", "Define ...").
- State the domain and codomain of every function (the build **refuses** a stem that introduces a function with no domain): `Let $f:\mathbb{R}\to\mathbb{R}$ be ...`, `Let $f:(0,\infty)\to\mathbb{R}$ ...`.
- State every condition fully and quantify it: "for all $x\in\mathbb{R}$", "for every point $P(x,y)$ on the curve".
- Clarify non-universal notation in the stem: "where $[t]$ denotes the greatest integer less than or equal to $t$",
  "Here $\log_e$ denotes the natural logarithm", "Considering only the principal values of the inverse trigonometric functions".
- Use "such that", "satisfying", "respectively", "attains its minimum value", "the number of distinct real roots",
  "the area of the region bounded by ... and ...", "the point of intersection", "is equal to".
- Do not start a stem with an imperative ("Find", "Calculate", "Compute", "Determine", "Evaluate", "Solve", "Show that",
  "Prove", "What is"). The only imperative allowed is "Match". Questions end with "Then the value of ... is",
  "Then ... is equal to", "the number of ... is", or "Which of the following statements is(are) TRUE?".
- No hint of the method in the stem. Do not reveal the key idea.

## Stock phrases by type
| Type | Stem ending / frame |
|---|---|
| SCQ | "... Then $f(2)$ is equal to" / "... then the value of ... is" / "Then the number of ... is" |
| MCQ | "... Then, which of the following statements is(are) TRUE?" (or "Which of the following statement(s) is(are) correct?"). Each of (A)-(D) is a complete, independent, checkable statement. |
| PARA | The paragraph is set-up only ("Let ... Consider ..."), with no question in it. Each sub-question is a noun phrase: "The minimum value of ... is", "The area of the region ... is". |
| MTC | "Match each entry in List-I to the correct entry in List-II and choose the correct option." List-I (P)-(S) are noun phrases; List-II (1)-(5) are values or phrases. |
| INT | "... Then the value of ... is" (the answer is a non-negative integer; do not mention digits). |
| Numerical | "... Then the value of ... is ______." (the script adds the 2nd-decimal instruction). |

## Model phrasings (original sentences in the JEE Advanced manner; adapt, do not copy)
- Function set-up: "Let $f:\mathbb{R}\to\mathbb{R}$ be a twice differentiable function such that ... for all $x\in\mathbb{R}$."
- Definitions: "For $x\in\mathbb{R}$, let $g(x)=\int_0^x ...$." / "Let $f:(0,\infty)\to\mathbb{R}$ be defined by ..."
- Sets and counts: "Let $S$ denote the set of all real numbers $x$ for which ... Then the number of elements in $S$ is".
- Parameters: "Let $\alpha$ and $\beta$ be real numbers such that ... Then the value of ... is".
- Geometry: "Let $P$ be a point on the parabola ... The tangent at $P$ meets the $x$-axis at $Q$ ... Then the area of triangle $PQF$ is".
- Choosing among statements: "Then, which of the following statements is(are) TRUE?"
- Matching: "Match each entry in List-I to the correct entry in List-II and choose the correct option."
- Paragraph: "Consider ... Let ... denote ..." (set-up only), then "The value of ... is", "The number of ... is".
- Clarifying notation: "Here $\tan^{-1}$ takes values in $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$." / "where $[t]$ denotes the greatest integer less than or equal to $t$".

## Precision
- Every object exists and is unique; the answer is unique (no hidden second root, branch or sign).
- "Region bounded by" needs the curves and lines named; if the region could be read two ways, define it as a set:
  `$\{(x,y): ...\}$`.
- No rounding ambiguity: decimals have at most two decimal places and are exact or clearly rounded to two places.
- No superfluous hypotheses. If a condition is not needed for the answer, remove it.
- MCQ statements: no "all/none of the above", no statements that depend on one another, wrong statements are wrong for a
  typical mistake (sign, missing factor, wrong interval), not arbitrary.

## Naturalness (what made the first test paper unsatisfactory)
- Prefer defining an object by a natural property over an arbitrary condition. Example: define a curve by what its
  tangent does ("the tangent at every point P(x,y) meets the y-axis at (0, 8/x - 5)") rather than by "f attains its minimum at x = 2".
- Avoid contrived normalisers. Multiply or divide only when the raw answer would not fit the type (an integer-type
  answer, a clean decimal), and then in the way JEE does ("16 S/pi").
- A question should read as one situation seen from two angles, not two tasks glued together.
- Parameters are named conventionally: a, b, c, k, lambda, alpha, beta, n; functions f, g, h, F, G; points P, Q, R.
- A level-1 or level-2 question is still phrased with full rigour; short is not casual.

## Before and after
- Before: "Let $C$ be the curve ... Then the area ... is ______." with the area asked for as "$8A$".
  After: a parameter question with a natural answer: "... the area of the region bounded by $C$ and $L_a$ is $\frac{27}{64}$. Then the value of $a$ is ______."
- Before: "Match the items in List-I with the entries in List-II."
  After: "Match each entry in List-I to the correct entry in List-II and choose the correct option."
- Before: "Let $f$ be ... It is given that $f$ attains its minimum value at $x=2$."
  After: a geometric condition on the tangent that determines $f$ without an arbitrary hint.

## Review pass (every question; run `scripts/review_stems.py` and record the result in `stem_review`)
1. Read the English stem aloud as a student would: is any symbol undefined, any condition missing, any word loose?
2. Is the answer unique and independent of how an ambiguous phrase is read?
3. Do the options have one form (all values, or all statements)? Is exactly the planned one correct?
4. Is the Hindi a faithful mirror (same symbols, same numbers, same options)?
5. Syllabus: no hyperbolic functions, no asymptotes.
