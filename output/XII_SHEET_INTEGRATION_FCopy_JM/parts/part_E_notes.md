# Part E notes (Q41-Q50)

## CORRECTED (PDF working had slips; all final answers/keys were right)
- Q41: PDF's (1)+(2) line typesets the first bracket term as e^{1/(x|x|+1)}; should be 1/(e^{x|x|}+1).
- Q43: PDF first line shows sin^2 x on the right (derivative uses sin^3 x); last lines write f(1/sqrt3) for f'(1/sqrt3).
- Q44: sign slip in last line: "+7(ln(1-1/7) - 1/7)" should be "+7(ln(1-1/7) + 1/7)"; final 1+6 ln(6/7) is right.
- Q46: denominator printed cos h should be sin h (sec(pi/2-h)=cosec h); L'Hopital line sign wrong (limit of f/sin h is -1, so 2-(-1)=3).
- Q49: third integrand printed without x (cos(pi(-[x/2]))); should be cos(pi(x-[x/2])).
- Q50: several slips (missing "+" in first line, garbled line, "=1" for b, b integral upper limit t, "f(x)=18x(-4)/13", "f(10)"); correct f(x)=(18x-4)/13, f(6)=8.

## WRITTEN
- None (every question had a usable PDF solution).

## Answer-key problems
- None; all ten keys match computation (Q41 D=6, Q42 B, Q43 B, Q44 A, Q45 C, Q46 B, Q47 C, Q48 C, Q49 D, Q50 D), each verified numerically.
- Q43 (question flaw, not a key problem): the stated identity cannot hold at x->0+ (LHS->0, RHS->1) for a continuous f; it holds only up to the constant. Differentiating (as intended) gives answer (B). Not mentioned on slides.

## NO ALTERNATE
- Q46: integrand is an exact derivative; the only variation is the limit step (L'Hopital vs derivative definition), a re-framing, not a new method.
- Q48: both parts (non-differentiability count and the integral) follow directly from the piecewise graph; no distinct method.
- Q50: any method (moments, differentiating, degenerate kernel) is the same linear system as the PDF.

## Alternates that are mild re-framings
- Q41 (odd part via tanh): same symmetry as king property, seen as odd+constant decomposition.
- Q47 (subtract mean n/2, anti-periodic h): same period/integral facts, different bookkeeping.
- Q49 (anti-periodic with anti-period 2): same blocks, shorter bookkeeping.
- Q45 (layer-cake level-set lengths), Q44 (layer-cake 7^{-m}=1-6 sum 7^{-k}), Q42 (F(x^2) composition), Q43 (substitute s=cos x first): genuinely different viewpoints/techniques.

## Assumptions
- Marks 4 each; concepts chosen by me. Levels: Q41=1; Q42,43,45,46,47,49,50=2; Q44,Q48=3.

## LaTeX that pandoc might not convert
- Q48 question stem uses \begin{cases} with \max_{t\le x}; supported per schema but worth watching.
- \operatorname{cosec} (Q46 solution) and \mathbf 1\{...\} (Q44, Q45 alternates) may fail; fallbacks: \text{cosec} / plain "1".
- \tanh (Q41 alternate) is a standard command, expected fine.
