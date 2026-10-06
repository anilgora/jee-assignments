# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_07

Paper: 20 questions (printed Q121-Q140), deck numbers 1-20, all Differential Equations. Q1-5 single-correct, Q6-20 numerical value.

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.30** (184 / 80 marks; all questions 4 marks). No equivalence-relation adjustment or MCQ floor applied.
- Questions per level: Level 1: 1 (Q18) | Level 2: 12 (Q1, 2, 3, 5, 6, 8, 10, 11, 13, 14, 16, 20) | Level 3: 7 (Q4, 7, 9, 12, 15, 17, 19) | Levels 0, 4, 5: none.
- Lowest-confidence ratings: Medium for Q2, 4, 5, 7, 9, 12, 17, 19.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): +4 for every question (single-correct and numerical), as the run instructions say (JEE Advanced default 4 for single-correct/integer). Note: the earlier paper 06 run used 3 for single-correct; stated on the section dividers.

## Solutions whose source is corrected or written
- Q1 (printed 121) - corrected: the PDF's final line `y(2) = 2(1+sin2) - 2sin2` does not follow from its antiderivative (the two brackets at x=2 add to 0, so y(2) = C = 2). Answer (C) unchanged.
- Q4 (printed 124) - corrected: the PDF writes `dt/dx - 1 = 2x t^3 - xt`; the right side should be `... - 1` too, so `dt/dx = 2xt^3 - xt`. Later working is right. Answer (C) unchanged.
- Q5 (printed 125) - corrected: PDF only says "alpha>0 but alpha=-3"; the alpha<0 case was not excluded and was added. Conclusion (Bonus) unchanged.
- Q15 (printed 135) - corrected: the PDF differentiates the numerator wrongly (`2 + f(x) - x^2 f'(t)`, limit written as x->infinity); correct is `2t f(x) - x^2 f'(t)` as t->x, giving `2xf - x^2 f' = 1`. Rest and answer 24 unchanged.
- Q16 (printed 136) - corrected: the PDF's final evaluation `30 - 12` does not match its brackets (40/3 and -14/3); correct value 18 (answer unchanged).
- All other questions are `pdf` (working verified). Small notation typos fixed silently: Q3/Q14 minor wording, Q11 (PDF prints y(x) for y'), Q14 (PDF writes tan^-1(x+y+z) for x+y+2), Q17 (figure labels (7,11) instead of (7,1)), Q10 (PDF writes "dy/dx" instead of dy/(y+1) in the integral line, and skips f(0) and f(2) steps - added).

## Answer key
- Q5 (printed 125): key is "Bonus"; I agree - alpha cannot satisfy the data (see above).
- All other printed answers were checked (analytically; numerical RK4 integration of the ODEs for Q1, 2, 3, 4, 6, 8, 13; Q12 verified by substituting y = (sin^-1(x/2))^2 - 2 into the ODE) and are correct. No key errors.

## Alternates
Alternate solutions given for **all 20 questions** (1-20). Each was checked analytically (and numerically where listed above). Closer relatives of the main method (stated honestly): Q6 (x = sin(theta) just makes the I.F. visible as d(y cos theta)), Q10 (constancy of (f+1)/(x+2)^3 is the integrating-factor result in ratio form), Q20 (equilibrium shift is the linear solution in different notation), Q7 (explicit solution of f''=f vs first integral is a different method).

### Questions with NO alternate
None.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide.

## make_ppt.py warnings
None. The build printed no warnings and no "could not convert" notes; 865 equations converted to native PowerPoint equations; 127 slides. Slides were not rendered or opened in PowerPoint here (no soffice rendering in this environment).

## Skipped / assumed / guessed
- Concepts and levels are self-assigned; levels are judgement against the calibrated anchors (cited per question in the ratings file). Anchors are Advanced questions at L3-4, so this Main-level bank sits at L1-3.
- Marks assumed 4 per question (see above); question type labels "Single Correct Type" and "Numerical Type" taken from the answer format (options vs. blank).
- Q15: the printed limit variable "x->infinity" was read as t->x (as the question statement says).
