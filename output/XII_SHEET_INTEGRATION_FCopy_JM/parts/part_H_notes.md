# Part H notes (Q71-Q80)

## CORRECTED questions (solution_source = corrected)
- Q71: PDF writes upper limit 3 instead of e^3 in the line "integral of ln t / t dt"; answer unchanged.
- Q75: PDF a_2 = 3 + 3/2 = 9/2 is wrong (true 15/4); a_3 = 100/9 is wrong (true 82/9); no argument given for n >= 5 (added). Answer 5 unchanged.
- Q76: PDF line I2 = -n(2n+1){I2 + I1} has wrong sign (should be I2 - I1); next line is consistent with the correct sign. Answer 24 unchanged.
- Q79: three print slips (factor 15 vs 30 after the u-substitution; coefficient 2/5 vs 2/3; bracket "-1/5 + sqrt3 + ..." should be "-sqrt3/5 + ..."). Answer 10 unchanged.

## WRITTEN questions
- None.

## Answer-key problems
- None. All ten answers (D, A, 5, 8, 5, 24, 385, 12, 10, 104) verified numerically with mpmath.
- Q72/Q74/Q80 PDF text has minor typesetting garbles (e.g. "3x^2-3x-2x+2I+1" = 3x^2-5x+2 split) but the working is correct; kept as pdf.

## NO ALTERNATE
- Q75: no genuinely different method; the problem is term-by-term integration followed by direct evaluation and bounding.

## Alternates that are re-framings (not wholly new ideas)
- Q73: Riemann-sum reading of the LHS plus monotonicity test instead of the closed-form AP sum and quadratic.
- Q74: integrate by parts first (reduces to the same one-derivative-at-0 argument).
- Q79: power-rule integration in t after writing t-1=(t+1)-2, instead of the second substitution.
- Genuinely different: Q71 (differentiate f(a)+f(1/a)), Q72 (layer-cake / level-set lengths), Q76 (Beta/Gamma), Q77 (f+|f|=0 cancellation), Q78 (parts under the integral, no substitution), Q80 (Chebyshev U_5 + Wallis).

## Assumed / guessed
- Level calibration (Q71 2, Q72 3, Q73 2, Q74 2, Q75 3, Q76 3, Q77 2, Q78 3, Q79 2, Q80 1) is by anchor comparison only; Q75 confidence Low.
- Q75 shows interval (2,30) open, so a_1 = 2 is excluded.
- Q72 stem is the "+1" inside the bracket version; options as printed.

## LaTeX that pandoc might struggle with
- Q75/Q79 use \sqrt3^{\,5} (thin-space in superscript); Q79 \left[ ... \right]_{a}^{b} subscript/superscript after \right]; Q76 uses \Gamma and B(p,q) only as plain letters. If any fails, replace \, with nothing.
- Q72 alt uses a_{-1}, a_0, a_1 symbols (plain subscripts).
