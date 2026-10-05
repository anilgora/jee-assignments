# RUN REPORT – JEE_Main_Question_Bank_01_Coordinate_Geometry_07 (PDF Q121–Q128, Hyperbola)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Numbering:** the PDF numbers the questions 121–128; the deck numbers them 1–8 (deck n = PDF n+120; the JSON also stores `q_ref`). Types: single correct = 1; numerical = 2–8.
**Marks assumed:** none printed; 4 marks each (JEE Advanced default for single-correct and numerical), stated in the section dividers.

## Difficulty
Marks-weighted difficulty index (all 4 marks; no equivalence-relation or multi-correct adjustment applies): **2.38** (19/8, computed by hand; Excel formulas not recalculated).
L2 = 5 (Q1, 2, 5, 7, 8); L3 = 3 (Q3, 4, 6). No L0, L1, L4, L5. Confidence Medium (JEE Main-style questions rated on the Advanced scale; anchors only indicative).

## Solutions corrected / written
- Q3 (PDF 123) corrected: the statement prints "a² + b² = α√2 − β", but a²+b² = a²e² = 9 is a constant. The PDF's solution (and the original JEE question) use a²b² = 6a³ = 810√2 − 1134; statement corrected to a²b². Working unchanged. A figure label "(−a, e, 0)" should read (−ae, 0).
- Q6 (PDF 126) corrected: printed directrices x = ±4/√3 are inconsistent (tangency + latus rectum 9 force a = 2, b² = 9, e² = 13/4, directrix ±4/√13; with 4/√3 e = √3/2 < 1). The PDF's own line "2/e = 1/√3 ⇒ e = √3/2" is also inconsistent with 4/√3, and it ends "question is bonus" with no value, while its answer key says 61. Statement corrected to 4/√13; solution completed (contact point (4, 3√3), focal distances, m = 48, 4e²+m = 61).
- Small bridging lines added without changing the PDF's method (source stays pdf): Q1 (point-on-hyperbola check, which focus is nearer), Q4 (the squaring step, factorisation of the quadratic; the PDF's circle-centre symbol α renamed h to avoid clashing with the hyperbola's α). No question needed "written".

## Answer key
All 8 answers verified by hand and by numerics and agree with the PDF key: 1 B, 2 141, 3 1944, 4 19, 5 55, 6 61 (only for the corrected directrix; as printed the question has no valid hyperbola, which the PDF treats as bonus), 7 40, 8 182.

## Alternates and Useful Results
- Alternates given for Q1, 2, 3, 5, 6, 7, 8; each checked to reach the same answer.
- NO alternate: Q4 – the problem is one linear chain (tangent distance → chord condition → quadratic in the centre → hyperbola relations); the only other routes (e.g. setting up the circle equation) are the same equation reworded, so none was invented.
- Alternates only partly different (same ingredients, different packaging) - flagged for review: Q2 (centre via partial derivatives), Q8 (quadratic in b² via ae = √(a²+b²) instead of e), Q6 (point form of the tangent for the contact point).
- Useful Result / Pattern given for all 8 questions.

## make_ppt.py warnings
None printed (380 equations converted, 57 slides, 8 questions); no "could not convert" notes.

## Skipped / assumed
- Slides were not rendered or visually inspected (no soffice step here); recalc of the Excel skipped (no /mnt/skills).
- The PDF text layer is garbled; all questions and solutions were read from page images (80 dpi).
- Concepts and levels self-assigned; marks assumed as above.
