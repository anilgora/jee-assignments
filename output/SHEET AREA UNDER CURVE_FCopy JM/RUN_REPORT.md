# Run report — SHEET AREA UNDER CURVE_FCopy JM

Paper: `papers/SHEET AREA UNDER CURVE_FCopy JM.pdf` (35 pages, "Exercise J-M", 47 questions: JEE Main previous-year area questions, Jan/Apr 2023 and Jan/Apr 2024; Q1–Q8, Q16–Q21, Q28–Q31, Q39–Q45 are single-correct, the rest numerical). The text layer lost the maths symbols, so every page was read as an image. Hindi translations were left out (English deck).

Files: `…_Analysis.pptx` (274 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **No blueprint was used** (`blueprints/` has no file for this paper). **Concepts self-assigned (no blueprint) - please review.**
- The paper prints no marks. Assumed (stated on the section divider): **4 marks** for every question — single-correct and numerical alike (JEE Advanced defaults; the real JEE Main scheme is +4/−1, not printed in the paper). No matching, paragraph or multi-correct questions occur.
- Question types: options present → "Single Correct Type"; no options (integer-valued answers, no digit range printed) → "Numerical Type".

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **2.09** (total 188 marks). It is a chapter sheet of JEE Main questions, so it sits below the official Advanced range 2.59–3.21, as expected.
- Questions per level: Level 1 — 9 (Q1, Q9, Q15, Q16, Q19, Q28, Q30, Q35, Q46); Level 2 — 25 (Q2, Q3, Q5–Q8, Q10–Q13, Q17, Q18, Q20, Q21, Q23, Q25, Q31, Q33, Q36, Q40, Q41, Q43–Q45, Q47); Level 3 — 13 (Q4, Q14, Q22, Q24, Q26, Q27, Q29, Q32, Q34, Q37, Q38, Q39, Q42); Levels 0, 4, 5 — none.
- No equivalence-relation adjustment and no multi-concept MCQ floor (no one-or-more-correct questions).
- Anchors: the bank has only Advanced area questions (2021-P1-Q2, 2024-P2-Q2, 2025-P2-Q2 are L3, 2026-P2-Q15 is L2); Main questions were placed relative to these. Confidence Medium for Q4, Q7, Q11, Q14, Q22–Q24, Q26, Q27, Q29, Q32, Q34, Q37–Q39, Q42; High for the rest; none Low.
- Excel built with `build_report.py`; `recalc.py` skipped (no `/mnt/skills`), so formula cells have no cached values until opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q8 — corrected (assumption stated):** as printed ($xy\le8,\ 1\le y\le x^2$, no sign condition) the set also contains all points with $x\le-1$, $1\le y\le x^2$ (there $xy<0$), so its area is infinite. The PDF silently uses $x>0$; the first bullet now says so. Key (B) is right for that region.
- **Q24 — corrected:** the PDF says "there can be infinitely many parabolas through the given points". False for $y=p(x)$ (a quadratic polynomial is unique through three points: $p=1-x^2$). Derivation replaced; the PDF's area work and the answer 16 are right.
- **Q29 — corrected:** the PDF's case "(i) $y>0$" requires the fraction $<0$ and gives $x\in(1,2)\cup(3,4)$ — wrong sign (for $y>0$ it must be $>0$, i.e. $(0,1)\cup(2,3)$). Its final sum covers all four intervals so $\frac{32}{3}$ is right. Cases reassigned correctly.
- **Q46 — corrected:** the PDF subtracts in the wrong order ($\int(2x^2-12x)$, value $-72$) and then writes "$36(-2)=72$"; its printed key is **198** (wrong; the PDF itself adds "Answer by Matrix is (72)"). Corrected working integrates $12x-2x^2$ and gives 72.
- All other questions — `pdf`: checked step by step and reproduced. Where the PDF skips arithmetic (Q10 evaluation of the second area, Q32 the three integrals, Q42 the cancellation of $\sqrt3$ terms) the omitted lines were filled in, and in Q7 one line was added saying the normal to a circle passes through the centre; these are additions, not corrections. In Q3 the print of "area of A" is hard to read; the deck shows quarter-disc minus triangle, $\pi-1$, which is the PDF's result.

## Answer key
Every answer was checked by numerical integration (and exact computation). **Q46's printed key (198) is wrong; correct answer 72.** All others are correct: Q1 B, Q2 B, Q3 D, Q4 D, Q5 A, Q6 D, Q7 D, Q8 B (first quadrant, see above), Q9 36, Q10 600, Q11 22, Q12 25, Q13 72, Q14 125, Q15 62, Q16 A, Q17 C, Q18 A, Q19 C, Q20 A, Q21 D, Q22 5, Q23 17, Q24 16, Q25 27, Q26 16, Q27 42, Q28 A, Q29 A, Q30 C, Q31 D, Q32 119, Q33 304, Q34 171, Q35 164, Q36 5, Q37 7, Q38 8, Q39 D, Q40 B, Q41 B, Q42 D, Q43 D, Q44 A, Q45 C, Q46 72, Q47 16.

## Alternate solutions and useful results
- **Alternates: 45 of 47 questions** (all except Q5 and Q43). Each was verified against the answer, numerically where possible. Examples: Q1 $y$-slices with $\frac{|a|\Delta^3}{6}$; Q4 circular segment with $\theta=\sin^{-1}\frac2{\sqrt7}$ (no identity needed); Q6 difference of squares; Q7 area + point on circle gives $a$, then similar triangles; Q11 whole parabola-chord area minus the small piece; Q13 big triangle minus parabola; Q20 symmetry about $x=\frac\pi4$; Q21 complement of the $y<1$ part; Q22 vertical slices; Q29 one admissible sign of $y$ per $x$ so area $=\int_0^4 2\sqrt x\,dx$; Q32 horizontal slices (no radicals); Q34 direct integration; Q37 Archimedes; Q38 AM-GM on $k+\frac4k$; Q39 golden-ratio reduction; Q42 triangle minus area under curve; Q47 shift by $\pi$ links it to Q20.
- **Questions with NO alternate (2), one line each:**
  - Q5 — the only other organisations are re-groupings of the same $\int(\sin x-|\cos x-\sin x|)\,dx$ calculation; a bounding/estimation argument cannot separate the options rigorously without the same integral.
  - Q43 — the area is the single integral $\int_1^2\left(\frac1x-\frac a{x^2}\right)dx=\ln2-\frac a2$; no different method exists.
- **Useful results given for all 47 questions.**
- Several alternates are changes of slicing (vertical vs horizontal), complement/subtraction, or formula-based ($\frac{|a|\Delta^3}{6}$); each is a different calculation from the main solution but they are not all radically different ideas.

## make_ppt.py warnings and notes
- No warnings and no "could not convert" messages: 1441 equations converted to native PowerPoint equations. 274 slides.
- Rendering/thumbnails were skipped (no soffice/`/mnt/skills`); the deck was not visually inspected.

## Skipped / assumed / guessed
- Concepts self-assigned; marks assumed as above (all 4); one section divider for the whole paper.
- Levels for a JEE Main sheet were judged against Advanced anchors (hence 1–3 only); please review if you want a Main-specific scale.
- Hindi text of the PDF omitted.
