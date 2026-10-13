# Run report - JEE_Main_Question_Bank_02_Integral_Calculus_05

Paper: `papers/JEE_Main_Question_Bank_02_Integral_Calculus_05.pdf` (20 pages, Matrix JEE Academy; 12 single-correct questions + 8 integer-type questions with printed solutions, English + Hindi). Printed numbers are 81-100; deck numbers are 1-20 (deck Qn = printed Q(n+80)).
Files: `_Analysis.pptx` (136 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint was used.
- No marks printed. Assumed **4 marks per Single Correct question (Q1-12)** and **4 marks per Numerical question (Q13-20)**, no negative marking (stated in the section dividers). Total 80 marks. The paper's "Integer Type" answers are not limited to 0-9 (26, 62, 25...), so they are labelled "Numerical Type".

## Difficulty
- **Marks-weighted difficulty index: 2.10** (equal marks; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 4 (Q3, Q5, Q8, Q15); Level 2: 10 (Q2, Q4, Q6, Q7, Q9, Q10, Q11, Q14, Q16, Q19); Level 3: 6 (Q1, Q12, Q13, Q17, Q18, Q20); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q3 (printed 83): PDF's last line has `-c e^{-at}` where the solution has `+c e^{-alpha t}` (sign slip, limit unchanged); the case alpha = beta (division by alpha-beta) was not covered - added.
- Q13 (printed 93): **PDF answer is wrong.** PDF writes I = 2*int_0^{pi/2} g dx and then evaluates int_0^{pi/2} 2g dx = 13pi/8, giving k = 26. Correct: I = (1/2) int_0^pi g = int_0^{pi/2} g = 13pi/16, so **k = 13** (numerical quadrature: 16I/pi = 13.000).
- Q18 (printed 98): PDF uses b both for the abscissa of R and of Q (writes b = 3, "c = 1", R(b, f(2))); notation fixed to a = 3. Value Q(3, 1/2) and answer 5 are right.

## Solutions whose source is written
- None.

## Answer key
- All 20 answers verified numerically/symbolically (mpmath quadrature, differentiation of closed forms, ODEs substituted back).
- **Q13 (printed 93): key 26 is wrong; correct k = 13** (see above). The deck shows 13.
- **Q10 (printed 90): option (A) is misprinted** as log|(x^3+x)/x| (= ln(x^2+1)), which is not an antiderivative. The working yields ln|(x^3+1)/x| + C, which is what (A) is meant to say; the key (A) is kept and the misprint is stated in the answer box and the last solution step.
- Q6 (printed 86): for 0 < theta < pi/2 the radicand sin^n(theta) - sin(theta) is negative, so the integrand is real only formally; the key (A) follows the formal antiderivative (differentiation reproduces the integrand). Noted in the Useful Result slide.
- Q14 (printed 94): key 1 correct; comparison "alpha = 10, beta = 9" relies on the rational / e^20 parts argument (stated in the results slide).

## Alternates
- Given for 19 of 20 questions (all except Q17).
- **No alternate:** Q17 (printed 97): the integral reduces to the standard form int dt / sqrt(2t^2 - 1); the other routes (t = tan x, w = sqrt(1 - t^2)) lead to the same standard log form, and matching the stated shape then needs the same squaring identity, so no genuinely different method exists.
- Weaker alternates (flagging for review, all verified): Q2 (single-sine form of the height - same split), Q5 (multiplier trick instead of solving - same equations), Q6 (rationalising substitution and "differentiate option (A)"), Q9 (shifted origin instead of trapezium), Q10 (partial fractions - different but routine), Q11 (vertical instead of horizontal slicing), Q14 (exact derivative in t = ln x instead of parts), Q15 (reflection and parabola-arch area), Q19 (centred coordinates), Q8 (slope test on the options - an exam technique).
- Genuinely different: Q1 (w = x^2/y^2 has a y-free derivative), Q3 (L'Hopital on y e^{alpha t}), Q4 (convexity + symmetry), Q7 (w = x y^2 exact), Q12 (y = sqrt(x) z and s = x^{3/4}), Q13 (cos 3x polynomial -> sin^4 + 4cos^6, Wallis), Q16 (uniqueness / homogeneous shift), Q18 (particular + complementary), Q20 (special case m = n = 1 fixes the constant alpha).
- Useful results: all 20 questions have `useful_results`.

## make_ppt.py warnings
- None. 868 equations converted to native PowerPoint equations; no "could not convert" notes.
- `build_report.py` ran without warnings.

## Skipped / assumed
- No rendering or thumbnails (no soffice); the deck was not visually inspected. Hindi text not transcribed.
- Concepts and levels are my own judgement (Medium confidence; the rubric's anchors are Advanced-level, so for this Main-level bank I placed questions relative to the lowest anchors, as in the earlier banks).
- Numbering: deck numbers 1-20 differ from printed 81-100; the question text itself does not show printed numbers.
- Q9: the single-point value f(1/2) = 1/2 is irrelevant to the area; the region was taken as bounded between x = 1/2 and x = sqrt(3)/2 as in the PDF.
