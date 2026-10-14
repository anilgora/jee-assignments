# Run report - SHEET_MATRICES_FCopy_JM

Paper: Exercise J-M (Matrices, JEE Main previous-year questions Jan 2023 - Apr 2024), 55 questions (Q1-55, numbered as in the PDF). The PDF has answers and solutions (English and Hindi; only the English was used). Date of run: 2026-10-14. Deck: 317 slides, 1839 native equations.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper; stated in the section dividers): 4 marks for every question (single correct Q1-12, 16-30, 32-38, 43-49; numerical Q13, 14, 15, 31, 39, 40, 41, 42, 50-55). Total 220. Sections are the exam sessions printed in the PDF (Jan 2023: Q1-16, Apr 2023: Q17-31, Jan 2024: Q32-42, Apr 2024: Q43-55).

## Difficulty
Marks-weighted difficulty index (adjusted): **1.91** - well below the official JEE Advanced range (2.6-3.2), as expected for a set of JEE Main questions.
Level counts: L0 = 1 (Q27), L1 = 12 (Q3, 4, 16, 19, 22, 32, 33, 34, 35, 38, 40, 51), L2 = 33, L3 = 9 (Q15, 24, 26, 31, 36, 41, 43, 49, 50), L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor (the paper has no one-or-more-correct questions). Medium/Low confidence: Q50 and Q51 are Low (Q50 answer is easy to guess but needs a bounding argument; Q51 is a defective question); many others Medium (see the workbook). Nearest anchors are the closest Advanced anchors in the bank; none of these questions is an official Advanced question, so no anchor level was copied.

## Solutions whose solution_source is "corrected" (13) or "written" (0)
- Q1 (corrected): PDF working garbled ('(A^2-I)(B-I) ...(1)' without the right side, incomplete 'A^2B(B-I)^-1' line); rewritten as (A^2-I)(B-I)=I and the inverse commutes, giving BA^2=A^2+B=A^2B.
- Q3 (corrected): PDF takes |A|=12^(1/2) from |A|^8=12^4; the negative root also satisfies it (the value would then be -2 sqrt 3, not an option); remark added.
- Q8 (corrected): PDF equates coefficients of A and I without noting A must not be scalar; assumption stated. Answer unchanged.
- Q15 (corrected): the sum=7 line repeats the sum=5 working (8C5-4=52) though the total uses 80; correct 10C7-4*5C2=80 written. **The printed answer key "196" is wrong**: the total is 204 (also by brute force).
- Q23 (corrected): as printed (scalar 1/(5!6!7!) times the matrix) |A| would not be 2; the PDF/key use |A|=2 (prefactor read as the compensating factor of the row extraction). Intended reading kept and stated; answer 2^16.
- Q24 (corrected): typos '|A||A-1|' (should be |A-I|) and '2(1-alpha)^3=-alpha' (should be squared). Answer 5/2 unchanged.
- Q36 (corrected): **PDF key (D) looks wrong.** Statement (II) is a conditional whose hypothesis (trace(adj adj R)=0) can never hold, so it is vacuously true; with (I) false the answer is (B). The PDF reasons that (II) is false because the trace is non-zero. Please compare with the official key. Also rewrote the 'x+y+z=0 and xy+yz+zx=0 => all 0' step as (x+y+z)^2 = x^2+y^2+z^2.
- Q37 (corrected): last step assigned right-hand sides to wrong rows (z=-3, x=-1); correct (x,y,z)=(-3,-2,-1). Unique solution, answer (D) unchanged.
- Q41 (corrected): iterated-determinant exponent garbled ('2^2^2004'); correct n=2^(2^2024); remainder 4 and the parity of K justified. Answer 7 unchanged.
- Q42 (corrected): PDF proves only lambda^2=1 and does not show both +1 and -1 occur; added AM=-M and AX=X for X perpendicular to M. Answer 2 unchanged.
- Q43 (corrected): PDF never excludes |P|=-4 (|P|=+-4 from |P|^4=2^8); 1+3*alpha>1 excludes it. Answer 16 unchanged.
- Q50 (corrected): PDF only asserts the maximum is at A=3I; added the upper bound (Hadamard) and equality case.
- Q51 (corrected): working expanded (Cayley-Hamilton, A not scalar so (x,y) unique). Key "Bonus" kept.
- Q54 (corrected): exponents in the PDF chain garbled (|A|^12.|A|^(2^3)); rewritten, noted |A|=-1/6 is also possible but only |A|^2 matters. Answer 14 unchanged.
(Q7, Q9, Q10, Q39 were reproduced as in the PDF with extra intermediate lines; counted as pdf.)
No question needed "written" (every question had a usable PDF solution).

## Answer key / question problems
- **Q15: key 196 is wrong; correct 204.**
- **Q36: key (D) is probably wrong; correct (B)** (vacuous truth of the conditional). Medium confidence about the official key; the mathematics is as stated above.
- Q23: the question as printed does not give |A|=2 (see above); the key follows the intended reading.
- Q51: key "Bonus" - the question is defective (the solution set is a single point). Answer shown as Bonus.
- All other final answers were re-derived (sympy / brute force / numerical checks): Q2, 3, 5, 9, 12-15, 19-26, 28-31, 37-39, 43, 45-49, 53-55 and the rest by hand.

## Alternate solutions
Alternates (a different technique) for 52 of 55 questions: all except Q27, Q28, Q51. Each was checked to reach the same answer (hand check; many by computation).
Weaker alternates (same underlying idea with a different route), worth a look: Q3, Q19, Q22 (test-matrix / peeling-scalars variants of the same formula chain), Q4 (bijection with permutations), Q8 (polynomial division), Q20, Q26 (direct B=I+F), Q29, Q30, Q47, Q54 (peeling scalars), Q33 and Q34 (elimination by testing), Q44, Q48 (invariants), Q52 (Cayley-Hamilton), Q24 (scalar c).
Questions with NO alternate (3), and why:
- Q27: the count is a single step (six free entries); no other method exists.
- Q28: determinant for alpha then a quadratic form: each step is forced; re-organisations of the arithmetic are not a different method.
- Q51: the question is defective (no numerical answer); there is nothing to solve a second way.

## Useful Result / Pattern
Every question (1-55) has useful_results (3-4 general statements with conditions; formulas spot-checked on numerical cases).

## make_ppt.py output
- First build: "Q27: only 3 solution bullets - a complete solution normally has more": harmless (the PDF's solution is one line); a fourth clarifying bullet was added and the note disappeared.
- No "could not convert" warnings: all 1839 equations became native PowerPoint equations.

## Skipped, assumed or guessed
- No rendering or thumbnails were made (no soffice in the environment); the deck was built with make_ppt.py only and not opened in PowerPoint.
- Levels are my own application of the calibrated skill (no blueprint, no official anchor questions).
- Concept names are my own wording.
- Marks: 4 each (defaults; no marks printed).
- The PDF's Hindi text was not used.
- Q36's corrected answer (B) is a logical judgement; compare with the official key.
