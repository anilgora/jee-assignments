# Anchor bank - the user's own ratings of official JEE Advanced maths questions

172 questions: 2021, 2023, 2024, 2025 and 2026, both papers. Every level below is the user's rating, not a model rating. These ratings already include format and topic effects; the section-9 rules in `rubric.md` apply only to new papers. `anchors.csv` also has an `EqRel` column marking equivalence-relation questions (only 2026-P1-Q9 so far).
Reference format: `Year-P<paper>-Q<n>`. Marks are the full marks printed in the paper. The same data, machine-readable, is in `anchors.csv`.

How to use: before fixing a level, find 2-3 anchors with the same chapter or the same *kind* of demand (same trick, same counting style, same format) and rate the new question relative to them. Quote the closest one in the report's `nearest_anchor` field.

## Contents
- Level 0 - Easier than JEE Main (4 questions)
- Level 1 - JEE Main level (17 questions)
- Level 2 - Easier than Advanced (39 questions)
- Level 3 - Average Advanced (47 questions)
- Level 4 - Slightly difficult (55 questions)
- Level 5 - Very difficult (10 questions)

## Level 0 - Easier than JEE Main

| Ref | Type | Marks | Chapter | What the question asks |
|---|---|---|---|---|
| 2024-P2-Q1 | SCQ | 3 | ITF | tan(sin^{-1}(3/5) - 2cos^{-1}(2/sqrt5)) - direct evaluation |
| 2023-P1-Q15 | MTC SCQ | 3 | Statistics | Mean, median, mean deviations of a frequency table |
| 2024-P1-Q16 | MTC SCQ | 3 | Vector 3D | Coplanar lines L1,L2: lambda, normal, distances - direct |
| 2024-P2-Q11 | INT | 4 | Vector 3D | Express vector in basis 2p+q, p-2q, pxq; dot with pxq gives gamma |

## Level 1 - JEE Main level

| Ref | Type | Marks | Chapter | What the question asks |
|---|---|---|---|---|
| 2023-P1-Q13 | INT | 4 | Binomial Theorem | Equate coefficients in two binomial expansions; find 2b |
| 2024-P1-Q15 | MTC SCQ | 3 | Circle | Line y=2x tangent to circle centre (0,beta); r, contact point, diameter end |
| 2025-P1-Q7 | MCQ | 4 | Complex Number | &#124;z-z1&#124;=2&#124;z-z2&#124; Apollonius circle; centre and radius |
| 2021-P2-Q11 | Q Stem | 2 | Definite Integration | 16 S1/pi where S1 = integral of sin^2 x over [pi/8,3pi/8] |
| 2026-P2-Q4 | SCQ | 3 | Definite Integration | Integral 0..2 of 1/(3^x+3) by king property |
| 2023-P1-Q14 | MTC SCQ | 3 | Determinant | System with alpha, beta, gamma: unique/none/infinite/particular solution matching |
| 2024-P2-Q3 | SCQ | 3 | Limit | (sin(sin kx)+cos x+x)^{2/x} = e^6; 1^infinity form gives k |
| 2026-P1-Q3 | SCQ | 3 | Matrices | Which matrix is row-equivalent to I: pick the invertible one |
| 2025-P1-Q15 | MTC SCQ | 4 | Maxima & Minima | Short parts: GIF continuity of cubic/n, local minimum of polynomial, etc. |
| 2024-P2-Q10 | INT | 4 | Monotonicity | Zeros of f: sin x + 2 > 0 so reduce to increasing polynomial; one root |
| 2021-P2-Q6 | MCQ | 4 | Parabola | Tangents from (-2,4) (on directrix) to y^2=8x; standard focal-chord properties |
| 2021-P2-Q17 | INT | 4 | Probability | P(multiple of 3 or 7) in 1..2000 by inclusion-exclusion |
| 2021-P1-Q17 | INT | 4 | Quadratic Equation | Number of real roots of 3x^2-4&#124;x^2-1&#124;+x-1=0 (case split) |
| 2021-P1-Q7 | Q Stem | 2 | Vector 3D | Consistency of 3x3 system gives alpha-2beta+gamma=1; &#124;M&#124; equals 1 |
| 2023-P2-Q4 | SCQ | 3 | Vector 3D | Coplanarity and section-formula checks for four position vectors |
| 2024-P1-Q12 | INT | 4 | Vector 3D | (OPxOQ).OR=0 fixes parameters; point on plane gives l |
| 2024-P2-Q6 | MCQ | 4 | Vector 3D | Line through P parallel to line meets plane at Q; perpendicular to R; centroid, perimeter |

