# Run report - SHEET_QUADRATIC_EQUATION_FCopy_JA (Quadratic Equation, Exercise J-A: JEE Advanced PYQs)

Files: `_content.json`, `_Analysis.pptx` (64 slides, 9 questions), `_ratings.json`, `_difficulty.xlsx`.

## Difficulty
- Marks-weighted difficulty index: **2.74** (31 marks; adjusted = unadjusted, no equivalence-relation question; the multi-correct floor of 2.5 did not change any level).
- Level 1: 1 (Q5); Level 2: 3 (Q1, Q6, Q9); Level 3: 3 (Q2, Q3, Q4); Level 4: 3 (Q7, Q8 ... see below); Levels 0 and 5: none.
  Exact: L1 = Q5; L2 = Q1, Q6, Q9; L3 = Q2, Q3, Q4; L4 = Q7, Q8. (1 + 3 + 3 + 2 = 9 questions.)
- Q7, Q8, Q9 are JEE Advanced 2024 questions with the user's own ratings in the anchor bank (4, 4, 2); I used those levels. Q2 and Q3 rated Medium confidence (no close anchor).

## Blueprint / marks
- No blueprint: **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. JEE Advanced defaults assumed: Q1, Q2, Q6 single-correct = 3; Q3, Q7 one-or-more-correct = 4; Q4, Q5 paragraph single-correct = 3; Q8, Q9 numerical = 4. Stated in the section dividers.

## Solutions with source corrected or written
- Q6 (corrected): the PDF's expansion line omits the term -bc^2 (eight terms needed, seven written). Next line and answer are right; inserted -bc^2. Answer 16000 unchanged.
- All other questions (Q1-Q5, Q7-Q9) reproduced from the PDF after independent checks (sympy / numerical). Small added clarifications (not errors): Q2 spells out why p(x)=ax^2+c; Q4 states why the recurrence holds and which part is rational/sqrt5; Q7(C) uses the determinant ac-b^2 where the PDF writes a/b != b/c (equivalent, and valid also when b=0).

## Answer key
- All 9 keys verified (Q1 resultant b(b^2+3); Q3 interval test; Q4 p=q=4; Q5 Lucas numbers; Q6 exact 16000; Q7 by definiteness; Q8 root sum 20; Q9 logs numerically). No answer key is wrong.

## Alternates and results
- Alternate solutions given for Q1, Q2, Q3, Q4, Q5, Q7, Q8, Q9 (8 of 9), each verified numerically or symbolically.
- Closeness note: Q1's alternate (subtract, substitute) is a standard second method rather than a radically new idea.
- **No alternate**: Q6 - every route evaluates the same symmetric sum from a+b, ab, c+d, cd; the only variation (closed form in S and P of both pairs, giving 16000 + 0) is the same expansion reorganised, so it is given as a useful result instead.
- Every question 1-9 has `useful_results` (formulas checked on a numerical case: common-root condition, Lucas numbers, closed form for Q6 on random integers, etc.).

## make_ppt.py notes
- No warnings. 389 equations converted to native equations; no "could not convert" messages.

## Skipped / assumed
- No visual rendering of the deck (no soffice here); fit judged from script output only.
- Maths text was garbled by pdftotext, so pages were read from page images.
- Q4 and Q5 share one paragraph; it is repeated on both question slides.
- Q1 answer: b = 0 is also a mathematical solution but is not among the options.
