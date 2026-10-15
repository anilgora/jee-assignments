# Part A notes (Q1-Q10)

Range note: Q10's working runs onto PDF p9 (read there); Q11 starts on p9, not p8, and was left untouched.

## CORRECTED
- Q5: PDF keeps limits -pi/4..pi/4 for the cos f integral (must be -pi/2..pi/2), writes log(n+sqrt(x^2+1)) / log_e(4+sqrt(x^2+1)) for log(x+sqrt(x^2+1)), and never shows f is odd. Answer B unchanged.
- Q9: PDF has int_1^1 (should be int_1^2), "n<=x n+1" missing "<", piecewise label "x(x-1)/2" should be n(n-1)/2 at x=n; one-sided derivatives at integers not shown. Answer C unchanged (at x=0 only a right derivative exists, f'(0+)=0; key treats it as differentiable).
- Q10: PDF writes f'(2-)=2; correct value is 5 (its own line above says f'=5 for x<2). Answer D unchanged.

## WRITTEN
- none (all ten had usable PDF working).

## PDF kept as is (verified)
- Q1, Q2, Q3, Q4, Q6, Q7, Q8. Q1: the PDF's stacked fraction under -9 reads as (-15)(-14)/7 = 30 (value is correct); a couple of intermediate lines were split into separate bullets for clarity. Q2: added the justification of [a]=10 (comparing coefficient of e) and the check e^{{a}}=2 in [1,e).

## Answer-key problems
- None. All ten keys (9, B, A, C, B, C, A, C, C, D) verified numerically (mpmath / numpy).

## NO ALTERNATE
- Q5: the only workable idea is parity of f (x -> -x averaging is the same idea in other words).
- Q8: every route (king property, centring the interval via y = 2x - pi/4 with h(y)+h(-y)=1) is the same reflection idea; the direct substitution t=tan 2x gives a messy cube-root integral.

## Alternates that are partly re-framings
- Q1 alternate (closed form A_k = (-1)^k C(20,k)/20!, binomial ratio): same residues, but a general closed form rather than direct products; closer to a re-framing.
- Q2 alternate (test the four options with G(a)=[a](e-1)+e^{{a}}-1): a special-value/option check, not a derivation.
- Q9 alternate (FTC + boundedness instead of explicit f): different argument but same conclusion route.

## Skipped / assumed
- Marks = 4 for all. Levels follow rubric F1-F6 (Main sheet; max level given is 3, Q3).
- Concepts assigned by me (no blueprint). Q9 and Q10 each have two concepts from different chapters (definite integral; continuity and differentiability).
- Q1 is partial fractions (algebra) though it sits in the integration sheet; chapter set to "Partial Fractions (Algebra)" in ratings.

## LaTeX that pandoc may not convert
- Cases environment in Q10 question stem (\begin{cases}); supported per schema. Nested fractions with \left\{ \right\} (Q9 not used; Q7 uses \left\{\frac{x}{\pi}\right\}) and \lceil are not used. Otherwise standard commands only; \mathrm{Re}, \mathrm{LCM}, \sinh^{-1} are used (Q5 res, Q7 alt, Q7 sol) and might be kept as text.
