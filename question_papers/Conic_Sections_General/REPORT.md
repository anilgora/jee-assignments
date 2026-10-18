# Conic_Sections_General: generation report

Blueprint: `qp_blueprints/Conic_Sections_General.xlsx`. There is no `Conic_Sections_General_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`; installed with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The paper title in `meta.json` is "Conic Sections General" (no underscores, which break xelatex); file names use `Conic_Sections_General`.
- `build_paper.py` passed on the first run with no errors and no warnings. No script was edited.
- Page 1 of each of the three PDFs was rendered and checked: Hindi shaped, equations in 2D, display formulas readable.

## Blueprint check
- **Pattern:** inferred as **JEE Main** (only Numerical type, nothing above level 3). The paper name comes from the file name.
- **Paper:** 6 questions, all Numerical (Sr No 365-370 -> Q1-Q6).
- **Reorder:** none needed. The mapping is the identity: 365->1, 366->2, 367->3, 368->4, 369->5, 370->6.
- **Answer Plans:** the blueprint had none, so the script drew all six:
  Q1 negative decimal, Q2 positive 3-digit integer, Q3 negative integer, Q4 positive 2-digit integer, Q5 positive decimal, Q6 decimal between 0 and 1.
  Every answer matches its plan (the build checks this).
- **Warnings (recorded, not fixed; the blueprint is yours):**
  - Rows 1 and 2 contain a concept cell with ";" ("Definition of a conic; focus-directrix property PS = e.PM" and "Classification by eccentricity; degenerate conics"). No config was supplied, so each was kept as **one concept**. Both parts of each cell are used: in Q1, PS = e.PM plus the e < 1 test; in Q2, classification by e plus the degenerate cases.
  - "Common tangents to any two conics" is used in Q3 and Q4, and "Common chord and common normal of two conics" in Q5 and Q6. These are expected in a single-chapter paper, and each repeat uses a different mechanism.
- No errors. The blueprint file was not edited.

## Answers
Q1 -3.20, Q2 223, Q3 -9, Q4 10, Q5 3.25, Q6 0.80.
Each was recomputed with sympy/numpy separately from the hand solution. Q1 was also checked by scanning the directrix position numerically. Q2 was checked by brute-force enumeration of all 400 pairs. Q3 was checked by counting tangent lines for k = +-3, 2, 4, -5. Q4 and Q6 were checked by solving the curves exactly, including the perfect-square check for double contact in Q6. Q5 was checked by solving the two parabolas symbolically.

## Difficulty
- Level distribution: **3 questions at level 2 (Q1, Q3, Q5) and 3 at level 3 (Q2, Q4, Q6)**. Every question is rated at its target level.
- Marks-weighted index: **2.50**. No equivalence-relation or multi-correct adjustments apply. This is a Main-pattern chapter paper, so it is not expected to fall in the Advanced range of 2.6-3.2.
- No question is one level off target. Borderline ratings (Medium confidence):
  - Q4 (rated 3): once the centre is seen to be the focus, the algebra is light; it could be read as 2.
  - Q6 (rated 3): the key step is the familiar "normal meets the major axis at e^2 x1"; it could be read as 2 by a student who knows that result well.
  - Q2 (rated 3): the lattice count is long and precise; it could be read as 4.
- Consistency pass: the level-2 questions were read next to the level-3 ones, and the order was kept.

## Originality report (per question)
Each mechanism was named before the stem was written and checked against `known_skeletons.md`. Every question was web-searched (WebSearch, standard mode).

| Q | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|
| Q1 | 2 | 2 | The directrix and e are unknown and are recovered from two points through PS = e.PM. The two absolute-value cases give a hyperbola and an ellipse, and "ellipse" selects one (way 3) | not found |
| Q2 | 3 | 3 | A focal-sum locus and a focal-difference locus share foci p and qi. "Ellipse and hyperbola at once" becomes an annulus 100 < p^2+q^2 < 400 with degenerate conics on both boundaries, followed by a lattice count (way 2) | not found |
| Q3 | 2 | 2 | Common tangents of an ellipse and xy = k come from a quadratic in the slope. "Exactly two" forces the touching case, which happens for both signs of k (way 3) | ingredient only (tangency conditions) |
| Q4 | 3 | 3 | The circle's centre is the parabola's focus, so the tangency condition collapses to sqrt(1+m^2)/abs(m) = r. The radius-tangent right angle then gives the kite T B1 K B2 (way 4) | ingredient only |
| Q5 | 2 | 2 | Two coaxial parabolas share a focus and open opposite ways. Their common chord is x = b - a with length 4 sqrt(ab), and that length fixes the second parabola (way 5) | ingredient only |
| Q6 | 3 | 3 | Circles of double contact with an ellipse are found through the common normal (centre at e^2 x0 on the axis); their common chord and its length follow (way 5) | not found |

Standard ingredients worth flagging:
- Q3: the tangency condition for xy = c^2 is the same ingredient as the published JEE Main problem "common tangent of y^2 = 8x and xy = -1". Here an ellipse replaces the parabola and the unknown k is fixed by the count of tangents.
- Q4: the first design asked for the area of the quadrilateral of all four contact points. That is the same ask as the official 2023-P1-Q2 (with an ellipse), so it was replaced by the kite T B1 K B2. The fact that the feet of perpendiculars from the focus lie on the tangent at the vertex is a known property.
- Q5: confocal parabolas are known (they cut orthogonally). The common-chord-length set-up was not found.
- Q6: the normal-meets-major-axis-at-e^2 x1 result is standard. The double-contact circles were not found as a problem.
- Novelty cannot be guaranteed; please flag any question you recognise.

## Problems found while verifying
- Q2: the first draft of the shortened solution miscounted the p = 16 row (it gave 12; the correct value is 11, because (16,12) lies on the boundary). It was corrected to 292 - 69 = 223 before the build, and the brute-force count confirms 223.
- Q2: the word "and" inside the display formula was replaced by a comma, so no text sits inside the maths (Hindi copy).
- Q4: the ask was changed for originality (see above).

## Rows whose concepts were hard to combine naturally
- None was forced. Q1, Q3 and Q5 are single-concept rows at level 2, which left little room for a deep new mechanism. Q6's pairing (common normal + common chord of two circles) worked through double-contact circles.

## Notes
- The Hindi is the assistant's own translation; please review specialised terms (नियता for directrix, उभयनिष्ठ जीवा for common chord, उभयनिष्ठ स्पर्श रेखाएँ for common tangents).
- The stem review is a self-check; an independent reader may still find things.
- `_source/` holds `blueprint.json`, every `qNN.json` and `meta.json`, so a question can be fixed and the paper rebuilt with `build_paper.py`.
