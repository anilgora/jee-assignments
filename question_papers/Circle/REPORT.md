# Circle: generation report

Blueprint: `qp_blueprints/Circle.xlsx`. There is no `Circle_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing. `pip install` put them under a different Python (pip belongs to Python 3.13, and `python3` is 3.11), so they were installed again with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/` as instructed.
- `build_paper.py` passed on the first full build with no errors and no warnings.

## Blueprint check
- **Pattern:** inferred as **JEE Main**. The blueprint has only Single Correct and Numerical types and nothing above level 3. The paper name ("Circle") comes from the file name.
- **Paper:** 35 questions: 7 Single Correct (Q1-Q7), then 28 Numerical (Q8-Q35). This is the blueprint's own mix, kept as given.
- **Reorder (`--reorder`)**, old Sr No -> new Q:
  330->1, 333->2, 335->3, 336->4, 337->5, 351->6, 353->7, 331->8, 332->9, 334->10, 338->11, 339->12, 340->13, 341->14, 342->15, 343->16, 344->17, 345->18, 346->19, 347->20, 348->21, 349->22, 350->23, 352->24, 354->25, 355->26, 356->27, 357->28, 358->29, 359->30, 360->31, 361->32, 362->33, 363->34, 364->35.
- **Answer Plans:** the blueprint had none, so the script drew all 35 at random:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A, Q6 Option B, Q7 Option D, Q8 negative integer, Q9 positive 2-digit integer, Q10 negative decimal, Q11 decimal between 0 and 1, Q12 positive 3-digit integer, Q13 positive decimal, Q14 positive decimal, Q15 negative decimal, Q16 positive 2-digit integer, Q17 positive 3-digit integer, Q18 negative integer, Q19 decimal between 0 and 1, Q20 negative integer, Q21 negative decimal, Q22 positive 3-digit integer, Q23 decimal between 0 and 1, Q24 positive decimal, Q25 positive 2-digit integer, Q26 positive decimal, Q27 negative decimal, Q28 negative integer, Q29 positive 2-digit integer, Q30 decimal between 0 and 1, Q31 positive 3-digit integer, Q32 positive 2-digit integer, Q33 positive decimal, Q34 decimal between 0 and 1, Q35 negative integer.
  Every answer matches its plan (the build checks this), and no numerical answer repeats.
- **Warnings (recorded, not fixed; the blueprint is yours):**
  - The concept cells in file rows 19, 20 and 35 contain ";": "Direct and transverse common tangents; length of a common tangent" and "Definition of a conic; focus-directrix property PS = e.PM". No config was supplied, so each was kept as **one concept**.
  - Q14 (old 341) lists **4 concepts**, and Q7 and Q15 (old 353, 342) list **3**, although the Main pattern normally has at most two. Every listed concept was used.
  - Concepts repeat within the paper because this is a single-chapter paper. For example, "Tangent and normal to a circle" appears in Q4, Q5, Q11-Q15 and Q30; "Chord of contact for Circle" in Q6, Q14, Q15, Q16 and Q19. Each repeat uses a different mechanism and different circles.
- No errors. The blueprint file was not edited.

## Originality report (per question)
Each mechanism was named before the question was written and checked against `known_skeletons.md`. Every question was web-searched (standard mode).
"not found" means no similar problem turned up. "ingredient only" means only the standard ingredient or method turned up, not this construction. "found: redesigned" means a near-identical problem turned up and the question was replaced.

