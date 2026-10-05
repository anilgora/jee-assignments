# RUN REPORT – JEE_Main_Question_Bank_01_Coordinate_Geometry_02 (PDF Q21–Q40, Straight Line and Circle)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Numbering:** the PDF numbers the questions 21–40; the deck numbers them 1–20 (deck n = PDF n+20; the JSON also stores `q_ref`).
**Marks assumed:** none printed; 4 marks each (JEE Advanced default for single-correct and for numerical), stated in the section dividers. Q1–12 and Q18–20 are single-correct; Q13–17 are numerical (PDF Q33–37).

## Difficulty
Marks-weighted difficulty index (all 4 marks; no equivalence-relation or multi-correct adjustment applies): **2.15**.
L1 = 2 (Q9, Q11); L2 = 13 (Q1–7, 10, 12, 13, 18, 19, 20); L3 = 5 (Q8, 14, 15, 16, 17). No L0, L4, L5. Confidence Medium (JEE Main-style questions rated on the Advanced scale; anchors only indicative).

## Solutions corrected / written
- Q1 (PDF 21) corrected: the PDF takes −(3k−2h−5)=20, i.e. 2h−3k=15, which is the locus BELOW AB; it reads a=2, b=−3 and 5a+2b=4 (option B), contradicting its own key D. For P above AB the branch is 3k−2h−5=20, 2x−3y=−25, rescaled to ax+by=15: a=−6/5, b=9/5, 5a+2b=−12/5 (D).
- Q10 (PDF 30) corrected: the PDF writes h=4/3; from −(8/3)xy=2hxy, h=−4/3 (its final sum already uses −4/3). Answer 14 unchanged.
- Q17 (PDF 37) corrected: the PDF shows slope of CE as 2/3 (y=2x/3); CE ⟂ AB (slope −2/3), so the slope is 3/2 (its next lines 3x−2y=0 already use 3/2). Answer 16 unchanged.
- Q18 (PDF 38) corrected: the PDF's "(1)−(2): 13f+3g=0" should be 13f+39=0; f=−3 and the rest are right. Answer 35 unchanged.
- Q19 (PDF 39) corrected: the figure labels the centre of C1 as (−3,3), but the question says third quadrant and the working uses (−3,−3). Answer 22 unchanged.
- Small bridging lines added without changing the PDF's method (source stays pdf): Q2 (explicit modulus), Q4 (checks of the two intersections), Q6 (sign of L2(0)), Q9 (derivation of tan15°), Q11 (consistency check that integer data exist: A(−2,−1), C(4,3)), Q13 (determinant value 8−10α and slopes), Q15 (PDF figure shows B(−2,5), correct is (−2,−5)), Q16 (why AB, AC are the two lines at π/6), Q7 and Q20 (explicit reasoning for the centre).
- No question needed "written".

## Answer key
All 20 PDF answers verified by computation (sympy / numerical checks) and agree with the key: 1 D, 2 C, 3 D, 4 A, 5 C, 6 C, 7 A, 8 D, 9 C, 10 D, 11 D, 12 B, 13 32, 14 145, 15 14, 16 14, 17 16, 18 D, 19 D, 20 D. The key is right everywhere; only the PDF working for Q1 disagrees with its own key (corrected above).

## Alternates and Useful Results
- Alternates given for 18 questions: Q1–Q10, Q12, Q13, Q15–Q20.
- NO alternate:
  - Q11 - it is a one-step mid-point identity (A+C=B+D); any other route (using AB and the line) is a longer way to the same two sums, not a different method.
  - Q14 - the only routes are the 2:1 Euler-line ratio and the vector sum H=A+B+C (the same fact in another form); the squaring step for sin2α has no different alternative worth showing.
- Alternates only partly different (same ingredients, different packaging) - flagged for review: Q4 (vector parametrisation + general circle equation), Q13 (substitute the intersection point instead of the determinant), Q19 (unit vector along the line of centres instead of the section formula).
- Useful Result / Pattern given for all 20 questions.

## make_ppt.py warnings
None printed (962 equations converted, 130 slides, 20 questions); no "could not convert" notes.

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step here); recalc of the Excel skipped (no /mnt/skills).
- Greek letters in the PDF text layer were lost; the question statements of Q1, 4, 6–9, 13, 14, 16, 19, 20 were read from page images and every answer was recomputed.
- Concepts and levels self-assigned; marks assumed as above.
