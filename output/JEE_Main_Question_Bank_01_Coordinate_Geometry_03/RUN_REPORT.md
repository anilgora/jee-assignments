# RUN REPORT – JEE_Main_Question_Bank_01_Coordinate_Geometry_03 (PDF Q41–Q60, Circle)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Numbering:** the PDF numbers the questions 41–60; the deck numbers them 1–20 (deck n = PDF n+40; the JSON also stores `q_ref`).
**Marks assumed:** none printed; 4 marks each (JEE Advanced default for single-correct), stated in the section divider. All 20 questions are single-correct. Options printed as (1)–(4) in PDF Q53–Q55 and Q59 are shown as (A)–(D) in the deck (NTA keys 2, 2, 1 become B, B, A).

## Difficulty
Marks-weighted difficulty index (all 4 marks; no equivalence-relation or multi-correct adjustment applies): **2.05**.
L1 = 3 (Q6, 8, 9); L2 = 13 (Q1–5, 7, 10–14, 17, 18); L3 = 4 (Q15, 16, 19, 20). No L0, L4, L5. Confidence Medium (JEE Main-style questions rated on the Advanced scale; anchors only indicative). Index computed by hand from the levels ((3·1+13·2+4·3)/20); the Excel has formulas that were not recalculated here (no recalc step).

## Solutions corrected / written
- Q11 (PDF 51) corrected: the PDF writes the circle as (x−4)²+(y−2)²=20; completing squares gives (x−8)²+(y−2)²=68. Its next line already uses centre (8,2), so the answer 18 is unaffected. A check m<0 and f''>0 was added.
- Q15 (PDF 55) corrected: for α=28/3 the PDF gives centre (28/3, −109/2) and r≈49.78; correct is β=−109/9, r=80/9≈8.89 (still >8, rejected). Answer 7 unchanged. Added the intermediate equation |25α−100|=|7α+68|.
- Q16 (PDF 56) corrected: typo in line 3 (both terms written cos²(θ2/2); should be θ2 and θ3) and the last line says θ3=π/2 where θ2=π/2 is meant. Answer D unchanged.
- Q19 (PDF 59) corrected: the PDF silently assumes the circle is the incircle. Three lines have four tangent circles; incentre and the excentre opposite A give h+k=5, the excentre opposite B gives 5+5√2 (option D), the one opposite C gives 5−5√2. Added a step stating the incircle assumption. Key (A) 5 kept.
- Small bridging lines added without changing the PDF's method (source stays pdf): Q1 (b²=β²−4γ derivation, PDF's "P²" is a garble for r²), Q3 (explicit ON), Q4 (why distance √2 and the second line's quadratic), Q5 (side-of-O remark: only 3−√2 is an option), Q6 (why centre (2,1)), Q7 (why CF=r√2+r), Q8 (explicit C2 expansion), Q10 (PDF prints 15/α where 15/2 is meant, in the section-formula and r2 lines), Q15 (A(4,−5) is a contact point), Q17 (reason for α=0; expansion to option D), Q18 (check A,B on circle, derivation of AB), Q20 (why B=A+(2,−2): A is at distance r from T).
- No question needed "written".

## Answer key
All 20 answers verified by computation (numeric / sympy checks) and agree with the key: 1 A, 2 D, 3 A, 4 C, 5 C, 6 A, 7 A, 8 C, 9 B, 10 D, 11 A, 12 B, 13 B, 14 B, 15 A, 16 D, 17 D, 18 A, 19 A, 20 C. Q5: the other possible distance 3+√2 is not an option. Q7: the root 4+2√2 of r²−8r+8=0 is rejected geometrically but option A holds for both roots. **Q19 (PDF 59) is ambiguous**: the key 5 is correct for the incircle (and the A-excircle), but 5(1+√2) (option D) is the value for the B-excircle.

## Alternates and Useful Results
- Alternates given for 18 questions: Q1–Q5, Q7–Q9, Q11–Q20.
- NO alternate:
  - Q6 - a one-step result (tangent lines fix the centre, shortest distance = d − r); any other route is the same computation.
  - Q10 - the section formula is the only route to the centres; the vector form C1=3P−2C2 is the same formula rewritten, and r1=2r2 gives the same distances.
- Alternates only partly different (same ingredients, different packaging) - flagged for review: Q5 (coordinate form instead of the geometric chord-distance), Q7 (coordinates instead of the diagonal), Q20 (uses y_A directly instead of both centres), Q2 (cross product of diagonals vs ½d1d2).
- Useful Result / Pattern given for all 20 questions.

## make_ppt.py warnings
None printed (694 equations converted, 122 slides, 20 questions); no "could not convert" notes.

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step here); recalc of the Excel skipped (no /mnt/skills).
- The PDF text layer lost the Greek letters; all question statements were read from page images (80 dpi) and every answer was recomputed.
- Concepts and levels self-assigned; marks assumed as above.
