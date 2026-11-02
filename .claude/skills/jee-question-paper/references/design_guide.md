# Design guide - turning a concept into a graded set

## Contents
1. From source to blueprint
2. What each tier looks like (with the inverse-derivative set as the worked case)
3. Verification checklist
4. Format rules
5. Solution style
6. Originality

## 1. From source to blueprint

1. **Map the source.** For each source question write: key step, family, format, level on the user's scale. Official JEE Advanced questions are usually in `anchors.md`; use the user's level, not yours. Coaching/Main questions are not anchors: place them relative to the nearest anchor.
2. **List the idea ladder of the concept.** Order the ideas from "one formula" to "needs a non-routine step". Example for *derivative of inverse function*:
   - L1: find x0 by inspection, then 1/f'(x0).
   - L2: second derivative of the inverse, inverse inside a product/tangent line.
   - L3: statement-checking with symmetry and concavity; curve meets its inverse only on y = x; domain restriction choosing a branch.
   - L4: second derivative of f o g^{-1}; third derivative by repeated implicit differentiation; asymptotics of an inverse with no closed form.
3. **Assign slots.** Spread ideas across the set; reuse an idea at a different tier only if the demand really differs. Mix formats (see section 4). A slot is a row: number, level, format, idea.
4. **Source questions only seed ideas.** The set must contain ideas beyond the source's own range, because the higher tiers (above Advanced) need something the source does not already cover.

## 2. What each tier looks like

Use the calibrated rubric for the full definition; this is the working summary.

| Level | The user's label | Demand | Typical shape |
|---|---|---|---|
| 1 | JEE Main | One familiar move applied once | Direct formula, point found by inspection, SCQ or short integer |
| 2 | Between Main and Advanced | Routine chain of 3 steps, no insight | Standard result plus a second routine step (product rule, tangent line, second derivative) |
| 3 | JEE Advanced | Two ideas linked, or several statements each needing a real check | Multi-statement MCQ with a trap; a lemma that must be argued; a domain/branch decision plus exact arithmetic |
| 4 | One above Advanced | Non-routine idea, or long exact execution with no options | Higher-order derivatives, composite of an inverse with another function, asymptotics, hidden-idea integral relations |
| 5 | Two above Advanced | Unfamiliar idea plus several stages, or very heavy exact casework | Use only when asked |

Format nudges: Numerical/INT run about half a level above the same maths as an SCQ; a one-or-more-correct MCQ with several concepts never ends below 2.5. So put multi-concept MCQs at L3 or L4, and keep L1 and L2 to SCQ and simple integer questions.

## 3. Verification checklist (run code, every question)

- **Answer:** recompute with sympy or mpmath, independently of your hand solution.
- **Well-posed:** domain and range stated; function bijective if an inverse is used (say "bijective" in the question when the proof is not the point); no division by zero at the evaluation point; the object exists and the answer is unique.
- **Hidden roots / branches:** solve the defining equation fully; if more than one root exists, the question must say which (restricted domain) or the answer must not depend on it.
- **MCQ statements:** verify every statement numerically or symbolically, true and false ones. Aim for 1-3 correct options; make wrong statements wrong for a typical reason (sign, missing factor, wrong point), not arbitrary.
- **Limits and asymptotics:** check numerically at large values (mpmath with high precision).
- **Numerical answers:** prefer integers (JEE Advanced style) or values that are exact to two decimals. Avoid answers like 1.625 whose rounding is ambiguous. For INT type the answer must be a non-negative integer; otherwise use Numerical.
- **Hindi:** same numbers, same options, same symbols as English.

## 4. Format rules

- `SCQ`: four options, exactly one correct. Options are plausible results of typical errors.
- `MCQ`: four statements (A)-(D), one or more correct.
- `INT`: answer is a non-negative integer. Build the question so the answer comes out an integer (the "k = ..." or "3 h'(3)" device is standard).
- `Numerical`: decimal answer, correct to 2 decimals.
- Option lines start `(A) `, `(B) `, `(C) `, `(D) `, one per line, in both languages. The script adds the "Only one option is correct." style line from the type.
- Blanks are written `______`.
- Mix formats across the whole set and inside each tier where the level allows.

## 5. Solution style (user-approved)

Reader: a student at about the 90th percentile who knows the concept but has not seen this question. Slightly more detailed than maximal shortening.

Keep: the key idea in words where not obvious; the reason for each non-routine step (why a root is outside the domain, why a function is increasing, why a limit is zero); intermediate results of computations; for one-or-more-correct questions, one line per statement ending "so (X) is correct" / "so (X) is wrong".
Drop: restating the question; "we know that", "thus we get"; separate lines for single arithmetic moves (merge with `$\Rightarrow$`); decimal approximations unless they settle a comparison.

Layout: every list item is one line in the Word file; `""` is a blank line. The last non-blank line is the answer line: `Correct Option: (B)`, `Correct Options: (A), (C)`, or `Final Answer: 6`. Prose in plain text outside `$...$`; no bullets or bold inside solutions. Open the solution with the existence/monotonicity check when an inverse or domain is involved.

LaTeX: `\dfrac`, `\sqrt`, `\Rightarrow`, `\lim_{y\to\infty}`, `\left| ... \right|`, `\mathbb R`. Never put `%`, `&`, `#`, `_`, `^`, `{`, `}` or `\` outside `$...$`.

## 6. Originality

New functions, constants and phrasing. If a source question uses `x^3+3x+2`, do not use it or a trivial variant. A different structure on the same idea is fine (and wanted). Do not quote source wording. If the user's PDF is an official paper, the set must still read as new.
