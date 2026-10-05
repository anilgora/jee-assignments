# RUN REPORT – JEE_Main_Question_Bank_01_Coordinate_Geometry_06 (PDF Q101–Q120, Ellipse and Hyperbola)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Numbering:** the PDF numbers the questions 101–120; the deck numbers them 1–20 (deck n = PDF n+100; the JSON also stores `q_ref`). Types by deck number: single correct = 1–7, 11–14, 16–20; numerical = 8, 9, 10, 15.
**Marks assumed:** none printed; 4 marks each (JEE Advanced default for single-correct and numerical), stated in the section dividers.

## Difficulty
Marks-weighted difficulty index (all 4 marks; no equivalence-relation or multi-correct adjustment applies): **1.90**.
L1 = 3 (Q3, Q5, Q11); L2 = 16 (Q1, 2, 4, 6, 7, 9, 10, 12–20); L3 = 1 (Q8). No L0, L4, L5. Confidence Medium (JEE Main-style questions rated on the Advanced scale; anchors only indicative). Index computed by hand ((3·1+16·2+3)/20); the Excel formulas were not recalculated (no recalc step here).

## Solutions corrected / written
- Q2 (PDF 102) corrected: PDF writes x = ±√6/5; the correct value is ±√6/√5 (x² = 6/5). Its area line already uses √6/√5, so the answer 24√6/5 is unchanged. Also the skipped factor 4/9 in the aB step is written out.
- Q5 (PDF 105) corrected: the question statement prints B(β,0); the PDF's own solution (and the original JEE question) use B(0,β). Statement fixed; working correct.
- Q7 (PDF 107) corrected: last line printed "e² = √117/21 = √13/7" should be "e = ...". The section-formula step R = (3P+4Q)/7 was missing; added.
- Q10 (PDF 110) corrected: PDF says "Putting y² = 2x²"; it must be y² = 3x² (as the following lines use). The reason b = 4 is rejected is spelled out.
- Q13 (PDF 113) corrected: the PDF ends with xy − 2√3x + 3√3y − 6 = 0 (γ = −6); the correct constant is +6 (γ = +6; checked numerically). α²+β²+γ² = 75 is unchanged.
- Small bridging lines added without changing the PDF's method (source stays pdf): Q1 (intermediate T = S1 arithmetic, 3/√2 factor), Q4 (the integration steps), Q8 (which point belongs to E1/E2), Q9, Q12, Q15 (squared focal distances), Q20 (β = 2 step). No question needed "written".

## Answer key
All 20 answers verified by hand and by plain-Python numerics (sympy/numpy not installed) and agree with the PDF key: 1 B(22), 2 A, 3 C(11), 4 B, 5 A, 6 A, 7 D, 8 46, 9 54, 10 432, 11 A, 12 D, 13 B, 14 A, 15 120, 16 B, 17 D, 18 A, 19 A, 20 B. No key looks wrong.

## Alternates and Useful Results
- Alternates given for all 20 questions (1–20); every alternate was checked to reach the same answer.
- NO alternate: none.
- Alternates only partly different (same ingredients, different packaging) - flagged for review: Q5 (semi-latus rectum = e × focus–directrix distance), Q11 (same idea for the hyperbola), Q12 (m = (S² − 4a²)/4), Q18 (c-based formulas), Q20 (parametric form).
- Useful Result / Pattern given for all 20 questions.

## make_ppt.py warnings
None printed (875 equations converted, 137 slides, 20 questions); no "could not convert" notes.

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step here); recalc of the Excel skipped (no /mnt/skills).
- The PDF text layer is garbled; all questions and solutions were read from page images (90 dpi).
- Concepts and levels self-assigned; marks assumed as above. The option text of Q116(D) is kept as printed ("9x − 9y = 32").
