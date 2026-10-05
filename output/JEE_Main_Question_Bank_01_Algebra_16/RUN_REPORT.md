# RUN REPORT – JEE_Main_Question_Bank_01_Algebra_16 (Q301–Q320: Binomial Theorem Q301–307, Complex Numbers Q308–320)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Marks assumed:** no marks printed; 4 marks for every question (numerical Q1–Q7 = PDF 301–307, single correct Q8–Q20 = PDF 308–320), as in the Algebra_15 run; stated in the section dividers. Deck numbering 1..20 = PDF 301..320.

## Difficulty
Marks-weighted difficulty index (all 4 marks, no equivalence-relation or MCQ-floor adjustment applies): **2.30**.
Levels: L1 = 1 question (Q2), L2 = 12 questions, L3 = 7 questions (Q4, Q5, Q12, Q13, Q17, Q18, Q20). No L0, L4, L5. Confidence Medium (JEE Main-style questions rated on the Advanced scale).

## Solutions corrected / written (solution_source)
- Q2 (302) corrected: PDF says 3125 = 2124 + 1 (should be 3124 = 11·284) and writes [11k×19+1]; fixed.
- Q5 (305) corrected: base printed as (√4 − 6/x^{3/2}) (should be √x); coefficient written 4C1(−6)^3 (term is k=3, 4C3(−6)^3, same value); "by observation" n=4 now justified by excluding n=8, 12.
- Q7 (307) corrected: PDF lists "n = 1, 7, 13, 20, …, 97" (20 should be 19), gives no reason for period 6 and does not exclude n=1, 7 (< 10) before counting 15.
- Q10 (310) corrected: typo "3z_6²" for 3z_0²; the equilateral-triangle condition Σz_i² = Σz_iz_j was used without being stated.
- Q16 (316) corrected: PDF says β = 2 for 5 − 2√2; β = −2 (α²+β² = 29 unchanged).
- All others: pdf (reproduced; verified). Small bridging lines added without changing the PDF's method: Q3 (why odd powers of 21 cancel), Q6 (103 = 6·16+7 step), Q9 (check z ≠ 2−i), Q12 (z = i is the only S1 element), Q19 (the factor 2 in |2cos2θ|=1), Q8 (expanding k|z|²). No question was "written".

## Answer key
All 20 PDF answers verified (exact integer arithmetic / numerical checks with numpy) and agree with the key. No key errors found.

## Alternates and Useful Results
- Alternates given for 17 of 20 questions (Q1–Q3, Q5, Q6, Q8–Q13, Q15–Q20).
- **No alternate for Q4 (304):** the m-equation (2·C(m,2)=C(m,1)+C(m,3)) and the quadratic in 3^x have no different method; any other route is the same algebra reworded.
- **No alternate for Q7 (307):** the only route is the period-6 cycle of 3^n mod 7 and counting the progression.
- **No alternate for Q14 (314):** solving the three linear equations for a, b and reducing with ω³ = 1 is the only natural route.
- Useful Result / Pattern slides given for all 20 questions.
- Weaker alternates (partly the same core idea / only the final step differs): Q1 (x = t³ substitution), Q5 (ratio via 4C3 = 4C1 for the last step only), Q9 (reducing z² with the equation itself), Q15 (tan θ form + odd-square-sum formula) – flagged for review.

## make_ppt.py warnings
None. The script printed only "766 converted to native PowerPoint equations" (no "could not convert" messages). build_report.py ran without warnings.

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step in this environment).
- Concepts and chapters self-assigned; chapter names used in ratings: "Binomial Theorem" (Q1–7), "Complex Numbers" (Q8–20); the nearest anchors cited are only indicative.
- Q12: "purely real/imaginary" taken to allow the value 0 (z = i in S1, z = 1 in S2); the verdicts do not depend on this.
- Q4: the sixth-term condition read as "T6 with respect to increasing powers of 3^{x-2}", as in the PDF; m = 2 rejected because a sixth term needs m ≥ 5.
