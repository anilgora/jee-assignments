# Run report - JEE_Main_Question_Bank_02_Integral_Calculus_06

Paper: `papers/JEE_Main_Question_Bank_02_Integral_Calculus_06.pdf` (16 pages, Matrix JEE Academy; 16 numerical questions with printed solutions, English + Hindi). Printed numbers are 101-116; deck numbers are 1-16 (deck Qn = printed Q(n+100)).
Files: `_Analysis.pptx` (104 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint was used.
- No marks printed. Assumed **4 marks per Numerical question (Q1-16)**, no negative marking (stated in the section divider). Total 64 marks. Answers are not limited to 0-9, so all are labelled "Numerical Type".

## Difficulty
- **Marks-weighted difficulty index: 2.38** (equal marks; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 1 (Q8); Level 2: 8 (Q3, Q5, Q6, Q7, Q10, Q12, Q15, Q16); Level 3: 7 (Q1, Q2, Q4, Q9, Q11, Q13, Q14); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q4 (printed 104): PDF line "(k alpha + 0)/(k+1) = 0" should be "= x"; later working correct. Answer is the expression 4 + ln 3, not a number (PDF key "Bonus").
- Q5 (printed 105): PDF writes the inner limit of int_0^n {x}dx = n int_0^n x dx as n (should be 1) and "n - 20 = 20" (should be n - 1 = 20); n = 21 is right.
- Q13 (printed 113): PDF's last lines are cut ("6A+ = 5 sqrt5", no evaluation shown); filled in A = (5 sqrt5 - 11)/6, (6A+11)^2 = 125.
- Q15 (printed 115): PDF sets the integration constant to 0 without justification and never uses the given relation a - 2 sqrt2 b = 3. Corrected: keep C, eliminate it by subtracting the two point conditions, use the given relation -> b = 0, a = 3 (C = 0 follows). Answer 9 unchanged.

## Solutions whose source is written
- None.

## Answer key
- All 16 answers verified numerically (mpmath quadrature, ODEs substituted back, closed forms differentiated).
- **Q4 (printed 104): key "Bonus" is right** - 4y(1) - 5 ln 3 = 4 + ln 3 (about 5.0986) is not a single number. The deck shows this in the answer box.
- Q2 (printed 102): with the sqrt taken as non-negative the equation forces y/x = sin(ln x) only while cos(ln x) >= 0 (x <= e^{pi/2}); beyond that y = x is the only continuation, which would change the area. The key 4 follows the intended formal solution y = x sin(ln x); deck follows the PDF.
- Q9 (printed 109): the integral equation also has the constant solution f = e (radicand vanishes at x = 0), which would give 36. The key 27 follows the intended non-constant solution e^{cos x}; noted in the Useful Result slide.
- All other keys correct as printed.

## Alternates
- Given for all 16 questions (Q1-Q16).
- No question without an alternate.
- Weaker alternates (flagging for review, all verified): Q1 (definite integral between the two given points - same antiderivative, no constant), Q3 (quotient-rule recognition), Q4 (slope from intercepts + definite integral), Q8 (polynomial particular solution by inspection), Q12 (trapezoid + inverse-function area), Q13 (shifted origin t = x - 1/2), Q16 (horizontal strips), Q15 (equidistance geometry - close to the corrected main solution).
- Genuinely different: Q2 (complex exponent Im x^{1+i}), Q5 (areas + common ratio), Q6 (t = ln x, particular + complementary), Q7 ([x]+[-x] = -1), Q9 (u = cos theta, guess and verify), Q10 (integrate the equation, answer = amplitude C), Q11 (Bernoulli v = 1/y), Q14 (change variable to t = ln cos y first).
- Useful results: all 16 questions have `useful_results`.

## make_ppt.py warnings
- None. 694 equations converted to native PowerPoint equations; no "could not convert" notes. `build_report.py` ran without warnings.

## Skipped / assumed
- No rendering or thumbnails (no soffice); the deck was not visually inspected. Hindi text not transcribed.
- Concepts and levels are my own judgement (Medium confidence; rubric anchors are Advanced-level, so for this Main-level bank questions were placed relative to the lowest anchors, as in the earlier banks).
- Numbering: deck numbers 1-16 differ from printed 101-116.
- Q4: ratio PA:PB = 1:k was taken as P = (k A + B)/(k+1), as in the PDF.
