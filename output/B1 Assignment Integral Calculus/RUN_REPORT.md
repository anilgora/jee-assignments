# RUN REPORT - B1 Assignment Integral Calculus

Blueprint used: NO. **Concepts self-assigned (no blueprint) - please review.** No marks printed; JEE Advanced defaults assumed: single correct 4, one-or-more correct 4, integer/numerical 4, paragraph-based single correct 3, matching 3 (stated in the section dividers). Q57-Q99 are typed "Numerical Type" (4 marks).

## Difficulty
Marks-weighted difficulty index (adjusted levels): **2.35** over 103 questions (398 marks).
Questions per level: L1: 11, L2: 49, L2.5: 2 (Q27, Q43 - multi-concept multi-correct floor), L3: 36, L4: 5. No equivalence-relation adjustments.
Low-confidence ratings: Q14, Q28, Q37, Q49, Q87, Q100, Q103. Ratings produced by 10 sub-agents (one per question range) with the calibrated rubric; consistency across ranges was not re-checked by one person.

## Solutions: source counts
pdf 48, corrected 36, written 19. Corrected: Q6, Q11, Q15, Q17, Q25, Q26, Q28, Q29, Q31, Q32, Q35, Q36, Q37, Q38, Q40, Q44, Q46, Q60, Q61, Q62, Q64, Q65, Q66, Q68, Q71, Q74, Q75, Q86, Q87, Q91, Q93, Q96, Q100, Q101, Q102, Q103. Written: Q8, Q22, Q34, Q42, Q47, Q48, Q49, Q51, Q54, Q55, Q63, Q67, Q72, Q73, Q79, Q84, Q90, Q94, Q99.
Per-question one-line reasons are in the sub-agent notes below (and in each question's correction_note in the content JSON, shown in the speaker notes).

## Answer keys that look wrong / questions reconstructed (headline)
Q32 (A,D -> A), Q35 (A,C,D -> A,B,C), Q37 (self-contradictory key), Q62 (2 -> pi/2), Q68 (key 20 vs 5 as printed; probable typo), Q71 (key 7 vs 5 as printed; probable misprint), Q86 (4 -> 2), Q87 (inconsistent stem), Q100 (no exact option), Q101 (C -> A), Q103 (corrupted duplicate of Q102; PDF key B kept). Q59: 0.66 vs 2/3=0.67. Q63 and Q28 figures missing in the PDF (solutions written/reconstructed from text). Q18 options B and C identical. Reconstructed stems/options: Q6, Q10, Q35, Q37, Q40, Q44, Q46, Q77, Q91. Please review these.

## Alternates / useful results
Alternates given for all 103 questions except Q87 (printed question inconsistent). Some alternates are only weakly different from the main method (flagged by the agents for Q42, Q43, Q50, Q52, Q54, Q56). Useful results given for ALL 103 questions.

## make_ppt.py output
"Equations: 4743 converted to native PowerPoint equations." Initial warning "could not convert" for Q53 answer came from a corrupted escape (\f read as form feed) in the merge; fixed in the JSON and rebuilt - no conversion warnings remain. Notes only: Q100-Q103 "very long question - font reduced to 20 pt" (harmless). Deck: 700 slides. The ratings JSON had the same escape problem in two justifications (also fixed) which had stopped the Excel build; rebuilt OK.

## Skipped / assumed / guessed
No rendering or visual check of the deck (no soffice). Duplicate Q41 (done by two agents) - the Q41-50 agent's version kept. Sections set by consecutive question type.

## Sub-agent notes (verbatim, per question range)

### Q1-10
# Notes, worker A (Q1-Q10)
Corrected / written
- Q6 corrected: PDF final line y = 1/(4x)+3x^2/4 is wrong; solving gives 1/(4x)+3x^3/4 (checked by sympy: limit = 1/2, f(1)=1). Printed option (C) reads 1/(4x)+3x/4 (exponent apparently lost); key C kept, option C reconstructed in JSON as 1/(4x)+3x^3/4. Read literally, no printed option equals the true f.
- Q8 written: PDF gives only the last 3 lines (tangent at Q); derivation of the curve y=e^{a(x-1)} added.
Answer keys: all 10 keys agree with the correct answers (Q6 only after reading option C as above).
Reconstructed / garbled text
- Q10: option (A) prints "e^x + c" but PDF solution ends at e^{e^x}+c (superscript lost); option A reconstructed as e^{e^x}+c. Options B-D left as printed (C probably also lost a superscript).
- Q9: stem prints (ln x)(ln x^x) = x (ln x)^2; used as such.
PDF solutions completed (still source "pdf"): Q2 (last substitution u=x^2 added), Q7 (PDF stops before back-substitution; steps added), Q10 (explicit f(x) step added), Q1 (explicit ST, SN lengths added).
Other issues
- Q4: initial point t(1)=pi/2 is a singular point of dt/dx = tan t (tan undefined there); intended answer (C) from sin t = c e^x is used. All four options pass the initial condition, which the alternate solution points out.
- Q1 PDF's text does not label ST/SN, only their sum; fine.
No alternate omitted: every question has one.
Low-confidence ratings: none Low. Medium: Q3 (3 vs 2), Q5, Q6, Q7 (4 vs 3), Q10.
Assumed: marks 4 for all (single correct default); chapter Differential Equation for Q1-Q8, Indefinite Integration for Q9-Q10.


### Q11-20
# Notes for B (Q11-Q20)
- Q11 corrected: PDF's first line wrote the integrand as x e^{tan x} + x e^{tan x}(1+sec^2 x); the factor must be (1 + x sec^2 x). Rest and key (B) correct.
- Q15 corrected: PDF wrote cos^{-1}(2010x) (typo for cot^{-1}) and stopped at 2I = integral of pi x^2010 dx without evaluating; evaluation added. Key (C) correct.
- Q17 corrected: PDF's "f(x) > f(1) so f(x) > 0" treats f(1)=0, but f(x) -> ln(3/2) as x -> 1+ (f not continuous at 1); replaced by the limit argument. Conclusion and key (A) unchanged.
- No question written from scratch; no wrong answer keys in Q11-Q20 (all keys A/B/C/D verified: B, A, C, D, C, A, A, D, B, D).
- Q18: options (B) and (C) are identical in the PDF (both sqrt(pi^2+2)); reproduced as printed; answer D unaffected.
- Q20: PDF solution text shows the second integral with garbled limits; reconstructed as integral from pi/2 to x (matches the next line f(x)=pi/2 - x).
- Q19: PDF has only the diagram, 1<=x+3y<2 and the area; steps expanded (parallelogram vertices, constant height 1/3), nothing changed.
- Q12 solution: PDF skips the cos x multiplication and substitution; added as explicit steps (assumes cos x > 0 near 0).
- Alternates given for every question (Q11-Q20); none omitted. Q12 alternate is series matching (differentiation check was judged too close to the main route); Q19 alternate is a Jacobian/shear change of variables.
- Low-confidence rating: Q14 (L3, implicit-differentiation link is unusual; could be 2 or 4). Medium for most others; Q15 High.
- Assumptions: marks 4 for all (single correct default per brief); no eq_relation/multi_concept flags. type_label "Single Correct Type" for all ten.
- Answers verified numerically/symbolically (sympy/mpmath): derivative checks for Q11-Q13, parametrisation check for Q14, numeric integrals for Q15-Q18, Q20; Q19 area 1/3 by direct geometry. Results in useful_results (power reduction, Wallis, f(1+)=ln(3/2), integral of [cos t] over a period = -pi) also checked numerically.


### Q21-30
# Notes for C (Q21-Q30)
Marks: JEE Advanced defaults (all 4: SCQ Q21-24, MCQ Q25-30).

## Corrected / written
- Q22 (written): PDF gives only the factorisation (x^2+y^2-4)(y^2-1)=0; area computation written. Region interpretation: the central part |y|<=1 inside the circle (the only region matching an option; caps are 4pi/3 - sqrt3 each).
- Q25 (corrected): PDF line "e^{-x^3}f(x) >= e^{-1}f(1) => >= e^2" should be e (e^{-1}*e^2 = e); next line f >= e^{x^3+1} is right. Added the IVT check that 8 and 10 are attained.
- Q26 (corrected, typo only): PDF back-substitution prints sqrt(a + sec^2 x - b tan^2 x); should be sqrt(a sec^2 x - b tan^2 x). Added why (B),(C) fail.
- Q28 (corrected): figure missing; PDF "-(x-a)(x-b)(x+c) = (x-a)(x)(x+c)" is inconsistent (sign and +c); correct f = -x(x-a)(x-c). Option (A) is printed with int_a^b twice (typo for int_b^c). PDF says "from graph" for sign of int_a^c f; exact value (c-a)^3(a+c)/12 added.
- Q29 (corrected): PDF decimal I = pi^2/2 - 2 ~ 2.89 is wrong; it is 2.9348. Options (B),(C),(D) checks added (PDF only did (A)).
- Pdf-source but with added missing steps (no error): Q23 (substitution x=4/t step missing), Q24 (breakpoint justification), Q27 (area step a=4 and option checks not in PDF), Q30 (PDF checks only D; A,B,C added).

## Answer keys
- All ten keys verified correct (Q21 A, Q22 C, Q23 B, Q24 A, Q25 A,B, Q26 A,D, Q27 A,C, Q28 B,C,D under the reconstructed figure, Q29 A,C, Q30 A,B,C). No wrong keys.

## No alternate solutions
- None omitted; all ten have an alternate.

## Garbled / reconstructed
- Q28: figure absent from PDF (broken image). Reconstructed as falling cubic with zeros a<b=0<c (f(a)=f(b)=f(c)=0); stated in the question text. Note options (B) and (C) are logically equivalent (both say int_a^c f < 0). Rating confidence Low.
- Q30: stray broken image after "x/(1+x^2)" in PDF, ignored.

## Low / medium confidence ratings
- Q28 Low (figure missing). Q22 Medium (3 vs 2: factorisation plus region ambiguity). Q23 Medium (L1 by analogy with the king property anchor). Q27 level 2 raised to 2.5 by the multi-concept MCQ floor (content "level" = adjusted).
- Content "level" holds the adjusted level (Q27 = 2.5); ratings file holds integer level + flags.
- Q26 chapter label "Definite Integration" used in ratings although it is indefinite integration (no matching anchor chapter).


### Q31-41
# Notes for D (Q31-Q40; Q41 also done since page 15 holds it)
Range delivered: Q31-Q41 (11 questions).
## Corrected / written
- Q31 corrected: PDF has no derivation of a+b=5 and stops at f'(x)=0; area computation and sign analysis added. Answer A,B,C,D correct.
- Q32 corrected: working fine; KEY WRONG as printed (A,D): I1=I2=b-a, (D) I1+I2=10 holds only if b-a=5 (no data in the question). Answer given: (A).
- Q34 written: PDF Sol is blank. Answer A,B,C,D verified (sympy: y=1+C sqrt(x^2-1)).
- Q35 corrected: stem prints sqrt(4-f^2) but should be sqrt(4+f^2); KEY WRONG (A,C,D): (B) g=f/sqrt(1+f^2)=sin x is true (cos x>0), (D) g^2 f'=f'-g^2 is false (true if RHS were f'-1). Answer given: (A,B,C).
- Q36 corrected: PDF prints g=1/(x-3)^3 for x<3 too (negative); should be c'/(3-x)^3, c'>0. Answer C,D unchanged.
- Q37 corrected: stem prints tan^-1 e^{-x} in the denominator; the PDF working uses tan^-1 e^{x}; stem reconstructed with e^x. KEY WRONG ("A,B" is self-contradictory); answer given (A,C). As printed (e^{-x}) the value is (pi/2)ln(1+2tan^-1(e^a)/pi) -> only (B). Also integrand exists only for x<=0 (a<=0).
- Q38 corrected: PDF incomplete (never evaluates D term, no conclusion). Answer A,B,C correct.
- Q40 corrected: option (D) printed "I1>1, I2>ln2" is false (I1=0.590); reconstructed as "I1<1, I2>ln2" to match PDF working and key (B,D). If read literally the answer would be (B) only.
## pdf (unchanged, verified): Q33, Q39, Q41 (page 16 of the PDF repeats the closing lines of Q41 twice; math correct).
## Wrong keys: Q32, Q35, Q37 (and Q40 depends on a typo in D).
## Alternates: given for all Q31-Q41. None omitted. (Q37 alternate is a scaling argument, a modest variant of the substitution; Q40 alternate is an exact I1 plus sharper bound for I2.)
## Low confidence ratings: Q37 (garbled stem). Medium: Q31, Q32, Q34, Q35, Q36, Q40, Q41.
## Assumptions: marks all 4 (MCQ). Chapter names: Definite Integration, Differential Equation, Indefinite Integration. Q38/Q36/Q34/Q35/Q37/Q31 flagged multi_concept; the 2.5 floor therefore lifts Q36 (2->2.5) and Q38 (1->2.5).


### Q41-50
# Notes, worker E (Q41-Q50)
Corrected: Q44, Q46 (3 questions counting reconstructions: none other). Written: Q42, Q47, Q48, Q49.
- Q44 corrected: printed option (B) `y^2/(x^2+y^2) c = -tan(x^2+y^2)` does not satisfy the ODE (numerically checked). Key (A,B) only works if (B) is `y^2/(x^2+c y^2) = -tan(...)` (inverted form of A); option reconstructed. PDF working stops at (A).
- Q46 corrected: printed stem lacks factor y before dx. Printed ODE is not exact and B does not solve it; PDF working/key B fit `y(2+2x^2 sqrt y)dx + x(x^2 sqrt y+2)dy=0`. Stem reconstructed. PDF also prints 2x^3 y^(3/2) dx (should be 2x^2 y^(3/2)) and ends "=0" instead of "=C".
- Q42 written (PDF Sol is "-"). Q47, Q48, Q49 written (PDF Sol is "-").
- Q45: PDF working is a single line (area = 4x(1x1)); expanded to 6 bullets, marked "pdf". Q50: PDF skips the f^2 step; one bridging bullet added, marked "pdf". Q41: PDF working is duplicated/garbled on the page; reproduced once, boundary-term justification added, marked "pdf".
Answer keys: all agree with computation (Q41 A,B,D; Q42 A,C; Q43 A,C; Q44 A + B(only as reconstructed); Q45 A,B; Q46 B (reconstructed stem); Q47 A; Q48 C; Q49 C; Q50 A). Q44 as literally printed would have answer A only.
No alternate omitted. Weak alternates: Q42 (verification-style: derive the arctan form from the options, same u-substitution in disguise), Q50 (mild variant: product/ratio plus cube recognition), Q43 (superposition, fairly close to the linear-DE route).
Reconstructed: Q44 option B, Q46 stem. Q46 typed MCQ because the stem says "is/are" (key is single).
Low-confidence rating: Q49 (L3 vs 2). Medium on most. Marks: JEE Advanced defaults assumed (MCQ 4, Para SCQ 3).
Q43: level 2 + multi_concept (DE + maxima) -> adjusted 2.5 (content level field = 2.5).
Q47-49 share the passage; Q50 passage printed on p19 itself. Q41 is on p15, Q42-43 p16, Q44 p17.
Python with sympy: use /usr/bin/python3 (default python3 lacks it).


### Q51-60
# Notes F (Q51-Q60)
Corrected / written
- Q51 written (PDF Sol "-"). Q54 written (PDF only gives g = x-1; option verdicts written by me). Q55 written (PDF Sol "-"; question text from the paragraph on p20-21).
- Q60 corrected: PDF working has the second integrand term as 2/(x^2+1); the question (and the next PDF line) need 2/(x^4+1). Answer 3 correct.
Wrong / doubtful answer keys
- Q59: key 0.66 but S/5 = 2/3 = 0.666..., which rounds to 0.67 (0.66 is a truncation). Kept answer 2/3 ~ 0.67 and said so. Rest of PDF working correct.
- All other keys (Q51 C, Q52 D, Q53 B, Q54 D, Q55 A, Q56 B, Q57 2.33, Q58 1, Q60 3) verified correct by sympy/mpmath.
Minor PDF typos left as "pdf" (reproduced in correct form): Q56 PDF writes f'(x)/f(x-1) for f'(x)/(f(x)-1); Q53 PDF working is duplicated and omits t = 1 - 1/x definition (supplied). Q56 PDF extra Rolle/(D) lines belong to a different option set; dropped.
Alternates (all verified), weak ones
- Q54 alternate is weak (graph reading of the same four checks; only g is found differently via g' = 1). Q56 alternate (h = 1 - f, range by extrema of f) and Q52 (substitution phi = u y) are close to the primary, only reformulated. Q53 alternate = direct antiderivative sqrt(x^2+(x-1)^2)/x (no substitution). No question was left without an alternate.
Garbled / reconstructed
- Q51 option (B) printed x^4/4 + x^2/3 + x^2 + 2x + c (kept as printed). Q55: paragraph tangent geometry read as P=(x,y), x,y>0, B = x-intercept of tangent, C = foot on x-axis; "ratio of ordinate to abscissae" = y/x. Q59: "line f(x)=2/e" interpreted (as the PDF figure/working) as the vertical line x = e-1.
Ratings
- Para SCQ marks 3, Numerical 4 (defaults). All levels Medium confidence except Q58 (High). Q55 level 4 is the highest/least certain (could be 3). Q52/Q54 at 2 could be 3 given paragraph-format average. No eq_relation or multi_concept flags (no MCQ).
Other
- Paragraph for Q52-54 printed on p19 before Q52; Q55's paragraph is at the bottom of p20 / top of p21; Q51 shares the paragraph with Q50 (not in my range).


### Q61-70
# G notes (Q61-Q70, pages 25-28)
All marks = 4 (no marks printed; answers are not 0-9 so type = Numerical for all).
## Corrected
- Q61: PDF "f(1)=f(0) or f(1)=f(0)" typo; second must be f(1)=-f(0). Answer 491 correct.
- Q62: WRONG KEY. PDF working gives area pi/2 (correct) but printed answer is 2 (from stray lines "3*lambda=pi/2, c^2+m^2=2" of another question). Answer kept: pi/2.
- Q64: PDF line 2 has stray factor x in integrand x(x+x^3/2+...); should be x(1+x^2/2+...). Answer 30 correct.
- Q65: PDF simplifies bracket to (3n)!/((2n)!(n)!) (wrong) and has extra n! blocks; correct is (3n)!n!/((2n)!)^2 = prod (3n-r)/(2n-r). Answer 43 correct.
- Q66: PDF garbled second integration (limits t=0..1, "295/370 kt"); correct ln(5/80) = -kt. Answer 40 correct.
- Q68: WRONG KEY. As printed (upper limit x^2), 100(f^-1)'(0)=5 (verified numerically, branch x>0; branch x<0 gives -5). PDF working ends at 1/20 ("Ans 1/20"); printed key 20 matches the variant f(x)=int_4^x sqrt(9+t^2)dt (100/5=20). Answer kept: 5. Possible question-text typo (x^2 vs x): worth user's decision.
## Written
- Q63: PDF has only the area (8/3) and a missing image; k=4 and rectangle area 32 written. Figure missing in PDF; described in words.
- Q67: PDF has no solution (key 11.55 correct, verified; unit is percent per year).
## PDF correct as is
- Q69 (8/7, 15), Q70 (A_n=2n/3+n(n-1)/2, 24); Q70's PDF has a garbled middle line but sums are right.
## No alternate omitted: every question has one (Q65 has two).
## Ratings
- All Medium confidence except Q66 High. Q68/Q69/Q70 could be 1-2 (borderline); Q63/Q64/Q65 could be 2-4.
- Assumed: Q68 domain x>0; Q62 r=7 only value with infinitely many solutions.


### Q71-80
# Notes H (Q71-Q80)
- All 10 typed "Numerical" (fill-in-blank; answers single digit except Q72), 4 marks each (no marks printed).
- Corrected (3): Q71 (WRONG KEY: PDF ignored the 2tx term of AC, got 3/4 -> key 7; for lines as printed x_A=3/2, p+q=5; key 7 would be right only if AC were y=0 - possible misprint, user should check), Q74 (PDF first line misses the factor 4 from sin4x; answer A=2 right), Q75 (PDF's final expansion line has sign/term slips and a missing image; setup and k^2-4k+2=0 right; answer 2 right).
- Written (3): Q72, Q73, Q79 (PDF has "Sol. -").
- PDF correct (4): Q76, Q77, Q78, Q80.
- Wrong answer keys: Q71 only (key 7, correct 5 as printed).
- Reconstructed question: Q77 - printed integrand reads h(x)f(x) but the PDF working and "twice continuously differentiable" show it is h(x)f''(x) (primes lost). Triangle figure described in words (vertices (A,0),(0,C),(B,0), A<0<B).
- Q79: improper at e=1 (integrable); treated as convergent.
- Alternates given for all 10. Q75 alt (area of the lower part) and Q72 alt (antiderivative at sign-change points) are lighter variants of the primary rather than wholly different ideas.
- Low-confidence ratings: none Low; all Medium except Q76 High. Levels: Q71 2, Q72 2, Q73 3, Q74 3, Q75 3, Q76 2, Q77 2, Q78 2, Q79 2, Q80 3.
- All answers/steps/alternates/results numerically verified with mpmath/sympy (/usr/bin/python3).


### Q81-91
# Notes, range Q81-Q91 (NAME = I)
Corrected / written:
- Q84: written (PDF solution stops after sin x = sin(y +- pi/3) and a figure; boundary lines, region and area pi^2/6 completed and verified, k=6 correct).
- Q86: corrected + WRONG KEY. PDF gets 2I=4 but answers 4; correct I=2 (numerical integration 2.0000). Answer in content = 2.
- Q87: corrected + question inconsistent. PDF integrating factor e^{e^{-x}} is wrong (correct e^{-e^{-x}}); step t e^{e^{-x}}=x unsupported. Correct solution cos y+sin y = 1-e^{e^{-x}-1} never reaches y=0, so no point (t,0) exists. Key 1 retained as keyed (answer "1"), flagged; likely misprinted question. Low confidence.
- Q90: written (PDF gives only the piecewise f and the area sum; reasoning for the pieces added). Answer 2 verified.
- Q91: marked corrected only because the question text was reconstructed: printed coefficient looks like sqrt(2/pi) but PDF working/key use sqrt(2)/pi (with the literal form the value is sqrt(pi)/2, irrational). Working and answer 3 verified.
Other wrong keys: only Q86 (and Q87 unsupported).
No alternate: Q87 (question inconsistent, no meaningful alternate). All others have an alternate.
Garbled/reconstructed: Q85 figure described from the page (L1: 2y-x=4 tangent at C, L2: 2y-x=1 through A,B; shaded between L1 and curve); Q83 underbrace written as "composed 2017 times".
Marks: all numerical, 4 marks (JEE Advanced default; none printed).
Low-confidence ratings: Q87 (Low). Medium: Q81, Q82, Q84, Q85, Q90, Q91.
Q82: PDF working is correct (by-parts with sin(n+1)x as first function); kept as pdf.


### Q92-103
# Notes for J (Q92-Q103, pages 38-46)

Marks: no marks printed; JEE Advanced defaults used (numerical/subjective 4, matching 3). Q94-Q99 are open "find/prove/solve" items, typed Numerical (4).

## Corrected / written solutions (solution_source)
- Q92 pdf (correct, 0).
- Q93 corrected: PDF wrote dy/y = (2n/(x ln x) + 1/x)dx; dividing by x y ln x gives "+ 1", so f = e^x (ln x)^{2n}, not x e^{e-1}(ln x)^{2n}. Answer 0 unchanged. (PDF is right for (2ny + y ln x)dx - x ln x dy = 0; probable misprint.) Printed "log_e x dy = 0" read as "log_e x != 0".
- Q94 written: PDF has no answer/solution. k = 12, area of triangle = 72 (verified symbolically).
- Q95 pdf (correct; first integral checked by sympy).
- Q96 corrected: PDF line "x=1: {f(1)}^n = n/(k(n+1)) = 0" should be 1; PDF has no key and stops at {f(10)}^n = 10; k/4 = 5/2 added. The question re-uses the letter k; read as {f(10)}^n = k, proportionality constant renamed lambda.
- Q97 pdf (correct; text layer had HTML garble "\<br >").
- Q98 pdf (correct).
- Q99 written: PDF has no solution; answer 0 (a = -1/6, b = 9/2).
- Q100 corrected (see wrong keys).
- Q101 corrected (see wrong keys).
- Q102 corrected: part (d) printed exponent is nx but PDF solves exponent 1/ln x; both give ln L = 0, both shown. Key A correct.
- Q103 corrected: see below.

## Wrong / unreliable answer keys
- Q100: PDF key (A) matches none of the four items (PDF working gives (a) 1/2, (b) -1, (c) 1, (d) 1/2). Both (a) and (d) map to (r), so no option is exactly right as printed. Option (C) agrees on (b),(c),(d) and would be right if (a) were 0 (e.g. denominator sin x; verified numerically, limit 0). Answer recorded as (C), Low confidence. PDF's (d) working (Leibniz rule on limits) is invalid and its expression tends to 0; replaced by a squeeze; limit 1/2 verified numerically. Also "I = 5 - ln 2" slip in (b) (should be 5 - 6 ln 2).
- Q101: PDF key (C) is wrong; correct is (A): a-s, b-p, c-q, d-r (PDF working gives c=4, d=12, and (a)=1 computed here). Printed f in (b) is inconsistent: f(x)=x^5+e^2+e^{x^3} has f(0)=e^2+1, f'(0)=0 and g'(2)=0.0505; the PDF uses f(0)=2, f'(0)=1/2, so f is misprinted; value (p) kept. Part (a) had no working in the PDF.
- Q103: printed Column-I is a copy of Q102 (with (d) as x->0^-, exponent 1/ln x), values 2, 4, 2, 0, matching no option; PDF key is B and its working starts with other integrals (original items lost; its second half repeats Q102). Answer (B) kept as PDF key / closest (matches (c)-p and (d)-r), Low confidence. x->0^- read as 0^+.

## Garbled / reconstructed question text
- Q93 ("log_e x dy = 0" -> "log_e x != 0"), Q94 (trailing stray "x"; wording tidied, "intersects on x-axis" read as intersect at a point on the x-axis), Q96 (stem tidied, k reused), Q101 (Column-I/II heading artefact "[I02/5/171.]" dropped; option (D) "p - r" read as "a - r"; (b) function as printed kept in the question).

## No alternate
- None omitted. Q101(b) has no different method (inverse-function rule only), stated in the alternate's bullet.

## Low / medium confidence ratings
- Q100 (Low: defective key; level 3 vs 2 debatable), Q103 (Low: corrupted question), Q92, Q93, Q94, Q96, Q97, Q98 (Medium).
- Q98 rated 1 (single Leibniz move) and Q97 rated 2; both open to +1.

