# Run report - SHEET_SEQUENCE_&_PROGRESSION_FCopy_JM (Sequence & Progression, Exercise J-M: JEE Main PYQs, 77 questions)

Files: `_content.json`, `_Analysis.pptx` (487 slides, 77 questions), `_ratings.json`, `_difficulty.xlsx`, `per_question_notes.md` (one line per question: key status, source, alternate remarks).

## Difficulty
- Marks-weighted difficulty index: **1.95** (308 marks, every question 4 marks, so equals the mean level; no equivalence-relation or multi-concept adjustment applies).
- Level 1: 18 (Q2, 3, 16, 17, 23, 26, 30, 32, 37, 44, 45, 48, 56, 65, 66, 67, 70, 75); Level 2: 45; Level 3: 14 (Q6, 9, 15, 20, 40, 42, 50, 51, 57, 59, 72, 73, 74, 77); Levels 0, 4, 5: none.
- JEE Main sheet, so well below the Advanced range (2.6-3.2); reported as it is. Confidence is Medium on several items (few close Advanced anchors for routine series questions).

## Blueprint / marks
- No blueprint: **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. Assumed 4 for single-correct and 4 for numerical (JEE Advanced defaults per the task); stated in the section dividers.

## Solutions corrected or written (source = corrected; none written from scratch)
- Q9: the PDF's two intermediate inequalities have the wrong direction for m>1 (errors cancel; answer 12 right); fixed, m=1 excluded.
- Q15: stem says only "a1 = b1" (no value); answer 461 holds only for a1=b1=1 (general: 461+509(c-1)). Stem completed with "=1" (the PDF's own working assumes it); mislabelled steps fixed, skipped a9=37, b10=130 added.
- Q22: the PDF's displayed sets are wrong (S2 ends at 239) and have no congruence argument; final set {47,107,167} and sum 321 right; derivation rewritten.
- Q24: PDF drops the factor 1012 in "1012 m^2 n =" and does not exclude (m,n)=(1,2023); fixed, answer unchanged.
- Q28: no numerical error; PDF jumps from S_n to 223, so S_29=13920 and S_9=540 supplied.
- Q39: sign error after the subtraction step; final 2175 right.
- Q43: typo "9(n-1).15" should be 9+(n-1)15.
- Q67: perimeter labels shifted. Q68: "8m = 4.24.25/2 = 150" should be 1200. Q71: 9717/9746 should be 9747. Q72: "13d" should be 3d and d=-3 was not rejected. Q74: typos "3600-t", "g=60". Q75: 103x104/2 = 5356, not 5336. Q77: index typos (2012/2022/2011, alpha+10/2). All answers unaffected.
- Small gap-fills kept as source pdf: Q1, Q5, Q6, Q10, Q11, Q17, Q20, Q25, Q27, Q51, Q53, Q56, Q57, Q59, Q65 (see per_question_notes.md).

## Answer key
- All keys verified by computation. No numerical answer is wrong. Remarks: Q61 key printed as "A" although the question has no options - answer recorded as 1 (the PDF working gives 1). Q15's 461 needs a1=b1=1. Q51: English options used (D = both true); the Hindi version orders the options differently and its statement (I) has a typo ("a and b" for "a and c"). Q74: "a(b)^b + b" also fits b=1 literally; the intended b=61 (a=3599, answer 3660) used. Q34 option (D) read as 2(A1+A2)G1^2G3^2 from the text layer; the page image was unclear on the exponent.

## Alternates and results
- Alternate solutions given for 76 of 77 questions (Q1-Q64, Q66-Q77), each verified numerically/symbolically. Every question has useful_results (2-5 bullets, formulas checked on cases).
- **No alternate: Q65** - both sums telescope in one natural way; any other route is the same telescoping reworded.
- Alternates close to the main method (same core step, different packaging; flagged in per_question_notes.md): Q1, 3, 7, 10, 11, 12, 14, 18, 20, 26, 28, 30, 31, 33, 38, 41, 43, 44, 45, 46, 47, 49, 51, 53, 55, 56, 57 (second alternate), 59 (part), 62, 64, 66, 67, 68, 70, 75. Q50 and Q34 use option-based elimination/special cases.
- Q44 has only 5 solution bullets (one-line question).

## make_ppt.py notes
- No warnings. 3166 equations converted to native equations; no "could not convert" messages.

## Skipped / assumed
- No visual rendering of the deck (no soffice); fit judged from script output only.
- Maths text from pdftotext was garbled, so each question was read from page images by the workers (seven parallel workers, one block of 11 questions each); the merged JSON was validated and built once.
- Hindi duplicates ignored.
