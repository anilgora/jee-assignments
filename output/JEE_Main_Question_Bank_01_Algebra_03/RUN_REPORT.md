# Run report: JEE_Main_Question_Bank_01_Algebra_03

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_03.pdf` (printed Q41-Q60, renumbered 1-20; all Sequence and Series).
Files: `_content.json`, `_Analysis.pptx` (121 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** for the single-correct questions (Q1-8, Q10-20) and the numerical question (Q9), JEE Advanced defaults; stated on the section dividers.
This is a JEE Main-style bank rated on the Advanced scale, so the index is low.

## Difficulty
Marks-weighted difficulty index: **1.75** (no equivalence-relation or multi-correct adjustments).
Level 1: 7 questions (Q2, 3, 5, 6, 7, 12, 14). Level 2: 11 questions (Q1, 4, 8, 9, 10, 11, 13, 15, 16, 19, 20). Level 3: 2 questions (Q17, Q18). Levels 0, 4, 5: none.

## Solutions: corrected / written
No question was `written` (the PDF has a solution for all 20). Corrected (answers unchanged in every case):
- **Q14 (printed 54, corrected):** PDF line "a1 = -39 x 4 = -156" mislabels 39*d2 as a1 (a1 = -3 is right); relabelled, and the missing step b1+99d1 = a1+69d2 written out.
- **Q15 (printed 55, corrected):** PDF stops at ">= 2 sqrt(a)" without showing equality is attained; added the equality step (a^x = 1/2; a = 1 trivial).
- **Q16 (printed 56, corrected):** PDF prints the factor as 5 sqrt2 - (4 sqrt2 + 16)/2; "16" is a misprint for k.
- **Q17 (printed 57, corrected):** PDF eq. (2) repeats "3 log y / log z" as its second term (should be 3 log x / log y) and eq. (3) has "log 2" for "log z"; fixed.
Questions 1-13, 18-20 are reproduced from the PDF (`pdf`); in Q8 the omitted algebra n^2 - 101n + 2440 = 0 was filled in.

## Answer key
All 20 keys agree with my own computation (brute-force/symbolic checks of Q8, 10, 11, 16, 19, 20 and hand checks of the rest). No key looks wrong.

## Alternates and results
All 20 questions have one alternate solution (a different technique each time, e.g. midpoint/middle-term shortcuts, double-sum factorisation for Q4, Cauchy-Schwarz for Q13, column splitting for Q16, mod-23 inverse for Q19) and all 20 have useful_results. Every alternate reaches the same answer; a few are option-testing or substitution methods (Q3, Q8, Q11), which is a different strategy but less "proof-like". No question lacks an alternate. The alternates for Q9 and Q12 are modest rewordings of viewpoint (linear-interpolation view; eliminate a by a ratio of sums) because the problems are single-step; flagging that they are the weakest.

## make_ppt.py warnings
None printed (731 equations converted natively; no "could not convert" notes).

## Skipped / assumed
No rendering/thumbnail check was possible (no soffice step). Concepts and marks are assumed as above. Level ratings were made by judgement against the anchors, not by running the full anchor comparison for each question.
