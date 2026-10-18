# Definite_Integration: generation report

Blueprint: `qp_blueprints/Definite_Integration.xlsx`. There is no `Definite_Integration_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. They were installed with `python3 -m pip install pandas openpyxl sympy mpmath python-docx lxml`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The paper title in `meta.json` is "Definite Integration". The file names use `Definite_Integration`.
- `build_paper.py` passed on the first run, with no errors and no warnings. No script was edited.
- Page 1 of each of the three PDFs was rendered and checked. The Hindi is shaped correctly and the equations are 2D.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the paper has only Single Correct and Numerical types and nothing above level 3. The paper name comes from the file name.
- **Paper:** 37 questions: 8 Single Correct (Q1-Q8), then 29 Numerical (Q9-Q37).
- **Reorder (`--reorder`):** the single-correct rows moved to the front. Old -> new:
  589->1, 597->2, 605->3, 610->4, 612->5, 613->6, 624->7, 625->8, 590->9, 591->10, 592->11, 593->12, 594->13, 595->14, 596->15, 598->16, 599->17, 600->18, 601->19, 602->20, 603->21, 604->22, 606->23, 607->24, 608->25, 609->26, 611->27, 614->28, 615->29, 616->30, 617->31, 618->32, 619->33, 620->34, 621->35, 622->36, 623->37.
- **Answer Plans:** the blueprint had none, so the script drew all 37:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A, Q6 Option B, Q7 Option D, Q8 Option C;
  Q9 negative integer, Q10 positive 2-digit integer, Q11 negative decimal, Q12 decimal between 0 and 1, Q13 positive 3-digit integer, Q14 positive decimal, Q15 positive decimal,
  Q16 negative decimal, Q17 positive 2-digit integer, Q18 positive 3-digit integer, Q19 negative integer, Q20 decimal between 0 and 1, Q21 negative integer, Q22 negative decimal,
  Q23 positive 3-digit integer, Q24 decimal between 0 and 1, Q25 positive decimal, Q26 positive 2-digit integer, Q27 positive decimal, Q28 negative decimal, Q29 negative integer,
  Q30 positive 2-digit integer, Q31 decimal between 0 and 1, Q32 positive 3-digit integer, Q33 positive 2-digit integer, Q34 positive decimal, Q35 decimal between 0 and 1,
  Q36 negative integer, Q37 positive 3-digit integer. Every answer matches its plan; the build checks this.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **Cells containing ";":** the reader warned about rows 3 and 4. The cell is "Evaluation via the antiderivative; handling discontinuous antiderivatives" (Q10 and Q11). There is no config, so it was kept as **one concept**. Both questions use both halves: evaluation through an antiderivative, and the jump of that antiderivative.
  - **More than two concepts in a Main row:** Q2, Q4, Q6, Q16 and Q23 list 3 concepts, and Q15 lists 4. All were kept, and every concept is used.
  - **Concepts repeated across rows:** this is expected in a one-chapter paper, and each repeat uses a different mechanism. King's rule appears in Q2, Q13, Q14, Q15 and Q16. Queen's rule appears in Q2, Q14, Q15 and Q17. Odd/even appears in Q2, Q15, Q16 and Q18. The 2a-property appears in Q15, Q18, Q19 and Q20. Periodic functions appear in Q20 and Q21. Newton-Leibniz appears in Q5, Q6, Q8, Q9 and Q27. Max/min of an integral function appears in Q6, Q27, Q28 and Q29. FTC appears in Q1, Q9 and Q11. Additivity appears in Q3, Q22 and Q23. GIF/fractional part appears in Q3, Q23, Q24 and Q25. Modulus/max-min appears in Q23 and Q25. Function and inverse appear in Q4 and Q26. Limit of a sum appears in Q16, Q30 and Q31. Estimation appears in Q32 and Q33. Wallis appears in Q34, Q35 and Q37. Gamma appears in Q7 and Q35. Reduction appears in Q36 and Q37. Substitution appears in Q12 and Q13. Limits and functional equations appear in Q6 and Q8.
  - There were no errors. The blueprint file was not edited.

## Answers
Q1 (C) -192, Q2 (A) pi^2/2, Q3 (B) 53/6, Q4 (D) 6/pi^2, Q5 (A) (e^2-1)/4, Q6 (B) -81/20, Q7 (D) 1/2, Q8 (C) 3,
Q9 -30, Q10 21, Q11 -2.36, Q12 0.70, Q13 144, Q14 3.50, Q15 1.57, Q16 -2.09, Q17 35, Q18 256, Q19 -8, Q20 0.41, Q21 -20, Q22 -5.50,
Q23 105, Q24 0.30, Q25 1.50, Q26 64, Q27 2.41, Q28 -29.50, Q29 -3, Q30 54, Q31 0.50, Q32 449, Q33 90, Q34 31.42, Q35 0.45, Q36 -41, Q37 261.
Each answer was recomputed with mpmath or sympy, separately from the hand solution:
- Quadrature over the split points was used for Q2-Q4, Q10-Q15, Q17-Q19, Q22-Q25, Q28, Q32-Q37. Q4 used a numerical inverse.
- Symbolic checks were used for Q1, Q5, Q6 and Q9: solving the system, checking the solution satisfies the integral equation, checking the functional equation.
- Q16, Q30 and Q31 were checked with the Riemann sum at large n.
- Q20 was checked with the period average and a long-interval average.
- Q21 was checked with the example f = pi sin(pi x).
- Q26 used root-finding for the implicit g.
- Q27 used a root of F'.
- Q29 used the signs of G' on both sides of each critical point.
- Decimal answers that are rounded (Q11 -3pi/4, Q15 pi/2, Q16 -2pi/3, Q20 sqrt2-1, Q24 2 ln2 - 13/12, Q27 1+sqrt2, Q34 10 pi, Q35 pi/7) are all more than 0.0005 away from a rounding boundary (closest: Q16, -2.0944).

## Difficulty
- **Level distribution:** 22 questions at level 2 and 15 at level 3. Every question is rated at its target level, and none is one level off.
- **Marks-weighted index: 2.41.** No equivalence-relation or multi-correct adjustments apply. This is a Main-pattern chapter paper, so it is not expected to fall in the Advanced range of 2.6-3.2.
- **Borderline ratings (Medium confidence):**
  - Q10, Q12 and Q24 at level 2 could be read as 1. Each has a single trap: the antiderivative jump, a non-monotone substitution, and the breakpoints of [1/x].
  - Q2, Q14, Q15 and Q23 at level 3 are the hardest of their level. Q15 chains four properties and Q23 has 14-piece casework, so either could be read as 4.
- **Consistency pass:** the hardest level-2 questions (Q13, Q21, Q25) were read next to the easiest level-3 ones (Q9, Q14, Q20), and the order was kept.

## Originality report (per question)
Each mechanism was named before the stem was written and checked against `known_skeletons.md`. None matched, and the build's skeleton lint gave no warning. Every question was web-searched with WebSearch (standard mode); the results are in the table. Two first designs were found online and redesigned:
- **Q3:** int_1^5 {x}^[x] dx. allen.in has int_1^4 {x}^[x] dx.
- **Q24:** int_0^1 {2x}{3x} dx. allen.in has int_0^1 ({2x}-1)({3x}-1) dx.

A third, **Q31** (lim prod (k/n)^(k/n^2)), turned out to be listed in OEIS A366271 and was also redesigned.

| Q | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|
| Q1 | 2 | 2 | three vanishing integrals of an unknown cubic are read as roots of its antiderivative, which fixes P up to a constant; p(0) = P'(0) fixes the constant (way 5) | not found |
| Q2 | 3 | 3 | the weight x + sin x is split as a constant plus a part odd about x = pi, on an interval centred at pi, and the remaining modulus integrand reduces to a king pair (way 5) | not found |
| Q3 | 2 | 2 | the greatest integer function is the exponent of a variable base, so each unit interval carries a different power of x (way 2) | found: redesigned |
| Q4 | 3 | 3 | a perturbation x - sin(pi x)/(2 pi) of the identity whose graph and inverse graph form a chain of loops through the integer points, cut by a strip (way 4) | ingredient only |
| Q5 | 2 | 2 | an integral equation with the kernel e^{x-t} and a forcing x^2, whose differentiation feeds the integral back through the equation itself (way 5) | ingredient only |
| Q6 | 3 | 3 | a cubic functional equation fixed by a limit, followed by the extremum of the integral of f over the moving interval [x, 2x] (way 5) | ingredient only |
| Q7 | 2 | 2 | the Gamma integral is placed inside a power series so that n! cancels and a geometric series remains, equal to int_0^inf e^{2x} e^{-4x} dx (way 5) | ingredient only |
| Q8 | 2 | 2 | the integrand is known only through a functional equation and a limit, and the integral runs over [x, x^2], whose length is first order in x - 1 while the integrand is also first order, giving a second-order zero (way 5) | not found |
| Q9 | 3 | 3 | the integral of f over a sliding window of fixed length is prescribed, which becomes a difference equation for f; the lost constant must be recovered from the integral itself (way 5) | ingredient only |
| Q10 | 2 | 2 | the unknown is the upper limit k, so the student must count how many quarter-periods the integral covers while the obvious antiderivative resets at every pole of tan x (way 5) | ingredient only |
| Q11 | 3 | 3 | the evaluation point is chosen beyond the jump of the natural antiderivative tan^-1(x/(1-x^2)) and exactly where its argument equals 1, so the naive answer pi/4 is wrong and the correct one is -3 pi/4 (way 4) | not found |
| Q12 | 2 | 2 | an integrand whose natural substitution u = x^2 looks valid over the whole interval but is not one-one there, so the limits must be changed piecewise (way 5) | not found |
| Q13 | 2 | 2 | a logarithmic integrand on [1, e^12] that becomes a king pair only after the exponential substitution, with a symmetric polynomial weight t(12-t) (way 5) | not found |
| Q14 | 3 | 3 | one integrand is integrated over two nested intervals sharing the centre 2, so the king pair and the queen pair act together and the ratio of two symmetric polynomial integrals remains (way 5) | not found |
| Q15 | 3 | 3 | an interval of length 2 pi centred at pi/2 (not at 0), on which a reflection about pi/2 removes the exponential factor and the remaining integral must be reassembled from three pieces by evenness, the 2a-property and king's rule (way 5) | not found |
| Q16 | 3 | 3 | a Riemann sum over [0,2] whose integral has no elementary antiderivative but collapses by the king pairing of cot^-1(y) and cot^-1(-y), with a symmetric weight (way 5) | not found |
| Q17 | 3 | 3 | the complementary tan^5 factor sits on a non-constant symmetric weight 1/(sin^4 x cos^4 x) over [pi/8, 3pi/8], so after the queen pairing a genuine trigonometric integration remains (way 5) | ingredient only |
| Q18 | 2 | 2 | a two-level symmetry: the integrand is even about 0 after the odd part is dropped, and the even part is itself symmetric about 4 on [0,8], so the modulus is removed by halving twice (way 5) | not found |
| Q19 | 2 | 2 | a product of a quadratic and the modulus of a shifted copy of it, both symmetric about x = 2, so the 2a-property halves the interval and removes one of the two sign changes of the modulus (way 5) | not found |
| Q20 | 3 | 3 | the long-run mean value of a periodic function, where the period integral must be halved by symmetry so that the tan substitution is legitimate (way 5) | ingredient only |
| Q21 | 2 | 2 | an anti-periodic function (f(x+1) = -f(x)) with only int_0^1 f known, so the weighted integral must be computed without knowing f, the unknown moment cancelling (way 4) | not found |
| Q22 | 2 | 2 | a rational function with a modulus denominator that reduces to x times a sign pattern, so the piecewise structure (and the jump at 1) is hidden in a single formula (way 5) | not found |
| Q23 | 3 | 3 | the maximum of a step function and a V-shaped function, where the V wins only on [0,4] and the steps win elsewhere; the student must locate the switch (way 2) | not found |
| Q24 | 2 | 2 | the fractional part of a reciprocal on a finite interval, whose breakpoints are 1/n (unequally spaced), giving a log sum minus a harmonic sum (way 2) | found: redesigned |
| Q25 | 2 | 2 | the minimum of the sawtooth {x} and a slow V-shaped line /x-3//3, whose crossing points move inside each tooth (way 2) | not found |
| Q26 | 2 | 2 | the function is given only by the implicit relation g^3 + g = x, so the student must recognise g as an inverse before using the inverse-integral relation (way 5) | ingredient only |
| Q27 | 2 | 2 | the window integral of t^2 2^{-t} has its maximum where the integrand takes equal values at both ends, which here gives (x+1)^2 = 2x^2 and the irrational point 1 + sqrt2 (way 5) | not found |
| Q28 | 2 | 2 | the integrand has a stationary point without sign change (the modulus factor) and the global minimum is at the other root, where the integral must be split at the corner (way 5) | not found |
| Q29 | 3 | 3 | the upper limit x^2 + 2x and the double zero of the integrand at t = -1 combine into a fifth-power factor (x+1)^5 in G', so x = -1 is an extremum invisible to the second derivative test (way 5) | not found |
| Q30 | 2 | 2 | a Riemann sum over [0,6] with a modulus that changes sign at k = 3n, so the sum cannot be done by one power-sum formula and the integral needs a split (way 5) | not found |
| Q31 | 3 | 3 | a product of the ratios 2k/(n+k), each tending to a different value, whose geometric mean tends to exactly 1/2 through cancellation of log integrals (way 4) | found: redesigned |
| Q32 | 2 | 2 | a non-elementary integral pinned between two consecutive integers by subtracting the main term x and bounding the small remainder by x e^{-x} (way 4) | not found |
| Q33 | 3 | 3 | a Fresnel-type integral with no elementary antiderivative, bounded tightly enough to fix two digits by polynomial inequalities proved with monotonicity (way 5) | ingredient only |
| Q34 | 2 | 2 | an algebraic integral over [0,4] that turns into a mixed Wallis integral sin^6 cos^2 under x = 4 sin^2 theta (way 5) | ingredient only |
| Q35 | 2 | 2 | two Wallis-type integrals with half-integer exponents, neither elementary, whose product is elementary (pi/7) by the Gamma form (way 4) | ingredient only |
| Q36 | 2 | 2 | a reduction formula whose constant terms build up as -(1 + n + n(n-1) + ...), i.e. I_n = n! e - sum n!/k!, so the integer part b is a 'partial factorial sum' (way 1) | not found |
| Q37 | 3 | 3 | moments of cos^-1 x, where one integration by parts turns them into Wallis integrals of the next order, giving a two-step reduction with squared denominators (way 1) | not found |
**Standard ingredients worth flagging** ("ingredient only" in the table):
- Q4: the area between f and its inverse is a textbook type; allen.in has f(x) = x + sin x. Here the loops sit at the integers and the region is cut by a strip.
- Q5: integral equations with an exponential kernel are textbook. The x-dependent kernel and polynomial forcing are new.
- Q6: cubic functional equations are standard.
- Q7: the Gamma formula for int x^n e^{-ax} dx.
- Q9: the derivative f(x+1) - f(x-1) of a window integral appears in a homework sheet. The polynomial recovery with the lost constant was not found.
- Q10: arctan(tan x / a) antiderivatives with jumps are known. The count-of-pieces question was not found.
- Q17: a related allen.in problem uses tan^5 x + cot^5 x on [pi/6, pi/4] with a different weight.
- Q20: the period average and int dx/(1+cos^2 x) are standard.
- Q26: the inverse-integral identity for x^3 + x is standard. Here the inverse is given only implicitly.
- Q33: the Fresnel-type value is known. The monotonicity bounds are the exercise.
- Q34: x^n sqrt(2ax - x^2) integrals appear in textbooks.
- Q35: the Wallis identity W_n W_{n+1} = pi/(2(n+1)) for integer n is standard. Here it is extended to fractional exponents via Gamma.
- Novelty cannot be guaranteed. Please flag any question you recognise.

## Problems found while verifying
- **Q3, Q24, Q31:** redesigned after the web check, as described above.
- **Q2 and Q15:** the first draft of Q15 used the same "x-weight and queen reflection" idea as Q2, with the same value pi^2/2. Q15 was rebuilt around a 1/(1+e^{cos x}) pairing.
- **Q14 and Q16:** both then used the same exponential complement device. Q14 was switched to the sqrt x/(sqrt x + sqrt(4-x)) pair and Q16 to cot^-1, so the three questions use three different pairing devices.
- **Q27:** F(x) = int_x^{x+1} t^2 2^{-t} dt has no global maximum, because F tends to infinity as x tends to minus infinity. The stem asks for the (unique) local maximum.
- **Q9:** without "polynomial" in the stem, f would not be unique, so the word was added.
- **Q28:** x = 2 is a stationary point that is not an extremum; the solution says so.
- **Q29:** the second derivative test fails at x = -1; the first derivative test is used there.
- The shortened solution of Q1 and the full solutions of Q11 and Q37 had loose wording in a first draft. This was corrected before the build.

## Rows whose concepts were hard to combine naturally
- **Q15** (four concepts: King, Queen, odd/even, 2a-property). All four are used, but in one sense they are the same reflection idea. The question uses an off-centre interval [-pi/2, 3pi/2] so that each property does a distinct job.
- **Q2** (King, Queen, odd/even): the queen step and the odd-function step are two views of the same cancellation. The solution shows both.
- **Q14** (King and Queen): two integrals of one function over nested intervals, [0,4] and [1,3], asked as a ratio.
- **Q35** (Wallis and Gamma): Wallis alone cannot handle fractional exponents. The Wallis product relation is extended through the Gamma form.

## Notes
- The Hindi is the assistant's own translation. Please review the specialised terms: एकैकी आच्छादक (bijection), स्थानीय चरम बिन्दु (point of local extremum), मुख्य मान (principal value).
- The stem review is a self-check; an independent reader may still find things.
- `_source/` holds `blueprint.json`, every `qNN.json` and `meta.json`, so a question can be fixed and the paper rebuilt with `build_paper.py`.
