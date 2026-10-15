# Run report - SHEET_TRIGONOMETRIC_RATIO_FCopy_C2 (Exercise C-II, 34 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for Q1-27 (numerical-value and subjective/"prove that" questions), 3 marks for the paragraph questions Q28-33 and 3 for the matching question Q34. Stated in the section dividers. Total 129 marks. Type labels: "Numerical Type" for value answers, "Subjective Type" for prove/derive/range answers (my labelling).

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.98** (no equivalence-relation or multi-correct adjustments apply).
- Levels: Level 1 = 1 (Q18), Level 2 = 6 (Q1, Q6, Q11, Q16, Q25, Q31), Level 3 = 20, Level 4 = 7 (Q5, Q7, Q10, Q13, Q17, Q24, Q27); Levels 0 and 5 = none.
- Ratings are my judgement against the anchors (many Medium confidence; Q8 Low).
- Workbook: `SHEET_TRIGONOMETRIC_RATIO_FCopy_C2_difficulty.xlsx` (recalc.py not available, cached formula values absent until opened in Excel).

## Solutions corrected / written
- **Q23 (corrected, answer key wrong)** - the PDF adds the largest root of both factors of $(2\sin x+1)(2\cos y+1)=0$ ($\frac{11\pi}6+\frac{4\pi}3=\frac{19\pi}6$). Only one factor needs to vanish and the other variable is then free, so $x=\frac{11\pi}6$, $y=2\pi$ gives $\frac{23\pi}6$. Correct answer $\frac{23\pi}{6}$, not the key's $\frac{19\pi}6$.
- **Q10 (corrected)** - the PDF drops the sign in $\cos\frac{3\pi}{11}=-\cos\frac{8\pi}{11}$ and takes $\sin\frac{16\pi}{11}=\sin\frac{5\pi}{11}$ (really $-\sin\frac{5\pi}{11}$). The two slips cancel, so the final result is right; signs made explicit.
- No question needed `written`.

## Answer key
Q23's key ($\frac{19\pi}{6}$) is wrong (see above). All other answers were checked numerically (Q3, Q5, Q7, Q8, Q9, Q10, Q14, Q15, Q17, Q23 and Q34 by direct computation; the others by algebra): no other problem.

## Gaps / notes while keeping solution_source = pdf
- Q27: the PDF's first method is a very long unbroken expansion (text garbled); it is reproduced in the same route but regrouped with $e_1,e_2,e_3$; the PDF's second method (tan substitution) is the alternate.
- Q25: the PDF's printed solution is cut at the end of a page; its remaining working was read from the next page (the $t=\cot\frac\theta2$ route).
- Q31: the PDF has three lines; a line showing why $\sum\tan A=\prod\tan A$ was added.
- Q13: the problem assumes the infinite series in the hypothesis converges; stated, not proved.
- Q22: the PDF prints the triple as (1,1,2) and the value $\sqrt5-2$; confirmed numerically ($0.2361$).
- Q28-30 paragraph text and options, Q33 options (B) and the first term of Q34(A) ($\cos\frac\pi{19}$) were reconstructed from the page images; a garbled option, if any, would be option B of Q33 ($\frac{q^3}{p^3}$ assumed).

## Alternates and results
- Alternates were written for **31 of 34** questions (all except Q6, Q23, Q33).
- **No alternate:** Q6 (the identity $\sin(\alpha-2\beta)=\sin4\beta$ is the only natural route; any other route is a rewording), Q23 (factor-and-compare-cases is the only route; bounding by case is the same thing), Q33 (the cube/Newton identity is the one method; no different idea).
- Weaker alternates (variant of the PDF route rather than a wholly new idea): Q1 (cancel $1-\cos y$), Q4 (sin 2A form with monotonicity), Q28 (t-formulas), Q31/Q32 (expansion of $\sin/\cos(A+B+C)$ in place of tan addition).
- Every question has useful_results (3 bullets each).

## make_ppt.py output
- 1178 equations converted to native PowerPoint equations; 207 slides, 34 questions. No "could not convert" warnings.
- One note on first build ("Q31: only 3 solution bullets"): resolved by adding the explanatory step. No rebuild notes remain.
- No rendering check was possible (no PowerPoint/LibreOffice).

## Skipped / assumed / guessed
- Concepts and chapter name self-assigned ("Trigonometric Ratio"); ratings are my judgement.
- recalc.py and slide rendering were skipped (not available).
- The text layer of the PDF lost most maths; questions and solutions were read from page images (80-110 dpi) plus the text layer.
