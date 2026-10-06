# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_01_03

Paper: 20 questions, all Single Correct Type, Algebra (matrices/determinants, linear systems, sequences, quadratics). Printed Q41-Q60; numbered 1-20 in the deck (deck Q n = printed Q n+40). 126 slides, 849 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.05** (164 / 80 marks, 4 marks each). No equivalence-relation adjustment, no MCQ floor (all single-correct).
- Questions per level: Level 1: 3 (Q5, Q6, Q11) | Level 2: 13 | Level 3: 4 (Q9, Q13, Q17, Q19) | other levels: none.
- Medium confidence: Q2, Q3, Q8, Q9, Q13, Q17, Q19. The rest High. Nearest anchors are approximate (closest chapters in anchors.md).

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): +4 for single-correct (JEE Advanced default), 0 otherwise; stated on the section divider.

## Solutions whose source is corrected or written
- Q2 (printed 42) - corrected: PDF's last lines swap the right-hand sides: "-z=3 => z=-3, -x=1 => x=-1". Correct: row 1 is -z=1 and row 3 is -x=3, so (x,y,z)=(-3,-2,-1). Answer (D) unchanged.
- Q6 (printed 46) - corrected: PDF writes the series total as pi^2/90 instead of pi^4/90 (typo; cancels in alpha/beta). Answer (C) unchanged.
- Q8 (printed 48) - corrected (gap): PDF stops at D=0 (lambda = 3 or -1/2) and does not reject -1/2; at lambda=-1/2 the system is inconsistent. Consistency check added. Answer (B) unchanged.
- Q9 (printed 49) - corrected (gap): PDF ends at "n=289" common terms and never computes n(A u B); also no check that common terms lie in B's range. Added 2025+2025-289 = 3761. Answer (A) unchanged.
- Q13 (printed 53) - corrected (gap): PDF does not show that b = GM is attainable when b < AM; example a=4,b=2,c=1 added.
- Q14 (printed 54) - corrected (gap): PDF jumps from P10=P9+P8 to x^2=x+1 without justification; added alpha*beta=-1 from the Newton recurrence.
- Q16 (printed 56) - corrected (gap): consistency of the first system at k=3 was not checked; added (row 3 = row 1 + row 2, 2+1=3=k).
- Q17 (printed 57) - corrected (minor): PDF takes |A|=sqrt3 and drops -sqrt3; harmless (exponents 12 and 2 are even), noted.
- Q19 (printed 59) - corrected (gap): PDF derives the three cases only; options (A)-(D) were never tested. Option-by-option check added.
- Q20 (printed 60) - corrected (gap): same - options never tested; added.
- No question was `written`. The other 11 are source pdf.

## Answer key
All 20 keys verified with sympy/numerics (determinants, adjugate chains, (I+A)^8, power sums, union count 3761 by brute force, ranks for each parameter case). No key is wrong.
Note on Q13 (printed 53): the Hindi options in the PDF are in a different order (A both ... D neither) from the English ones (D both); the printed key D matches the English order, which the deck follows.

## Alternates
Given for 17 of 20 questions (all except Q6, Q11, Q17).
Honest strength notes: Q12 (parametrise GP as p, pr, pr^2) and Q18 (factorising 1+r+...+r^8) are lighter variants of the main route; Q15 (invariant 2a_{n+1}-3a_n, b_n=a_n+1) and Q9 (congruence count) are different bookkeeping of the same facts; the others use clearly different ideas (case split on z Q1, eigenvalues Q2, matrix-structure Q3, Cayley-Hamilton Q4, even function/monotone Q5, ratio of differences Q7, cancelling x and y Q8/Q20, row elimination Q10, GP-of-logs Q12, x=a-b,y=b-c Q13, reversed coefficients Q14, dependency E1+E2-E3 Q16, multipliers Q19).
Questions with NO alternate:
- Q6 - splitting the series into odd and even parts and using even = S/16 is the only idea; a general-p formulation is the same step reworded.
- Q11 - the only natural route is the 4r-3 / 4r-1 split with sum formulas; "total of odd squares minus a correction" is the same sums reorganised.
- Q17 - the chain adj-exponents -> |A|^2=3 -> equate exponents -> quadratic has no different elegant route.

## Useful Result / Pattern
All 20 questions have a useful_results slide (3 bullets each); formulas spot-checked numerically (adjugate exponents, Lucas P_n = 47, 76, 123, partial sums of a_n, union count, Q20 solutions (4,0,0) and (17/9,-4/9,1)).

## make_ppt.py warnings
None printed (only the note "849 converted to native PowerPoint equations"). No "could not convert" messages. Slides were not rendered (no soffice).

## Skipped / assumed / guessed
- Concepts and levels self-assigned; PDF text layer garbled for maths, so all 19 pages were read as images.
- Excel built with build_report.py; recalc step skipped (no /mnt/skills), so formula cells have no cached values.
- Deck title "JEE Main Question Bank 02 Algebra 01 (Paper 03)" chosen by me (the paper has no title for this part).
