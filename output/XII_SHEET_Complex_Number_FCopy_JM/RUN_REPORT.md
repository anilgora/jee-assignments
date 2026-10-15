# Run report - XII_SHEET_Complex_Number_FCopy_JM (Exercise J-M, 47 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (Q1-6, Q10-14, Q20-28, Q34-44 single correct; Q7-9, Q15-19, Q29-33, Q45-47 numerical value). Stated in the section dividers. Total 188 marks. All questions are JEE Main (2021-22) problems.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.04** (96/47; all questions 4 marks; no equivalence-relation adjustment and no multi-correct floor applies). Below the official Advanced range (2.6-3.2), as expected for JEE Main questions.
- Levels: Level 1 = 9 (Q8, Q10, Q11, Q12, Q15, Q34, Q36, Q38, Q42); Level 2 = 27 (Q1-5, Q7, Q9, Q13, Q14, Q16, Q17, Q19-22, Q24, Q26, Q27, Q29, Q30, Q37, Q39, Q40, Q43, Q44, Q46, Q47); Level 3 = 11 (Q6, Q18, Q23, Q25, Q28, Q31, Q32, Q33, Q35, Q41, Q45); Levels 0, 4 and 5 = none. Low confidence on Q22 and Q35 (the questions themselves are flawed); the rest High/Medium (anchors for these loci are loose).
- Workbook: `XII_SHEET_Complex_Number_FCopy_JM_difficulty.xlsx` (recalc.py not available; cached values appear when opened in Excel).

## Solutions corrected / written (solution_source)
Ten corrected, none written:
- **Q6 (corrected)** - PDF's last line gives $\frac{5+\sqrt2}{4}$ (misses the 2 in $2\sqrt2$); correct value $\frac{5+2\sqrt2}{4}$ = key (D). Also "$|z-2|\le$" has no 1, and no justification that $A$ is the farthest point (added via $\frac54-\cos t$).
- **Q9 (corrected)** - PDF's first fraction has denominator $1+2\cos^2\theta$; it is $1+9\cos^2\theta$ (used correctly one line later); misprints $\cos\theta$ for $\cos^2\theta$ at the end. Answer 1 unchanged.
- **Q13 (corrected)** - PDF's reduced determinant has $e^{i4\theta}(e^{i\theta}-1)$ in row 3 (should be $e^{i7\theta}(\dots)$) and says "$=0$" without the reason (new column = $(e^{i\theta}-1)\times$ first column). Fixed.
- **Q22 (corrected)** - PDF's first line has misplaced conjugation bars, and it solves the argument equations as exact equalities: $2\arg z_1=\frac\pi2$ gives $\arg z_1=\frac\pi4$ **or** $-\frac{3\pi}4$. Both satisfy the data, so (D) is also correct. See answer-key section.
- **Q27 (corrected)** - PDF uses only the roots $\omega,\omega^2$ of $1+x+x^2$; the quartic also has $-\omega,-\omega^2$ ($\alpha^3=-1$). Value is 1 for them too (added). Answer unchanged.
- **Q29 (corrected)** - PDF's figure puts $P$ on the line towards $-4i$, but the question (and the PDF's coordinates $\left(\frac{12}5,\frac45\right)$) is for $4i$; towards $-4i$ the point would be $\left(\frac{12}5,-\frac45\right)$ and the answer 40. Also the half-plane inequality is never checked at $P$ (added). Answer 80 unchanged.
- **Q32 (corrected)** - PDF reverses the sign of the $2xy$ term in both the real and imaginary equations and gives $x=\frac{-1\pm\sqrt2}2$ (correct: $\frac{1\pm\sqrt2}2$ from $x^2-x-\frac14=0$). The sum of $|z|^2$ is unaffected: 2.
- **Q33 (corrected)** - PDF swaps $PB=\sqrt{17}$, $PC=\sqrt{13}$ (correct: $PB^2=13$, $PC^2=17$), writes "$\alpha=30$ and $\alpha=-4$" ($\beta$), and does not check the arc. Still picks $z_2=C$ correctly. Answer 26 unchanged.
- **Q35 (corrected)** - PDF's Case 2 itself gives infinitely many $n$ yet the key is (D) 4. See answer-key section.
- **Q39 (corrected)** - PDF writes $|1+2i+6i|^2$ for the third term of $v_0$ (should be $|1+2i-6i|^2=17$); value 30 and answer 1000 correct.
- Misprints that I fixed silently while transcribing, source kept `pdf`: Q4 ("let $x=x+iy$", garbled root list), Q8 ("$n+1=y$" for $x+1=y$), Q15 ("$|z-2-zi|$" for $2i$), Q17 (eq. (3) with $y_1^2$ for $y_2^2$, "(B)-(3)" for (2)-(3), "$x_1-x_1$"), Q40 (final product-looking brackets that are really a sum).
- PDF working correct but terse; I added the missing justification (source `pdf`): Q5 (only "$S_1\cap S_2\cap S_3=A$"), Q7 (why only multiples of 8), Q10 (which centre), Q11 (angle reduction), Q12, Q16 (arc check), Q18 (why 6 is least, odd $n$), Q20, Q21 (solving the quadratic), Q23 (arc/quadrant), Q25 (inside/outside and the $y\le\sqrt5$ bound), Q28, Q34 (coprimality), Q43 (attainment), Q44, Q45 (even $n$), Q47.

