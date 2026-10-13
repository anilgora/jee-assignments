# Run report - SHEET CIRCLE LINE_FCopy C2 (Exercise C-II, Circle & Line)

Deck: `SHEET CIRCLE LINE_FCopy C2_Analysis.pptx` (170 slides, 27 questions, 981 native equations). Also: `_content.json`, `_ratings.json`, `_difficulty.xlsx`.

## Difficulty
- Marks-weighted difficulty index (adjusted = unadjusted; no equivalence-relation or MCQ-floor cases): **2.20**
- Questions per level: Level 1 = 3 (Q2, Q21, Q23); Level 2 = 16; Level 3 = 8 (Q3, Q6, Q12, Q13, Q17, Q19, Q26, Q27); no Level 0, 4 or 5.
- Chapter-sheet, so no official-paper spread is expected (JEE Advanced 2021-2026: 2.59-3.21).

## Blueprint
No blueprint was available (`blueprints/` has only a README). **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper), JEE Advanced defaults: subjective / numerical Q1-20 = 4 each; paragraph-based single correct Q21-26 = 3 each; matching Q27 = 3. Stated in the section dividers. Type labels: "Subjective Type" for prove / find-the-equation questions and "Numerical Type" for single-number answers (Q4, Q5, Q13, Q15, Q16, Q17); in the ratings file these are "Numerical" (Q4, Q16 "INT"). Question numbers 1-27 are the paper's own.

## Solutions whose source is corrected or written
- Q3 (corrected): the PDF's part (iii) (harmonic mean) ends with an unexplained radical-axis step after a garbled harmonic-conjugate argument; the answer 4x+3y=24 is right. Replaced by the explicit substitution M = 24(x,y)/(x^2+y^2) into the circle on OC. Parts (i), (ii) as in the PDF.
- Q21 (written): the PDF only says "refer figure" with the answer (B); the reasoning is written out.
- All other questions: source `pdf` (PDF working verified step by step, numerically where useful; Q3-Q27 final answers checked). Some PDF text was garbled by the text layer and was read from page images (Q6, Q14, Q17, Q21, Q22, Q26); Q10 had an added line checking that the minimum radius is attained (k = -3/2), and Q5 an added line excluding external tangency.

## Answer key
- All final answers match the PDF's key (Q14 key reads "= 3^2", i.e. radius 3, which is right; Q17 key is sqrt 3).
- Layout slip in the PDF: the line "Ans. 75 sq. unit" is printed under Q6, but it is the answer of Q5 (Q5 has an empty "Ans."); Q6 is a proof. Used 75 for Q5.
- The Q22 stem in the paper has no lead-in; it is read as the value at the point of A ∩ B ∩ C (as in the PDF's solution).
- The figure of Q24-26 is not reproduced in the deck; the question stem describes it in words.

## Alternate solutions and useful results
- Alternates (genuinely different method, checked against the answer): Q1 (polar / CM·CP = r²), Q2 (general circle through three points), Q3 (polar form of the secant), Q5 (trigonometric: sin α = 3/4), Q6 (Ptolemy, apex on y = x), Q7 (axes are the only tangents from the origin), Q8 (power of a point on AB), Q9 (centre on the normal), Q10 (r² as a quadratic in k), Q11 (powers equal), Q12 (half-angle between the lines), Q13 (distances to both tangents), Q14 (rotation of AC by ±45°), Q15 (difference of triangles), Q16 (intersecting chords), Q17 (law of cosines, r₁r₂ = OP² tan²φ), Q18 (Pitot), Q19 (Euler OI² = R² - 2Rr), Q20 (Heron), Q21 (algebraic roots), Q22 (expand with the circle equation), Q23 (square OT₁PT₂), Q24 (limiting cases), Q25 (tangent T = 0 form), Q26 (direct coordinates at θ = π/4), Q27 (line of centres).
- Weaker alternates: Q26 (only changes the order of work: plugs θ = π/4 first) and Q27 (new method only for parts A and D; B and C reuse the right-triangle conditions of the main solution); Q12 and Q17 share the second half of the main solution but differ in the key step.
- **No alternate: Q4** - the only route is "radii form a G.P. with ratio 1/√2"; the self-similarity form S = r + S/√2 is the same computation reworded, so it was not padded.
- useful_results given for all 27 questions.

## make_ppt.py warnings
- First build: "Q23: only 3 solution bullets" (fixed by writing the PDF's steps out in 4 bullets) and "Q24 / Q25: very long question - font reduced to 22 pt" (fixed by shortening the paragraph text). The final build prints no warnings and no "could not convert" messages.

## Skipped, assumed or guessed
- Rendering / thumbnails were not done (no LibreOffice step in this environment); the xlsx formulas have no cached values (recalc.py not available) - they calculate when opened in Excel.
- Levels are my own ratings with the calibrated skill; those with Medium confidence (about half) are the most likely to be moved.
