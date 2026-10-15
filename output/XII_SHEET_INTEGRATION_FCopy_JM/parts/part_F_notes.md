# Part F notes (Q51-Q60)

All 10 questions: every PDF answer matched the true answer (checked numerically with mpmath); no answer-key problems.

## CORRECTED (PDF working had slips; answer unchanged)
- Q54: PDF's second display line ends with ln(49/50) where the RHS is still ln(49/40); 49/50 only appears after moving ln(4/5) across.
- Q57: PDF's first line equates the constant sqrt3/2 to the integral (I missing, factor sqrt3/2 not carried into the numerator); also jumps from the split integrals to the answer without the cosec/sec integrals (added).
- Q60: PDF has -3e^{-x} in the numerator (given: -6e^{-x}); antiderivative drops the factor sqrt2 (correct: sqrt2*arctan(sqrt2 e^x/3)); constant c = -pi/4 - arctan(sqrt2/3) is inconsistent with the given point (correct c = pi/(2sqrt2) + sqrt2*arctan(sqrt2/3)). Final e^alpha is right.

## WRITTEN
- None. (Q52, Q57, Q59 PDF steps were terse; I expanded skipped one-line steps such as A=2B, the integrals of csc/sec, and the periodic shift, but kept the PDF's method. Q51/Q55 PDF has typos "(A)+(2)" and a misplaced bracket in the last line; treated as notation only, source = pdf.)

## NO ALTERNATE
- Q52: separable-kernel (degenerate kernel) method is the only route; parity/linear-system variants are the same idea.
- Q54: partial fractions is the only practical route; substituting t=1/x or hyperbolic forms are re-labellings of the same decomposition.
- Q60: split + u=e^x + arctan is the only route; a definite-integral version between the two points (no constant c) is only a re-framing, so omitted.

## Alternates that are partly re-framings (flag for review)
- Q55 alternate (shift x = pi/2 + u, even/odd parts): the same symmetry as the king property viewed about the midpoint; still gives a different computation.
- Q58 alternate (u = cot x, exact derivative of (1+u^2)^1011/u): replaces by-parts by spotting an exact derivative; the closed form is the same antiderivative.
- Q59 alternate is a Fourier/orthogonality argument (genuinely different, but beyond the usual syllabus; kept as an elegant extension).
- Q53 alternate (max{f,x} = x + (f-x)^+) is a different decomposition of the same integral rather than a new idea.

## Levels (rubric-based, all Main-style)
Q51 2, Q52 2, Q53 3, Q54 2, Q55 2, Q56 3, Q57 3, Q58 2, Q59 3, Q60 3. Chapter for Q57/Q58 given as "Indefinite Integration", Q60 as "Integration - Differential equation". Marks 4 assumed for all (no marks printed).

## Assumptions / checks
- Q51 options, Q57 and Q58 options (B)-(D) were read from the page images.
- Q54 uniqueness of b shown by monotonicity (positive integrand).
- Q60 verified by solving the ODE numerically (odefun) from the first point: it passes through (alpha, e^{2 alpha}/2) with e^alpha = 5.9049.

## LaTeX that pandoc may not convert
- Q54 useful result uses \operatorname{arcoth}; may fall back to plain text.
- Q57/Q59/Q51 use \begin{cases} (Q59 question) which the schema says is supported; \mathrm{odd} in subscripts (Q59 useful result, Q57 none) may need checking.
- Q51 option (B)/(D) and Q55/Q56 contain nested \frac inside integrals; standard, but long bullets in Q51 solution bullet 2 (~225 chars) are near the length limit.
