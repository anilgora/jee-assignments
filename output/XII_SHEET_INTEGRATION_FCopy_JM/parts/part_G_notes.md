# Part G notes (Q61-Q70)

## CORRECTED / WRITTEN
- Q66 CORRECTED (substantive): PDF turns bounds on f' over (pi/4,pi/3) into 5x<f(x)<4sqrt2 x; that needs f' on (0,x). Lower bound true (concavity), upper bound false (f(pi/4)/(pi/4)=5.93>5.66). Also print slip f'(x)=8 sin x-2cos2x (should be 8cos x-2cos2x).
- Q68 CORRECTED (print slips only): lower limit "1/2" should be -1/2, missing "+" between pieces, intermediate values 9/8 and 11/24 not shown. Answer 19/12 unchanged.
- Q69 CORRECTED (incomplete + sign slip): PDF stops at "Put n = 5"; final steps (n=5 relation, I_5'=(x^2+5)^-5, match to A) added; misprinted sign in the by-parts line fixed.
- No question is fully WRITTEN.
- Q61, Q62, Q63, Q64, Q65, Q67, Q70 marked `pdf`. Q62/Q67 PDF is terse (evaluation lines/slopes not shown); I expanded intermediate arithmetic without changing method. Q70: PDF drops a factor 2 (dt=1/2 sec^2) and writes the variable as x in the last line; both are harmless slips, silently fixed.

## ANSWER-KEY PROBLEMS
- Q66: key is (C) 5pi/12<I<sqrt2*pi/3, but true I=1.53624 > sqrt2*pi/3=1.48096, so (C) is false as printed; (A) fails too (I<pi/2=1.5708), (B),(D) fail. No printed option is fully correct. `answer` field keeps "(C) ... as keyed" with the caveat, since a student must choose a letter. Rigorous bounds: 7sqrt3/8<I<(4sqrt2-1)/3, i.e. 1.5155<I<1.5523.
- All other answers match the key and were verified numerically (mpmath): Q61=2, Q62=52/e, Q63 (C), Q64=20(pi+2), Q65=-2, Q67 (D) (S1 sum is 4), Q68=19/12, Q69 (A), Q70=atan2-pi/4.

## NO ALTERNATE
- Q70: every route (R-form + standard formula, half-angle) reduces to the same tan(x/2) substitution; no genuinely different elegant method.

## Alternates that are re-framings / partly overlapping
- Q64 alternate (expand to 1+|sin2x|, count humps) is close to the PDF (both use period pi/2); different only in avoiding dropping the moduli.
- Q61 alternate (monotone squeeze) is different in technique but is mainly a rigour argument.
- Q66 alternate (series) overlaps conclusions with the corrected primary but is a different method.

## Assumptions / guesses
- Marks 4 for all; type SCQ; levels: Q61 1, Q62 2, Q63 2, Q64 1, Q65 2, Q66 3, Q67 2, Q68 2, Q69 2, Q70 1 (Q69 could arguably be 3).
- Q67 (statement pair, single correct) rated as SCQ (no multi-correct floor).
- Q66 answer field is not a bare letter.
- Question stems were taken from the English text; the stem of Q67 uses "\n" before (S1) and (S2).

## LaTeX that pandoc may not convert
- `\operatorname{sgn}` in Q67 alternate (use `\mathrm{sgn}` if it fails).
- `\left\{ ... \right\}` with long integral sum in Q62 solution (length only).
- Long answer string with prose + $...$ in Q66 `answer`.
