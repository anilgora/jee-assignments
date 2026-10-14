# Run report - SHEET_QUADRATIC_EQUATION_FCopy_C2 (Quadratic Equation, Exercise C-II)

Files: `SHEET_QUADRATIC_EQUATION_FCopy_C2_content.json`, `_Analysis.pptx` (119 slides, 19 questions), `_ratings.json`, `_difficulty.xlsx`.

## Difficulty
- Marks-weighted difficulty index: **2.43** (70 marks). All levels are integers; no equivalence-relation or multi-correct adjustment (no such questions).
- Level 1: 2 (Q9, Q14); Level 2: 8 (Q1, Q2, Q3, Q7, Q8, Q11, Q15, Q16); Level 3: 8 (Q4, Q5, Q10, Q12, Q13, Q17, Q18, Q19); Level 4: 1 (Q6); Levels 0 and 5: none.
- Chapter sheet, not an Advanced-pattern paper, so below the official range (2.6-3.2). Q6 and Q12 rated with Low confidence.

## Blueprint / marks
- No blueprint: **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. Assumed JEE Advanced defaults: Q1-Q13 (find / solve / prove) = 4 marks, typed "Numerical"; Q14-Q16 (paragraph single-correct) = 3 marks; Q17-Q19 (matching) = 3 marks. Stated in the section dividers.
- Q10 is a "show that" proof; given the Numerical type and 4 marks.

## Solutions with source corrected or written
- Q2 (corrected): PDF typos in the rejection checks: "3x+7 = 1 < 0" at x=-2 (1 is positive; x=-2 is still rejected via 2x+3=-1) and 3x+7 at x=-1/4 computed as 11/2 (correct 25/4). Added the base-not-1 check. Answer unchanged.
- Q5 (corrected): PDF never solves Case II (0<p<4: 2-2p=3 gives p=-1/2, no solution) and does not say why 1+sqrt2 and 5-sqrt10 are rejected. Added. Answer unchanged.
- Q12 (corrected): PDF tests only (k,w) for common factors, never computes f for k=6,9,12, and reads "relatively prime" as pairwise. Completed. If it meant only gcd(k,w,f)=1, k=9 (9,132,19) would also qualify and give 160; the key's 96 needs the pairwise reading.
- Q19 (corrected): in (D) the PDF gives the roots of x^2+2x-1 as -1 -/+ sqrt3; they are -1 +/- sqrt2, so the valid root is sqrt2-1 (PDF: sqrt3-1). Count 2 and match D-Q unchanged. Also added the missing justification in (A) for why the common roots are the complex pair.
- Q8, Q10, Q11, Q16, Q17 are marked `pdf` although I added a missing intermediate line (sqrt = t+4 in Q8; IVT closing line in Q10; the trig value 4 in Q11; the three differences' bounds in Q16; matching conclusions for (B),(C) in Q17). The PDF's working is correct as far as it goes.
- All other questions reproduced from the PDF after independent checks.

## Answer key
- All 19 answers were checked by computation (sympy / numerical search: Q1, Q3, Q4, Q5, Q6 root counts, Q7, Q8, Q12, Q13 incl. existence with distinct a,b,c,d, and by hand for Q2, Q9-Q11, Q14-Q19). No answer in the key is wrong (Q10 has no printed answer; it is a proof).

## Alternates and results
- Alternate solutions given for 16 of 19 questions: Q1, Q3-Q9, Q11, Q12, Q14-Q19. Q18's alternate covers parts (B) and (C) only; Q19's covers (A)-(C) (D has no shorter route).
- Closeness note: Q4's, Q5's and Q12's alternates are different manipulations of the same idea (u-polynomial expansion; completing the square with s=2x; factored form) rather than a new method; the others (Q1, Q3, Q6, Q7, Q8, Q9, Q11, Q14-Q17, Q19) use a clearly different technique.
- **No alternate**: Q2 (every route goes through t = log_A B and its reciprocal, only reordering domain checks), Q10 (f(alpha)<0<f(beta) is the only short route; others are heavier forms of the same sign test), Q13 (eliminating b,d first is the same elimination as the PDF).
- Every question 1-19 has `useful_results`.

## make_ppt.py notes
- Q17: "very long question - font reduced to 20 pt"; Q18: "... reduced to 22 pt" - four-part matching lists; harmless.
- No "could not convert" warnings; 808 equations converted.

## Skipped / assumed
- No visual rendering of the deck (no soffice here); fit judged from script notes only.
- The text layer was garbled for maths, so every page was read from page images.
- Levels are my judgement against the calibrated anchors (few quadratic/logarithm chapter-sheet anchors).
