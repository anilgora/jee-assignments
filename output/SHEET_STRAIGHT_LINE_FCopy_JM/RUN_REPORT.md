# Run report - SHEET_STRAIGHT_LINE_FCopy_JM (Exercise J-M, 44 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every single-correct question (Q1-6, 9-14, 18-27, 32-41) and 4 marks for every numerical/integer question (Q7-8, 15-17, 28-31, 42-44). This is stated in the section dividers. (The questions are JEE Main questions, which actually carry +4/-1 and +4/0; the deck only uses the 4.)

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.05** (no equivalence-relation or multi-correct adjustments apply).
- Levels: Level 1 = 9 questions, Level 2 = 24, Level 3 = 11, Levels 0, 4, 5 = none. This is a JEE Main practice sheet, so there is no expected Advanced spread.
- Lower-confidence ratings (Medium): Q4, Q7, Q8, Q16, Q17, Q21, Q25, Q29, Q31, Q32, Q33, Q41, Q42, Q43.
- Workbook: `SHEET_STRAIGHT_LINE_FCopy_JM_difficulty.xlsx` (recalc.py not available here, so cached formula values are absent until opened in Excel).

## Solutions that were corrected (solution_source = corrected)
- **Q16** - the PDF takes "the image of Q about l2", but Q lies on l2; it must be the image about the bisector l1 (the numbers used are for l1). Wording fixed; answer 348 unchanged.
- **Q25** - the PDF writes h = 4/3; from 2h = -8/3, h = -4/3 (its last line already uses -4/3). Answer 14 unchanged.
- **Q32** - the PDF's figure and working use B(2,2), C(3,1) and AB as x - y - 4 = 0; with the given B(-2,2), C(3,-1), AB is x - y + 4 = 0. It also never fixes the inward sign nor compares distances. Redone; answer (A) unchanged.
- **Q33** - the PDF solves the 45-degree condition only for m = 1/7 and then writes OP as y = 7x; the other root is m = -7, OP: y = -7x (its later P(-12/25, 84/25) uses -7x). Answer 46 unchanged.
- **Q34** - the PDF takes the wrong modulus branch (2h - 3k = 15, a = 2, b = -3, giving 5a + 2b = 4), which contradicts its own key (D). "Above AB" gives 3k - 2h - 5 = 20, so a = -6/5, b = 9/5 and 5a + 2b = -12/5 (D).
- **Q43** - the PDF gives the altitude from C slope 2/3 (y = 2x/3); it must be 3/2 (y = 3x/2, which its next lines actually use). Answer 16 unchanged.

No question needed `written` (the PDF has a solution for all 44).

## Gaps in the PDF filled while keeping solution_source = pdf
- Q10: PDF jumps to the circumcentre; added the third vertex (9,11) and the right-angle reason. Q15: added vertex B (-1,7) used for BD. Q17: PDF asserts the maximum is at t = 4; added the convexity/endpoint comparison. Q24: added the step matching y = (2-sqrt3)(x-9) to option (C). Q42: added that the angle at C is also pi/6. Q7 and Q21: the PDF's notation is garbled in the text layer only; the steps are consistent.

## Answer key
No answer key looks wrong. Q34's key (D) is right although the PDF's working does not reach it (see above). All 44 final answers were checked by computation (sympy / exact arithmetic / brute-force count for Q8, numerical scan for Q17).

## Text-layer problems in the PDF
The extracted text lost Greek letters and several minus signs (for example "a^2 - b^2" in Q4, "(alpha-beta)^2" in Q10). The question stems and the options were read from page images wherever symbols were unclear, and every answer was confirmed against the key.

## Alternates and results
- Alternate solutions (a different technique) were written and checked for **42 of 44** questions (all except Q11 and Q13).
- **No alternate:** Q11 - the area condition gives alpha*beta = 4 and the midpoint relation hk = 1 directly; the only other routes are the same two lines of algebra reworded. Q13 - it is pure intersection-and-averaging of three vertices with no second technique that is not the same computation.
- Every one of the 44 questions has useful_results (3 bullets each).

## make_ppt.py output
No warnings. 1608 equations converted to native PowerPoint equations; 276 slides, 44 questions. Nothing stayed as LaTeX text. No rendering check was possible (no PowerPoint/LibreOffice step in this environment).

## Skipped / assumed / guessed
- Concepts and chapter names were self-assigned from each question's content (all Straight Lines; Q1 also uses the parabola tangent).
- Sections were built from runs of equal question type (8 dividers).
- recalc.py and slide rendering were skipped (not available).