## Level 2 - Easier than Advanced

| Ref | Type | Marks | Chapter | What the question asks |
|---|---|---|---|---|
| 2021-P1-Q2 | SCQ | 3 | Area Under Curve | Area of region bounded by x<=9/4, y<=1, x>=3y, x+y>=2 |
| 2024-P2-Q2 | SCQ | 3 | Area Under Curve | Area of region bounded by y^2<=4x, y^2<=12-2x and a line |
| 2025-P2-Q2 | SCQ | 3 | Area Under Curve | Area of region xy>1 between two lines |
| 2026-P2-Q15 | Q Stem | 2 | Area Under Curve | Intersections of e^{-x} and e^{-x}(sin x+cos x) on [0,10pi] |
| 2026-P1-Q2 | SCQ | 3 | Circle | Points from tangent slopes on parabola, circle, ellipse; right angle gives circumradius |
| 2021-P2-Q3 | MCQ | 4 | Definite Integration | Continuous f with f(0)=1 and integral 0 on [0,pi/3]; IVT/Rolle and limits |
| 2023-P2-Q1 | SCQ | 3 | Definite Integration | Integral equation 3 int f = x f(x) - x^3/3; differentiate, linear DE; f(e) |
| 2024-P2-Q16 | Q Stem | 3 | Definite Integration | 2 int fg - int g with f=sin^2 x, g=sqrt(pi x/2 - x^2); king property |
| 2023-P2-Q9 | INT | 4 | Differential Equation | Linear DE, y(2)=7; maximum of y |
| 2024-P1-Q1 | SCQ | 3 | Differential Equation | Limit definition gives linear DE for f; solve with f(1)=2 |
| 2025-P1-Q13 | Numerical | 4 | Differential Equation | Three separable DEs; limit of product |
| 2025-P2-Q9 | Numerical | 4 | Differential Equation | Homogeneous-type DE x^2y'+xy=x^2+y^2, y(1)=0; evaluate expression |
| 2026-P2-Q3 | SCQ | 3 | Differential Equation | Separable DE y'=y^3(e^{5x}+1)/(e^x(1+y^4)); quartic finish |
| 2026-P2-Q8 | MCQ | 4 | Differential Equation | xy'=y-x^3, y(1)=0; extrema, monotonicity, intersections with cubic |
| 2021-P2-Q18 | INT | 4 | Ellipse | Max distance between midpoints M(P,Q), M(P,Q') on ellipse = half the major axis |
| 2024-P1-Q4 | SCQ | 3 | Ellipse | Tangents from S to ellipse; one at minor-axis end; find p,q from area ratio |
| 2026-P2-Q17 | Q Stem | 2 | Ellipse | Angle between tangents to x^2+4y^2=1 and 4x^2+y^2=1 at intersection |
| 2024-P2-Q8 | INT | 4 | Function | Cauchy additive and multiplicative functional equations; evaluate expression |
| 2025-P1-Q1 | SCQ | 3 | Function | Coefficient of x^3 in f(x+1)-g(x+2) for quartics |
| 2025-P2-Q4 | SCQ | 3 | Hyperbola | Locus of intersection of line pair is hyperbola; tangent parallel to given line |
| 2023-P1-Q8 | INT | 4 | ITF | Number of solutions of sqrt(1+cos2x)=sqrt2 tan^{-1}(tan x) in given union of intervals |
| 2026-P1-Q4 | SCQ | 3 | ITF | cot^{-1}(cot(-11)) + 10 sin(2cos^{-1}(1/sqrt2)) + 10 sin(2tan^{-1}2) with range shift |
| 2025-P2-Q1 | SCQ | 3 | Limit | e^{x0}+x0=0; limit of &#124;(f(x)+ ...)/(x-x0)&#124; for given f |
| 2024-P1-Q8 | INT | 4 | Logarithm | Two log equations with bases 3^(1/2)... ; 4x+5y |
| 2021-P1-Q11 | MCQ | 4 | Matrices | Permutation matrix P with given E,F; determinant/trace statements |
| 2024-P1-Q14 | MTC SCQ | 3 | Matrices | Matrices with entries from {1,alpha,beta} with zero row/column sums; counting |
| 2021-P1-Q12 | MCQ | 4 | Monotonicity | f=(x^2-3x-6)/(x^2+2x+4): monotonic intervals, onto, range |
| 2021-P2-Q8 | Q Stem | 2 | Parabola | Same stem; x-coordinate alpha of contact point |
| 2023-P1-Q7 | SCQ | 3 | Parabola | Normal at P meets axis at Q, area PFQ=120, integer slope; find (a,m) |
| 2024-P2-Q7 | MCQ | 4 | Parabola | Tangents from (-4,0) to y^2=8x; lengths and orthocentre |
| 2026-P2-Q2 | SCQ | 3 | Parabola | Perpendicular tangents to y^2=16x, t1 t2=-1; focal distance of second point |
| 2021-P2-Q1 | MCQ | 4 | Permutation & Combination | Counting ordered triples/pairs/quadruples in four sets S1..S4 |
| 2026-P1-Q5 | MCQ | 4 | Probability | Two boxes with equal red proportion; independence and conditional probabilities |
| 2021-P1-Q18 | INT | 4 | Solution of Triangle | (cotA+cotC)/cotB with sides sqrt23,3,4 via cosine rule |
| 2025-P1-Q14 | MTC SCQ | 4 | Statistics | Frequency table with unknown f1,f2, median 6; mean deviation, variance |
| 2026-P2-Q12 | Numerical | 4 | Statistics | Mean/variance of 10 and of first 8 observations; recover x9, x10 |
| 2025-P1-Q16 | MTC SCQ | 4 | Vector | u x v = w, v x w = u with linear conditions; &#124;v&#124;^2 and components |
| 2021-P2-Q5 | MCQ | 4 | Vector 3D | OC from cross product with lambda; projections, areas, angle between diagonals |
| 2026-P2-Q1 | SCQ | 3 | Vector 3D | &#124;a+b&#124;, &#124;a-b&#124;, a perp (a-b); area of triangle OPR |

## Level 3 - Average Advanced

| Ref | Type | Marks | Chapter | What the question asks |
|---|---|---|---|---|
| 2026-P2-Q18 | Q Stem | 2 | Area Under Curve | Common area of the two ellipses; cot alpha |
| 2021-P1-Q1 | SCQ | 3 | Circle | Triangle with two sides on x-axis and x+y+1=0, orthocentre (1,1); find circumcircle |
| 2026-P1-Q16 | MTC SCQ | 4 | Circle | Four conic items: circle touching line, common tangent circle-parabola, normal at latus rectum end, hyperbola from focus-directrix |
| 2021-P1-Q4 | SCQ | 3 | Complex Number | z_k = product of e^{i theta}; chord sums vs arc length 2pi and 4pi (P and Q statements) |
| 2021-P1-Q16 | MCQ | 4 | Complex Number | arg((z+alpha)/(z+beta))=pi/4 lies on given circle; find alpha, beta |
| 2023-P1-Q11 | INT | 4 | Complex Number | (1967+1686 i sin t)/(7-3i cos t) contains exactly one positive integer n |
| 2023-P1-Q17 | MTC SCQ | 3 | Complex Number | &#124;z&#124;^3+2z^2+4 zbar-8=0 with Im z nonzero; evaluate expressions |
| 2024-P1-Q5 | MCQ | 4 | Complex Number | S={a+b sqrt2}, T1,T2 powers of (-1+sqrt2),(1+sqrt2); intersections and statements |
| 2023-P1-Q1 | MCQ | 4 | Continuity & Differentiability | Functions from S=(0,1)U(1,2)U(3,4) to T={0,1,2,3}: infinite, increasing, continuous counts |
| 2023-P2-Q6 | MCQ | 4 | Continuity & Differentiability | f=[4x](x-1/4)^2(x-1/2) on (0,1); discontinuity and non-differentiability points |
| 2024-P1-Q17 | MTC SCQ | 3 | Continuity & Differentiability | h = combination of f, g with x&#124;x&#124;sin(1/x); continuity/differentiability for given a,b,c,d |
| 2026-P1-Q7 | MCQ | 4 | Continuity & Differentiability | g = x f(x), f arbitrary; continuity/differentiability implications, counterexamples |
| 2021-P2-Q16 | Para SCQ | 3 | Definite Integration | Same paragraph; inequality statements using series bounds |
| 2023-P2-Q8 | INT | 4 | Definite Integration | Minimum of integral 0..x tan^{-1}x of e^{t-cos t}/(1+t^2023) |
| 2024-P2-Q13 | INT | 4 | Definite Integration | Piecewise linear f, g = integral; zeros of g and right-derivative at 1 |
| 2021-P2-Q4 | MCQ | 4 | Differential Equation | Linear DE y'+alpha y = x e^{beta x}, y(1)=1; which functions belong to the family |
| 2023-P1-Q2 | MCQ | 4 | Ellipse | Common tangents of ellipse x^2/6+y^2/3=1 and y^2=12x; quadrilateral area, x-intercept |
| 2025-P2-Q7 | MCQ | 4 | Ellipse | Points on ellipse mapped to auxiliary circle via angles; lines and ratios |
| 2026-P2-Q13 | Numerical | 4 | Hyperbola | Hyperbola with reciprocal eccentricity and same foci as ellipse; intersections with parabola; d^2=a+b sqrt5 |
| 2021-P1-Q15 | MCQ | 4 | ITF | Telescoping sum of cot^{-1}((1+k(k+1)x^2)/x); limit and root statements |
| 2023-P2-Q3 | SCQ | 3 | ITF | tan^{-1}+cot^{-1} equation =2pi/3; sum of solutions with range care |
| 2025-P2-Q3 | SCQ | 3 | ITF | Number of solutions of x = tan^{-1}(2tan x) - (1/2)sin^{-1}(6tan x/(9+tan^2 x)) |
| 2021-P1-Q14 | MCQ | 4 | Matrices | G=(I-EF)^{-1}; algebraic identities with FE, FGE |
| 2023-P2-Q5 | MCQ | 4 | Matrices | Matrix a_ij=1 if i divides j+1; invertibility, eigenvector, null space |
| 2026-P1-Q8 | MCQ | 4 | Matrices | M=[[2,-1],[1,0]], (M-I)^2=0; M^26, sum of powers, Jordan similarity, integer solutions |
| 2025-P2-Q14 | Numerical | 4 | Methods of Differentiation | Derivative of f o g^{-1} at 2 |
| 2023-P2-Q7 | MCQ | 4 | Monotonicity | f''>0 on (-1,1) with &#124;f&#124;<=... ; number of fixed points X_f |
| 2026-P1-Q1 | SCQ | 3 | Monotonicity | f = sqrt x ln x - x + 1; sign of f' via auxiliary ln x + 2 - 2sqrt x; extrema and f' |
| 2026-P1-Q11 | Numerical | 4 | Permutation & Combination | 10 identical red, 14 identical blue pens to 4 people, 6 each; bounded integer solutions |
| 2021-P1-Q13 | MCQ | 4 | Probability | Bounds on probabilities of intersections/unions of E,F,G |
| 2023-P1-Q6 | SCQ | 3 | Probability | Lattice points inside ellipse and parabola; probability triangle has integer area |
| 2023-P2-Q2 | SCQ | 3 | Probability | Toss until two consecutive outcomes match, P(H)=1/3; P(stops with head) |
| 2024-P1-Q2 | SCQ | 3 | Probability | True-false quiz, knows vs guesses; Bayes' theorem |
| 2024-P2-Q9 | INT | 4 | Probability | Bag with N balls, three draws; joint and conditional probability give N |
| 2025-P2-Q11 | Numerical | 4 | Probability | Three units, defect rates, Bayes; P(defective &#124; U3) |
| 2026-P2-Q11 | Numerical | 4 | Probability | 6 books from 6 maths + 5 physics; mean of &#124;difference&#124;; 77 alpha |
| 2026-P1-Q13 | MTC SCQ | 4 | Quadratic Equation | Roots of x^2+x+1 (omega) and x^2+x-1; equations/values with high powers |
| 2021-P2-Q2 | MCQ | 4 | Solution of Triangle | Inequalities involving cos P, cos R and sides of a triangle |
| 2024-P1-Q3 | SCQ | 3 | Trigonometric Ratio | cot x=-5 in (pi/2,pi); evaluate sin(11x/2)(...)+cos(11x/2)(...) |
| 2026-P1-Q14 | MTC SCQ | 4 | Trigonometric Ratio | Count solutions of four trig equations (sin^6+cos^4=1 etc.) in given intervals |
| 2021-P1-Q19 | INT | 4 | Vector 3D | Unit vectors u,v, w with u.w=1, v.w=1, w.w=4, volume given; find value |
| 2023-P1-Q5 | SCQ | 3 | Vector 3D | Max shortest distance between face diagonals and main diagonals of unit cube |
| 2023-P1-Q16 | MTC SCQ | 3 | Vector 3D | Planes containing line l1; maximise distance from l2; distances of points from H0 |
| 2024-P1-Q7 | MCQ | 4 | Vector 3D | S and T are planes from distance-difference conditions; triangle/point statements |
| 2025-P1-Q5 | MCQ | 4 | Vector 3D | Line of intersection of planes, parallel line through P meets plane M; lengths |
| 2026-P1-Q6 | MCQ | 4 | Vector 3D | Plane containing a line and perpendicular to a plane; parallel plane, distances, angle |
| 2026-P2-Q7 | MCQ | 4 | Vector 3D | Foot of perpendicular, point T by ratio; orthocentre and area of triangle PRT in 3D |

## Level 4 - Slightly difficult

| Ref | Type | Marks | Chapter | What the question asks |
|---|---|---|---|---|
| 2023-P1-Q3 | MCQ | 4 | Area Under Curve | Green/red regions under cubic in unit square; existence of h balancing areas (IVT reasoning) |
| 2023-P1-Q9 | INT | 4 | Area Under Curve | Piecewise linear f with parameter n; area 4 fixes n; maximum of f |
| 2025-P2-Q6 | MCQ | 4 | Area Under Curve | Locus of midpoints of chords of y^2=x cutting area 4/3; region area |
| 2026-P2-Q16 | Q Stem | 2 | Area Under Curve | Same stem; area between alpha1 and alpha4 via antiderivative e^{-x}(1-cos x) |
| 2025-P2-Q10 | Numerical | 4 | Binomial Theorem | Largest coefficient in (1+2x/5)^23; index m |
| 2026-P2-Q5 | MCQ | 4 | Binomial Theorem | f = 10th derivative of (x^2-1)^10: coefficient, f(1)+f(-1) via Leibniz, degree, constant term |
| 2021-P2-Q13 | Para SCQ | 3 | Circle | GP-radius circles C_n inside disc of radius 1025/513; count and non-intersecting maximum |
| 2021-P2-Q14 | Para SCQ | 3 | Circle | Same paragraph; circles D_n inside disc of radius (2^199-1)sqrt2/2^198 |
| 2023-P2-Q13 | INT | 4 | Circle | Common tangents of two circles; midpoints lie on radical axis; AB=sqrt5 gives r^2 |
| 2025-P2-Q13 | Numerical | 4 | Complex Number | arg of sum of (-omega)^k, k=1..2025; 3 theta/pi |
| 2025-P1-Q3 | SCQ | 3 | Continuity & Differentiability | f = 2 - 2x^2 - x^2 sin(1/x) type near 0; monotonicity/extremum near 0 |
| 2026-P1-Q10 | Numerical | 4 | Continuity & Differentiability | (&#124;x&#124;+&#124;x-1&#124;) sin x + [x sin x] on (-pi/2,pi/2); discontinuities + non-differentiable points |
| 2026-P2-Q14 | Numerical | 4 | Continuity & Differentiability | [x^3] log(1+sin^2(pi{x})) and x^3 sin^2(pi log(1+{x})); count discontinuities with cancellations |
| 2021-P2-Q9 | Q Stem | 2 | Definite Integration | f1=integral of product (t-j)^j, j=1..21; count local maxima/minima via parity of exponents |
| 2021-P2-Q12 | Q Stem | 2 | Definite Integration | 48 S2/pi^2 with weight &#124;4x-pi&#124;; symmetry and by-parts |
| 2021-P2-Q15 | Para SCQ | 3 | Definite Integration | psi1, psi2, f, g defined by integrals; MVT-type existence statements |
| 2021-P2-Q19 | INT | 4 | Definite Integration | Integral 0..10 of [sqrt(10x/(x+1))]; locate breakpoints of greatest integer |
| 2024-P2-Q17 | Q Stem | 3 | Definite Integration | 16/pi^3 int fg; needs area of semicircle interpretation |
| 2025-P1-Q11 | Numerical | 4 | Definite Integration | Limit of (alpha int dt/sqrt(1-t^2) + beta x cos x)/x^3 = 2; series expansion |
| 2025-P2-Q16 | Numerical | 4 | Definite Integration | Integral 1/2..2 of tan^{-1}(x/(2x^2-3x+2)); king-type substitution |
| 2024-P2-Q4 | SCQ | 3 | Function | Zeros of x^2 sin(pi/x^2) in various intervals; counting |
| 2024-P2-Q14 | Q Stem | 3 | Function | Relations on {1..6} with 6 elements and &#124;a-b&#124;>=2; n(X)=mC6 |
| 2024-P2-Q15 | Q Stem | 3 | Function | Same paragraph; n(Y)+n(Z)=k^2 |
| 2025-P1-Q6 | MCQ | 4 | Function | f: N->Z, g: Z->N piecewise; one-one/onto of g o f and f o g |
| 2025-P1-Q12 | Numerical | 4 | Function | f(x+y)=f(x)f(y), AP a_i, f(a31)=64f(a25), sum given; partial sum |
| 2026-P2-Q10 | Numerical | 4 | Function | Functions A->B with f(2)!=2, f(4)!=4 for which g(f(x))=2x exists (i.e. f one-one); inclusion-exclusion |
| 2023-P1-Q4 | SCQ | 3 | Limit | f=sqrt n on [1/(n+1),1/n), g bounded by integral inequality; limit of fg by sandwich |
| 2024-P2-Q5 | MCQ | 4 | Limit | lim of sin(x^2)(log x)^a sin(1/x^2)/(x^{ab}(log(1+x))^b)=0; conditions on (a,b) |
| 2024-P1-Q10 | INT | 4 | Matrices | Count 3x3 {0,1} matrices of given form with determinant +-1 |
| 2025-P1-Q4 | SCQ | 3 | Matrices | Count orthogonal integer 3x3 Q commuting with diag(2,2,3) |
| 2025-P2-Q5 | MCQ | 4 | Matrices | X with non-zero entries satisfying AX = XB-type condition; determinants |
| 2026-P1-Q15 | MTC SCQ | 4 | Matrices | MM^T=I with partial entries; columns as vectors; gamma^2+delta^2, coefficients, box and triple products |
| 2021-P2-Q10 | Q Stem | 2 | Maxima & Minima | f2=98(x-1)^50-600(x-1)^49+2450; count local extrema |
| 2025-P2-Q8 | MCQ | 4 | Maxima & Minima | f=(6x+sin x)/(2x+sin x); local extrema at 0 and counts in intervals |
| 2021-P2-Q7 | Q Stem | 2 | Parabola | Largest circle with centre on x-axis inside region x>=0, y^2<=4-x; radius |
| 2024-P2-Q12 | INT | 4 | Parabola | Normal of slope 1/sqrt6 from (0,-alpha) to x^2=-4ay; latus rectum ratio gives 24a |
| 2024-P1-Q11 | INT | 4 | Permutation & Combination | 9 students into teams of 2,3,4 with two restrictions |
| 2021-P1-Q3 | SCQ | 3 | Probability | Three-stage random selection between sets E,F,G; conditional probability S1={1,2} given E3=E1 - heavy casework |
| 2021-P1-Q5 | Q Stem | 2 | Probability | Three numbers with replacement from 1..100; P(max>=81) via complement |
| 2021-P1-Q6 | Q Stem | 2 | Probability | Same stem; P(min<=40) via complement |
| 2023-P2-Q10 | INT | 4 | Probability | Five-digit numbers from 1,2,2,2,4,4,0; P(multiple of 20 &#124; multiple of 5) - counting with repeats and zero |
| 2023-P2-Q16 | Q Stem | 3 | Probability | 7x7 grid, friends = adjacent; 7E(X) for number of friends |
| 2023-P2-Q17 | Q Stem | 3 | Probability | Same stem; probability two random points are friends, 7p |
| 2025-P1-Q2 | SCQ | 3 | Probability | Events U,V,W,T for three students; V is a conditional probability; find P(T) |
| 2024-P1-Q6 | MCQ | 4 | Quadratic Equation | Positive-definite quadratic forms ax^2+2bxy+cy^2; consequences for linear systems |
| 2024-P1-Q9 | INT | 4 | Quadratic Equation | Quartic with f(1)=-9, i sqrt3/2 root of derived cubic; sum of squares of roots |
| 2026-P2-Q6 | MCQ | 4 | Quadratic Equation | a,b,c in AP, integer roots: (r+2)(s+2)=3 forces roots -3,-5 |
| 2025-P1-Q8 | Numerical | 4 | Relation | Reflexive symmetric relations on 6-element set with exactly 10 elements |
| 2023-P2-Q15 | Q Stem | 3 | Solution of Triangle | Same stem; inradius |
| 2021-P1-Q9 | Q Stem | 2 | Straight Line | Locus: product of distances from two lines = lambda^2; chord RS=sqrt270 gives lambda^2 |
| 2025-P2-Q15 | Numerical | 4 | Trigonometric Ratio | Telescoping sum 1/(sin k sin(k+1)) from 60 to 119 degrees; (cosec1/alpha)^2 |
| 2026-P1-Q12 | Numerical | 4 | Trigonometric Ratio | Product of (1-2cos(3^k pi/11)), k=0..4; telescoping via cos(3a)/cos a |
| 2021-P1-Q8 | Q Stem | 2 | Vector 3D | Same stem; plane of consistent (alpha,beta,gamma), squared distance of (0,1,0) |
| 2025-P1-Q9 | Numerical | 4 | Vector 3D | SP+5SQ+6SR=0; ratio EF/ES with mass-point/section reasoning |
| 2025-P2-Q12 | Numerical | 4 | Vector 3D | Coplanarity of three vectors built from a,b,c with p,q; p+q-3 |

## Level 5 - Very difficult

| Ref | Type | Marks | Chapter | What the question asks |
|---|---|---|---|---|
| 2023-P2-Q11 | INT | 4 | Complex Number | Regular octagon on circle radius 2; max of product of distances PA_i via z^8-2^8 |
| 2023-P2-Q12 | INT | 4 | Matrices | Count invertible 3x3 matrices with entries from primes set; count ad=bc cases |
| 2026-P2-Q9 | MCQ | 4 | Matrices | S, T 2x2; ST entries, Mobius map (az+b)/(cz+d), omega fixed point, order of ST, upper half-plane preserved |
| 2025-P1-Q10 | Numerical | 4 | Permutation & Combination | Seven-digit numbers from 0,1,2 with at least one of 0,1 appearing exactly twice - overlapping casework, leading zero |
| 2024-P1-Q13 | INT | 4 | Probability | Points (x,P(X=x)) collinear for x=0..4, mean 5/2; variance - non-standard setup |
| 2026-P1-Q9 | Numerical | 4 | Relation | Equivalence relations on 10-element set with exactly 42 elements: partitions with sum of squares 42, then count |
| 2023-P1-Q10 | INT | 4 | Sequence & Progression | Sum of numbers 7 5...5 7; express as (7 5..5 7 + m)/n; heavy manipulation |
| 2023-P2-Q14 | Q Stem | 3 | Solution of Triangle | Obtuse triangle, sides in AP, largest-smallest angle = pi/2, R=1; (64a)^2 - heavy trig |
| 2021-P1-Q10 | Q Stem | 2 | Straight Line | Same stem; perpendicular bisector of RS meets locus at R',S'; square of R'S' - long precise computation |
| 2023-P1-Q12 | INT | 4 | Vector 3D | Unit vectors at distance 7/2 from plane forming equilateral triangle; parallelepiped volume |
