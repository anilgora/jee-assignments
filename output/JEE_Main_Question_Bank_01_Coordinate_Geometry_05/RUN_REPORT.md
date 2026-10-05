# RUN REPORT – JEE_Main_Question_Bank_01_Coordinate_Geometry_05 (PDF Q81–Q100, Parabola and Ellipse)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Numbering:** the PDF numbers the questions 81–100; the deck numbers them 1–20 (deck n = PDF n+80; the JSON also stores `q_ref`). Deck Q1–Q11 are numerical (Q1 circle+parabola, Q2–Q11 parabola); Q12–Q20 are single correct (ellipse).
**Marks assumed:** none printed; 4 marks each (JEE Advanced default for single-correct and numerical), stated in the section dividers.

## Difficulty
Marks-weighted difficulty index (all 4 marks; no equivalence-relation or multi-correct adjustment applies): **2.05**.
L1 = 4 (Q6, 15, 17, 18); L2 = 11 (Q1, 2, 4, 5, 10, 11, 12, 14, 16, 19, 20); L3 = 5 (Q3, 7, 8, 9, 13). No L0, L4, L5. Confidence Medium (JEE Main-style questions rated on the Advanced scale; anchors only indicative). Index computed by hand ((4·1+11·2+5·3)/20); the Excel has formulas that were not recalculated (no recalc step here).

## Solutions corrected / written
- Q1 (PDF 81) corrected: typographical slips in the working - $x^3$ for $x^2$, $-124$ for $-12y$, the constant line ends "= 8" instead of "= 0", and "$g^2=6$" for $g^2=c$. Method, λ = −12, the circle and r = 30 are right. Also added the line saying why λ = 4/3 is rejected.
- Q13 (PDF 93) corrected: the middle coefficient of the quadratic in r is printed as $2\sqrt5(2\sqrt5\cos\theta+36\sin\theta)$ but should be $2\sqrt5(25\cos\theta+36\sin\theta)$; and $PA\cdot PB=r_1r_2$ is written without the sign ($r_1r_2=-595/(25+11\sin^2\theta)$, take the absolute value). Answer 338 unchanged.
- Small bridging lines added without changing the PDF's method (source stays pdf): Q2 (shift of origin), Q3 (the sign of the y-term picks t), Q4 and Q5 (the identity $(t-1/t)^2+4=(t+1/t)^2$), Q7 (why QR is parallel to an angle bisector), Q8 (t = 0 chord, count of three chords), Q10 (the chord is a segment; both roots give the same product), Q12 (θ-parametrisation), Q16 (tangency condition), Q18 (monotonicity of C(m,4)), Q19 (circle radius),. No question needed "written".

## Answer key
All 20 answers verified by hand and numerically (plain Python; sympy not installed) and agree with the PDF key: 1 30, 2 15, 3 1328, 4 72, 5 108, 6 10, 7 68, 8 80, 9 36, 10 192, 11 72, 12 D, 13 A, 14 B, 15 D, 16 C, 17 B, 18 C, 19 B, 20 C. No key looks wrong.

## Alternates and Useful Results
- Alternates given for 18 questions: all except Q14 and Q18.
- NO alternate:
  - Q14 - the PDF's one-line argument (base 2a on y = −b, apex at the top of the circle) is already the shortest route; no other genuinely different method exists.
  - Q18 - Pascal's rule plus monotonicity of C(m,4) is the only sensible route to n; the ellipse part is one formula.
- Alternates only partly different (same ingredients, different packaging) - flagged for review: Q6 (contact-point formula instead of double root), Q15 (focus-directrix distance instead of 2b²/a), Q17 (closed form in e and ℓ), Q10 (Vieta-style shortcut after the same chord).
- Useful Result / Pattern given for all 20 questions.

## make_ppt.py warnings
None printed (779 equations converted, 123 slides, 20 questions); no "could not convert" notes.

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step here); recalc of the Excel skipped (no /mnt/skills).
- The PDF text layer is garbled; all questions and solutions were read from page images (90 dpi, Q13 also at 200 dpi).
- Concepts and levels self-assigned; marks assumed as above. The Q3 sign choice (t = −√3/2) is forced by the −64√3 y term in the given circle.