## Answer key
- **Q35 - key looks wrong for the question as printed.** $S_n,T_n$ are circles; $S_n\cap T_n=\phi$ for $n=1,2,3,4$ (apart) **and every $n\ge7$** (the huge circle $S_n$ contains the tiny $T_n$), so the set is infinite and no option is correct. The PDF's own Case 2 shows this. Key (D) 4 is right only if $S_n,T_n$ were discs ($\le$). The answer field of the slide states this.
- **Q22 - two options are correct**: $\arg z_1=\frac\pi4$ (C, the key) and $\arg z_1=-\frac{3\pi}4$ (D); checked numerically. The slide keeps (C) and mentions (D).
- The other 45 keys agree with my derivations; checked by direct computation (Python) for Q2, Q6, Q7, Q11, Q16-19, Q21, Q24-26, Q28-33, Q37, Q39-47 and by hand for the rest.

## Alternates and results
- Alternates for **42 of 47 questions**: Q1-Q7, Q9-Q24, Q26-Q35, Q37, Q39-Q43, Q45-Q47. Every alternate uses a different technique (special case, polar form, parametrisation, Vieta, rank-one factorisation, Thales/inscribed-angle geometry, power reduction, complement counting ...) and each was checked against the answer. Milder ones that are a different method but short: Q1 (test one admissible pair), Q3 (test $A=I$), Q15 (triangle inequality), Q16 and Q29 (parametrisation), Q20 (parametrisation), Q24 (equilateral-triangle area formula), Q30 (tabulating the period-3 values), Q34 (power reduction + Vieta), Q41, Q42.
- **No alternate (5): Q8** (a routine conversion of two loci; no second idea), **Q25** (the only reliable method is the inside/outside test; a precise count needs the ellipse-circle quartic), **Q36** (min of a sum of distances is the triangle inequality - one idea), **Q38** (perpendicular bisector then substitute; no second route), **Q44** (three loci intersected; no second route).
- Every question (1-47) has `useful_results`.

## make_ppt.py warnings
- None. The build printed only "1688 converted to native PowerPoint equations" and "285 slides, 47 questions". No "could not convert" messages and no bullet-count warnings.

## Skipped / assumed / guessed
- Only the English text was read (the PDF is bilingual; Hindi text ignored). Figures in Q5, Q6, Q10, Q15, Q16, Q20, Q21, Q23, Q28, Q29, Q33, Q37, Q41, Q44 are described in words, not reproduced.
- No visual rendering check of the deck (no soffice here).
- Question types: Q7-9, Q15-19, Q29-33, Q45-47 treated as numerical-value (no options printed); the rest single correct. All marks are the assumed defaults (4).
- Difficulty chapter labels: "Complex Number" for most; "Matrices" for Q3, Q7, Q45 and "Determinants" for Q13 (their key step is matrix/determinant based). Nearest anchors are loose; levels are Medium confidence.
- Q25: the count of exactly 2 intersection points is supported by the inside/outside argument and a numerical sign-change check, not by an algebraic proof.
