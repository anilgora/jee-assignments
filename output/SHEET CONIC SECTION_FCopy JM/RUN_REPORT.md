# Run report — SHEET CONIC SECTION_FCopy JM

Paper: `papers/SHEET CONIC SECTION_FCopy JM.pdf` (52 pages, "Exercise J-M", **64 questions**: JEE Main previous-year conic-section questions, Jan/Apr 2023 and Jan/Apr 2024). 37 single-correct (options) and 27 numerical (no options). The text layer lost the maths symbols, so every page was read as an image. Hindi translations were left out (English deck).

Files: `…_Analysis.pptx` (376 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (stated on the section divider): **4 marks for every question** — single-correct and numerical alike (JEE Advanced defaults; the real JEE Main scheme is +4/−1, not printed in the paper). Total 256 marks. No matching, paragraph or multi-correct questions occur.
- Types: options present → "Single Correct Type"; no options (integer-valued answers, no digit range printed) → "Numerical Type".

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.41** (256 marks). A chapter sheet of JEE Main questions, so it sits below the official Advanced range 2.59–3.21, as expected.
- Questions per level: Level 1 — 4 (Q14, Q39, Q47, Q51); Level 2 — 31 (Q1–Q6, Q8, Q13, Q16, Q19, Q20, Q22–Q25, Q27, Q32, Q34–Q36, Q40, Q42–Q45, Q48, Q54, Q58, Q59, Q62, Q64); Level 3 — 28 (Q7, Q9–Q12, Q15, Q17, Q18, Q21, Q26, Q28–Q31, Q33, Q37, Q38, Q41, Q46, Q49, Q50, Q52, Q53, Q55, Q57, Q60, Q61, Q63); Level 4 — 1 (Q56, chords of a circle bisected by a parabola: three chords, interval of $\alpha$); Levels 0 and 5 — none.
- No equivalence-relation adjustment and no multi-concept MCQ floor (no one-or-more-correct questions).
- Anchors: the bank has only a few conic anchors (2023-P1-Q2, 2023-P1-Q7, 2024-P1-Q4, 2024-P2-Q7, 2024-P2-Q12, 2025-P2-Q16, 2026-P1-Q2, 2026-P2-Q2, 2026-P2-Q13); Main questions were placed relative to these. Confidence Low for Q63 (inconsistent data, see below); Medium for Q7, Q10, Q15, Q17, Q18, Q21, Q26–Q28, Q30, Q31, Q33, Q41, Q46, Q49, Q50, Q52, Q53, Q55–Q57, Q60, Q61; High for the rest.
- Excel built with `build_report.py`; `recalc.py` skipped (no `/mnt/skills`), so formula cells have no cached values until opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q3 — corrected:** the PDF writes $-8k\cdot4k^2=-32k^2$ and solves $32k^2+k-33=0$ (roots $1,-\frac{33}{32}$). It should be $-32k^3$, giving $32k^3+k-33=(k-1)(32k^2+32k+33)$, whose only real root is $k=1$. $P(4,1)$ and the answer 6 stand.
- **Q9 — corrected:** the PDF's $Q\left(\frac4{\sqrt3},\frac1{\sqrt5}\right)$ should be $\left(\frac4{\sqrt5},\frac1{\sqrt5}\right)$ (typo; its determinant already uses $\frac4{\sqrt5}$).
- **Q11 — corrected:** the tangent is written with $\frac{\sqrt{13}}2$ for $\cos30^\circ$; it is $\frac{\sqrt3}2$ (the next line is right).
- **Q14 — corrected:** $2ae=|(1+\sqrt2)-(1+\sqrt2)|$ should be $|(1+\sqrt2)-(1-\sqrt2)|$ (sign typo).
- **Q27 — corrected:** one line has $\frac1{OP^2}=\frac1{48}$; $OP^2=\frac{48}7$, so $\frac7{48}$ (the next line already uses $\frac7{48}$).
- **Q38 — corrected:** the simplified chord $\frac x5+\frac y4=\frac14$ is wrong; $T=S_1$ gives $\frac x{25}+\frac y{40}=\frac1{20}$, i.e. $8x+5y=10$ (the following lines already use this).
- **Q43 — corrected:** "Putting $y^2=2x^2$" should be $y^2=3x^2$ (the curve in the question); everything after is consistent with $3x^2$.
- **Q60 — corrected:** $a^2(e-1)^2=4\Rightarrow a(e-1)^2=2$ should be $a(e-1)=2$ (then $e-1=\frac13$ as the PDF uses).
- **Q61 — corrected (statement and last line):** the statement prints $\alpha^2+\beta^2$; with $\beta=105$ that is $11091$, no option. The key (C) 171 and the PDF's own last line ($66+105$) correspond to $\alpha^2+\beta$ (as in the original JEE question). The deck quotes the question with $\alpha^2+\beta$. The PDF's "$a=6$" is also $a^2=6$.
- **Q63 — corrected (see answer key below):** the PDF reaches $a=2$, $b^2=9$, then uses the directrix data to get $e=\frac{\sqrt3}2$ and calls the question "bonus". The deck completes the working with the latus-rectum + tangency data ($e^2=\frac{13}4$, contact point $(4,3\sqrt3)$, $m=48$), giving 61.
- **`pdf` with additions (not corrections):** gaps in the PDF filled with extra lines — Q13 (which of the two points with tangent slope $-\frac32$ is nearer), Q32 (the final squaring, $116$; the PDF stops at $2\sqrt{29}$), Q47 (the PDF ends at $e=\sqrt{3/2}$, question asks $e^2$), Q56 (the $t=0$ chord is the third chord, which the PDF leaves implicit), Q59 (evaluation of $\int\sqrt{18-3y^2}\,dy$), Q10 (the minimisation at $\tan^2\theta=\frac b2$ is stated, not derived, in the PDF; the alternate gives it by Cauchy–Schwarz), Q53 (the PDF's "f" in "$3(f+\frac1t)^2$" read as $t$).
- **Q40 — statement fixed (solution `pdf`):** the printed statement has $B(\beta,0)$ (both points on the $x$-axis, which would make $A=B$); the PDF's solution uses $B\left(0,\frac{50}7\right)$, as in the original JEE question, so the deck quotes $B(0,\beta)$.
- All other questions — `pdf`: every step was checked and reproduced.

## Answer key
Every answer was verified by exact/numerical computation (sympy). The printed key is right for all 64 questions, with these remarks:
- **Q61:** key 171 is right for $\alpha^2+\beta$, not for the printed $\alpha^2+\beta^2$ (see above).
- **Q63:** the printed data are inconsistent (the directrices $x=\pm\frac4{\sqrt3}$ cannot go with the hyperbola fixed by the latus rectum 9 and the tangent $y=\sqrt3x-\sqrt3$, which has directrices $x=\pm\frac4{\sqrt{13}}$). Key 61 comes from latus rectum + tangency only; kept as the answer. The question is flawed as printed.
- Keys: Q1 D, Q2 D, Q3 B, Q4 B, Q5 B, Q6 10, Q7 146, Q8 16, Q9 A, Q10 B, Q11 39, Q12 C, Q13 B, Q14 D, Q15 216, Q16 A, Q17 D, Q18 B, Q19 292, Q20 16, Q21 32, Q22 D, Q23 C, Q24 C, Q25 D, Q26 C, Q27 C, Q28 C, Q29 9, Q30 2, Q31 306, Q32 116, Q33 8, Q34 12, Q35 B, Q36 192, Q37 72, Q38 A, Q39 D, Q40 A, Q41 A, Q42 D, Q43 432, Q44 A, Q45 B, Q46 B, Q47 D, Q48 B, Q49 182, Q50 51, Q51 C, Q52 72, Q53 108, Q54 10, Q55 68, Q56 80, Q57 36, Q58 C, Q59 B, Q60 D, Q61 C, Q62 A, Q63 61, Q64 40.

## Alternate solutions and useful results
- **Alternates: 59 of 64 questions** (all except Q33, Q43, Q44, Q58, Q62). Each was checked against the answer, numerically or symbolically where possible. Highlights: Q10 Cauchy–Schwarz (max normal distance $a-b$); Q16 both centroid coordinates, no line needed; Q17 right-angle incentre $(r,r)$; Q18 $\frac1{PF}+\frac1{QF}=\frac1a$; Q21 tangent length = power of a point; Q23 Thales; Q27 $\frac1{OP^2}+\frac1{OR^2}=\frac1{a^2}+\frac1{b^2}$; Q28 pole at distance $\frac{r^2}d$; Q29 equilateral triangle $FB_1A_1$; Q30 gradients (orthogonality gives confocal); Q31 Pell equation; Q38 walking from the mid-point; Q45 focal-triangle area $b^2\cot\frac\theta2$ + median formula; Q46 sum/difference of focal distances; Q47/Q48 $e_E^2+e_H^2=2$; Q52/Q53 $l\,d^2=4a^3$; Q56 Thales circle on $OA$; Q57 $f=y^2-4ax$ restricted to a line; Q59 ellipse→circle scaling (a $60^\circ$ sector); Q60 radius $c-a$; Q61/Q63 $PF_1PF_2=OP^2+\text{conj}^2-\text{trans}^2$; Q64 median halves the area.
- **Questions with NO alternate (5), one line each:**
  - Q33 — after the slope-form tangents from $P$ ($m=1,-\frac34$) the only way to $Q$ is to intersect the two chosen tangents; contact-point or polar approaches reduce to the same two linear equations.
  - Q43 — substitution of $y^2=3x^2$ in both conics is the only route (the rejection of $b=4$ is forced); the rectangle area is a one-line follow-up.
  - Q44 — the foci being on the ellipse forces $a=5$ and $e_2=\frac45$ gives $b$; every other route (parametric, $c$-based) is a rewording.
  - Q58 — the circle-on-diameter comparison (or putting $A$ on the circle) is a single coefficient comparison; no different idea.
  - Q62 — $c=5$, $a_H=\frac c{e_H}$, $b_H^2=c^2-a_H^2$ is the only sensible route; any shortcut is the same computation.
- A few alternates are lighter variations rather than radically different ideas, flagged for review: Q2 (parametric tangent instead of slope form), Q13 (slope-form tangent and contact-point formula instead of the PDF's parametric derivative), Q15 (implicit slope; segment length $x_1\sqrt{1+m^2}$), Q20 (specialisation to one convenient pair, valid because the answer is constant), Q36 (completing the square on the $\alpha$ quadratic), Q37 (trigonometric distance), Q51 (midpoint slope), Q54 (contact-point formula), Q55 (half-angle slopes), Q5 (numerical elimination of options).
- **Useful results given for all 64 questions.**

## make_ppt.py warnings and notes
- No warnings and no "could not convert" messages: 2067 equations converted to native PowerPoint equations; 376 slides. (No errors on valid/invalid `solution_source`, corrected-without-note, short-solution or missing-key-idea checks.)
- Rendering/thumbnails were skipped (no soffice/`/mnt/skills`); the deck was not visually inspected.

## Skipped / assumed / guessed
- Concepts self-assigned; marks assumed as above (all 4); one section divider for the whole paper.
- Levels for a JEE Main sheet were judged against Advanced anchors (hence 1–4 only); please review if you want a Main-specific scale.
- Hindi text of the PDF omitted.
- Q40 and Q61 statements were fixed to the original JEE wording (see above); Q63's inconsistent directrix datum is quoted as printed and flagged.
