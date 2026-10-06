# RUN REPORT - JEE_Main_Question_Bank_01_Vector_3D_03

Paper: 20 questions printed as Q41-Q60 (14 single-correct, 5 numerical, 1 single-correct). The deck numbers them 1-20 (deck Q1 = printed Q41, ..., deck Q20 = printed Q60). Note: printed Q60 (deck Q20) is a determinants / linear-equations question, not Vector 3D.

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **1.80** (36 / 20 questions, 4 marks each). No equivalence-relation adjustment or MCQ floor applied (no MCQs).
- Questions per level: Level 0: none | Level 1: 6 (Q1, Q5, Q6, Q9, Q10, Q20) | Level 2: 12 (Q2, 3, 4, 7, 8, 11, 12, 13, 14, 15, 16, 18) | Level 3: 2 (Q17, Q19) | Levels 4 and 5: none.
- All ratings are Medium confidence; this is a JEE Main-style bank, so the index sits well below the JEE Advanced range.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper): JEE Advanced default of 4 for single-correct and for numerical/integer questions (+4 correct, 0 otherwise, stated on the section dividers).

## Solutions whose source is corrected or written
No question is `written`. `corrected` ones:
- Q1 (printed 41) - gap: the PDF goes from t = +-3/2 to the point (7,-5,9) without showing why it is the *farther* point. Added the comparison with (-5,1,-3). Answer 155 unchanged.
- Q2 (printed 42) - gap: k = -4/3 is stated with no working. Added the two linear equations that give alpha = -4k-6 and 3k = -4. Answer (3) unchanged.
- Q7 (printed 47) - typos: third condition printed "x/sqrt2 + 4/sqrt2 = -1/2" (4 stands for y) and a stray "kn" after the vector difference. Corrected. Answer (1) unchanged.
- Q8 (printed 48) - typo: |c|^2 = 4|a x b| + 9|b|^2 missing the square on |a x b|; restored, and gave the reason for c.a = -6, b.c = -48. Answer (3) unchanged.
- Q11 (printed 51) - sign error: Method II gives AD = (i - 8j - 3k)/2, which is DA; AD = (-i + 8j + 3k)/2. The projection length uses |AD.AC| so 37/(2 sqrt38) is unchanged. Also added cos A = -1/38 in Method I.
- Q12 (printed 52) - error: the PDF's final line (x-1)/(+-1) = (y-6)/1 = (z-3)/sqrt2 loses the minus signs of m and n and keeps +-, though "acute with the x-axis" forces l = +1/2. With the printed line (3,4,3-2sqrt2) is not on it. Corrected to direction (1,-1,-sqrt2). Answer (4) unchanged.
- Q15 (printed 55) - error: d = 2(c-b) is written 2(-i + 2j + k); c - b = (-1,2,-1) so d = 2(-i + 2j - k). |d|^2 = 24 is the same, answer 128 unchanged.
- Q17 (printed 57) - typo: vertex A printed (-1,1,0); the lines x+2 = y-1 = z and (x-3)/5 = y/(-1) = (z-1)/1 meet at (-2,1,0). The vectors AB = (5,-1,1), AC = (2,2,2) used later are consistent with (-2,1,0), so 56 is right. Added the last step A^2 = 56 and the other two vertices' parameters.
- Q18 (printed 58) - gap/typo: stray dash in "|a+c| - = 7" and no explicit equation for lambda; the cross product components were not shown. Added both. Answer 16 unchanged.
- Q19 (printed 59) - error: "(|a||c| sin(pi/4))^2" should be |d| (the angle pi/4 is between d and c). (|d||c| sin(pi/4))^2 = 4, which is the "4" the PDF writes. Constants a.b = 5, |a|^2 = 3, |b|^2 = 9 spelled out. Answer 6 unchanged (both roots b.c = 8/3 and 4 give 6).
- Q20 (printed 60) - typo: "m^2 - 3x + 2 = 0" should be m^2 - 3m + 2 = 0. Answer 440 unchanged.
- All other questions (Q3, Q4, Q5, Q6, Q9, Q10, Q13, Q14, Q16) are `pdf`; the working was verified and reproduced.

## Answer key
All 20 printed answers were checked by independent computation (sympy / hand check): none looks wrong.

## Alternates
Alternate solutions given for all 20 questions (Q1-Q20), each verified numerically or symbolically and ending at the same answer. Some are close in spirit to the primary method (a different organisation of the same idea rather than a new idea):
- Q9 (choose axes with b = k), Q10 (tan(theta) shortcut |a x b| = a.b), Q11 (AD = (AB+AC)/2), Q13 (centroid via median 2:1) and Q20 (row dependency R3 = 3R2 - 2R1) are shorter reformulations; the rest use a clearly different technique (unit direction, plane through a line, explicit solving for c, inradius, Apollonius, bisector-length formula, perpendicular components, sum of squared sides, etc.).

### Questions with NO alternate
- None.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide.

## make_ppt.py warnings
- "Q9: only 3 solution bullets - a complete solution normally has more": the PDF's complete working for printed Q49 is three lines (expand, perpendicular term vanishes, evaluate); nothing was dropped. Left as is.
- No "could not convert" notes. 717 equations converted to native PowerPoint equations; 122 slides.

## Skipped / assumed / guessed
- Concepts and levels are self-assigned (nearest anchors cited per question in the ratings file).
- Slides were not rendered or checked visually (no soffice rendering in this environment); the PDF was read from page images (text layer is garbled).
- Marks assumed 4 per question (not printed in the paper).
- Section dividers: Single Correct (Q1-14), Numerical (Q15-19), Single Correct (Q20), following the paper's order.
