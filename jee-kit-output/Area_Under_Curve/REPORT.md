# Area Under Curve: revision kit report

- Items in the Quick Review: 29
- Batch XII: 92 graded questions, High threshold 8 -> High 9, Medium 9, Low 11
  - High items (numbers): [1, 3, 4, 5, 6, 9, 10, 13, 17]
- Batch XIII: 83 graded questions, High threshold 8 -> High 10, Medium 7, Low 12
  - High items (numbers): [1, 3, 4, 5, 6, 9, 10, 13, 16, 17]

## Added items
- 2: How to find the area of an unbounded region (a region that extends to infinity)?  [source: J-II:7, J-II:36]
- 24: How to find a parameter when the area of a region (or a relation between areas) is given?  [source: QB:156, QB:167, J-I:29, J-II:16, J-II:17, J-II:18, J-II:22, J-M(XII):22, J-M(XII):27, J-A:9, J-A:15, J-M(XIII):7, J-M(XIII):10, J-M(XIII):43]
- 25: How to find the line (or curve) that divides a region into two parts of given ratio, e.g. bisects its area?  [source: J-I:18, J-I:37, J-I:38, J-II:4, J-II:5, J-II:6, J-II:21, J-M(XII):6, J-M(XII):19, J-A:7, J-A:14]
- 26: How to find the greatest or least value of an area that depends on a parameter?  [source: QB:185, QB:186, J-I:23, J-II:17, J-II:19, J-II:20, J-M(XIII):37, J-M(XIII):38]

## Rephrased items
- 9 (original 8): Can you plot graph of $e^x$, $\ln x$, $\{x\}$, $[x]$, $|x|$?

## Questions with no matching item
- C-II:22
- C-II:23
- C-II:24
- C-II:25
- C-II:26
- C-II:27
- J-II:24
- J-II:26
- J-II:27
- J-II:28
- J-II:30
- J-II:32
- J-A:3

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191]

## Validation warnings
- none

## Item numbering
- Master prompt 1 is final 1. Added item 2 (N4, unbounded region) follows it under "Area Bounded by a Curve".
- Master prompts 2-22 are final 3-23. Added items 24 (N1, parameter from a given area), 25 (N2, line dividing or bisecting an area) and 26 (N3, greatest or least area depending on a parameter) follow under "Variable Area".
- Master prompts 23-25 are final 27-29. All 10 master headings are kept, in the master's order.

## Graded counts and High threshold
- **Batch XII:** J-M(XII) 33 + J-A 16 + QB 43 = 92 graded questions. High threshold = max(2, round(0.091 x 92)) = 8.
  - Counts (master numbers): area between two curves (m2) 56, inequalities (m16) 34, standard conics (m4) 32, e^x / ln x / [x] / {x} / |x| graphs (m8) 24, polynomial graphs (m3) 22, shifted conics (m5) 19, horizontal strips (m12) 18, curve and x-axis (m1) 15, transformations (m9) 12.
- **Batch XIII:** J-M(XIII) 47 + J-A 16 + QB 20 new = 83 graded questions. 23 QB questions are J-M(XIII) questions and are counted once. High threshold = max(2, round(7.6)) = 8.
- **Many graph items are High:** the master places the graph-plotting prompts (3-10) under "Area bounded between two curves". A graph item is mapped as "also used" only when the question cannot be solved without sketching that curve type, as the printed solution does. Low means only "not tested in these questions".

## Question Bank overlap (checked by eye on the page images)
- **XIII**, QB -> J-M(XIII): 164 -> 39, 165 -> 41, 166 -> 42, 167 -> 43, 168 -> 45, 169 -> 29, 170 -> 31, 171 -> 18, 172 -> 19, 173 -> 20, 174 -> 39, 180 -> 47, 181 -> 32, 182 -> 33, 183 -> 34, 184 -> 35, 185 -> 37, 186 -> 38, 187 -> 22, 188 -> 23, 189 -> 24, 190 -> 26, 191 -> 27.
  - QB 164 and 174 are the same question printed twice in the QB, and both equal J-M(XIII) 39.
  - The script missed 171 -> 18 because of the garbled text layer. Every weaker pair it suggested was rejected (for example, 177 is not JM 35 and 175 is not JM 25).
