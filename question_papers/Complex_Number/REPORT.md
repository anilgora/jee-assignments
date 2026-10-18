# Complex_Number: generation report

Blueprint: `qp_blueprints/Complex_Number.xlsx`. There is no `Complex_Number_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`; installed with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/` as instructed.
- The first build stopped in xelatex because the title "Complex_Number" in `meta.json` contained an underscore. The title was changed to "Complex Number" (file names still use `Complex_Number`). After that, `build_paper.py` passed with no errors and no warnings. No script was edited.
- Page 1 of each PDF (and the page with the determinant in Q16) was rendered and checked: Hindi shaped, equations in 2D.

## Blueprint check
- **Pattern:** inferred as **JEE Main** (only Single Correct and Numerical types, nothing above level 3). Paper name taken from the file name.
- **Paper:** 26 questions: 4 Single Correct (Q1-Q4), then 22 Numerical (Q5-Q26), as in the blueprint.
- **Reorder (`--reorder`)**, old Sr No -> new Q:
  218->1, 222->2, 228->3, 231->4, 214->5, 215->6, 216->7, 217->8, 219->9, 220->10, 221->11, 223->12, 224->13, 225->14, 226->15, 227->16, 229->17, 230->18, 232->19, 233->20, 234->21, 235->22, 236->23, 237->24, 238->25, 239->26.
- **Answer Plans:** the blueprint had none, so the script drew all 26:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 positive 2-digit integer, Q6 negative decimal, Q7 negative integer, Q8 positive decimal, Q9 decimal between 0 and 1, Q10 positive 3-digit integer, Q11 negative integer, Q12 positive 2-digit integer, Q13 negative decimal, Q14 decimal between 0 and 1, Q15 positive 3-digit integer, Q16 positive decimal, Q17 positive decimal, Q18 negative decimal, Q19 positive 2-digit integer, Q20 positive 3-digit integer, Q21 negative integer, Q22 decimal between 0 and 1, Q23 negative integer, Q24 negative decimal, Q25 positive 3-digit integer, Q26 decimal between 0 and 1.
  Every answer matches its plan (the build checks this), and no numerical answer repeats.
- **Warnings (recorded, not fixed; the blueprint is yours):**
  - File rows 19 and 20 contain a concept cell with ";": "Circle in complex form; Apollonius locus |z-z1|/|z-z2| = k". No config was supplied, so it was kept as **one concept** (used in Q19 and Q20, where both the circle form and the Apollonius locus are needed).
  - Q7 (old 216) lists **4 concepts**, and Q2, Q3, Q8 (old 222, 228, 217) list **3**, although the Main pattern normally has at most two. Every listed concept was used.
  - Concepts repeat within the paper because this is a single-chapter paper (for example "Conjugate, modulus and argument of a complex number" in Q5-Q8, "De Moivre theorem" in Q8, Q14, Q15). Each repeat uses a different mechanism.
- No errors. The blueprint file was not edited.

## Answers
Q1 (C), Q2 (A), Q3 (B), Q4 (D); Q5 82, Q6 -1.24, Q7 -3, Q8 2.25, Q9 0.64, Q10 596, Q11 -8, Q12 17, Q13 -1.92, Q14 0.5, Q15 127, Q16 3.5, Q17 8191.75, Q18 -0.6, Q19 18, Q20 902, Q21 -5, Q22 0.8, Q23 -27, Q24 -1.5, Q25 117, Q26 0.6.
Every answer was recomputed independently with sympy/numpy (dense numerical sampling of loci, exact symbolic solution, or brute-force enumeration for the lattice count in Q12 and the iteration in Q13).

## Difficulty
- Level distribution: **12 questions at level 2, 14 at level 3**. Every question is rated at its target level.
- Marks-weighted index (adjusted): **about 2.52** (no equivalence-relation or multi-correct adjustments apply). This is a Main-pattern chapter paper, so it is not expected to match the Advanced range of 2.6-3.2.
- No question is one level off target. Borderline ratings (Medium confidence), worth a look:
  - Q4 (rated 3): the pieces are routine; level 3 rests on the two traps (scaled coefficients, factor 2 in the distance) built into the options. It could be read as 2.
  - Q8 (rated 3): short once the GP form (z^5 - zbar^5)/(z - zbar) is seen; could be read as 2.
  - Q13 (rated 3): the invariant of a complex-weight recurrence is uncommon; could be read as 4.
- Consistency pass: the hardest level-2 questions (Q9, Q16, Q19) were read next to the easiest level-3 questions (Q4, Q8); the order was kept.

## Originality report (per question)
Each mechanism was named before the stem was written and checked against `known_skeletons.md`. Every question was web-searched (standard mode).
"not found" = no similar problem turned up; "ingredient only" = only the standard ingredient or method turned up, not this construction.

| Q | Type | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|---|
| Q1 | SCQ | 3 | 3 | a sum of two counter-rotating vectors of unequal length traces a rotated ellipse whose major axis lies along half the sum of their arguments, so the compound-angle formula fixes the axis (way 4, hidden structure) | ingredient only |
| Q2 | SCQ | 3 | 3 | an argument-locus arc whose nearest point to the given point is an excluded end point, so the triangle-inequality minimum is an infimum and the range is half-open (way 5, the link between the arc's end points and the extremum is the discovery) | ingredient only |
| Q3 | SCQ | 3 | 3 | the exponent k^2 hides a multisection, because omega^{k^2} only separates multiples of 3 from the rest (way 4, hidden structure) | not found |
| Q4 | SCQ | 3 | 3 | two parallel pairs given in the complex form with differently scaled coefficients; in this form the area reduces to |b1-b2||b3-b4|/(4|Im(a1 conj a2)|) (way 4, the moduli cancel) | ingredient only |
| Q5 | Num | 2 | 2 | the conjugate in the denominator turns the equation into z times a positive real, so the argument is fixed and only a quadratic in |z| remains (way 4, hidden structure) | ingredient only |
| Q6 | Num | 3 | 3 | zbar/z = e^{-2i theta} turns the expression into a function of arg z, and the range of arg z on a circle touching the real axis is [0, 2 phi] by the tangent symmetry, so the extremum sits at a tangent point (way 5) | not found |
| Q7 | Num | 3 | 3 | the rotation that carries B to D also carries the circle of B to a circle, which is intersected with the line of D (way 3, an object fixed by two conditions on different vertices) | not found |
| Q8 | Num | 3 | 3 | a symmetric sum of mixed powers of z and zbar is a GP whose sum is (z^5 - zbar^5)/(z - zbar) = r^4 sin 5theta / sin theta, real by symmetry (way 4, hidden structure) | not found |
| Q9 | Num | 2 | 2 | the orthocentre of a triangle inscribed in |z| = 1 is z1+z2+z3, and with zbar = 1/z the second symmetric sum equals (z1 z2 z3) times the conjugate of the orthocentre (way 5, link between Euler line and conjugation) | ingredient only |
| Q10 | Num | 2 | 2 | the Apollonius circle is used only as the carrier of a distance extremum, with the point placed so that the answer comes through the triangle inequality (way 5) | ingredient only |
| Q11 | Num | 3 | 3 | the constant in |z^2 + 7 - 24i| is minus the square of the circle's centre, so the expression factors and one factor is constant on the circle (way 4, hidden factorisation) | not found |
| Q12 | Num | 3 | 3 | the set between two argument arcs over the same chord is a lune-like region, and the question counts its lattice points, so both arcs, the half-plane and the inclusion of boundary points matter (way 2, a set defined by a construction) | not found |
| Q13 | Num | 3 | 3 | an iterated right-isosceles construction gives the complex recurrence p_{n+2} = c p_n + (1-c) p_{n+1}, whose weighted invariant p_{n+1} + c p_n gives the limit point (way 1, iteration) | not found |
| Q14 | Num | 3 | 3 | the principal-argument condition on (1+it)^3 selects two of the three roots of tan 3theta = -1, because 3 arctan t ranges over (-3pi/2, 3pi/2) (way 5, the branch selection is the discovery) | not found |
| Q15 | Num | 3 | 3 | a geometrically weighted cosine series with angles in AP whose partial sums, via De Moivre, collapse to 2^n - 1, -1 or -2^n - 1 according to n mod 6, and the question asks for the largest partial sum (way 2, a sequence analysed after a construction) | not found |
| Q16 | Num | 2 | 2 | the data fix only a+b+c and the modulus of a+b omega+c omega^2, yet the determinant is determined because the omega-factorisation pairs conjugate factors (way 4, invariant) | ingredient only |
| Q17 | Num | 2 | 2 | the weight cos^2(k pi/3) takes only the values 1 and 1/4, so the sum is a weighted multisection of the binomial row (way 4) | not found |
| Q18 | Num | 2 | 2 | tangency of a family of complex-form lines to a circle, then the contact point read off as the centre moved along the unit normal a/|a| (way 3) | ingredient only |
| Q19 | Num | 2 | 2 | the product of the two intercepts of a ray from one Apollonius point on the Apollonius circle is the power of that point, k^2|AB|^2/(k^2-1), independent of the ray (way 4, invariant) | not found |
| Q20 | Num | 3 | 3 | a circle given in diametric form is rewritten as an Apollonius circle with a prescribed second point; alpha is the inverse point of beta and k = R/|beta - c| (way 3, an object fixed by two conditions) | ingredient only |
| Q21 | Num | 2 | 2 | the perpendicular-bisector locus is used as a mirror whose defining points give the image of the ray's vertex at once, and the ray's meeting point with the mirror fixes the image direction (way 5) | not found |
| Q22 | Num | 2 | 2 | the directrix is hidden in the conjugate expression |z + zbar - 34|, so the eccentricity is twice the visible coefficient (way 4) | ingredient only |
| Q23 | Num | 3 | 3 | an ellipse given by a complex focal-sum locus with an oblique axis; the latus rectum end points are found by turning the axis direction through pi/2 (multiplication by i) and using b^2/a (way 5) | not found |
| Q24 | Num | 2 | 2 | a pair of equations in which z and w appear conjugated in opposite places; conjugating one equation makes the system linear in z and wbar (way 4) | ingredient only |
| Q25 | Num | 2 | 2 | z^5 = 81 zbar gives the origin plus a regular hexagon, and the asked sum is a moment of the solution set about one of its own points, where forgetting z = 0 gives 108 (way 3) | ingredient only |
| Q26 | Num | 2 | 2 | a circle and a line both given in complex form, with the angle at the centre asked, so the centre-radius form, the line's normal form and the double-angle step are chained (way 5, routine combination) | ingredient only |

Standard ingredients worth flagging:
- Q9: the identity |z1+z2+z3| = |z1z2+z2z3+z3z1| on the unit circle appears on the web as a proof exercise. The question uses the signed form with the product z1z2z3 and the orthocentre as data, but the core ingredient is that known identity.
- Q10, Q18, Q22, Q24, Q26: routine combinations of standard results (Apollonius circle plus distance extremum; tangency of a complex-form line; focus-directrix with z + zbar = 2x; a linear system after conjugation; circle and line in complex form). These are acceptable level-2 variants but not new ideas.
- Q25: the count of solutions of z^n = zbar is a known skeleton; here it is only the first step, and the sum over the solution set (with the trap z = 0) is asked.
- Q3 and Q17 both weight a binomial row with a root-of-unity pattern (omega^{k^2} and cos^2(k pi/3)); the mechanisms differ but the flavour is similar.
- Novelty cannot be guaranteed; please flag any question you recognise.

## Problems found while verifying (fixed before the build)
- Q9: the first design asked only |z1z2+z2z3+z3z1| given the orthocentre. The web check showed that the modulus identity is a published exercise, so the product z1z2z3 = i was added and the real part of the signed sum is asked. The data were checked to be consistent (the cubic has three distinct roots of modulus 1).
- Q6: the first draft of the solution compared 4 phi with 3 pi/4 using a wrong decimal; corrected to the exact comparison cos 4phi = -7/25 > -1/sqrt2 before the build.
- Q13: the numerical check values in the solution were corrected (p4 = 3 - i, p5 = 2 - i, p6 = 2.5 - 0.5i).
- Q12 (stem review): "z != +-2" was added to the stem so the domain of the argument is explicit.

## Rows whose concepts were hard to combine naturally
- Q7 (4 concepts: conjugate/modulus/argument, polar form, loci, rotation): all four are used, but "conjugate, modulus and argument" enters only through z + zbar = 2 Re z for the line and |iz| = |z|.
- Q9 and Q24 and Q26 are single-concept rows, which made level-2 questions with little room for a new mechanism.

## Notes
- The Hindi is the assistant's own translation; please review specialised terms (for example मुख्य कोणांक for principal argument, नाभिलम्ब for latus rectum).
- The stem review is a self-check; an independent reader may still find things.
- `_source/` holds `blueprint.json` and every `qNN.json` plus `meta.json`, so a question can be fixed and the paper rebuilt with `build_paper.py`.
