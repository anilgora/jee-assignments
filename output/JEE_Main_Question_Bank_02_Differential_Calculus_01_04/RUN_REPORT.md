# Run report - JEE_Main_Question_Bank_02_Differential_Calculus_01_04

Paper: `papers/JEE_Main_Question_Bank_02_Differential_Calculus_01_04.pdf` (14 pages, Matrix JEE Academy; 3 single-correct + 17 numerical questions, solutions printed). The PDF prints them as Q61-Q80; the deck numbers them 1-20 (deck n = printed n+60).
Files: `_Analysis.pptx` (118 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. Assumed (JEE Advanced defaults / run instructions): single-correct 4, numerical 4, no negative marking; total 80 marks. Stated in both section dividers. Q4-Q20 are numerical-value type; some answers exceed 9, so they use the "Numerical Type" label.

## Difficulty
- **Marks-weighted difficulty index (adjusted): 2.05** (80 marks; unadjusted 2.00) - a JEE Main-level bank, well below the Advanced range (2.6-3.2).
- Levels before adjustment: Level 1: 3 (Q2, Q9, Q12); Level 2: 14 (Q1, Q3, Q5, Q6, Q7, Q8, Q11, Q13, Q14, Q15, Q17, Q18, Q19, Q20); Level 3: 3 (Q4, Q10, Q16); Levels 0, 4, 5: none.
- Adjusted: Q13 and Q17 get +0.5 (relation-property questions, treated as in the previous banks) -> 2.5 each. No MCQs, so no multi-correct floor. The content JSON carries the adjusted level (2.5) for these two.
- Low confidence: Q4, Q10, Q16 (no close Main-level anchors, nearest Advanced anchors are all harder); the rest Medium.
- `_difficulty.xlsx` built with `build_report.py`; recalc skipped (no /mnt/skills), formulas fill in on opening in Excel.

## Solutions whose source is corrected (one line each)
- Q1 (printed 61): PDF never names S = H_n, writes the last block as (lambda+1)/2p and "k <= lim (p+1)/2p = 0" (as printed that tends to 1/2; the division by n >= 2^p is unstated); fixed to S/n < (p+1)/2^p. Key D right.
- Q4 (printed 64): PDF assumes a > 0 silently (a, b are only non-negative); added the case a = 0, which forces b = 1 and also gives a + b = 1. Key 1 right.
- Q5 (printed 65): PDF displays the product of limits with the x-powers and the factor 2 missing ("lim (sin x+x)/2 . lim (x-sin x)/2", then 1 x 1/6); rewritten with explicit 2, P/x -> 1, R/x^3 -> 1/12. Key 6 right.

## Solutions whose source is written
- Q15 (printed 75): the PDF stops after "f(x)=||x-3|-2|, the graph is shown below" and the graph; it never finds S or evaluates f(f(x)). Written in full using the PDF's own graph points. Key 3 right.

## Solutions kept as pdf (reproduced, small expansions only)
- Q2, Q3, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q18, Q19, Q20. Lines added where the PDF skipped them: the range check kx+theta in (0,pi) in Q7; f'(0), g''(0), h''(0) justification in Q8; f^4 in Q14; the explicit case-by-case pair listing in Q17; value tables and multiplicities in Q18; the match of coefficients in Q19; why only d = 0, -2 work in Q20; the unstated remark that f(x)=a^x in Q9 (kept as the PDF's method).

## Answer key
- No answer key looks wrong. All 20 keys (D, B, D, 1, 6, 8, 91, 5, 3, 3240, 43, 19, 7, 3125, 3, 2, 19, 6, 2039, 18) were re-derived. Computations run: Q4 (hand check of both cases), Q5 (sympy limit 1/6), Q6 (one-sided check at the nine points gives 8), Q7 (sum of squares 91), Q1 (numeric: (1+H_n/n^2)^n = 1.000014 at n = 10^6), Q3 and Q16 (numeric evaluation = pi/3 at the roots), Q10 (dynamic-programming count of strict subset chains 3240, and the inclusion-exclusion sum 3240), Q11 (brute force 43), Q12 (brute force 19), Q13 (closure adds 7), Q14 (sympy matrix power: 1563, 1562), Q15 (f(f(1)), f(f(3)), f(f(5)) all 1), Q17 (|R| = 19 and 19 additions), Q18 (brute force 6 solutions, same as both methods), Q20 (brute force 18).

## Alternates
- Given for 15 of 20: Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q14, Q16, Q17, Q18. All verified numerically or symbolically to reach the same answer. Q3's (convert sec^-1 to tan^-1 then double angle) is a modest variation of technique rather than a wholly new idea.
- **No alternate (no genuinely different method), one line each:**
  - Q2: the domain is just the intersection of the two stated conditions; there is no second route.
  - Q13: the answer is |missing diagonal| + |one-way pairs|; any other phrasing (e.g. |R union diagonal union R^-1| - |R|) is the same count.
  - Q15: the piecewise formula and the graph are the same corner-counting; no independent method.
  - Q19: inverting the inverse and matching coefficients is the only route (a numeric guess is not a method).
  - Q20: the quadratic d(2d+3) restricted to {0..4} and the difference count are the only steps.
- Useful results: **all 20 questions have `useful_results`** (formulas checked on a numerical case where numeric).

## make_ppt.py warnings
- None. 803 equations converted to native equations; no "could not convert" notes, no solution-source warnings.

## Skipped / assumed
- Rendering/thumbnails were not done (no soffice); the deck was not opened in PowerPoint.
- Level ratings are my own judgement (Main-level bank, few close anchors). The +0.5 on Q13 and Q17 (relation-property questions) is an assumption carried over from the previous banks.
- The Hindi text in the PDF (legacy font) was not transcribed; only the English statements were used. All maths was read from page images (text layer garbled).
- Q10: the symbol in the statement was read as proper inclusion; since f must be one-one, "subset" and "proper subset" give the same count, so the answer is unaffected.
- Concepts self-assigned; Q11 chapter "Sets" has no anchor-chapter equivalent.