- **XII:** no QB question equals a J-M(XII) question. QB 149-163 and 175-179 appear in neither sheet.

## Added items (coverage check) and the cross-chapter rule
Every candidate was checked with search_master.py, using synonyms ("parameter area", "determination of parameter", "bisect area", "divide area", "ratio of area", "unbounded", "improper", "infinite region", "maximum area", "least area", "optimization", "variable area").
- **24 Find a parameter from a given area:** no match. It is the theory sheet's section 5.1, which has no master prompt. Used by graded J-M(XII) 22, 27; J-A 9, 15; J-M(XIII) 7, 10, 43; QB 156, 167; also J-I 29 and J-II 16-18, 22.
- **25 Line dividing / bisecting an area, ratio of areas:** no match in any chapter. The only hit is the Parabola triangle-ratio prompt, which is a different concept. Used by J-M(XII) 6, 19; J-A 7, 14; J-I 18, 37, 38; J-II 4-6, 21.
- **26 Greatest / least area depending on a parameter:** master prompt 22 covers only the c = (a+b)/2 result, and nothing else matched. This is the theory sheet's section 5.2, questions 2-4. Used by QB 185, 186 (= J-M(XIII) 37, 38); J-I 23; J-II 17, 19, 20.
- **2 Unbounded region (improper integral):** no match. Used by J-II 7 and 36 (also C-I 10, C-II 28). It is not graded in this kit (Low), but it is a standard JEE type.

**Candidates not added** (covered in another chapter, or needed only by Challenger questions):
- **Area function A(x) given -> f = A'(x):** covered in Definite Integration / "Determination of function" (and Method of Differentiation / Leibnitz rule). J-I 51-53, J-M(XII) 31 and J-A 4 are mapped to item 1.
- **Area between a curve and its tangent / normal:** the tangent or normal equation is covered in Tangent & Normal. J-I 21, 22, 34; J-M(XII) 5, 8; J-M(XIII) 19, 26; QB 150, 172, 190 are mapped to area-between-curves (3) plus the graph items they need.
- **Curve obtained from a differential / functional equation first:** covered in Differential Equation and in Continuity & Differentiability / "Determination of Function". J-M(XII) 1, J-A 8, J-M(XIII) 7, J-II 34 and QB 154 are mapped to the area item they then use.
- **Bounds on an area by comparison:** covered in Definite Integration / "Definite Integration by Estimation". J-A 1 -> 1. J-A 3 is a differential-inequality question with no area work, so it is mapped "-".
- **Geometric probability as a ratio of areas:** covered in Probability / "Geometrical Probability". J-M(XII) 15 is mapped to 17 (inequalities);4 (polynomial graph).
- **Largest rectangle in a region** (QB 157): covered in Maxima and Minima / "Geometrical Problems". It is mapped to 17 because the region is given by inequalities.
- **Area of a circular segment ½r²(θ − sin θ)** (J-M(XIII) 34 = QB 183): elementary geometry, mapped to area between curves (3) and standard conics (5).
- **Rational (wavy-curve) inequality region** (QB 169 = J-M(XIII) 29): the wavy curve method is covered in Quadratic Equation. It is mapped to 17.
- **Piecewise constants fixed by differentiability** (QB 178): covered in Continuity & Differentiability.
- **Astroid graph** (J-M(XII) 23): mapped to the curve-sketching / image items. **Ellipse area πab** (J-M(XII) 24) is part of item 5's answer.
- **Challenger only** (excluded from the coverage check): arc length (C-II 22-24, mapped "-"); limit of an area (C-I 5, C-II 8); sum of rectangles (C-I 11); King property applied to an area (C-I 13); reduction relation for A_n (C-II 16).

