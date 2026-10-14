# Run report - SHEET_FUNCTION_FCopy_C2

Paper: Exercise C-II (Functions, JEE-Advanced-style sheet), 24 questions (Q1-24, numbered continuously as in the PDF). The PDF has answers and solutions. Date of run: 2026-10-14.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper; stated in the section dividers): Subjective and Numerical questions 4 marks each (Q1-14, total 56); Paragraph single-correct 3 marks each (Q15-21, total 21); Matching 3 marks each (Q22-24, total 9). Total 86. Question types were taken from the paper: Q1 and Q7-12 are subjective ("Subjective Type" label, not in the standard label table), Q2-6 and 13-14 numerical, Q15-17 and Q18-21 two paragraph sets, Q22-24 match-the-column.

## Difficulty
Marks-weighted difficulty index (adjusted): **2.15** (below the official JEE Advanced range 2.6-3.2; this is a chapter sheet, no expected distribution).
Level counts: L0 = 0, L1 = 6 (Q2, 4, 6, 18, 19, 20), L2 = 9 (Q1, 3, 9, 13, 16, 17, 21, 23, 24), L3 = 9 (Q5, 7, 8, 10, 11, 12, 14, 15, 22), L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied (no such questions). Medium-confidence ratings: Q5, 7, 8, 10, 11, 12, 14, 15, 22.

## Solutions whose solution_source is "corrected" (3)
- Q8: not wrong but incomplete. The PDF does not show the x = 1/2 substitution's right side, skips the value of the modulus argument, and never states the conclusion f(2)+f(1)=0. Steps added; f(1)=-1, f(1/2)=0, f(2)=1 as in the PDF.
- Q9: not wrong but incomplete. The PDF stops at f(x)=2x^2 and never proves the second part f(x+y)f(1/(x+y))=k; that proof (and a check that 2x^2 satisfies the relation) was added.
- Q23: part (B) is wrong in the PDF: it says "for t = cos x in [0,1], 1+t-t^2-t^3 lies in [0,1]". t ranges over [-1,1] and the expression reaches 32/27 at t = 1/3. Corrected to LHS <= 32/27 < 2 <= RHS; the conclusion (empty set) and the answer S are unchanged.

## Solutions with solution_source "written" (0)
None; the PDF has a solution for every question. Small additions inside "pdf" solutions: Q12 (explicit f(1)=f(-1)=1 for alpha=3 and a remark), Q15 (check that 4 is the fundamental period), Q18 (why a=1 is the largest value), Q19 (why the minimum is at 0).

## Answer key / question problems
- No printed answer disagrees with the correct answer; every final answer was re-derived (and checked by brute force or numerically for Q1, 2, 5, 12, 13, 14, 22C, 23B).
- Q12 is ill-posed: for every alpha > -9/8 the denominator alpha + 6x - 8x^2 has real zeros, so f is not defined on all of R. At alpha = 2 and alpha = 14 the numerator and denominator also share a factor. The key [2, 14] (discriminant method) is kept; a remark was added as the last bullet of the solution.
- Q22(A)/(B): two matches each (Q and R) are right only because "a period" / "a" may be any multiple of 2; the key's answer is kept.
- Q10: the question asks for sketches; the deck describes the graphs by their vertex points (no figure is drawn).

## Alternate solutions
Alternates (a genuinely different technique) were written for 14 of 24 questions: Q1, 2, 4, 5, 6, 9, 10, 13, 14, 15, 20, 21, 23, 24 (Q23's alternate covers all four parts, with the new bound in (B)). Each was verified by hand against the answer.
Questions with NO alternate (10), and why:
- Q3: the only route is oddness of the non-constant part plus the reciprocal-log identity; any other phrasing is the same computation.
- Q7: the cancellation of the two terms is the whole question; there is no second approach.
- Q8: a system of three linear equations in f(1), f(2), f(1/2) is the only reasonable route.
- Q11: the "linear space of solutions" viewpoint is the same three substitutions reworded.
- Q12: the discriminant method is the standard route; no simpler independent way to characterise onto-ness was found.
- Q16, Q17: one-step inequality / composition; the other routes (completing the square, writing 2+|x|) are the same computation.
- Q18, Q19: single-step vertex arguments; no different route.
- Q22: four unrelated direct checks (LCM, graph shape, sign pattern, endpoint mapping); no second method that is not a reword.

## Useful Result / Pattern
Every question (1-24) has useful_results (3-4 general, conditioned statements each, spot-checked numerically where a formula is stated).

## make_ppt.py warnings
Only the note "Q22: very long question - font reduced to 22 pt" (harmless; the question has four items with two columns). No equation was left as LaTeX text (850 equations converted, 136 slides).

## Skipped / assumed / guessed
- No rendering or thumbnail check (no soffice in this environment); the deck was built but not viewed. The difficulty xlsx was not recalculated (recalc.py not available).
- Levels are my calibrated estimates against the user's anchors (Function-chapter anchors are few); levels of Q5, 7, 8, 10, 11, 12, 14, 15, 22 are medium confidence.
- Concepts are self-assigned; Hindi text in the PDF was ignored. "Subjective Type" was used as the type label and "Subjective" in the ratings sheet (neither is in the standard table).
- Paragraph for Q18-21 is repeated on each question slide as printed in the PDF.
