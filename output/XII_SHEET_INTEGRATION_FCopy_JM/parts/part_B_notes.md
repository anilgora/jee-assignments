# Part B notes (Q11-Q20, PDF pages 8-17)

## CORRECTED
- Q12: PDF antiderivative `x + ln(x+2)` is wrong (should be `x + 2 ln(x+2)` since 4/(2x+4) = 2/(x+2)); its next line `1 + 2 ln(3/2)` and answer (B) are right.
- Q13: PDF step (2) reprints the reflected integrand with `e^{x cos x}`; after `x -> -x` it must be `e^{-x cos x}` (that sign change is what gives 1/(1+e^u)+1/(1+e^-u)=1). Rest and answer (D) fine.

## WRITTEN
- None (every question had a usable PDF solution). Q11, Q14, Q15, Q16, Q17, Q18, Q19, Q20 are `pdf`; the terse ones (Q11, Q14, Q18, Q20) were expanded into finer one-step bullets and Q14 gained an explicit "roots are distinct" bullet (kept as `pdf`).

## Answer-key problems
- None. All ten keys verified numerically (Q11 0, Q12 1+2ln(3/2)=1.81093, Q13 pi/(2 sqrt2)=1.11072, Q14 7 (polynomial example has exactly 7), Q15 1, Q16 16, Q17 5, Q18 A, Q19 15, Q20 7).

## NO ALTERNATE
- None omitted; every question has one alternate.

## Alternates that are re-framings rather than wholly new ideas
- Q15 alternate: complete-the-square for the domain is a genuinely shorter route, but the integral part (point symmetry about x=9) is the king property in centred coordinates.
- Q18 alternate: mirror substitution (factor out x+2, w=(x-1)/(x+2)) of the same ratio-substitution idea.
- Q16 alternate (solve for F explicitly first) reorders the same two facts (Leibniz, FTC with F(3)=0) but gives a closed form for F; kept as it is a different line of attack.
- Q14 alternate (Rolle on g^2) uses Rolle again, but on a different function, and counts the product directly.

## Assumptions / judgement
- Marks = 4 for all. Levels: Q11 1, Q12 2, Q13 2, Q14 2, Q15 2, Q16 3, Q17 3, Q18 2, Q19 2, Q20 1 (mean 2.0). Medium confidence on Q13-Q17.
- Q14: "at least seven" is not the best possible bound if one counts f(a)=0 at the (open, undefined) endpoint; intended answer (A) kept.
- Q10 begins on PDF page 8 and Q12/Q21 straddle page breaks; only Q11-Q20 were produced. Q20's Hindi/English text is identical; options of Q18 transcribed from the image ((C) and (D) have exponent 5/4).

## LaTeX
- All `$...$` formulas were round-tripped through pandoc (markdown -> docx) without error. Uses `\sinh^{-1}`, `\tan^{-1}`, `\sqrt[4]{...}`, `\Big[ ... \Big]_0^1`, `\Big|`, `\ldots`-free; `\sqrt[4]` and `\Big` are the only slightly unusual commands, if the deck builder mishandles them replace with `\left[ \right]` and `(\cdot)^{1/4}`.