## Rephrased items (why)
- **OCR slips corrected without a tag:** "ofa", "Howto", "Whatis", "Whatare", "of'a", the stray "|" at line starts.
- **Prompt 8 (tag rephrased):** the OCR reads "e*, In(x), {x}, [x]. [x]". It is read as $e^x$, $\ln x$, $\{x\}$, $[x]$, $|x|$; the second "[x]" is taken to be the modulus $|x|$ (uncertain).
- Prompts 13 and 14 got a question mark; the wording is otherwise the master's.
- **Unchecked:** the master PDF is not in the repo, so the printed wording could not be checked against the page image.

## Questions with no matching item (why)
- **J-II 24, 26, 27, 28, 30, 32:** no area content (pure coordinate geometry, differentiation or functions questions in the exercise).
- **J-A 3:** a differential inequality; no area work.
- **C-II 22-24:** arc length, which is not in the master Quick Review. **C-II 25-27:** a functional-equation paragraph with no area content.

## Uncertain decisions and notes
- **Counts:** J-I 53, J-II 37, J-M(XII) 33, J-A 16, C-I 13, C-II 31, J-M(XIII) 47, QB 43 (numbered 149-191) = 273 questions. The numbering in every exercise is continuous and the last number agrees with the PDF. The contents pages give page numbers only.
- **No DPP:** there is no DPP for this chapter, so the DPP part was skipped.
- **J-A of XIII:** the XIII sheet's J-A has 22 questions. Q1-16 equal XII's J-A (text diff), and Q17-22 (JEE Adv 2025/2026) are new.
  - As in the earlier kits, the skill takes J-A from the XII sheet, so Q17-22 are not graded or in the practice map.
  - They would map to: Q17 -> inequalities (m16);area between curves, conics; Q18 -> parabola-line (m15) and parameter (N1); Q19 and Q21 -> outside the chapter; Q20 -> area between curves;trig, e^x graphs; Q22 -> area in polar form ½∫r²dθ (not in the master) with ellipse.
- **Images:** every question was read from the page images, in six parallel mapping passes.
- **Sets given as {(x,y): ...}** are mapped with main = inequalities (m16), even when the work is a single integral (for example J-M(XIII) 6, 35).
- **Match-the-column / paragraph questions:** J-II 37 is cut off in the PDF; it is mapped from part (A) only. In C-II 29-31 the main item is that of the first area part; in C-II 30 only part (B) is about area.
- **J-II 23:** parts (a) and (b) are coordinate geometry; it is mapped from part (c) only. **J-A 5:** only part (D) is about area.
- **J-II 2:** the region is read as 64 (the area under g on [−4,0] plus the area under f on [0,4]), as the sheet does.
- **Shortcut items (m14, m15)** are added as "also used" only where the printed solution uses them.
- **J-M(XII) 15** (geometric probability): mapped 17;4, without item 25.

## Source errors / oddities found
- **Wrong printed answers or keys:**
  - **J-M(XIII) 46:** the answer line prints 198 (the NTA key), then "Answer by Matrix is (72)". The correct answer is 72. The solution integrates lower minus upper (−72).
  - **J-I 38:** the stem says x = 2, which gives m = 11/6 (option C). The key is A (13/6), which fits the classic version with x = 3/2. Either the stem or the key needs fixing.
  - **J-I 37 (JEE 2011):** the stem prints y = (1 − x²) in English and Hindi. The original problem and the solution use y = (1 − x)². With the printed stem, the answer b = 1/2 is wrong.
  - **J-A 14:** the Hindi options are the English ones in reverse order. The key BCD is right for the English options; for the Hindi options it should be ABC.
  - **J-I 11:** option (B)'s integral also equals 16π, so two options are numerically right.
- **Ill-posed questions (as in the official papers):**
  - **J-M(XII) 22 and J-A 10:** as printed, the regions are unbounded. The keys assume y ≥ 0 and x > 0.
  - **J-M(XIII) 8:** {xy ≤ 8, 1 ≤ y ≤ x²} is unbounded for x ≤ −1. The answer counts only x > 0.
  - **J-M(XIII) 24 = QB 189:** "the parabola" through three points is not unique. A vertical axis is intended.
