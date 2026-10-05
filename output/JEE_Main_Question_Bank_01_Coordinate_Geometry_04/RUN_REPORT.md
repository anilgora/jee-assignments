# RUN REPORT – JEE_Main_Question_Bank_01_Coordinate_Geometry_04 (PDF Q61–Q80, Circle and Parabola)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Numbering:** the PDF numbers the questions 61–80; the deck numbers them 1–20 (deck n = PDF n+60; the JSON also stores `q_ref`). Deck Q1–Q9 are Circle, Q10–Q20 Parabola.
**Marks assumed:** none printed; 4 marks each (JEE Advanced default for single-correct, integer and numerical), stated in the section dividers. Types: deck Q1 and Q10–Q20 single correct; Q2–Q9 numerical (answers 768, 100, 2, 1575, 3, 121, 2, 7).

## Difficulty
Marks-weighted difficulty index (all 4 marks; no equivalence-relation or multi-correct adjustment applies): **2.05**.
L1 = 3 (Q3, 14, 16); L2 = 13 (Q2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 19, 20); L3 = 4 (Q1, 7, 17, 18). No L0, L4, L5. Confidence Medium (JEE Main-style questions rated on the Advanced scale; anchors only indicative). Index computed by hand ((3·1+13·2+4·3)/20); the Excel has formulas that were not recalculated (no recalc step here).

## Solutions corrected / written
- Q4 (PDF 64) corrected: the working writes the first point of the line as (−22/7, **4**); the question and the later line 7x−3y+10=0 need (−22/7, **−4**). Answer 2 unchanged.
- Q18 (PDF 78) corrected: the PDF gives A(1/2, 1); for t₁=1/2, A=(t², 2t)=(1/4, 1). Its D(1/4, −1) and area 75/4 are right.
- Small bridging lines added without changing the PDF's method (source stays pdf): Q1 (β−α, α²+β²), Q2 (why centre is on the x-axis), Q3 (note that OP=4√2 is not needed, consistency check), Q4 (slope computation), Q5 (θ acute, radical axis), Q6 (b²+b=4 step), Q9, Q10 (t>0 root, tangency from double root), Q12 (how vertex, focus and directrix follow), Q20 (centre of the circle).
- No question needed "written".

## Answer key
All 20 answers verified by hand and numerically (plain Python; sympy not installed) and agree with the PDF key: 1 B, 2 768, 3 100, 4 2, 5 1575, 6 3, 7 121, 8 2, 9 7, 10 B, 11 A, 12 B, 13 B, 14 C, 15 C, 16 D, 17 C, 18 D, 19 B, 20 B. Q12: the quadratic gives k=1 or 9; 1 is not an option, 9 (B) is. No key looks wrong.

## Alternates and Useful Results
- Alternates given for 19 questions: all except Q8.
- NO alternate:
  - Q8 - the only route to the image circle is reflecting the centre in the line (formula, or midpoint + perpendicular, which is the same computation); the radius then follows from the equal-radius property.
- Alternates only partly different (same ingredients, different packaging) - flagged for review: Q4 (foot of perpendicular instead of tangent T=0), Q6 (algebraic inequalities instead of reading intersections), Q9 (substitution/Vieta instead of half-chord), Q13 (focal-distance parameter on x=−2), Q15 (three-triangle decomposition), Q19 (reduction to points (t,t)).
- Useful Result / Pattern given for all 20 questions.

## make_ppt.py warnings
None printed (732 equations converted, 125 slides, 20 questions); no "could not convert" notes.

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step here); recalc of the Excel skipped (no /mnt/skills).
- The PDF text layer is garbled (Hindi/Greek); all questions and solutions were read from page images (80 dpi).
- Concepts and levels self-assigned; marks assumed as above. The alternate in Q7 relies on a stated result (PQ² = product of distances to the two tangents), proved briefly in the slide and checked numerically.
