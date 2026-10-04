# Run report: JEE_Main_Question_Bank_01_ Algebra_01

Paper: `papers/JEE_Main_Question_Bank_01_ Algebra_01.pdf` (20 questions, all single-correct, chapter: Quadratic Equation).
Files: `_content.json`, `_Analysis.pptx` (126 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed: **4 per question** (the paper prints no marks; JEE Advanced default for single-correct). Stated on the section divider.
Note: this is a JEE Main-style bank, rated on the Advanced scale as instructed, so the index is low.

## Difficulty
Marks-weighted difficulty index: **1.70** (no equivalence-relation or multi-correct adjustments apply).
Level 1: 8 questions (Q3, 6, 8, 10, 11, 12, 13, 17). Level 2: 10 questions (Q1, 2, 4, 5, 7, 9, 14, 16, 18, 19). Level 3: 2 questions (Q15, Q20). Levels 0, 4, 5: none.

## Solutions: corrected / written
- **Q6 (corrected):** PDF stops at "Now check option"; the recurrence and p1..p5 are right, the check of options (A)-(D) was added.
- **Q8 (corrected):** PDF wrote f(2)=k(-1)(-2-alpha); the factor is (2-alpha). Following line k(5alpha+2)=0 and the answer are right.
- **Q15 (corrected):** PDF divides by sqrt(x-3) as if x>3 and never treats the domain branch x<=-3. Added the domain step and that case; it gives only x=7/6 again (rejected). Answer unchanged (1).
- **Q20 (corrected / completed):** PDF stops after the polar form and its key says (D) 9. Completed computation gives **81**, option (B).
- Other 16 questions: `pdf` (working correct). Minor typos reproduced correctly without a flag: Q12 PDF prints "B" for 8 in the quadratic formula; Q18 PDF did not show the rejection of 5-sqrt3 and x=2 (added).

## Answer key problems
- **Q20: the PDF key (D) 9 is wrong; correct answer is 81 = (B).** Verified numerically (ratio = 81.0000) and by two independent methods.
- All other keys agree with my computation (Q1 = 11 checked by brute force; Q15 root x=3 only, checked on a fine grid; Q2, Q9, Q12, Q16, Q18 checked numerically).

## Alternates and useful results
- Alternates: all 20 questions have one alternate; each was checked for the same answer. Several are formula or shortcut variants rather than wholly new ideas (e.g. Q2 ratio-of-roots formula, Q12 bounds argument, Q4 test value, Q10 explicit roots); the reasoning differs from the main solution, but these are the weakest "different methods".
- Questions with NO alternate: none.
- useful_results: given for all 20 questions.

## make_ppt.py warnings
None printed. Output: "824 converted to native PowerPoint equations", 126 slides, no "could not convert" notes.

## Skipped / assumed
- No rendering or visual check of the deck (no soffice here); text lengths were left to the builder's own checks (no warnings).
- Q1-Q20 levels are my own judgement against the anchors; confidence is Medium for most (see ratings JSON).
- Q19/Q20 list two concepts from different chapters (cubic/complex numbers); others a single concept.
