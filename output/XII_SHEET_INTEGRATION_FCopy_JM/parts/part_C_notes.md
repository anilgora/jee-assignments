# Part C notes (Q21-Q30, PDF pp. 17-26 top)

## CORRECTED / WRITTEN
- Q21 CORRECTED: PDF's step (t+1)/(t^2-t+1) = 1/2 * 2t/(...) + 1/(...) is wrong (should be 1/2 (2t-1) + 3/2); printed arctan argument has (t-1/sqrt2) instead of (t-1/2); factor 1/3 dropped between lines. Answer 3 unchanged.
- Q22-Q30: all PDF working verified correct (solution_source = pdf). Some PDF lines are terse (Q25 omits the final evaluation, Q27 omits the (x-22)^2 remark, Q28 omits sub-steps); these were expanded in the same order without changing the method.
- WRITTEN: none.

## Answer-key problems
- None. All ten keys (Q21 3, Q22 C, Q23 D, Q24 D, Q25 A, Q26 D, Q27 D, Q28 A, Q29 C, Q30 C) match numerical computation (mpmath).

## NO ALTERNATE
- Q22: only method is the Riemann sum; the u=2x substitution is a re-wording of it.
- Q26: only the Riemann-sum-of-log method; other ways (by parts vs substitution for the final integral) are the same idea.

## Alternates that are re-framings / mild
- Q21: differentiate the assumed antiderivative and match coefficients (equivalent to undetermined coefficients, but avoids integration).
- Q23: single u=1-x^2 substitution after simplifying to 4|x|/(1-x^2); same simplification as PDF, different integration route.
- Q24: uses 5a+6b=0 to need only alpha; same unit-interval decomposition.
- Q25: even-odd decomposition, a re-framing of the king property.
- Q27: point-symmetry (area) viewpoint, a re-framing of the king property.
- Q29: reflection x -> 2-x to merge pieces (new but mild).
- Genuinely different: Q28 (inversion x -> 1/x, integral over (0,inf)), Q30 (mean value theorem for integrals, no L'Hopital).

## Assumptions / other
- Marks = 4 for all (none printed). Levels: Q22, Q25, Q27, Q30 = 1; Q21, Q23, Q24, Q26, Q28, Q29 = 2.
- Q21 is a numerical question (no options); Q22-Q30 are SCQ. Q30 solution continues onto p. 26 (read there).
- Q23: Hindi/English text layer garbled; question read from the image.
- Q27 solution is only 4 bullets because the PDF's working is that short (not padded).
- LaTeX that pandoc may struggle with: the \Big|_0^1 evaluation bars in Q28; \ldots in a Q29 useful-result; \text{...} in a Q25 idea string ("(odd function)"). Replace if the build script warns.
