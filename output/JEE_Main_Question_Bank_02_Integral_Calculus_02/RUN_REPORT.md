# Run report - JEE_Main_Question_Bank_02_Integral_Calculus_02

Paper: `papers/JEE_Main_Question_Bank_02_Integral_Calculus_02.pdf` (17 pages, Matrix JEE Academy; 20 single-correct questions with printed solutions, English + Hindi). Printed numbers are 21-40; deck numbers are 1-20 (deck Qn = printed Q(n+20)).
Files: `_Analysis.pptx` (129 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint was used.
- No marks printed. Assumed **4 marks per Single Correct question**, no negative marking (stated in the section divider). Total 80 marks.

## Difficulty
- **Marks-weighted difficulty index: 2.25** (equal marks; no equivalence-relation or multi-correct adjustments apply).
- Level 1: 3 (Q11, Q15, Q19); Level 2: 9 (Q1, Q2, Q4, Q5, Q6, Q8, Q13, Q14, Q17); Level 3: 8 (Q3, Q7, Q9, Q10, Q12, Q16, Q18, Q20); Levels 0, 4, 5: none.

## Solutions whose source is corrected
- Q3 (printed 23): PDF's line after $c=-1/e$ reads "$x(1+1/y)-\frac1e e^{1/y}$ passes through (k,2)" - not an equation; correct curve is $x=(1+1/y)-\frac1e e^{1/y}$. Final value and answer (C) right.
- Q14 (printed 34): PDF's substituted integrand has denominator $t^2+5$ without the square root; must be $\sqrt{t^2+5}$ (its next line only follows from that). Answer (A) right.
- Q16 (printed 36): PDF writes $-\frac12\frac{(1+x^{-6})^{1/3}}{x^2}$ and $-\frac1{2x^3}x(1+x^{-6})^{1/3}$; correct is $(1+x^{-6})^{1/3}=(1+x^6)^{1/3}/x^2$, giving $-\frac1{2x^3}x(1+x^6)^{1/3}$. Answer (A) right.
- Kept as `pdf` with small notes (not errors): Q5 (printed 25) has a stray unrelated line "x dv/dx = (-1-v^2)/..." at the top of the solution (from another question; ignored); Q8 (printed 28) writes "c^y = t" for $e^y=t$ (typo, used $e^y$); Q7 (printed 27) says only "Case 2 not required" - I added the reason ($xy=1$ is a solution so $xy>1$ along the curve); Q10, Q11, Q13, Q18 extended with the PDF's missing last simplification steps.

## Solutions whose source is written
- None.

## Answer key
- All 20 keys verified (sympy/mpmath/direct numerics for Q1, Q3, Q4, Q5, Q7, Q10, Q12, Q13, Q14, Q16, Q18, Q19, Q20; by hand for the rest). No wrong key.
- **Q14 (printed 34): options (A) and (D) are printed identically** ($\frac12\sin\sqrt{(2x-1)^2+5}+c$), so both are correct; key (A). The answer box says so.

## Alternates
- Given for 19 of 20 questions (all except Q12).
- **No alternate:** Q12 (printed 32): the only route is period 1 + the value of $[\sin2\pi x]$ on each half-period; a different viewpoint would be a reworded copy.
- Weaker alternates (flagging for review): Q11 (calculus-of-two-variables view of the same sign idea), Q15 (elimination by differentiating/testing options), Q19 (bounding/elimination, not a derivation), Q5 (layer-cake sum, same periodicity), Q6 (first- vs second-derivative test), Q17 ($Y=vX$ instead of the I.F.).
- Useful results: all 20 questions have `useful_results`.

## make_ppt.py warnings
- First build: "Q19: only 3 solution bullets" - fixed by splitting the PDF's three-line working into 6 one-step bullets. Final build: no warnings; 866 equations converted to native PowerPoint equations; no "could not convert" notes.

## Skipped / assumed
- No rendering or thumbnails (no soffice); the deck was not visually inspected. Hindi text not transcribed.
- Concepts and levels are my own judgement (Medium confidence; the rubric's anchors are Advanced-level, so for this Main-level bank I placed questions relative to the lowest anchors).
- Numbering: deck numbers 1-20 differ from printed 21-40; the question text itself does not show printed numbers.
