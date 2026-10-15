# Run report - SHEET_SEQUENCE_&_PROGRESSION_FCopy_JA (Sequence & Progression, Exercise J-A: JEE Advanced PYQs)

Files: `_content.json`, `_Analysis.pptx` (118 slides, 16 questions), `_ratings.json`, `_difficulty.xlsx`.

## Difficulty
- Marks-weighted difficulty index: **2.59** (61 marks; adjusted; the equivalence-relation adjustment applies to no question and the 2.5 multi-correct floor changed no level).
- Level 1: 1 (Q1); Level 2: 7 (Q4, Q5, Q6, Q8, Q10, Q11, Q14); Level 3: 6 (Q2, Q3, Q7, Q9, Q12, Q13); Level 4: 2 (Q15, Q16); Levels 0 and 5: none.
- Q15 is the same question as 2023-P1-Q10 and Q16 the same as 2026-P2-Q6 in the anchor bank (both rated 4 by the user); I used those levels. Other levels rated from nearest anchors (Medium confidence for Q2, Q3, Q6-Q9, Q12-Q14).

## Blueprint / marks
- No blueprint: **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. JEE Advanced defaults assumed: single-correct (Q1, Q6, Q7) = 3; one-or-more-correct (Q3, Q9, Q14, Q16) = 4; integer type 0-9 (Q2, Q4, Q5, Q11, Q12) = 4; numerical (Q8, Q10, Q13, Q15) = 4. Stated in the section dividers. Integer vs numerical type was chosen from the size of the answer (single digit = integer type).

## Solutions with source corrected or written
- Q7 (corrected): the PDF says a2..a50 are arithmetic means "between a1 and a50" (should be a51) and asserts a_k > b_k "by A.M.>G.M." without saying that a_k is the weighted A.M. and b_k the weighted G.M. of b1, b51. Fixed the typo and added that step; answer (B) unchanged.
- All other questions reproduced from the PDF after independent checks (brute force / exact arithmetic / numerics). Small additions, not errors: Q2 justifies why n must be 4p+1 or 4p+2 and why n>=53 fails; Q3, Q9, Q14 spell out the option-by-option verdicts and intermediate sums that the PDF's text layer shows only as results; Q9(A) also checks n=1 (b1=1); Q15 gives the PDF's repunit method with each intermediate line and notes why n=9 is forced; Q16 adds the verdicts for options (A)-(D), which the PDF leaves after "b=8a, c=15a".
- Q15: the paper's overbrace notation is replaced by the symbol N_r (the (r+2)-digit number 7 5..5 7) in the question text, with the same meaning.

## Answer key
- All 16 keys verified (Q2 brute force k=25; Q3 S_n=4n(4n+1) for n=1..11; Q5 (a,d)=(81,9); Q8 set sizes by computer; Q9 series numerically 10/89 and 12/89; Q12 brute force gives only c=12; Q13/Q14 exact; Q15 9S-N_99=1210 exactly; Q16 brute force gives only (a,8a,15a)). No answer key is wrong.

## Alternates and results
- Alternate solutions given for Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q13, Q14, Q15, Q16 (14 of 16), each verified numerically or symbolically.
- Closeness notes: Q4's alternate ((sqrt c - sqrt a)^2 = 6) reaches the same key equation a(r-1)^2=6 by a different route; Q16's alternate (Vieta) reaches the same factorisation (p-2)(q-2)=3 as the PDF's x=-2 substitution; Q11's alternate (Jensen) is close in spirit to A.M.-G.M.
- **No alternate**: Q1 - the only routes (reciprocal A.P.; linear interpolation / similar triangles on the same A.P.) are the same linear calculation, so none is a genuinely different method. Q12 - the equation c(2^n-2n-1)=2n(n-1) with an exponential bound then enumeration of n=1..6 is the only route; any other ordering of the same steps would be a reworded copy.
- Every question 1-16 has `useful_results` (formulas checked on numerical cases, e.g. Lucas generating function, repdigit closed form 68*10^(r+1)+13, f(-2)=3a for A.P. coefficients).

## make_ppt.py notes
- No warnings. 782 equations converted to native equations; no "could not convert" messages.

## Skipped / assumed
- No visual rendering of the deck (no soffice here); fit judged from script output only.
- Maths text from pdftotext was garbled for several questions, so key pages (2, 3, 6, 12, 13) were read as images; the rest was reconstructed from text and verified by computation.
- Q9's definition b_1 = 1 is taken from the page image (the text layer drops it).
