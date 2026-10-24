# Run report: RPT 02 Paper 02 JEE Adv

## Inputs
- Paper: `papers/RPT 02 Paper 02 JEE Adv.pdf` (12 pages, scanned, no text layer; read from page images, solutions printed). 17 maths questions: single correct Q1-4, one-or-more correct Q5-8, paragraph Q9-10 (one paragraph, two single-correct parts), then two numerical groups (paper numbering restarts: 1-4 and 1-3) which are deck Q11-17. Deck numbering is continuous 1-17.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks assumed (not printed): JEE Advanced defaults, stated in the section dividers: single correct 4 (Q1-4), one-or-more correct 4 (Q5-8), paragraph 3 (Q9-10), numerical 4 (Q11-17). Total 66. Q11-17 have no options and answers such as 17, so they are "Numerical Type", not integer 0-9.

## Difficulty (calibrated skill)
- Marks-weighted difficulty index (adjusted): **2.71** (inside the official range 2.6-3.2).
- Questions per adjusted level: L1 = 1 (Q1); L2 = 3 (Q2, Q12, Q16); L2.5 = 2 (Q14, Q17, both equivalence-relation adjustment); L3 = 9 (Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q11, Q13); L3.5 = 1 (Q15, equivalence adjustment); L4 = 1 (Q10); L0 and L5 = 0.
- Equivalence-relation adjustment (+0.5): Q14, Q15, Q17. Multi-concept MCQ floor (2.5) set on Q5, Q6, Q7 but it did not change them (already level 3).
- Confidence: Low on Q9, Q10 (paragraph anchors differ); High on Q1, Q16; Medium elsewhere. The xlsx has live formulas without cached values (recalc.py not available here).

## Solutions whose source is corrected or written
- None. All 17 are `pdf`: every printed solution is correct and reproduced in full.
- Small gaps filled without changing the method (still `pdf`): Q3 (justification of T = 6 via the lcm of 3/2 and 2); Q4 (why g -> 2 from the left); Q5 (statement A is not discussed in the PDF; added the factorisation of f(f(x)) - x to show f = f^-1 has only the root of x^3+2x-1, so A is false); Q6 and Q8 (explicit verdict lines); Q12 (derivation of g and f(g(x)) before the graph); Q13 (the PDF's region listing kept, with the R6/R7 deductions written out); Q15 (the converse: every equivalence relation satisfies R o R^-1 = R).
- Typographical points in the PDF (no mathematical effect): Q8 text "Magnitude of jump = 7/6" is correct and is what makes (C) false; Q10 writes "g''(0)" where g'''(0) is meant in the last lines.

## Answer key check
- All 17 printed answers match my independent checks (numerical/brute-force with numpy and sympy): Q1 B (3), Q2 A, Q3 C (225, period exactly 6 by numeric scan, 225 by brute-force enumeration), Q4 D, Q5 B,C,D (f(f(x)) - x has a single sign change on [1/3,1]; numerator factors as -(3x^2-x+1)(x^3+2x-1)), Q6 A,B,C, Q7 A,B,C-false,D-false => A,B, Q8 A,B,D (series checked with sympy; jump in C is 7/6), Q9 A (4,6] (f'' formula checked symbolically), Q10 B, Q11 4 (limit values 3.9910, 3.9991 at n = 10^3, 10^4), Q12 9 (kinks at 0,1,2,3,4; integral 4.0000), Q13 6 (brute force over all 8^3 triples), Q14 3, Q15 5 (brute force over 64 reflexive relations), Q16 7, Q17 17. No wrong key found.

## Alternates and useful results
- Alternate solutions were written for 15 of 17 questions (Q1-8, Q11-17).
- Genuinely different methods: Q1 (compose first; one explicit polynomial), Q3 (direct count with overlapping pairs instead of complement), Q4 (positivity of 2-2cos x - x sin x by a derivative, no series), Q5 (AM-GM range via x/(x^2+x+1); factorisation of f(f(x)) - x), Q6 (max/min via |u-v|; corners only where the two expressions cross, slope jumps independent of a, b), Q7 (double-root factorisation (x-2)^2(x+3) shows smooth joining), Q8 (derivatives of the numerator instead of series), Q11 (tail estimate by integral comparison, no telescoping), Q12 (corners as zeros of nested arguments plus symmetry), Q13 (element-wise truth values and surjection counting), Q14 (graph view: only 2-edge paths fail), Q15 (Boolean matrix M^T M), Q16 (Gaussian integers / complex arguments), Q17 (logarithm expansion and (t-s)(t+s-4) = 0).
- Modest alternates (same core idea, different route): Q2 (sinh^-1 and growth/IVT instead of the sign of f'), Q7(A/B) overlaps partly with the PDF's root count, Q17 (log expansion is a variant of the standard 1^infinity route, the class analysis is new).
- **No alternate: Q9.** The only route is the exponent-counting pattern f^(k) ~ x^(m-k(n+1)); explicit differentiation of x^2... is the same computation made longer, so it would be a reworded copy.
- **No alternate: Q10.** Same threshold pattern with k = 3 and k = 4; nothing genuinely different exists.
- Every question 1-17 has useful_results.
- Checks run (sympy/numpy): see the answer-key list above; also Q2 (b = 0.9 not injective, b = 1, 1.5 injective), Q4 (h(x) > 0), Q7 (difference of pieces = -(x-2)^2(x+3)), Q16 (arguments).

## make_ppt.py output
- "894 equations converted to native PowerPoint equations", 129 slides, 17 questions. Only note: "Q8: very long question - font reduced to 20 pt" (harmless, four long statements). No warnings, no "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors are only loosely comparable (Q9/Q10 paragraph levels in particular; Q9 = 3, Q10 = 4 is my judgement).
- The paragraph is repeated on both parts Q9 and Q10.
- Python environment: the system PIL was broken; fixed with `pip install --force-reinstall pillow`; numpy and sympy installed for checks (not part of the repo).
