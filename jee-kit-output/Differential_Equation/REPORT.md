# Differential Equation: revision kit report

- Items in the Quick Review: 39
- Batch XII: 144 graded questions, High threshold 13 -> High 3, Medium 16, Low 20
  - High items (numbers): [13, 31, 39]
- Batch XIII: 108 graded questions, High threshold 10 -> High 3, Medium 15, Low 21
  - High items (numbers): [13, 25, 31]

## Added items
- 4: How to fix the constant when, instead of $y(x_0)$, a limit or boundedness condition is given (e.g. $y$ bounded, $y\to0$ as $x\to\infty$)?  [source: J-M(XII):14, J-M(XII):63, J-M(XIII):4, J-M(XIII):36, J-M(XIII):65, QB:125, QB:140, J-II:49, C-I:4]
- 12: How to solve simple second order differential equations?  [source: J-I:17, QB:127]
- 16: How to solve rate problems (growth and decay, Newton's law of cooling, mixture in a tank) by forming a differential equation?  [source: J-I:26, J-I:33-36, J-II:8, J-II:9, J-II:36, J-II:37, J-M(XIII):34, C-I:2, C-II:16, C-II:17, C-II:20]
- 32: How to handle a differential inequality such as $f'(x)>2f(x)$?  [source: J-A:9, C-II:21]

## Rephrased items
- 11 (original 10): What are the various types of differential equations?
- 18 (original 15): What do you mean by initial ordinate of a line (tangent)?
- 20 (original 17): How to solve $\frac{dy}{dx}=f(ax+by+c)$?
- 21 (original 18): How to solve $\frac{dy}{dx}=\frac{a_1x+b_1y+c_1}{a_2x+b_2y+c_2}$ if $a_2+b_1=0$?
- 38 (original 34): Write three results of exact differential.

## Questions with no matching item
- J-II:54
- J-II:55
- J-II:57
- J-II:58

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]

## Validation warnings
- none

## Item numbering
- Master prompts 1-3 are final 1-3. Added item 4 (N3, constant fixed by a limit / boundedness condition) follows under "Introduction".
- Master 4-10 are final 5-11. Added item 12 (N4, simple second order DEs) follows under "Elementary Types".
- Master 11-13 are final 13-15. Added item 16 (N1, rate problems) follows under "Variable Separable". Master 14-28 are final 17-31.
- Added item 32 (N2, differential inequality) follows under "Linear Differential Equation". Master 29-35 are final 33-39.
- All 11 master headings are kept, in the master's order.

## Graded counts and High threshold
- **Batch XII:** J-M(XII) 64 + J-A 20 + QB 60 = 144 graded questions. High threshold = max(2, round(0.091 x 144)) = 13.
  - Counts of the top items: 31 (solve linear DE) 67, 13 (variable separable) 38, 39 (exact grouping) 16, 25 (y = vx) 12, 15 (integral identity) 10.
- **Batch XIII:** J-M(XIII) 65 + J-A 20 + QB 23 new = 108 graded questions. 37 QB questions are J-M(XIII) questions and are counted once. High threshold = max(2, round(9.8)) = 10.
  - Counts of the top items: 31 = 59, 13 = 26, 25 = 10, 15 = 7, 35/39 = 6.
- Only 3 items are High in each batch. The chapter's graded questions are dominated by "solve a linear DE", so the 9.1% threshold is high. That is the fixed rule, not a judgement.
- Low means only "not tested in these questions".

## Question Bank overlap (checked by eye on the page images)
- **XIII**, QB -> J-M(XIII): 105-115 -> 45, 46, 48-56; 116 -> 57; 117-123 -> 27-33; 124 -> 35; 125 -> 36; 133-140 -> 58-65; 141-145 -> 37-41; 146 -> 42; 147 -> 43; 148 -> 44.
  - The script missed QB 116 = JM 57 and paired QB 146 with JM 31 (wrong; it equals JM 42). Both were found by eye.
  - Twins have identical mappings.
- **XII:** no QB question equals a J-M(XII) question. Every pair the script suggested (all only "possible") was checked by eye.

