# Quadratic Equation: revision kit report

- Items in the Quick Review: 75
- Batch XII: 55 graded questions, High threshold 5 -> High 8, Medium 25, Low 42
  - High items (numbers): [2, 3, 4, 8, 19, 34, 59, 72]
- Batch XIII: 45 graded questions, High threshold 4 -> High 7, Medium 25, Low 43
  - High items (numbers): [3, 4, 8, 19, 34, 35, 72]

## Added items
- 6: When the roots are required to be integers or natural numbers, how do you use the sum and product of roots?  [source: JM Q18]
- 10: How do you find $\alpha^n+\beta^n$ when the roots are complex conjugates (use of polar form)?  [source: JM Q12]
- 31: How do you solve equations and inequalities containing the modulus of a quadratic expression?  [source: JM Q10, Q13]
- 32: How do you solve a question in which the solution set of one inequality must be a subset of the solution set of another?  [source: J-II Q22; DPP-6 Q9]
- 57: What is the condition for $ax^2+2hxy+by^2$ to be positive for all $(x,y)\neq(0,0)$, and how is it used?  [source: JA Q7]
- 65: How do you find the number of real solutions of an equation like $x^4+px^2+q=0$ (a quadratic in $x^2$)?  [source: JM Q7; theory sheet]
- 66: What are the conditions for a quadratic (with $a>0$) to have at least one positive root, or to be positive for all $x>0$?  [source: theory sheet]
- 72: How do you solve an equation that reduces to a quadratic by a substitution such as $t=x+\frac1x,\ t=x^2,\ t=e^x,\ t=a^x$, and how do you restrict the range of $t$?  [source: JM Q1, Q4, Q17; theory sheet]
- 73: How do you solve an equation that is homogeneous in two expressions $u$ and $v$, such as $(x^2+2)^2+8x^2=6x(x^2+2)$?  [source: JM(XII) Q6; DPP-4 Q2]
- 74: How do you solve an equation that is a product of four linear factors, such as $(x+9)(x-3)(x-7)(x+5)=385$?  [source: J-II Q30]
- 75: How do you find the roots of a composite equation $p(p(x))=0$?  [source: JA Q2]

## Rephrased items
- 16 (original 14): What do you do when the coefficients of a quadratic equation are in cyclic form, such as $a(b-c)x^2+b(c-a)x+c(a-b)=0$?
- 18 (original 16): How do you simplify a long polynomial expression in a root $\alpha$ of a given quadratic equation?
- 20 (original 18): How do you find the value of a polynomial at a root of a quadratic equation by long division?
- 25 (original 23): What is the condition when exactly one root is infinite, what does it mean for a straight line, and how does it generalise to an equation of degree $n$?
- 26 (original 24): What is the condition when both roots are infinite, what does it mean for a straight line, and how does it generalise to an equation of degree $n$?
- 28 (original 26): When $\alpha$ and $\beta$ satisfy the same relation, how do you write the general equation having them as roots, and what happens if three distinct values satisfy it?
- 63 (original 58): When exactly one root lies in an interval $(d,e)$, what is the condition, and how do you handle the endpoint cases?
- 64 (original 59): How do you use the Intermediate Value Theorem ($f(p)f(q)<0$) in questions on quadratic equations?
- 67 (original 60): How do you solve a problem on an infinite continued radical or fraction, such as $x=\sqrt{a+\sqrt{a+\cdots}}$ or $x=a+\dfrac1{a+\frac1{a+\cdots}}$?

## Questions with no matching item
- C-I:7
- C-I:23
- C-II:2
- C-II:7
- C-II:8
- C-II:12
- C-II:17
- C-II:18
- DPP-4:6
- DPP-4:16
- J-A:9

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [13, 14, 15, 16, 17, 18, 19, 20, 21]

## Validation warnings
- none

## Run notes (unattended run, 2026-10-17)
- Input files used: chapters/Quadratic_Equation/Theory.pdf, XII.pdf, XIII.pdf, DPP.pdf, QB.pdf (unchanged).
- The chapter spec (Quick Review items, short notes, formula sheet, mind map, flowcharts, Hindi) and the question map were NOT authored from scratch in this run: they were taken from the skill's finished worked example (examples/quadratic_equation). I re-extracted the question index from your PDFs and compared it with the example's: same exercises, same question counts and numbers, same printed answers (only text-extraction noise differs). Question stems were not re-read one by one against the page images, so the mapping carries the example's judgement.
- Difference found: your QB.pdf has 21 questions (the example had 20). QB Q21 is identical to J-M(XIII) Q7 (Jan 2023, roots of x^7+3x^5-13x^3-15x=0), so I mapped it exactly like J-M(XIII):7 and added 21 to qb_overlap for XIII (now QB 13-21 counted once in XIII). It counts as a new graded question in batch XII (55 graded instead of 54), which makes XII item 4 High.
- detect_overlaps also lists "possible" matches for XII (QB 7-10, 13, 15, 18-20) at similarity 0.60-0.74; not treated as overlaps (not checked by eye - uncertain).
- Source files: the skill scripts kit_grading.py and render_kit.py on branch claude/jee-outputs contained unresolved merge-conflict markers; per the instructions I restored them from origin/main (this version has no DPP-only/Logarithm title support, which the earlier branch conflict side had - re-check before running Logarithm).
- Rendering: verify_outputs.py ALL GOOD; docx/PDF page rasters spot-checked (Quick Review XII HI page 1). docx validate.py not available.
