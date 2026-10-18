# Differential Equation: generation report

Blueprint: `qp_blueprints/Differential_Equation.xlsx`. There is no `Differential_Equation_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. They were installed with `python3 -m pip install pandas openpyxl sympy mpmath python-docx lxml`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The paper title in `meta.json` is "Differential Equation", and the file names use `Differential_Equation`.
- The build passed on the first full run with no errors and no warnings. No script was edited and no check was weakened.
- Page 1 of each of the three PDFs, and the page with Q2's case-defined options, were rendered and checked. The Hindi is shaped correctly and the equations (fractions, derivatives, cases) are 2D.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the paper has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 32 questions: 7 Single Correct (Q1-Q7), then 25 Numerical (Q8-Q32).
- **Reorder (`--reorder`):** the single-correct rows moved to the front. Old -> new:
  629->1, 630->2, 643->3, 644->4, 651->5, 654->6, 656->7, 626->8, 627->9, 628->10, 631->11, 632->12, 633->13, 634->14, 635->15, 636->16,
  637->17, 638->18, 639->19, 640->20, 641->21, 642->22, 645->23, 646->24, 647->25, 648->26, 649->27, 650->28, 652->29, 653->30, 655->31, 657->32.
- **Answer Plans:** the blueprint had none, so the script drew all 32:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A, Q6 Option B, Q7 Option D;
  Q8 negative integer, Q9 positive 2-digit integer, Q10 negative decimal, Q11 decimal between 0 and 1, Q12 positive 3-digit integer, Q13 positive decimal,
  Q14 positive decimal, Q15 negative decimal, Q16 positive 2-digit integer, Q17 positive 3-digit integer, Q18 negative integer, Q19 decimal between 0 and 1,
  Q20 negative integer, Q21 negative decimal, Q22 positive 3-digit integer, Q23 decimal between 0 and 1, Q24 positive decimal, Q25 positive 2-digit integer,
  Q26 positive decimal, Q27 negative decimal, Q28 negative integer, Q29 positive 2-digit integer, Q30 decimal between 0 and 1, Q31 positive 3-digit integer,
  Q32 positive 2-digit integer. Every answer matches its plan; the build checks this.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **Cells containing ";":** eight concept cells contain ";" (the check reported them as sheet rows 5, 6, 7, 17, 18 (two cells), 23 and 32; in the paper they are in Q2, Q3 (two cells), Q11, Q12, Q22, Q26 and Q32), for example "Linear differential equation in y; integrating factor". With no config, each cell was kept as **one** concept, as instructed. These names read as single concepts.
  - **Three concepts in a Main row:** Q12 (variable separable, homogeneous, linear) and Q15 (f(ax+by+c), general substitution, polar substitution). Both were kept, and every concept is used.
  - **Concepts repeated across rows:** this is expected in a one-chapter paper. Each repeat uses a different mechanism. The check listed 29 repeats, for example "Linear differential equation in y; integrating factor" in Q3, Q12, Q22 and Q32, and "Formation of a differential equation by eliminating arbitrary constants" in Q1, Q9, Q10 and Q28.
  - There were no errors. The blueprint file was not edited.

## Answers
Q1 (C), Q2 (A), Q3 (B) e^2+e, Q4 (D) 4e^2, Q5 (A) 4, Q6 (B) 2N/3, Q7 (D) e^4+7,
Q8 -8, Q9 12, Q10 -4.25, Q11 0.25, Q12 112, Q13 2.75, Q14 3.25, Q15 -0.50, Q16 88, Q17 110, Q18 -4, Q19 0.75, Q20 -3, Q21 -1.50,
Q22 144, Q23 0.40, Q24 3.60, Q25 27, Q26 5.50, Q27 -1.50, Q28 -5, Q29 16, Q30 0.72, Q31 194, Q32 50.

Each answer was recomputed with sympy, separately from the hand solution:
- **Direct substitution into the differential equation:** every closed-form solution was substituted back into its equation (residual 0), and the initial or boundary values were checked.
- **`dsolve` cross-checks:** Q3, Q4, Q7, Q12 and Q32.
- **Second routes:** Q10 (the slopes from the two circles a = 10 +- sqrt 42), Q21 (each straight-line solution substituted into the equation), Q27 and Q28 (orthogonality checked at a point, slope product -1), Q6 (the logistic formula differentiated back).
- **Numerical checks:** Q9 (rank 11 of the Wronskian matrix at a random point), Q15 (g stays positive on (-pi, 1)), Q17 and Q18 (residual of the equation at several points of the chosen branch), Q26 (branch continuity on [2, 11/4]).
- **Rational search:** used to pick the reading points so that answers are exact (Q26).
- All decimal answers are exact to two places; none is rounded.

## Problems found while verifying
- **Q27:** the first design (orthogonal trajectories of x^2 + 3y^2 = cy) turned up in the web check as a published tutorial exercise. It was replaced by the family y = c(x+1)/x, whose trajectories are the cubics 3y^2 = 2x^3 + 3x^2 + const. The new design was web-checked again (not found).
- **Q15 and Q28:** errors in the solution text were corrected before the build: a garbled intersection step in Q15, and an inverted slope fraction in Q28's shortened solution. The answers did not change.
- **Branch choices:** these were made explicit in the stems with a stated interval, sign or region, because the solution curves are conics or cubics with more than one branch:
  - Q11 (the splice point)
  - Q13
  - Q17
  - Q18 (the lower arc)
  - Q19
  - Q20
  - Q26

## Rows whose concepts were hard to combine naturally
- **Q12 (separable, homogeneous, linear):** a single equation that genuinely needs all three does not exist. The question uses two linked functions. f comes from a homogeneous equation that is solved by separation, and it is the forcing term of a linear equation for g. The integrating factor 1 + x^2 cancels f's denominator, which is the link.
- **Q15 (f(ax+by+c), general substitution, polar):** the equation is somewhat artificial. It uses the polar angle inside the bracket so that all three substitutions (polar, s = r^2, u = s + 2 theta) are needed.
- **Q22 (linear in y, linear in x):** the forcing term of the dx/dy-linear equation is the function found from a dy/dx-linear equation. This is a chained two-part question.

## Difficulty
- **Level distribution:** 27 questions at level 2 and 5 at level 3 (Q6, Q11, Q12, Q15 and Q21). Every question is rated at its target level, and none is one level off.
- **Marks-weighted index: 2.16** (SCQ 3 marks, Numerical 4 marks). No equivalence-relation or multi-correct adjustments apply. This is a Main-pattern chapter paper, so it is not expected to fall in the Advanced range of 2.6-3.2.
- **Borderline ratings (Medium confidence):**
  - Q8 at level 2 could be read as 1. It is order and degree only, with the clearing of two fractional exponents as the trap.
  - Q2, Q9, Q10, Q18 and Q28 at level 2 are conceptual or multi-step and could be read as 3.
  - Q6, Q12, Q15 and Q21 are the easiest level-3 questions.
- **Consistency pass:** the hardest level-2 questions (Q18, Q20, Q26, Q28) were read next to the easiest level-3 ones (Q6, Q12, Q21). The order was kept, because each level-3 question links two ideas and the level-2 questions are single chains.

## Stem review
`review_stems.py` was run, and each English stem was read as a student would read it: symbols and domains defined, conditions complete, one reading, a unique answer equal to the plan, and options in one form. The result is recorded in each question's `stem_review`. This is a self-check, and an independent reader may still find things. The Hindi is the assistant's own translation. Please review the specialised terms, for example लंबकोणीय संछेदी for orthogonal trajectory.

## Originality report (per question)
- **Mechanism check:** each mechanism was named before the stem was written and checked against `known_skeletons.md`. None matched, and the build's skeleton lint gave no warning.
- **Web check:** every question was web-checked with WebSearch (standard mode), searching the distinctive equation or construction. Only Q27's first design was found, and it was redesigned.
- **"ingredient only":** the method (Bernoulli, integrating factor, orthogonal trajectories, and so on) is a standard textbook ingredient, but the specific construction was not found.
- **Caveat:** perfect novelty cannot be guaranteed. Several level-2 questions are built on standard ingredients by design. Please flag any question you recognise.

| Q | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|
| Q1 | 2 | 2 | the differential equation of the family of all tangent lines of y = e^x (an envelope relation of d'Alembert type), obtained by eliminating the point of contact | ingredient only |
| Q2 | 2 | 2 | the general solution of xy' = 2y, obtained on each half-line, does not cover all solutions on R because the equation degenerates at x = 0; the question asks which function is a genuine solution outside the family | ingredient only |
| Q3 | 2 | 2 | a linear equation whose constant is fixed not by a value of f but by the limit of f(x)/x at the singular end x = 0, where x ln x vanishes (way 5) | ingredient only |
| Q4 | 2 | 2 | a curve given in differential form that is linear only when x is the dependent variable, and is then read at a given height | ingredient only |
| Q5 | 2 | 2 | a curve defined by where its normal meets the x-axis, relative to the abscissa of the point | ingredient only |
| Q6 | 3 | 3 | a logistic growth problem in which the two data points make the odds ratio R/(N-R) double each hour, read at a time after the midpoint | ingredient only |
| Q7 | 2 | 2 | a boundary value problem for x y'' + y' = 4x, whose left side is the exact derivative (x y')', with values given at x = 1 and x = e | not found |
| Q8 | 2 | 2 | a degree that is larger than expected because two fractional exponents with different denominators must be cleared together | ingredient only |
| Q9 | 2 | 2 | a family with 20 visible constants whose span is only the 11 functions 1, cos 2x, ..., cos 20x, so the order of its equation is 11 (way 4, hidden reduction) | ingredient only |
| Q10 | 2 | 2 | the differential equation of a one-parameter family of circles is quadratic in the slope, and its two roots at a point are the slopes of the two members through that point (way 5) | not found |
| Q11 | 3 | 3 | an equation with a singular solution where the two conditions y(0) = 0 and y(2) = 1 can be met only by a spliced solution (zero, then a parabola), so the particular solution is not a member of the general solution (way 5) | ingredient only |
| Q12 | 3 | 3 | the integrating factor 1 + x^2 of the linear equation for g is exactly the denominator of f, which comes from the homogeneous equation, so (1 + x^2) f = 2x^3 and g becomes a polynomial (way 5) | not found |
| Q13 | 2 | 2 | an equation that looks like the reducible-to-homogeneous type but has parallel lines, so the substitution u = x - y is forced and gives u^2 = x + 1 | ingredient only |
| Q14 | 2 | 2 | two successive substitutions, first t = e^y and then u = x + t, turn the equation into u' = u^2 (way 5) | ingredient only |
| Q15 | 3 | 3 | a Cartesian differential form that becomes, after the polar substitution and s = r^2, an equation of type f(s + 2 theta), integrated with u' = u^2, and then read on a circle (way 5) | not found |
| Q16 | 2 | 2 | the substitution y = vx used outside its usual homogeneous setting, where it gives the autonomous equation v' = 1/v^2 (way 5) | ingredient only |
| Q17 | 2 | 2 | a differential equation that in polar terms says dr = dx + dy, so the solution is a focus-directrix curve with eccentricity sqrt 2 (a rectangular hyperbola (x-10)(y-10) = 50) (way 4) | not found |
| Q18 | 2 | 2 | a homogeneous equation written in polar-friendly differentials whose solutions are the circles x^2 + y^2 = k(x + 2y) through the origin, read on the correct arc (way 5) | not found |
| Q19 | 2 | 2 | a reducible-to-homogeneous equation whose solutions are the hyperbolas (y - 1)(x + y - 2) = K, so the curve meets the line x + y = 5 where it meets X + Y = 3 and Y follows at once (way 4) | ingredient only |
| Q20 | 2 | 2 | a reducible-to-homogeneous equation with coefficient pattern (1,3;3,1) whose solution family is the parabolas X + Y = K(X - Y)^2, with a branch decision at the end (way 5) | ingredient only |
| Q21 | 3 | 3 | the straight-line solutions of a reducible-to-homogeneous equation are the members of the pencil through the centre whose slope is fixed by m = (a1 + b1 m)/(a2 + b2 m), so the parameter of the family of lines is the unknown (way 5) | not found |
| Q22 | 2 | 2 | the forcing term of a dx/dy-linear equation is a function found first from a dy/dx-linear equation, so the same tool is used with the roles of the variables swapped (way 5) | ingredient only |
| Q23 | 2 | 2 | a Bernoulli equation whose solution is the rational function 4x/(x^4 + 4), read at x = 2 | ingredient only |
| Q24 | 2 | 2 | a Bernoulli equation with n = -1 reduced by u = y^2, with the reading point chosen so that x^2 + 3x is a perfect square of a rational | ingredient only |
| Q25 | 2 | 2 | an equation whose solution is y = x^x, hidden behind the substitution u = ln y (way 4) | not found |
| Q26 | 2 | 2 | a non-exact equation that becomes d(xy + x^2/y) = 0 after dividing by y^2, followed by a branch choice for the quadratic in y (way 5) | ingredient only |
| Q27 | 2 | 2 | the orthogonal trajectories of the hyperbolas y = c(x+1)/x are the cubic curves 3y^2 = 2x^3 + 3x^2 + const, and the one through (12,36) is the nodal cubic 3y^2 = x^2(2x + 3) | found: redesigned |
| Q28 | 2 | 2 | the orthogonal trajectories of circles through the origin with centres on y = x are circles through the origin with centres on y = -x, read off one member's second x-intercept | ingredient only |
| Q29 | 2 | 2 | a curve defined by the constant area of the triangle formed by the ordinate, the tangent and the x-axis, which forces y' proportional to y^2 and a curve that blows up at x = 8 | ingredient only |
| Q30 | 2 | 2 | a mixture problem in which the tank drains, so the salt is a power of the volume, S = S0 (V/V0)^2, rather than an exponential (way 4) | ingredient only |
| Q31 | 2 | 2 | the functions for which the rule 3 integral_0^x f = x(f(x) + 2f(0)) holds exactly are the quadratics with no linear term, found by differentiating an integral identity (way 3) | not found |
| Q32 | 2 | 2 | a linear equation whose solution is selected by a growth condition at infinity instead of an initial value; only the polynomial solution survives (way 5) | ingredient only |
