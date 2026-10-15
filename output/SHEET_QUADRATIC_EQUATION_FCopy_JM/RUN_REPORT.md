# Run report - SHEET_QUADRATIC_EQUATION_FCopy_JM (Quadratic Equation, Exercise J-M: JEE Main PYQs, 2023-2024)

Files: `_content.json`, `_Analysis.pptx` (149 slides, 24 questions), `_ratings.json`, `_difficulty.xlsx`.

## Difficulty
- Marks-weighted difficulty index: **1.90** (79 marks; adjusted = unadjusted, no equivalence-relation question and no multi-correct question, so neither adjustment applied). Well below the JEE Advanced range (2.6-3.2), as expected for JEE Main questions.
- Level 1: 5 (Q1, Q6, Q15, Q16, Q17); Level 2: 17 (Q2-Q5, Q7-Q11, Q13, Q14, Q19-Q24); Level 3: 2 (Q12, Q18); Levels 0, 4, 5: none.
- Low confidence: Q12 and Q18 (no close anchor; Q12 also has a wrong printed key). Medium for most others; there is no exact anchor for JEE Main quadratic PYQs, nearest anchors are 2021-P1-Q17, 2024-P1-Q9, 2026-P1-Q13.

## Blueprint / marks
- No blueprint: **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. JEE Advanced defaults assumed: single-correct questions (Q1-6, Q10-12, Q15-17, Q19-23) = 3 marks each; numerical-answer questions (Q7-9, Q13, Q14, Q18, Q24) = 4 marks each. Stated in the section dividers. The paper's Hindi duplicate of each question was ignored (English only).

## Solutions with source corrected or written
- Q3 (corrected): PDF divides by sqrt(x-3) and treats only x>3; the other domain branch x<=-3 was omitted. Added it (no root there). Answer 1 unchanged.
- Q12 (written): PDF stops after alpha = sqrt3 e^{3 pi i/4} and gives no working; solution written. **The printed key (D) 9 is wrong; correct answer is 81, option (B)** (checked numerically to 12 digits).
- Q13 (corrected): PDF writes bounds 5 +- 3 sqrt2 (should be 5 +- 2 sqrt3) and lists the final set as {2,3,4,5,6,8} (keeps 5, drops 7); correct set {2,3,4,6,7,8}. Count 6 unchanged.
- Q16 (written): PDF working is cut off after the single line "a<0"; completed (denominator positive, S empty, answer 0). Answer unchanged.
- Q18 (corrected): PDF writes x^2-7x+lambda=0 (typo for 70x) and jumps to alpha=5 without showing why alpha=1..4 fail; fixed and added the check. Answer 60 unchanged.
- Q19 (corrected): PDF line 9(y+1)^2-64y(y-1)^2>=0 has a stray factor y and wrong power; correct is 9(y+1)^2-64(y-1)^2>=0 (which its next line uses). Answer unchanged.
- Q22 (corrected): last line of PDF reads x^2-195x+95x+9506=0 (stray +95x); correct x^2-195x+9506=0. Answer (C) unchanged.
- Q24 (corrected): PDF gives alpha+beta = sqrt2; correct sum is -sqrt2 (not used later). Answer 4 unchanged.
- All other questions (Q1, Q2, Q4-Q11, Q14, Q15, Q17, Q20, Q21, Q23) reproduced from the PDF after independent checks (sympy / numerical). Small clarifications were added without changing content (e.g. Q8 shows the discriminant of the quadratic in a; Q5 shows the discriminant expansion and why x=2,6 cause no loss; Q21 notes that a_2024 is not zero and the roots may be complex).

## Answer key
- Q12: PDF key (D) 9 is wrong; correct (B) 81. All other 23 keys verified (Q1 0; Q2 (A); Q3 1; Q4 (C); Q5 (C) with range checked numerically; Q6 1; Q7 9; Q8 45; Q9 13; Q10 9+sqrt3; Q11 19; Q13 6; Q14 51; Q15 (C); Q16 0; Q17 2; Q18 60; Q19 201; Q20 (B); Q21 -1/4; Q22 (C); Q23 (C); Q24 4).

## Alternates and results
- Alternate solutions given for 21 of 24 questions (all except Q7, Q15, Q21), each checked numerically or symbolically.
- **No alternate**:
  - Q7 - every route solves x^2=t for the three pairs +-sqrt(t_i) and multiplies each pair (product -t_i): the same computation as the main solution.
  - Q15 - the recurrence follows in one line from alpha^2=alpha+1; other routes (matrix form, checking options on small cases) are the same recurrence rewritten.
  - Q21 - the ratio equals alpha+beta by a one-line identity from alpha*beta=1 (this is Newton's recurrence itself); the cosine form only applies when |alpha+beta|<2 and is the same identity.
- Weaker alternates (kept, flagged for review): Q16 (limit at infinity versus leading-coefficient test) and Q20 (derivative reading of 2a+b) are short second views rather than radically new methods; Q23's alternate reduces a polynomial modulo the quadratic, which is a different technique from the main substitution chain.
- Every question 1-24 has `useful_results` (formulas checked on a numerical case: common-root condition, power-sum formulas, S4/S5 identities, a_{n+4}=-9a_n, 55y^2-146y+55, etc.).

## make_ppt.py notes
- No warnings. 973 equations converted to native equations; no "could not convert" messages.

## Skipped / assumed
- No visual rendering of the deck (no soffice here); fit judged from script output only.
- Maths text was garbled by pdftotext, so pages were read from page images (80 dpi).
- Q7: ordering |alpha_1|>=...>=|alpha_7| is descending (as printed on the page image; the text layer lost the symbols).
- Concepts self-assigned; each question has one combined concept phrase (all concepts are in the same chapter).