| Q | Type | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|---|
| Q1 | SCQ | 2 | 2 | the region {y > 0, angle APB >= pi/3} is the major segment of the circle through A, B, so its area needs the segment formula (way 2, a set defined by a construction) | not found |
| Q2 | SCQ | 2 | 2 | a point and two intercept lengths give four circles in two pairs; the position of the origin (sign of c) separates them (way 3, an object fixed by two conditions) | ingredient only |
| Q3 | SCQ | 2 | 2 | the parametric condition tan(theta/2)tan(phi/2) = 1/5 makes every chord pass through a fixed external point, and the midpoint locus is the circle on OA as diameter (way 5) | ingredient only |
| Q4 | SCQ | 2 | 2 | PT along the tangent at T is the tangent length to C1, so "equal tangents" puts P on the radical axis, intersected with the tangent line (way 5) | not found |
| Q5 | SCQ | 2 | 2 | the circle is centred at the focus, so the distance to the tangent at t is sqrt(1 + t^2) and the common tangents are those at t = +-2 (way 4, a hidden invariant) | found: redesigned (new design: ingredient only) |
| Q6 | SCQ | 3 | 3 | points whose polars with respect to two circles coincide (the limiting points, not named) found from proportional coefficients; the external one gives a chord of contact (way 4) | not found |
| Q7 | SCQ | 3 | 3 | the common chords of a family member with a fixed circle all pass through the radical centre, so the least common chord is the shortest chord through that point; attainment checked (way 5) | ingredient only |
| Q8 | Num | 2 | 2 | "a right angle is attained on the line but no obtuse angle" decodes, through the angle in a semicircle, into tangency to the circle on AB as diameter (way 5) | not found |
| Q9 | Num | 3 | 3 | a diametric circle plus lambda (x - y)^2 has exactly one degenerate member (Delta = 0); the lines meet at the pole of y = x (way 4, double contact) | not found |
| Q10 | Num | 2 | 2 | xy on a circle centred on y = x, through the parametric form and u = cos t + sin t, becomes a quadratic with its vertex inside the range of u (way 4) | ingredient only |
| Q11 | Num | 3 | 3 | the tangent of y = x^3 that also touches a small circle gives 100u^3 - 9u^2 - 1 = 0 with u = t^2; the answer is the contact point on the circle (way 5) | not found |
| Q12 | Num | 3 | 3 | normals of y^2 = 4x tangent to a circle centred at the focus; the focus-to-normal distance is \|t\| sqrt(1 + t^2) (way 4) | not found |
| Q13 | Num | 3 | 3 | a circle with a given centre on the major axis touching the ellipse at two points (common normal), then the kite of radii and ellipse tangents (way 5) | not found |
| Q14 | Num | 3 | 3 | the trapezium between the chord of contact and the parallel tangent at the nearest point of the circle (way 5) | not found |
| Q15 | Num | 3 | 3 | points on a line whose chord of contact touches a second, intersecting circle; 2h + k - 4 is constant on the line (way 4) | not found |
| Q16 | Num | 2 | 2 | the external point is recovered from the midpoint of its chord of contact through OM . OP = r^2 (way 3) | not found |
| Q17 | Num | 2 | 2 | chords through P selected by a second condition on their midpoints (a line), so the midpoint locus is intersected with that line (way 3) | ingredient only |
| Q18 | Num | 3 | 3 | a line through the focus bisected at the same point by a parabola and a circle; the two chord-with-midpoint conditions fix the midpoint, and the vertical line is excluded (way 5) | not found |
| Q19 | Num | 2 | 2 | from a point on the directrix, the chords of contact with respect to the parabola and to a circle centred at the focus are parallel, at distance r^2/SP (way 4) | not found |
| Q20 | Num | 2 | 2 | a family of circles through the origin whose centre and radius move together; absolute values give one external and one internal touch (way 2) | ingredient only |
| Q21 | Num | 2 | 2 | "all common tangents pass through one point" holds because the circles intersect (only direct tangents), so the point is the external division point (way 4) | ingredient only |
| Q22 | Num | 2 | 2 | the unknown radius is removed through L_d^2 - L_t^2 = 4 r1 r2 before d is found (way 4) | ingredient only |
| Q23 | Num | 2 | 2 | points on y = x whose polars (for interior points) touch a second circle (way 3) | ingredient only |
| Q24 | Num | 3 | 3 | the member of a two-circle family that bisects a third circle; the family must be normalised before the radical axis is taken (way 5) | ingredient only |
| Q25 | Num | 2 | 2 | K is the meeting point of two common chords (the radical centre, not named), and KA . KB on the first chord is minus the common power (way 5) | ingredient only |
| Q26 | Num | 2 | 2 | any circle centred on a line through a point of a circle cuts it at the complement of the line-circle angle, so the radius 7 does not matter (way 4) | not found |
| Q27 | Num | 2 | 2 | a circle through a point of the given circle whose angle formula reduces to cos theta = 5/r because the alpha^2 terms cancel (way 4) | ingredient only |
| Q28 | Num | 2 | 2 | orthogonality to a circle centred at the origin plus a point fixes c and g at once (inverse-point structure); a line fixes f (way 3) | ingredient only |
| Q29 | Num | 3 | 3 | the member of the family through two points that is orthogonal to a circle, then the common chord of orthogonal circles 2 r1 r2/d (way 5) | ingredient only |
| Q30 | Num | 2 | 2 | the image of a circle in an unknown line y = mx touches the y-axis; reflection seen as rotation by 2 alpha (way 5) | not found |
| Q31 | Num | 2 | 2 | M - m = 2 min(d, r), so the sum over moving points changes formula where the point leaves the circle (way 2) | not found |
| Q32 | Num | 3 | 3 | least distance from a circle to the branch xy = 18; the symmetric vertex is not the nearest point, and u = t + 18/t gives a quadratic (way 4, with a trap) | ingredient only |
| Q33 | Num | 3 | 3 | a moving circle whose centre distance and radius vary oppositely; d + r is minimised by an unequal-split three-term AM-GM (way 5) | not found |
| Q34 | Num | 2 | 2 | PS = e PM at two points with an unknown directrix gives an ellipse branch and a hyperbola branch (way 3) | not found |
| Q35 | Num | 3 | 3 | e is read from one point by PS = e PM, then the centre from a/e - ae and the direction away from the directrix (way 5) | ingredient only |

