# Part D notes (Q31-Q40)

## CORRECTED questions
- Q35: PDF working has typos: integrand written as sqrt((1-cos t)/(1+sin t)) (should be 1+cos t), garbled "x - sin t dx" (should be dx = -sin t dt), and it stops at pi/3 + ln(2-sqrt3) without matching option (A) form. Fixed and added the final matching step. Answer (A) unchanged.

## WRITTEN questions
- None (all ten had a usable PDF solution).

## Answer-key problems
- None. All ten keys (Q31 A, Q32 A, Q33 5, Q34 D, Q35 A, Q36 B, Q37 C, Q38 A, Q39 C, Q40 D) verified numerically (mpmath).

## Minor PDF slips left as is (notation only, no effect)
- Q33: PDF drops the zero first bracket in its last line (I = 8(1/8+1/2)); I show that bracket explicitly (= 0). Marked "pdf".
- Q34: PDF says "g(x) is increasing" and "f is increasing" (meant phi = g - g'); written correctly.
- Q40: Extra "Remark" bullet added: each b_n individually diverges at x=0 (cos^2(nx)/sin x -> infinity), only differences b_n - b_{n-1} converge. The question is technically ill-posed for b_n alone; the PDF ignores this. Answer unaffected.
- Q36: f is determined only up to adding k*e^{-x} (since the antiderivative is f e^x + C); the question assumes the elementary rational f = (x-1)/(x+1). Not mentioned in the slides.

## NO ALTERNATE
- Q31: NO ALTERNATE: the integral collapses by one cancellation and the determinant step is a single identity; the only other route (adj(M^-1) = M/|M|) is the same identity restated.

## Alternates that are re-framings / weaker than "wholly new"
- Q38: alternate shares the Riemann-sum step; only the integral evaluation differs (x = tan t instead of partial fractions).
- Q37: alternate shares the king-property step; the difference is the evaluation of the trigonometric integral (t = tan x, u = t - 1/t).
- Q40: alternate (sum identity for sin^2(nx)/sin x) is related to the product-to-sum route, but gives b_n in closed form (regularised) rather than just the difference.
- Q39, Q33, Q32, Q34, Q35, Q36: genuinely different techniques (even/odd split; fractional-part periodicity; inverse-function area; product-rule recognition + phase shift; rationalisation; subtract (x+1)^2).

## Assumed / guessed
- Marks = 4 each; Q33 is Numerical, rest SCQ.
- Levels: Q31 2, Q32 2, Q33 1, Q34 3, Q35 2, Q36 2, Q37 2, Q38 2, Q39 1, Q40 2 (adjusted = level). Q33/Q36/Q37 are the closest calls (1 vs 2).
- Page-break check: Q31 starts on PDF p26 after the end of Q30; its working crosses to p27; all of Q31-Q40 are complete (Q40 ends p36).

## LaTeX that pandoc may not convert
- Q31: \begin{cases}...\end{cases} in the stem and \begin{pmatrix} with fractions in the solution; \mathrm{adj} (Q31).
- Q38/Q37: \Big|_0^1 and \Big| (Q38 solution); \ldots; \Big| could be swapped for \left.\right| if it fails.
- Q36 concept string is plain text (no LaTeX).