- **Wrong solutions printed (the answers are right):**
  - **J-I 42:** the solution ends "Area = 2×2 = 4", but the key is 8, and 8 is correct.
  - **J-II 21:** the area under y = x²+1 on [0,a] is written a³/3; it should be a³/3 + a.
  - **J-II 19:** the area 3a³/(2(1+a⁴)) should be a³/(6(1+a⁴)).
  - **C-II 18:** the solution gets a = −1/2, which is outside [0,1]. The correct A' is a(2a−1)/√(1−a²).
  - **C-II 30(D):** the solution ends at f(6) ≤ 2 ln 4, but the key is 2 ln 6 (both bounds hold).
  - **QB 176:** the arcs are treated as straight lines. Two errors cancel, so the answer 12 is right only by coincidence.
  - **QB 169 = J-M(XIII) 29:** the y > 0 and y < 0 cases are swapped.
  - **J-II 22:** the root c = (8+√17)^{1/3} > 2 is not rejected.
  - **J-II 11:** only part (a) is solved.
  - **J-II 37:** the question is cut off (no answer or solution).
  - **C-II 17:** the ratio is never worked out.
- **Typos in working only** (the answers are unaffected):
  - J-I 4, 10, 13, 18, 21, 27, 28, 36, 39, 40.
  - J-II 1, 8, 12, 15, 17, 33.
  - J-M(XII) 1, 10, 11, 17, 24, 32.
  - J-A 4, 5, 8, 12, 15.
  - J-M(XIII) 3, 14, 23 (= QB 188), 37, 43.
  - QB 153, 154, 175, 179.
  - C-I 3, 4; C-II 17, 29.
  - XIII J-A 18, 22.
- **Hindi text garbled by an old font encoding:**
  - J-I 18, 27, 36, 37, 41, 42, 48, 49.
  - J-II 17, 19.
  - J-M(XIII) 2, 7, 10, 11, 23.
  - C-II 11, 18, 25-28.
- **QB 164 and QB 174** are the same question, printed twice.

## Examples verified with sympy
Every Ex line was checked with sympy (scratch script checks.py):
- 7/3; ∫|cos x| over [0,2π] = 4; 3/ln2 − 4/3; x³−3x gives 9/2; sin⁻¹/cos⁻¹ gives √2−1; ln x on [1/e,e] gives 2−2/e.
- Loop 8a²/15; 4/3 (twice); 16ab/3 with a = b = 1/4 gives 1/3; 8a²/(3m³) and 8/3; parabola-line 9/2 and 9 (y²+4x=4, y−2x=2).
- 12√3; shifted parabolas 4/3; tangent region 9; inverse of x³+3x+2 gives 9/2; x² and √x give 1/3; a = 2/3; 2/π; 1/√2; 4π; πab.
- Added items: ∫dx/(1+x²) = π; a³/6 = 9/2 gives a = 3; bisecting line c = 2^{−2/3}; least area 32/3 at k = 2.

## Hindi
New terms are listed in hindi_glossary_additions.md.

## Input files used (not modified)
- **chapters/Area_Under_Curve/Theory.pdf:** theory sheet, 36 pages.
- **chapters/Area_Under_Curve/XII.pdf:** XII sheet, 160 pages.
  - Exercises: J-I 53 (p2-37), J-II 37 (p38-70), J-M 33 (p71-97), J-A 16 (p98-114), C-I 13 (p115-123), C-II 31 (p124-160).
- **chapters/Area_Under_Curve/XIII.pdf:** XIII sheet, 179 pages. Only its J-M (47 questions, p74-108) was used; its J-A (p109-132) was compared with XII's.
- **chapters/Area_Under_Curve/QB.pdf:** JEE Main question bank, questions 149-191 = 43 questions, 34 pages.
- **No DPP** file exists for this chapter.
- **Master prompt list:** .claude/skills/jee-chapter-revision-kit/references/master_index.json.
  - Area Under Curve, master page 92: 25 prompts in 10 headings.
  - The master PDF is not in the repo; there is no jee-inputs/master_index.json.
