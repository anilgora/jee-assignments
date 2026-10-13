# Run report - JEE_Main_Question_Bank_02_Integral_Calculus_01

Paper: `papers/JEE_Main_Question_Bank_02_Integral_Calculus_01.pdf` (19 pages, Matrix JEE Academy; 20 single-correct questions with printed solutions, English + Hindi). Deck numbers = printed numbers 1-20.
Files: `_Analysis.pptx` (127 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint was used.
- No marks printed. Assumed **4 marks per Single Correct question**, no negative marking (stated in the section divider). Total 80 marks.

## Difficulty
- **Marks-weighted difficulty index: 2.25** (all questions equal marks; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 3 (Q2, Q18, Q19); Level 2: 9 (Q1, Q3, Q5, Q7, Q9, Q13, Q15, Q17, Q20); Level 3: 8 (Q4, Q6, Q8, Q10, Q11, Q12, Q14, Q16); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q10: **PDF answer is wrong** (see below); the PDF's final limits are wrong ($\int_{a-1}^{b-1}f(x)dx$ instead of $\int_{a+1}^{b+1}f(x)dx$).
- Q11: PDF writes the second integrand as $e^{2x}-e^{-x}-1$; it should be $e^{2x}+e^x-1=e^x(e^x-e^{-x}+1)$. Later steps and answer (A) are right.
- Q16: PDF's last lines are mistyped (second bracket and "10-ln2"); corrected to $-\frac\pi8+\frac14\ln2$; answer (D) right.
- Q19: PDF writes $A(\lambda)=\frac43\lambda$ and $\lambda/8=2/5$; correct is $\frac43\lambda^{3/2}$ and $\lambda^{3/2}/8=2/5$. Answer (D) right.
- Q3, Q4, Q6, Q17 kept as source `pdf` with small additions (not errors): Q3 added the breakpoints of $[t^2]$ and the intermediate evaluation; Q4 added the limits of $U$; Q6 added the intersection point and the reason for each term; Q17 added why $f\neq0$ (needed to divide by $f$). Q20's PDF has a stray "f" in the log term (typo, ignored).

## Solutions whose source is written
- None.

## Answer key
- **Q10: the PDF key (C) is wrong.** $I=\int_a^b f(x+1)dx=\int_a^b f(x)dx$, which equals (B) $\int_{a+1}^{b+1}f(x)dx$ and also (A) $\int_{a-1}^{b-1}f(x+1)dx$. Counter-example $f(x)=(x-2)^2$, $a=1,b=2$: $I=\frac13$, (A)=(B)=$\frac13$, (C)=$\frac73$, (D)=$\frac73$. So the question as printed has two correct options (A and B); the deck's answer box says so.
- All other keys verified by numerical integration / symbolic check (Q1, Q3-Q9, Q11-Q20 numerically with mpmath; Q2 by differentiation and a test point; Q17 by $f=e^{2x}$).

## Alternates
- Given for 18 of 20 questions (all except Q4 and Q12).
- **No alternate:**
  - Q4: every route (tan x = t, or sin/cos with division by cos^10 x) leads to the same integral $\int t^4dt/(2(1+t^{10}))$; no genuinely different method.
  - Q12: the only way to integrate $1/(3\sin x+\cos x+3)$ in closed form is the half-angle (or equivalent) substitution; the auxiliary-angle route is strictly worse; no genuinely different method.
- Weaker alternates (flagging for review): Q14 (fractional-part version of the same symmetry), Q17 (divides by $ff'$ instead of $f^2$; same idea), Q10 (centroid form of the same reflection).
- Useful results: all 20 questions have `useful_results`.

## make_ppt.py warnings
- None. 902 equations converted to native PowerPoint equations; no "could not convert" notes; no missing answers or key ideas.

## Skipped / assumed
- No rendering or thumbnails (no soffice); the deck was not visually inspected. Hindi text not transcribed.
- Concepts and levels are my own judgement (Medium confidence; anchors in the rubric are Advanced-level, so for this Main-level bank I placed questions relative to the lowest anchors).
- Q10's `answer` text reads "(A) and (B) are both correct ... printed key (C) is wrong" instead of a single option.
