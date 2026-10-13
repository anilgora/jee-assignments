# Run report — SHEET BINOMIAL THEOREM_FCopy JA

Paper: `papers/SHEET BINOMIAL THEOREM_FCopy JA.pdf` (6 pages, "Exercise J-A", 8 JEE Advanced previous-year questions 2013–2025). Hindi translations left out (English deck). Pages 5–6 were also read as images; the text layer was otherwise adequate.

Files: `…_Analysis.pptx` (57 slides), `…_content.json`, `…_ratings.json`, `…_difficulty.xlsx`.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.** No blueprint existed for this paper.
- The paper prints no marks. Assumed **4 marks** for every question (integer Q1, Q3, Q4, Q8; numerical Q5, Q7; single-correct Q2; one-or-more-correct Q6). Stated on the section divider. Question types were inferred from the answers/official source (Q1, Q3, Q4, Q8 integer 0–9; Q5, Q7 numerical).

## Difficulty (jee-advanced-difficulty-calibrated)
- Marks-weighted difficulty index (adjusted): **3.13** (32 marks). Chapter sheet of official questions, so no expected distribution; it sits inside the official range 2.59–3.21.
- Questions per level: Level 2 — 2 (Q1, Q3); Level 3 — 3 (Q2, Q4, Q5); Level 4 — 3 (Q6, Q7, Q8); Levels 0, 1, 5 — none.
- Q7 follows anchor 2023-P1-Q13 (L4) and Q8 follows 2025-P2-Q10 (L4), both in the anchor bank; the rest are rated by me. Confidence Medium for Q1–Q6, High for Q7–Q8.
- No equivalence-relation adjustment; multi-concept MCQ floor not applicable (Q6 is a single concept).
- `recalc.py` skipped (no `/mnt/skills`): formula cells have no cached values until opened in Excel.

## Solutions: corrected / written (none were `written`)
- **Q4 — corrected (omission):** the PDF states "n = 5 and m = 16" without showing that 16 is the smallest m or that m = 1 is excluded (gives n = 0). Added the divisibility argument. Answer 5 unchanged.
- **Q6 — corrected (omission):** the PDF never shows that (C) is false and its f-simplification line is garbled; rewrote the simplification step by step and added the (C) argument (equal only if m+n = 1). Answer ABD unchanged.
- **Q7 — corrected:** the PDF writes "b³ = 35×27/280 = 3/2"; b³ is 27/8 (b = 3/2). Fixed; answer 3 unchanged.
- Q1, Q2, Q3, Q5, Q8 — `pdf`: checked and reproduced (Q2's garbled first line was rewritten cleanly via the identity (1−x²)(1+x²)(1+x⁴)=1−x⁸; Q3 and Q8 were short in the PDF and were split into more bullets without adding new content, except the greatest-term formula stated explicitly in Q8).

## Answer key
All answers checked by computation (exact polynomial expansion, brute-force search for Q4, exact g(m,n) for m, n ≤ 4 in Q6, exact binomial maximum for Q8). No wrong key found: Q1 6, Q2 C, Q3 8, Q4 5, Q5 646, Q6 ABD, Q7 3, Q8 6.

## Alternate solutions and useful results
- **Alternates: all 8 questions.** Q1 closed formula N+1=(a+b)(b+c)/(b²−ac); Q2 the PDF's own solution-counting method 2x+3y+4z=11 (primary uses the generating-function route); Q3 Euler's distinct-parts = odd-parts theorem; Q4 geometric-series sum then factoring (m−1)(m+1); Q5 symmetry r↔10−r giving 5·C(20,10); Q6 small-value tables g(1,1)=4, g(1,2)=g(2,1)=8, g(2,2)=16 exposing 2^(m+n) (an evidence/pattern route, the proof is the primary solution); Q7 factor out x-power so coefficients become y³-coefficients; Q8 binomial-distribution mode ⌊(n+1)p⌋. Each verified numerically.
- **Questions with NO alternate:** none.
- **Useful results given for all 8 questions.**

## make_ppt.py warnings and notes
- None. 375 equations converted to native PowerPoint equations; no "could not convert" messages. The deck was not rendered or visually inspected (no soffice).

## Skipped / assumed / guessed
- Concepts self-assigned; marks assumed as above; question types inferred (no marks/digit range printed).
- Hindi text omitted.
