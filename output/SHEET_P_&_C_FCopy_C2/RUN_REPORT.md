# Run report - SHEET_P_&_C_FCopy_C2 (Permutation & Combination, Exercise C-II)

Files: `SHEET_P_&_C_FCopy_C2_content.json`, `_Analysis.pptx` (155 slides, 28 questions), `_ratings.json`, `_difficulty.xlsx`.

## Difficulty
- Marks-weighted difficulty index: **1.96** (102 marks). All levels are integers; no equivalence-relation or multi-correct adjustment applied (no such questions).
- Level 1: 8 questions (Q4, Q13, Q14, Q15, Q18, Q22, Q23, Q25); Level 2: 13 (Q2, Q5, Q7-Q12, Q17, Q19, Q24, Q26, Q27); Level 3: 7 (Q1, Q3, Q6, Q16, Q20, Q21, Q28); Levels 0, 4, 5: none.
- This is a chapter sheet, not an Advanced-pattern paper, so it sits below the official range (2.6-3.2). Q16 (ambiguous statement) is rated with Low confidence.

## Blueprint / marks
- No blueprint was available: **Concepts self-assigned (no blueprint) - please review.**
- No marks are printed in the paper. Assumed JEE Advanced defaults: Q1-Q18 (find / fill-in-the-blank, numerical or expression answers) = 4 marks, typed "Numerical"; Q19-Q27 (paragraph single-correct) = 3 marks; Q28 (matching) = 3 marks. Stated in the section dividers.
- Numbering: the paper's questions 1-28 were used as printed (Q28 is one matching question with parts A-E).

## Solutions with source corrected or written
- Q2 (corrected): PDF subtracts "3C2*2^n + 3" and ends with "3^n - 3*2^n - 3". Single-digit numbers sit inside the pair counts, so the correct number missing a digit is 3*2^n - 3; result 3^n - 3*2^n + 3 (the printed answer was right).
- Q5 (corrected): PDF solves only part (i); the working for part (ii) (answer 1260) was missing and has been added.
- Q13 (corrected): PDF working stops at (x-1)^x and does not subtract the all-rest state, contradicting its own answer (x-1)^x - 1.
- Q16 (corrected): PDF presents "3! for each subject" and then divides by 3!3!3!; reasoning rewritten (order inside a subject is fixed by the places, so choose the scholarship set per subject). Answer 1680 unchanged.
- Q19 (corrected, wording only): PDF says "4 different groups" but the number 16!/(4!)^5 is for identical groups.
- Everything else reproduced from the PDF (`pdf`) after independent checks.

## Answer key
- All 28 answers were checked by brute-force computation (Q1, Q3, Q5, Q6-Q12, Q14-Q17, Q19-Q21, Q23-Q25, Q28 parts). No answer in the key is wrong. Q7: the key gives expressions; numeric values 6062, 2702, 1008 are shown.

## Alternates and results
- Alternate solutions given for 24 of 28 questions: Q1-Q9, Q11, Q14-Q24, Q28 (Q28: parts A and E only). Q5's alternate covers part (i) only. Q2's alternate was checked numerically for n = 3..10; the others were verified by hand and by computer count.
- **No alternate** for Q10 (the PDF's method is already the divisor count; the only other route is the same divisor-counting shortcut), Q12 (the digit-by-digit casework is the natural method; alternatives are rewordings), Q13 (single multiplication-principle step), Q25, Q26, Q27 (one-step derangement results; no second genuinely different route).
- Every question 1-28 has `useful_results`.

## make_ppt.py notes
- Q4, Q25, Q26, Q27: "only 3 solution bullets" - the PDF's own working is that short; harmless, left as is.
- Q28: "very long question - font reduced to 20 pt" - five-part matching list; harmless.
- No "could not convert" warnings; 681 equations converted.

## Skipped / assumed
- Rendering and visual check of the deck was not possible (no soffice/thumbnail step in this environment); slide fit judged from script notes only.
- Levels are my judgement against the calibrated anchors (few P&C chapter-sheet anchors exist).
