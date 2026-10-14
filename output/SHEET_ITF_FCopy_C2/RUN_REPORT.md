# Run report - SHEET_ITF_FCopy_C2

Paper: Exercise C-II (Inverse Trigonometric Functions), 19 questions (Q1-19, numbered continuously as in the PDF; Q8, Q12, Q13 and the matching questions have several parts but are one question each). The PDF has answers and solutions. Date of run: 2026-10-14.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper; stated in the section dividers): Subjective and Numerical questions 4 marks each (Q1-13, total 52); Paragraph single-correct 3 marks each (Q14-16, total 9); Matching 3 marks each (Q17-19, total 9). Total 70. Types were taken from the paper: Q2, 5, 6, 7, 10 numerical (single numerical answer); Q1, 3, 4, 8, 9, 11, 12, 13 subjective ("Subjective Type" label, not in the standard table); Q14-16 one paragraph; Q17-19 match-the-column.

## Difficulty
Marks-weighted difficulty index (adjusted): **2.27** (below the official JEE Advanced range 2.6-3.2; a chapter sheet, no expected distribution).
Level counts: L0 = 0, L1 = 3 (Q3, 6, 14), L2 = 8 (Q1, 2, 5, 7, 12, 15, 16, 17), L3 = 8 (Q4, 8, 9, 10, 11, 13, 18, 19), L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied. Low-confidence rating: Q11 (anchors for ITF top out at L3; the principal-range bound on K might merit 4). Medium-confidence: most others. The workbook was not recalculated (no recalc.py here); the index above was computed by hand from the ratings.

## Solutions whose solution_source is "corrected" (5)
- Q1: PDF has a typo (sqrt(1-6x) instead of sqrt(1-6x^2)) and rejects x = -1/3 without a reason; typo fixed and the reason added (for x<0 the sum exceeds pi/2). Answer x = 1/3 unchanged.
- Q3: PDF replaces cot^-1 x by sin^-1(1/sqrt(1+x^2)), true only for x >= 0; rewritten with sin(cot^-1 x) = 1/sqrt(1+x^2) for all x. Result unchanged.
- Q4: Case II (pi/4 < A < pi/2) is only the last two lines in the PDF; the derivation (no pi added, same simplification) was added. Result unchanged.
- Q11: the PDF jumps to K = 2 without showing why no other integer works (D >= 0 only gives K >= 2); the bound p + q^2 <= pi + pi^2/4 < 3pi^2/4 for K >= 3 was added. Answer unchanged.
- Q19: Part (B) Case II in the PDF reads cos^-1(-x+1-x+2) = cos^-1(3-2x); the correct argument is (x-1)-(2-x) = 2x-3. The match (B -> Q) is unchanged.

## Solutions with solution_source "written" (2)
- Q2: the PDF has only a sketch and the answer 3; a full argument (sin t < t on each branch) was written. Answer 3 confirmed.
- Q10: the PDF stops after finding the roots (solution cut off) and prints only the answer 56; a complete solution was written (surds cancel to 14(alpha+beta) = 56) and checked numerically.
Small additions inside "pdf" solutions: Q5 (justification of cos^-1(x/sqrt(1+x^2)) = cot^-1 x), Q8 (typo "x in [-3,3]" in part (iii) is really "y"; written with y), Q13(a) (why sec^-1 x > 4 gives nothing), Q17(B) (explicit counterexample for "neither"), Q18 (justifications for (B) not aperiodic and for bounded domains).

## Answer key / question problems
- No printed answer disagrees with the correct answer. Every final answer was re-derived and checked numerically (Q1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 18, 19).
- Q13(b): the answer key gives nothing for part (b) (a proof); the proof is in the solution.
- Q13(b) is phrased "for all x, y in R"; it is only meaningful where tan x and tan y are defined, which is how it was treated.
- Q15: options (A) and (C) are printed identically (both 1/(1-x)) in the PDF; the key (B) x/(1-x) is correct. Kept as printed.
- Q18(B): the constant function 0 is periodic, so "aperiodic" (T) is not matched, consistent with the key (QRS).

## Alternate solutions
Alternates (a genuinely different technique) were written for 17 of 19 questions: Q1-9, Q11-15 and Q17-19. Each was checked against the answer by hand or numerically.
Questions with NO alternate (2), and why:
- Q10: every route (half-angle in cosine form, cot(theta/2) = (1+cos)/sin, tan(theta/2) quadratic) leads to the same rationalisation with c^2 - alpha^2 = beta^2; no genuinely different method found.
- Q16: the only route is cancelling the common GP factor to get x = x^2 + x^3; checking the options is the same equation reworded.
Borderline alternates (different viewpoint, not different arithmetic): Q3 (right-triangle construction versus inverse identities) and Q14/Q15 (common-factor / separate-series views); please judge.

## Useful Result / Pattern
Every question (1-19) has useful_results (3-4 general statements with conditions; each formula spot-checked numerically).

## make_ppt.py warnings
None. "923 converted to native PowerPoint equations", 132 slides, no "could not convert" notes. No rendering / thumbnail check was done (no soffice here), so the deck was built but not viewed.

## Skipped / assumed / guessed
- Levels are my calibrated estimates (ITF anchors are few: 2021-P1-Q15, 2023-P1-Q8, 2023-P2-Q3, 2024-P2-Q1, 2025-P2-Q3, 2026-P1-Q4).
- Concepts are self-assigned; Hindi text in the PDF was ignored.
- Q2 and Q18 graphs, and the sketches in Q12/Q13/Q18, are described in words only (no figures drawn).
- Paragraph for Q14-16 is repeated on each question slide as printed.
