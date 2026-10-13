# Run report — SHEET Complex Number_FCopy JM

Paper: `papers/SHEET Complex Number_FCopy JM.pdf` (34 pages, "Exercise J-M": JEE Main 2023-2024 complex-number questions with printed solutions). Deck numbering Q1–Q50: single-correct Q1–Q6, Q8–Q10, Q12–Q22, Q26–Q33, Q40–Q48; numerical Q7, Q11, Q23–Q25, Q34–Q39, Q49–Q50. The text layer garbles the maths, so everything was read from page images; Hindi duplicates left out (English deck).

Files: `…_Analysis.pptx` (290 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- No marks are printed. Assumed (task defaults, also stated on the section dividers): **4 marks** for every single-correct and numerical question (no one-or-more-correct, paragraph or matching questions in this paper). Total 200 marks.

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.06** (200 marks) - well below the official JEE Advanced range of 2.59–3.21, as expected for JEE Main questions.
- Questions per level (adjusted): Level 1 — 9 (Q3, Q4, Q7, Q8, Q9, Q17, Q26, Q29, Q33); Level 2 — 29 (Q1, Q2, Q5, Q6, Q10, Q13, Q14, Q15, Q16, Q18, Q19, Q20, Q22, Q27, Q28, Q30, Q31, Q34, Q36, Q37, Q40, Q41, Q42, Q43, Q45, Q46, Q47, Q48, Q50); Level 3 — 12 (Q11, Q12, Q21, Q23, Q24, Q25, Q32, Q35, Q38, Q39, Q44, Q49); Levels 0, 2.5, 4, 5 — none.
- No equivalence-relation adjustment and no multi-correct floor applied (no such questions). Low confidence: Q6, Q10, Q23, Q32, Q39, Q44. The rest Medium/High. All levels were set by me with nearest anchors named in the workbook.
- `recalc.py` skipped (no `/mnt/skills`), so the Excel formula cells have no cached values until opened in Excel.

## Solutions: corrected / written
`corrected` (8):
- **Q1:** PDF starts from $(1+\sqrt3 i)^{200}$ but the question has $(1-\sqrt3 i)^{200}$, so it gets $q=+\sqrt3$; correct values $p=-1,\ q=-\sqrt3$. The two roots only swap, answer (B) unchanged.
- **Q5:** PDF jumps from $y_1y_2=-x_1^2$ to "opposite signs"; the missing step $x_1\ne0$ (else one number is $0$) added.
- **Q12:** PDF's own last lines show infinitely many solutions for $a=-b$ although the key is $0$. Kept the key (D) and made the restriction $a\neq\pm b$ explicit (see answer-key note below).
- **Q23:** PDF assumes the circle is the diameter circle of $\alpha\beta$ ($2\lambda=|\alpha-\beta|^2$), which is not given. Replaced by the general identity $|z-\alpha|^2+|z-\beta|^2=2|z-c|^2+\tfrac12|\alpha-\beta|^2$; answer 2 unchanged (independent of $\lambda$).
- **Q25:** PDF stops after the line $2x-y+2=0$; it neither justifies the centre $(1,2)$ (vs $(1,0)$) nor computes the chord. Steps added, answer 24 agrees.
- **Q30:** PDF asserts $\omega,\omega^2$ are roots of the first equation without checking and never tests the third root $-1$ of the cubic. Both checks added; answer 2 unchanged.
- **Q34:** typo $24\alpha^5$ (should be $21\alpha^5$) in one line; corrected, values $A=43,B=43,C=42$ and the answer 5 unchanged.
- **Q44:** typo $|z_2|^2$ for $|z_1|^2$ in the first expanded term; corrected, answer (C) unchanged.

`written` (1): **Q26:** the PDF has only a hand sketch of three lines and no working; wrote the full solution.

All other questions are `pdf`: checked line by line and reproduced (several with intermediate steps expanded, e.g. Q3, Q6, Q7, Q9, Q10, Q14, Q29, Q32, Q35, Q38, Q46, Q47, Q49; Q9 uses $a$ for the coefficient and $\gamma$ for the radius where the PDF mixes $\alpha/\psi$; Q49: the PDF writes $|2i-x_k|^2=4+x_k^2$ without saying why, now justified for real or complex roots via $P(-2i)=\overline{P(2i)}$).

## Answer-key / question problems
- **Q10:** key is "Drop" - confirmed: the two admissible values are $-(1+\sqrt7)/4$ and $0$, none among the options. Answer printed as "none of the options (question dropped)".
- **Q12:** key (D) $0$ is right only for $a\neq\pm b$; for $b=-a$ the set is the hyperbola $x^2-y^2-x=1$ (infinite). The question as printed allows $b=-a$, so it is not well posed; (D) kept.
- **Q33:** key is "Bonus" - confirmed: the minimum is $0$ (the point $-\tfrac12(3+4i)$ lies in $|z|\ge1$), not in the options. (For $|z|\le1$ it would be $3/2$.)
- **Q35:** the key $20$ is the algebraic result, but the data are inconsistent: $|\alpha|^2=1/5$ is impossible for a point of $|z-(1+i)|=2$ (needs $|\alpha|\ge2-\sqrt2\approx0.59$), so no complex $\alpha$ satisfies both circle conditions. Answer 20 kept (it is what the question expects); remark added on the last solution slide.
- All other keys agree with my computation (every final answer was re-computed numerically/symbolically; Q39 and Q41/Q43 areas also checked by brute force).

## Alternates and results
- **Alternate solutions given for 43 of 50 questions** (Q1–Q17, Q19, Q20, Q22, Q23, Q25, Q26, Q28–Q32, Q34–Q45, Q47–Q49; each a different technique, e.g. Apollonius endpoints, Thales circle, cancelling cross terms, polar forms, symmetry/pairing, gcd, inversion; each checked numerically). 
- **No alternate (7 questions, no genuinely different method exists):**
  - Q18: for real $z$ each inequality is a linear inequality in $x$; the only route is that half-line argument with a counter-example.
  - Q21: splitting into real and imaginary parts is the only workable route (the equation mixes $z,\bar z$ and $\mathrm{Re}\,z$; polar form does not simplify it).
  - Q24: the only route is "numerator minus denominator is purely imaginary, so the denominator must be"; any other version is the same condition rewritten.
  - Q27: it is a real/imaginary-parts linear system; cancelling the imaginary part by inspection is the same equation.
  - Q33: one observation (fixed point inside the region, minimum 0); nothing else to give.
  - Q46: counting pairs and the factorial observation $4\mid n!$ - no second method.
  - Q50: lattice enumeration plus the half-plane test - no second method.
- **Useful Result / Pattern given for all 50 questions.**

## make_ppt.py warnings
- `note: Q42: very long question - font reduced to 22 pt.` - harmless (the paper's question has two long statements); left as is.
- No "could not convert" warnings: all 1700 equations converted to native PowerPoint equations. No other warnings.

## Skipped / assumed / guessed
- Marks assumed (4 each); concepts self-assigned; difficulty levels rated by me (no user ratings available).
- Rendering/thumbnail check skipped (per environment rules); the deck was checked programmatically (no stray LaTeX or `$` in any slide text).
- Q5/Q18/Q42 option lists: Q5's A-D statements are inside the question text (as in the paper) and the answer options (A)-(D) are the paper's.
