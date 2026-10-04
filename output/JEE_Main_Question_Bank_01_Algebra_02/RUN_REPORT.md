# Run report: JEE_Main_Question_Bank_01_Algebra_02

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_02.pdf` (printed Q21-Q40, renumbered 1-20; chapters: Polynomial Equations (Q1) and Sequence and Series (Q2-Q20)).
Files: `_content.json`, `_Analysis.pptx` (119 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** for the numerical question (Q1) and for single-correct questions (Q2-Q20), JEE Advanced defaults; stated on the section dividers.
This is a JEE Main-style bank rated on the Advanced scale, so the index is low.

## Difficulty
Marks-weighted difficulty index: **1.80** (no equivalence-relation or multi-correct adjustments).
Level 1: 5 questions (Q3, 6, 9, 11, 15). Level 2: 14 questions (Q1, 2, 5, 7, 8, 10, 12, 13, 14, 16, 17, 18, 19, 20). Level 3: 1 question (Q4). Levels 0, 4, 5: none.

## Solutions: corrected / written
- **Q2 (corrected):** PDF lists the APs as "2+9+...+91" and "5+12+...+94" (wrong lists; sums 654 and 702 are right for 16..93 and 12..96). Lists and term counts fixed.
- **Q12 (corrected):** PDF says "r != 1, so x != 2"; r = 1 corresponds to x = 3. Reasoning via the discriminant (x <= -1 or x >= 3, ends excluded) is what proves x != 2. Answer unchanged.
- **Q14 (corrected):** PDF takes b = +sqrt(ac) (root -sqrt(c/a)), assuming b > 0; the working now uses the double root -b/a, valid for any sign. Answer unchanged.
- **Q20 (corrected):** PDF concludes d = 2/3 by claiming A'' < 0 there. A'' = -60d+68 is +28 at 2/3 (local minimum) and -28 at 8/5 (local maximum). Correct answer 8/5 = (B).
- Other 16 questions: `pdf` (working correct).

## Answer key problems
- **Q20: PDF key (A) 2/3 is wrong; correct answer is 8/5 = (B).** Verified numerically (A(8/5)=2.88 is a local max; A(2/3)=-32/27 is a local min). The product is unbounded as d -> -infinity, so "maximises" can only mean the local maximum; the deck notes this.
- All other keys agree with my computation (Q1, 2, 6, 8, 10, 13, 17, 18 checked by brute force/exact arithmetic; Q4 by a partial-sum check).

## Alternates and useful results
- Alternates given for 19 of 20 questions (all except Q13 and Q19), each checked to reach the same answer. Weaker "different" methods: Q3 (linear form T_n = d(n-19), close to the main), Q6 (cancel squares first), Q8 (expand (k+1)^2 instead of shifting the index), Q20 (sign chart of A' instead of second-derivative test).
- Questions with NO alternate:
  - **Q13:** the problem is inclusion-exclusion of three AP sums; every other route (complement over coprime numbers) just recomputes the same three sums, so no genuinely different method exists.
  - **Q19:** after b=ar, c=ar^2 the only route is the AP middle-term condition and a quadratic in r; other approaches are restatements of it.
- useful_results given for all 20 questions.

## make_ppt.py warnings
None printed. Output: "725 converted to native PowerPoint equations", 119 slides, no "could not convert" notes.

## Skipped / assumed
- No rendering or visual check of the deck (no soffice here).
- Levels are my own judgement against the anchors; confidence Medium for most (see ratings JSON).
- Q1 is labelled Numerical Type (the paper prints no type; the answer is an integer) with 4 marks assumed.
- Q4, Q12, Q13, Q14, Q16, Q20 list two concepts from different chapters.
