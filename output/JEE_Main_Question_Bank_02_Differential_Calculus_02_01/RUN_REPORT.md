# Run report - JEE_Main_Question_Bank_02_Differential_Calculus_02_01

Paper: `papers/JEE_Main_Question_Bank_02_Differential_Calculus_02_01.pdf` (16 pages, Matrix JEE Academy; 20 single-correct questions with printed solutions). Numbered 1-20 as printed.
Files: `_Analysis.pptx` (123 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. Assumed: single correct type 4 marks each, no negative marking (stated in the section divider). Total 80 marks.

## Difficulty
- **Marks-weighted difficulty index: 2.05** (adjusted = unadjusted; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 5 (Q5, Q6, Q7, Q8, Q11); Level 2: 9 (Q1, Q2, Q3, Q4, Q10, Q12, Q16, Q17, Q19); Level 3: 6 (Q9, Q13, Q14, Q15, Q18, Q20); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q9: PDF says all four options fail for a constant function, then keys (C) - self-contradictory, and (A) is actually true for constants. Rewritten: constants kill (B),(C),(D); f(x)=x^2 kills (A) and (C). No option holds for every f.
- Q15: PDF's general solution 4t = n*pi + (-1)^n pi/3 solves sin4t = +sqrt3/2, not -sqrt3/2; its set S and sum (3pi/2) are therefore wrong. Correct S = {pi/3, 5pi/12, 5pi/6, 11pi/12}, sum 5pi/2, beta = 5pi/8. f(beta) = 5/4 either way (cos 3pi/2 = cos 5pi/2 = 0), so key (D) still right.
- Q16: PDF applies L'Hopital giving f'(3+x)+f'(2-x), which needs f' continuous (not given). Replaced by the definition of the derivative. Answer 1 unchanged.

## Solutions whose source is written
- None.

## Answer key
- **Q9: the key (C) looks wrong.** No option is true for every f in S (counterexamples above). The deck shows the answer as "None of (A)-(D) holds for every f (printed key says (C))". All other keys checked and right (Q1-Q8, Q10-Q20), several by numerical/symbolic check (Q10 finite difference, Q12 sign scan, Q13 sympy = 496, Q15 root sum, Q16 numeric limit = 1, Q20 turning-point count).
- Q20: PDF's working is correct but only shows the existence of two critical points; I added the remark about lambda = 0 and |lambda| >= 3/2 (one or no extremum) inside the last bullet. Kept as source `pdf`.

## Alternates
- Given for Q1-Q8 and Q10-Q20 (19 questions).
- **No alternate:** Q9 - the question is settled by counterexamples (constant function, x^2); there is no second genuinely different route to "no option is always true".
- Weaker alternates (flagging for review): Q2 (test-function elimination), Q12 (composition-monotonicity view of the same sign analysis), Q17 (direct lower bound), Q18 (iterate relation first, then differentiate once).
- Useful results: all 20 questions have `useful_results`.

## make_ppt.py warnings
- None (838 equations converted, no "could not convert" notes).

## Skipped / assumed
- Rendering/thumbnails not done (no soffice). Hindi text not transcribed. Concepts self-assigned. Levels are my own judgement (Medium confidence). Maths symbols were read from page images, as the text layer was garbled.
