# Run report - JEE_Main_Question_Bank_02_Differential_Calculus_02_03

Paper: `papers/JEE_Main_Question_Bank_02_Differential_Calculus_02_03.pdf` (5 pages, Matrix JEE Academy; 5 numerical-type questions with printed solutions). Printed numbers are 41-45; the deck numbers them 1-5 (deck Q = printed Q - 40).
Files: `_Analysis.pptx` (35 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint was used.
- No marks printed. Assumed 4 marks each for all five numerical-type questions (JEE Advanced default for numerical/integer), no negative marking (stated in the section divider). Total 20 marks. Labelled "Numerical Type" (not "Integer 0-9") because answers 14 and 0.5 are outside 0-9.

## Difficulty
- **Marks-weighted difficulty index: 1.80** (adjusted = unadjusted; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 2 (Q3, Q5); Level 2: 2 (Q1, Q4); Level 3: 1 (Q2); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q1 (printed 41): PDF has "c = 2 + b - b" (should be 2 + b - a); numbers and answer 5 are right. I also added the f' > 0 argument for the maximum at x = 1, which the PDF only shows by a sketch.
- Q4 (printed 44): PDF's x = 1 line in (2) reads "g'(1) + 2f(1) + 4 + g'(1)" (should be g'(1) = 2f(1) + 4 + g'(1)) and (3) is printed as 2(1)+4 (should be 2f(1)+4). Values and answer 14 are right.

## Solutions whose source is written
- None. Small additions kept as source `pdf`: Q2 (PDF's factorisation of P' was garbled in print; written clearly), Q3 (PDF stops after the two tangents; I added the final step a/b = 0.5).

## Answer key
- All five keys are right: Q1 f(1) = 5 and f(-1) = 2, f'(-1) = 1 checked with sympy; Q2 factor P' = 10(x^2+x+1)^2 and the identity P = x^5+(x+1)^5+5x+9 checked with sympy, only real root about -1.232 in (-2,-1); Q3 a = 1, b = 2 (also by discriminant); Q4 14 by the alternate; Q5 minimum 235 at x = 5 both ways.

## Alternates
- Given for all 5 questions (Q1-Q5). No question lacks one.
- Weaker alternates (flagging for review): Q4 (subtracting f and g is still the same system of equations, organised differently).
- Useful results: all 5 questions have `useful_results`.

## make_ppt.py warnings
- None (223 equations converted, no "could not convert" notes).

## Skipped / assumed
- Rendering/thumbnails not done (no soffice). Hindi text not transcribed. Concepts self-assigned. Levels are my own judgement (Medium confidence, no close Main-level anchors; rubric/anchors skimmed rather than matched line by line). The Q1 sentence "f(x) <= alpha ... least alpha" is read as the maximum of f on [-1,1].
