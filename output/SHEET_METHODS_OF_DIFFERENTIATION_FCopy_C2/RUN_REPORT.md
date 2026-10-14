# Run report - SHEET_METHODS_OF_DIFFERENTIATION_FCopy_C2

Paper: Exercise C-II (Methods of Differentiation), 25 printed questions with PDF solutions. Date of run: 2026-10-14.
Numbering: Paper Q5 has two independent parts, (a) and (b), each with its own answer, so they are separate deck questions. Deck Q1-4 = paper Q1-4, deck Q5 = Q5(a), deck Q6 = Q5(b), and deck Qn = paper Q(n-1) for n = 7..26 (paper Q25, the matching question, is deck Q26). 26 deck questions in all. Each question slide also shows the paper number where it differs ("(Paper Q20)" etc.).

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper; stated in the section dividers): Subjective and Numerical questions 4 marks each (deck Q1-20, total 80); Paragraph single-correct 3 marks each (deck Q21-25, total 15); Matching 3 marks (deck Q26). Total 98. Question types come from the paper: "Subjective Type" (prove / show / find an expression) and "Numerical Type" (numerical-value answers) - the first is not in the standard label table.

## Difficulty
Marks-weighted difficulty index (adjusted): **2.27** (below the official JEE Advanced range 2.6-3.2; this is a chapter sheet, so no expected distribution).
Level counts: L0 = 0, L1 = 2 (deck Q22, 23), L2 = 16 (Q1, 2, 3, 5, 6, 9, 10, 14, 15, 17, 18, 19, 21, 24, 25, 26), L3 = 8 (Q4, 7, 8, 11, 12, 13, 16, 20), L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied. Medium-confidence ratings: Q3, 4, 7, 8, 11, 12, 13, 16, 20, 26.

## Solutions whose solution_source is "corrected" (4)
- Q11 (paper Q10, determinant): the PDF expands the first determinant as (mr-qn)-(br-qc)+(bn+cm); the last term must be (bn-cm). Also fixed typos in its intermediate determinants (q-x, r+x, "c3+c3-x4", "s(0)" for f(0)).
- Q23 (paper Q22, limit): the PDF uses g(x) = 9/(x-3)^3 near x = 0, which is the x > 3 branch; near 0 it is 9/(3-x)^3 (g(0) = 1/3). The limit value 0 is unchanged.
- Q25 (paper Q24): the PDF substitutes sec^2 x = t and writes f = 1/(t^2+t+1); that is wrong (it would be 1/(t+sqrt t+1)). With t = sec x the expression and the range (0, 1/3] are correct. Answer (D) unchanged.
- Q26 (paper Q25), part (B): the PDF claims f(xy)=f(x)+f(y) on R implies f = ln x, which is not defined on R (and on R actually forces f = 0). Rewritten with f(1) = 0 and y = 1/x; value 0 (R) unchanged. Parts (A), (C), (D) agree with the PDF.

## Solutions with solution_source "written" (0)
None; the PDF has a solution for every question. Small additions inside "pdf" solutions: Q1 (the rewrite y' = -1 + 2x/(x-y) that the PDF skips), Q2 (explicit coefficient matching for a1, a2, a3), Q7 (real cube-root remark for the negative d2x/dy2), Q12 (the +/-infinity steps stated for 1/x -> 0), Q26(D) (domain (0, pi/2) stated). Obvious PDF typos (x^3 y''' for x^3 y'', "93y^2" for 27y^2, f(1/k)) were silently cleaned.

## Answer key / question problems
- No printed final answer disagrees with the correct answer; every answer was re-derived and checked numerically or symbolically (sympy) for Q1-4, 8-10, 13-19, 23 and the matching items.
- Paper Q20-22 paragraph (deck Q21-23): the paragraph calls g "decreasing", but g = 9/(3-x)^3 for x < 3 (the branch containing g(0) = 1/3) is increasing; the equation g'/g = 3/(3-x) is singular at x = 3 and no single decreasing function satisfies it on both sides. The key (C), then A, A, is the intended one: all options differ only in the constant k in k/(x-3)^3, g(0) = 1/3 fixes k = 9, and the answers to the next two parts do not depend on k. The key is kept; the issue is noted in a useful-result bullet of Q21.
- Paper Q5(a) is stated for the equation as printed; Q6 (paper Q6) needs real cube roots for the negative d2x/dy2 (added as a step).

## Alternate solutions
Alternates (a genuinely different technique) were written for 22 of 26 deck questions: all except Q8, 14, 23, 25. Each was verified (sympy / numeric check) against the answer.
Questions with NO alternate (4), and why:
- Q8 (paper Q7, JEE-2000): the only route is p(1) = 0 and the derivative as a limit; the factor-theorem version (p = (x-1)q) is the same limit reworded.
- Q14 (paper Q13): the factorisation P^4+P^2+1 = (P^2-P+1)(P^2+P+1) is the whole question; other routes (Fourier form of sin^2 x) are the same computation.
- Q23 (paper Q22): a direct limit once g near 0 is known; the "g is continuous at 0" version is the same step (recorded as a useful-result bullet instead).
- Q25 (paper Q24): "lambda >= f(x) for all x" and the range of f is the only reasonable route; the x -> 0+ local argument is a reorganisation of it.

## Useful Result / Pattern
Every question (1-26) has useful_results (3-4 general, conditioned statements each; formulas were spot-checked numerically, e.g. Q11, Q12, Q15, Q18, Q20).

## make_ppt.py warnings
None. 1007 equations converted, 173 slides, no "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check (no soffice in this environment); the deck was built but not viewed. The difficulty xlsx was not recalculated (recalc.py not available).
- Levels are my calibrated estimates against the user's anchors (Methods of Differentiation has no direct anchors; nearest anchors are listed per question in the ratings sheet); medium-confidence levels are listed above.
- Concepts are self-assigned; the Hindi text in the PDF was ignored.
- Paper Q5 was split into two deck questions (see Numbering); the matching question is rated as one question (Q26).
- The paragraph is repeated on each of its question slides as printed.