Standard ingredients worth flagging:
- Q2: circle through a point with given intercepts (common in textbooks). The new step is the four-circle case split by the position of the origin.
- Q3: "the chord with tan(a/2)tan(b/2) constant passes through a fixed point" is a known coaching result for the ellipse, and the midpoint locus of chords through a point is standard.
- Q10: maximum and minimum of xy on a circle through u = sin t + cos t is a known trigonometric device.
- Q17, Q20, Q21, Q22, Q23, Q27, Q28: each uses a standard formula (midpoint locus, touching condition, external centre of similitude, common-tangent lengths, polar, angle between circles, orthogonality) in a reversed or combined setting. These are routine variants, not new ideas.
- Q24, Q29: family-of-circles questions. The constructions (bisecting member of a two-circle family; orthogonal member followed by the common chord) are close to textbook exercises.
- Q35: finding a conic from its focus, directrix and e is a textbook exercise. Here e must first be read from a point and the centre is asked.

**Questions redesigned during this run:**
- **Q5 (after the web check):** the first design was "the circles touching y^2 = 4x at (4,4) and touching the x-axis; smaller radius". The search showed that this is the published problem for the point (1,2) with a new point. It was replaced by the common tangents of the parabola and a circle centred at its focus.
- **Q35 (provenance check):** the first design gave e = 1/2 directly, which made it the textbook "ellipse from focus, directrix and e" exercise. Now e must be read from the point (3,4).
- **Q25 (stem review):** the first stem defined K through equal tangent lengths, which named the idea. K is now the meeting point of two common chords.
- **Q8 (verification):** the first stem said "exactly one point P with angle APB = 90 degrees". Lines through A or B (k = -5, 15) also had exactly one such point, so the answer was not unique. The condition is now "a right angle is attained but no obtuse angle", which leaves only the two tangents.
- **Q18 (verification):** with the first circle (constant term 24), the latus rectum x = -2 was exactly tangent to the circle, a borderline case. The constant term was changed to 25 so the vertical line clearly misses the circle.

Complete novelty cannot be guaranteed. If you recognise any question, say which one.

## Difficulty (calibrated 0-5 scale)
- Distribution: **Level 2: 21 questions** (Q1-Q5, Q8, Q10, Q16, Q17, Q19-Q23, Q25-Q28, Q30, Q31, Q34); **Level 3: 14 questions** (Q6, Q7, Q9, Q11-Q15, Q18, Q24, Q29, Q32, Q33, Q35).
- Every rated level equals its blueprint target, so no question is one level off.
- Marks-weighted index: **2.41** (SCQ 3 marks, Numerical 4 marks; no equivalence-relation or MCQ-floor adjustment applies). This is a JEE Main paper, so there is no official range to compare it with.
- Consistency pass (questions sorted by level, neighbours compared): the borderline pairs are Q3 and Q8 (the hardest L2 questions) against Q33 and Q24 (the lightest L3 questions). Q3 could be read as a weak L3 (two linked coaching results). Q33 could be read as a strong L2 if a student simply differentiates. Ratings with Medium confidence: Q3, Q6, Q8, Q9, Q11, Q12, Q13, Q15, Q18, Q24, Q29, Q32, Q33, Q35.

## Verification
- Every answer was recomputed with sympy/mpmath, independently of the hand solution, and the geometric answers were also checked by a second route:
  - Q1: grid integration of the region (30.318 against 8 pi + 3 sqrt 3 = 30.329).
  - Q7: scan over lambda for the least chord.
  - Q14: coordinates of A, B, D, E and the shoelace formula.
  - Q32: numerical minimisation over the curve.
  - Q9 and Q35: partial derivatives of the expanded equation.
  - Q2 and Q34: every root of the system.
- Problems found while verifying: Q8 (non-unique answer) and Q18 (borderline tangency) were found here; both are fixed as described above. No other problems were found.
- The stem review (`review_stems.py`) is a self-check. An independent reader may still find things.
- The Hindi is my own translation. Please review the specialised terms, especially "ध्रुवी" (polar), "स्पर्श जीवा" (chord of contact), "अनुस्पर्श / तिर्यक उभयनिष्ठ स्पर्श रेखा" (direct / transverse common tangent) and "नियता" (directrix).

## Rows whose concepts were hard to combine naturally
- **Q14 (4 concepts: tangent and normal, length of tangent, tangents from an external point, chord of contact):** all four were placed in one figure (tangent triangle, chord of contact, parallel tangent). The question is natural, but it is a long single situation rather than a link between ideas.
- **Q34 and Q35 ("PS = e PM form for a conic", plus "Definition of a conic; focus-directrix property" in Q35):** these concepts belong to the conics chapter, not to circles, and the two concepts of Q35 are nearly the same idea. Both questions are about ellipses. A circle cannot be used, since it has no focus-directrix form with e > 0.
- **Q11 (tangent to a circle + equation of a tangent to a curve)** and **Q32 (distance of a point from a circle + minimum distance from a curve):** these combine naturally. The circle part is light in each, and the curve part carries the difficulty.