## Added items (coverage check) and the cross-chapter rule
Every candidate was checked with search_master.py, using synonyms ("growth decay", "cooling", "mixture", "rate of change", "population", "bacteria", "temperature", "differential inequality", "f'(x) >", "boundedness", "limit of solution", "higher order differential", "reduce order", "dy/dx = p", "constant solution"). None matched in any chapter.
- **16 Rate problems** (growth / decay, Newton's cooling, mixture): J-I 26, 33-36; J-II 8, 9, 36, 37; J-M(XIII) 34; also C-I 2, C-II 16, 17, 20. The theory sheet has a section on mixture problems (4.2) with no master prompt.
- **32 Differential inequality** (f' > 2f -> (e^{-2x}f)' > 0): J-A 9 (graded); also C-II 21.
- **4 Constant fixed by a limit / boundedness condition:** J-M(XII) 14, 63; J-M(XIII) 4, 36, 65; QB 125, 140; J-II 49; C-I 4; C-II 6. These questions keep their solving item as main; item 4 is added as "other".
- **12 Simple second order DEs** (integrate twice; multiply y'' = f(y) by 2y'): J-I 17, QB 127 (graded). C-II 31(C) also uses it.

**Candidates not added** (covered in another chapter, or needed only by Challenger questions):
- **DE obtained from a limit** (derivative definition / L'Hospital): J-A 11, 20; J-M(XIII) 40, 60; QB 135, 144. Covered in Method of Differentiation / "Differentiation by first principle" and "L'Hospital Rule". These questions are mapped to the DE item that solves them.
- **Functional equation converted to a DE** (f(x+y) = ...): QB 98, J-A 13, J-I 50; C-II 25-27. Covered in Continuity & Differentiability / "Determination of Function". Mapped to the solving item.
- **A constant definite integral treated as an unknown k** (J-M(XIII) 13): covered in Definite Integration / "Determination of function". Mapped to 31.
- **Verifying that a function is a solution** (J-I 5): mapped to item 2 (general solution).
- **Interval of existence of a solution** (J-M(XII) 9): a one-off; mapped to the homogeneous items 26;25.
- **Challenger only** (excluded from the coverage check): a first-order DE of higher degree solved by factorising in p (C-II 2); a piecewise-defined DE (C-I 15); equilibrium solutions (C-I 18); a limit relation converted to a DE (C-II 22).

## Rephrased items (why)
- **OCR slips corrected:** "ofa", "ifinformation", "Whatare the variious", "Howto", "Whatisthe", "Areall", the stray "|" and "—" at line starts, the stray "d" after prompt 16.
- **Maths restored:**
  - Prompt 17, OCR "x = f(ax+by+c)? dy ax+by+c": read as dy/dx = f(ax+by+c), per theory sheet 2.2.
  - Prompt 18, OCR "dx a,x+b,y+e, Ifa, +b, =0": read as dy/dx = (a1x+b1y+c1)/(a2x+b2y+c2) with a2 + b1 = 0, per theory sheet 2.3.
  - Prompt 15: "initial ordinate of a line" is shown as "(tangent)", because the theory sheet uses it for the tangent's y-intercept.
- **Other changes:**
  - Prompt 10 has only grammar changes.
  - Prompt 34 ("three results") is answered with nine standard results, all from the theory sheet's list of 13.
- **Unchecked:** the master PDF is not in the repo, so the printed wording could not be checked against the page image.

## Questions with no matching item (why)
- **J-II 54, 55, 57, 58:** paragraph follow-ups. They ask about area, the type of function, and a shortest distance. The DE work is in J-II 53 and 56, which are mapped.

## Uncertain decisions and notes
- **Counts:** J-I 60, J-II 59, J-M(XII) 64, J-A 20, C-I 21, C-II 33, J-M(XIII) 65, QB 60 (numbered 89-148) = 382 questions.
  - The contents pages give page numbers only.
  - In every exercise the numbering is continuous, and the last number agrees with the PDF.
- **No DPP:** there is no DPP for this chapter; the DPP part was skipped.
- **J-A of XIII:** the XIII sheet's J-A has 24 questions. Q1-20 equal XII's J-A, and Q21-24 (JEE Adv 2025/2026) are new.
  - As in the earlier kits, the skill takes J-A from the XII sheet, so Q21-24 are not graded or in the practice map.
  - They would map to Q21 -> 31 (linear), Q22 -> 25 (homogeneous), Q23 -> 13 (separable), Q24 -> 31.
- **Images:** every question was read from page images, in eight parallel mapping passes.
- **Method choice where two methods work** (the main item follows the printed solution):
  - J-M(XII) 5, 14, 29: linear, but grouped as exact -> 39.
  - J-M(XII) 30, 37, 53: homogeneous, but grouped -> 39.
  - J-M(XIII) 19 -> 31 (also separable).
  - J-M(XIII) 30 -> 25 (could be 38).
  - J-M(XIII) 2 -> 25;34.
  - J-I 23 -> 25 (polar also works).
  - J-I 30 -> 25 (or linear).
  - J-I 56 -> 39 (or Bernoulli).
  - J-II 43, 44 -> 39.
  - J-II 45 -> 35;31.
  - C-I 13, 17 -> 35;31.
  - QB 100 -> 39 (or 25).
- **Paragraph and matrix-match questions** are mapped once, by the dominant DE concept:
  - J-II 59 -> 39;34.
  - C-II 26, 27, 29, 30 are really AOD or limits work; they are mapped to the DE that the paragraph needs.
  - C-II 31 -> 11;13,30,31,39.
  - C-II 32, 33: only one row is a DE row -> 13.
- **J-A 5 -> 10:** the sheet itself calls this question controversial (P and Q are not unique).

## Source errors / oddities found
- **Wrong printed answers:**
  - **J-I 29:** the solution is y = K(1+cos x). f(π/2) = −1 gives K = −1, so f(0) = −2. The printed answer (A) 2 is wrong, and no option is right. The printed solution takes c = 0, which contradicts f(π/2) = −1.
  - **QB 104:** the printed answer is B, but the book's own solution ends at (4−√2)/14, which is option A. A was confirmed by re-solving.
  - **C-I 16:** option (D) is garbled ("∫y dx = x"). If it was meant to read −π (the true value), the answer would be AD.
- **Ill-posed or bonus questions:**
  - **J-M(XII) 1:** it needs √(1−y²) = 2e³ > 1, so (y(3))² = 1 − 4e⁶ < 0. The printed D is the official key.
  - **J-M(XII) 25:** at x = 5 the identity forces φ(5) = 0, but the solution uses 19. The official answer 4 follows from the solution.
  - **J-M(XII) 62:** at x = 3 the area is 0, but (3/3)³ = 1. The official answer 6 follows from the solution.
  - **J-M(XIII) 25 and 36 (= QB 125):** officially Bonus. In Q36 the data are inconsistent.
  - **J-M(XIII) 21:** printed as a numerical blank, but the answer is given as "B". The value is 2.
- **Wrong solutions printed:**
  - **J-M(XIII) 49 = QB 108:** the solution printed is the solution of the next question. The answer B (−3/e) was checked.
  - **J-M(XIII) 10:** the solution drops a factor 2. The correct (3t−t³)² = 4x³ gives answer A.
  - **J-M(XIII) 42 = QB 146:** the solution stops part-way. Completing it agrees with the printed answer.
- **Wrong or sloppy working with right answers:**
  - **J-I 2:** the solution uses a 1-constant family; the family really has 2 constants.
  - **J-I 33:** the English stem asks for V(t); the options and the Hindi stem use V(T).
  - **J-I 38:** the Hindi option A differs from the English.
  - **J-II 24:** dt/dx is printed as (3t+1)/(2(t+1)); it should be (3t+1)/(2t+1).
  - **J-II 29:** only the "+" case is worked out.
  - **J-II 31:** drops the minus case.
  - **J-II 34, 39, 41:** sign errors; in 41 they cancel.
  - **J-II 50:** the solution says "centres on the y-axis"; they are on the x-axis.
  - **J-II 52:** the answer assumes y = x⁻³; y = x³ (external division) also fits.
  - **J-M(XII) 46:** the solution ignores the branch for x > π/4. The answer 2 is still right.
  - **J-M(XII) 60:** the Hindi text says x < −1, the English says x > −1.
  - **C-II 6:** never uses the boundedness condition (c = 0).
  - **C-II 13:** "(e, 1/e)" should be (1, 1/e).
  - **C-II 24:** one wrong intermediate step.
  - **C-II 32(C):** the sign change at a maximum is reversed.
  - **C-II 33:** |x+1| should be |x−1|, and c^{x+c} should be e^{x+c}.
  - **J-A 19:** a non-standard integrating factor 1/|x²−5|.
  - **XIII J-A 21:** y₃ is misprinted.
  - **C-I 21:** uses ln x² on x > 0.
- **Typos only** (the answers are unaffected):
  - J-I 15, 19, 21, 28, 49, 51, 53, 59.
  - J-II 1, 2, 17, 19, 23, 26, 28, 30, 36, 37, 38, 54, 57.
  - J-M(XII) 5, 7, 15, 18, 32, 35, 37, 43, 53, 56, 59, 61, 64.
  - J-M(XIII) 16, 22, 37, 45, 50, 51, 59, 60, 61, 62; QB twins 109, 110, 114, 134, 137.
  - J-A 7, 10 ("Λετφ" for "Let f"), 16.
  - C-I 12, 20.
- **No printed answer** ("show that" questions): J-II 20, 25.
- **Theory sheet:** the text layer of the Bernoulli example (4.3.1 Q1) is garbled. The kit derives the linear equation itself (z' + xz = −x³, with z = 1/y) and checks it with sympy; this agrees with the sheet's printed answer.

## Examples verified with sympy
Every Ex line was checked with sympy (scratch script checks.py):
- **Formation:**
  - y = Ae^{2x}+Be^{-2x}+C -> y''' = 4y'.
  - Circles touching the x-axis at O -> (x²−y²)y' = 2xy.
- **Variable separable:**
  - (x²+1)(y²+1) = C.
  - xy = 6 (bisected tangent).
  - f = 2e^{e^x−1} − 1 (integral identity).
  - tan⁻¹(x+y) = x + C.
  - 3xy − y² − 2x² = c.
  - Polar example √(x²+y²) + y/x = C.
  - Normal = polar radius -> m = ±x/y.
- **Homogeneous:**
  - y = x ln|x| + cx.
  - Intersection (2, 1).
- **Linear and reducible:**
  - xy = x⁴/4 + C.
  - Bernoulli z = 2 − x² + Ce^{−x²/2}.
  - tan y = x − 1 + Ce^{−x}.
- **Orthogonal trajectories:** x² + y² = cx; the product of slopes is −1.
- **Exact:** x² − x/y = c, with c = 2 at (2,1), so y(1) = −1.
- **Added items:**
  - N(0) = 1000, N(2) = 1200, and the doubling time gives 2000.
  - y = e^{−x}/2 + Ce^x.
  - y'' = 6x.
  - f' = 2f -> Ce^{2x}.

## Hindi
- New terms are listed in hindi_glossary_additions.md.
- IF is kept as "IF" inside the mathematics, as in the Indefinite / Definite Integration kits. The Hindi text calls it समाकलन गुणक.

## Input files used (not modified)
- **chapters/Differential_Equation/Theory.pdf:** theory sheet, 46 pages.
- **chapters/Differential_Equation/XII.pdf:** XII sheet, 240 pages.
  - Exercises: J-I 60 (p2-40), J-II 59 (p41-105), J-M 64 (p106-167), J-A 20 (p168-186), C-I 21 (p187-206), C-II 33 (p207-240).
- **chapters/Differential_Equation/XIII.pdf:** XIII sheet, 241 pages. Only its J-M (65 questions, p106-161) was used.
- **chapters/Differential_Equation/QB.pdf:** JEE Main question bank, questions 89-148 = 60 questions, 59 pages.
- **No DPP** file exists for this chapter.
- **Master prompt list:** .claude/skills/jee-chapter-revision-kit/references/master_index.json.
  - Differential Equation, master pages 90-91: 35 prompts in 11 headings.
  - The master PDF is not in the repo; there is no jee-inputs/master_index.json.
