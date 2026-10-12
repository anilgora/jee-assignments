# Run report - JEE_Main_Question_Bank_02_Differential_Calculus_02_02

Paper: `papers/JEE_Main_Question_Bank_02_Differential_Calculus_02_02.pdf` (18 pages, Matrix JEE Academy; 18 single-correct + 2 integer-type questions with printed solutions). Printed numbers are 21-40; the deck numbers them 1-20 (deck Q = printed Q - 20).
Files: `_Analysis.pptx` (129 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint was used.
- No marks printed. Assumed 4 marks each for single correct (Q1-18) and integer type (Q19-20), no negative marking (stated in the section dividers). Total 80 marks.

## Difficulty
- **Marks-weighted difficulty index: 2.10** (adjusted = unadjusted; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 3 (Q2, Q3, Q15); Level 2: 12 (Q1, Q4, Q8, Q9, Q10, Q12, Q13, Q14, Q17, Q18, Q19, Q20); Level 3: 5 (Q5, Q6, Q7, Q11, Q16); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q6 (printed 26): the PDF solves f(x)=(2 - sin(1/x))x (x>0), a different function from the printed f(x)=(2 sin(1/x))|x| (the question looks like a misprint of (2 - sin(1/x))|x|). I solved the printed function; both are non-monotonic on each side, so (C) stands.
- Q7 (printed 27): the PDF's middle step has the denominator as 1/2 cos x + sqrt3/2 sin x (sign slip; it is minus). Also the PDF does not say the key (B) x - pi/6 holds only on (0, pi/6); on (pi/6, pi/2) the derivative is x - 7pi/6 (not an option). Both stated.
- Q11 (printed 31): the PDF uses sin^-1 f = pi - 2 tan^-1 x for x = -sqrt3 too, but for x < -1 it is -pi - 2 tan^-1 x. The derivative is the same, so the working continues to y = -tan^-1 x + c; the answer 5pi/6 assumes one constant on both pieces of the disconnected domain |x|>1.
- Q19 (printed 39): the PDF's f'(x) omits the factor cos x (positive on (0, pi/2), so the answer 9 is unchanged); I added that the range is [9, infinity).

## Solutions whose source is written
- None. Small additions kept as source `pdf`: Q5 (the PDF's printed derivative has typos such as 5x for 5x^2 and a missing factor, but its numbers and final 3pi^2/16 are right - I wrote the derivative correctly), Q9 (PDF only gave f'; I added the derivative steps and the other options), Q10 (added verdicts on options B-D), Q36->Q16 (PDF calls the auxiliary function g, then h - written as h).

## Answer key
- **Q7 (printed 27): key (B) is valid only for x in (0, pi/6)**; the question says x in (0, pi/2). On (pi/6, pi/2) dy/dx = x - 7pi/6, which is not an option. Answer shown as "(B) x - pi/6 (valid on (0, pi/6))".
- **Q11 (printed 31): strictly under-determined.** y(sqrt3)=pi/6 fixes the constant only for x>1; y(-sqrt3) needs an assumption. Key (A) 5pi/6 follows from one formula y = -tan^-1 x + pi/2 on |x|>1; (a different single-constant reading, y = 1/2 sin^-1 f + c, would give -pi/6, option D). I kept the key (A).
- Q6 (printed 26): key (C) right for the printed function (and for the one solved in the PDF).
- All other keys checked and right, several numerically/symbolically: Q4 limit 1/6 (sympy), Q5 y(1) = -1/8 and y'(1) = 3pi^2/16 (sympy), Q9 derivative identity (sympy), Q11 d/dx sin^-1 f = -2/(1+x^2) for both signs of x, Q7 derivative (finite differences, both branches), Q19 minimum 9.

## Alternates
- Given for 18 questions: Q1-Q8, Q10-Q16, Q18-Q20.
- **No alternate:** Q9 (printed 29) - the only route is the sign analysis of f' = (2x-1)(x - sin x); no second genuinely different method. Q17 (printed 37) - monotonic sets of a piecewise function are found only by the piece-by-piece sign analysis; no second method.
- Weaker alternates (flagging for review): Q3 (logarithmic differentiation, close to the main), Q7 (tan form of the same branch analysis), Q12 (shifted-cubic view of the same sign analysis), Q15 (surface-area formula, essentially a shortcut of the same related-rates idea).
- Useful results: all 20 questions have `useful_results`.

## make_ppt.py warnings
- None (778 equations converted, no "could not convert" notes).

## Skipped / assumed
- Rendering/thumbnails not done (no soffice). Hindi text not transcribed. Concepts self-assigned. Levels are my own judgement (Medium confidence, no close Main-level anchors). Maths symbols were read from page images because the text layer was garbled. Q19-Q20 (integer type) are labelled "Integer Type(0 to 9)" with 4 marks.
