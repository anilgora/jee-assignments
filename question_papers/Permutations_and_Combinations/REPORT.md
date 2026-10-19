# Permutations and Combinations: generation report

Blueprint: `qp_blueprints/Permutations_and_Combinations.xlsx`. There is no `Permutations_and_Combinations_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` ended with **no errors and no warnings**. The first run stopped on two errors, which I fixed in the question files: a `#` outside maths in the Q33 solution, and a Q35 stem sentence that the domain check read as a function without a domain. No script was edited and no check was weakened.
- I rendered and looked at page 1 of each of the three PDFs and page 9 of the full-solutions PDF. The Hindi is shaped and the fractions and sums display in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 50 questions: 9 Single Correct (Q1-Q9), then 41 Numerical (Q10-Q50).
- **Reorder (`--reorder`), old -> new:** 153->1, 160->2, 162->3, 171->4, 173->5, 174->6, 177->7, 179->8, 181->9, 132->10, 133->11, 134->12, 135->13, 136->14, 137->15, 138->16, 139->17, 140->18, 141->19, 142->20, 143->21, 144->22, 145->23, 146->24, 147->25, 148->26, 149->27, 150->28, 151->29, 152->30, 154->31, 155->32, 156->33, 157->34, 158->35, 159->36, 161->37, 163->38, 164->39, 165->40, 166->41, 167->42, 168->43, 169->44, 170->45, 172->46, 175->47, 176->48, 178->49, 180->50.
- **Answer Plans:** the blueprint had none, so the script drew all 50. Every answer matches its plan; the build checks this.
  - Q1 Option C; Q2 Option A; Q3 Option B; Q4 Option D; Q5 Option A; Q6 Option B; Q7 Option D; Q8 Option C; Q9 Option A; Q10 negative integer; Q11 positive 2-digit integer; Q12 negative decimal; Q13 decimal between 0 and 1; Q14 positive 3-digit integer; Q15 positive decimal; Q16 positive decimal; Q17 negative decimal; Q18 positive 2-digit integer; Q19 positive 3-digit integer; Q20 negative integer; Q21 decimal between 0 and 1; Q22 negative integer; Q23 negative decimal; Q24 positive 3-digit integer; Q25 decimal between 0 and 1; Q26 positive decimal; Q27 positive 2-digit integer; Q28 positive decimal; Q29 negative decimal; Q30 negative integer; Q31 positive 2-digit integer; Q32 decimal between 0 and 1; Q33 positive 3-digit integer; Q34 positive 2-digit integer; Q35 positive decimal; Q36 decimal between 0 and 1; Q37 negative integer; Q38 positive 3-digit integer; Q39 negative decimal; Q40 negative integer; Q41 positive 3-digit integer; Q42 decimal between 0 and 1; Q43 positive decimal; Q44 positive 2-digit integer; Q45 negative decimal; Q46 positive 3-digit integer; Q47 negative decimal; Q48 decimal between 0 and 1; Q49 positive 2-digit integer; Q50 negative integer.
- **Cells containing ";":** the check warned about three rows (spreadsheet rows 8, 13 and 14). With no config to split them, each cell was kept as **one** concept, as you instructed:
  - "Formation of words; rank of a word in dictionary order" (new Q17, old 139).
  - "Circular permutations; clockwise/anticlockwise; necklace and garland" (new Q22 and Q23, old 144 and 145).
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Rows with more than two concepts in a Main paper (kept, every concept used): Q20 (4 concepts), Q26, Q31, Q36 and Q40 (3 concepts each).
  - Concepts repeated across rows (each use has a different mechanism): Derangements (Q2, Q3, Q9, Q36); Principle of inclusion-exclusion for 2, 3 and n sets (Q2, Q8, Q34, Q36, Q37); Factorial notation (Q10, Q11); Legendre's formula (Q11, Q12); Formation of numbers with given digits (Q13, Q14); Formation of numbers divisible by a given number (Q13, Q15); Sum of all numbers formed (Q14, Q16); Permutations of alike objects (Q17, Q18); bundle method (Q19, Q20); gap method (Q19, Q20, Q21); no two alike adjacent (Q20, Q21); Committee formation (Q5, Q20, Q46); Circular permutations (Q22, Q23); Circular arrangements with restrictions (Q23, Q24); Selection of r from n (Q25, Q26); Selection from a mix (Q25, Q26); Total number of combinations (Q26, Q27); beggar's method (Q4, Q28); Multinomial as a counting tool (Q29, Q30); equal groups (Q1, Q31); unequal groups (Q1, Q31); distinct objects into boxes (Q31, Q32); identical objects into boxes (Q32, Q33); onto functions (Q34, Q35, Q36); number of divisors (Q38, Q39, Q40, Q50); product of two factors (Q38, Q40); pairs with given GCD/LCM (Q39, Q40); lines, triangles and diagonals (Q7, Q41, Q42); points of intersection and regions (Q41, Q43); no two consecutive selection (Q4, Q45); bijection and complement (Q44, Q46); properties of binomial coefficients (Q6, Q47); straight lines and triangles from points (Q7, Q48); squares and rectangles in a grid (Q44, Q49).
  - Near-duplicate concept pairs in one row (both kept and both used): Q7 (two wordings of lines and triangles from points), Q8 (two wordings of inclusion-exclusion), Q9 (De-arrangement and Derangements), Q49 (two wordings of squares and rectangles in a grid).

## Answers
| Q | Type | Answer |
|---|---|---|
| 1 | SCQ | (C) |
| 2 | SCQ | (A) |
| 3 | SCQ | (B) |
| 4 | SCQ | (D) |
| 5 | SCQ | (A) |
| 6 | SCQ | (B) |
| 7 | SCQ | (D) |
| 8 | SCQ | (C) |
| 9 | SCQ | (A) |
| 10 | Numerical | -3 |
| 11 | Numerical | 55 |
| 12 | Numerical | -1.50 |
| 13 | Numerical | 0.14 |
| 14 | Numerical | 246 |
| 15 | Numerical | 2.40 |
| 16 | Numerical | 1551.50 |
| 17 | Numerical | -0.15 |
| 18 | Numerical | 12 |
| 19 | Numerical | 864 |
| 20 | Numerical | -192 |
| 21 | Numerical | 0.40 |
| 22 | Numerical | -72 |
| 23 | Numerical | -0.20 |
| 24 | Numerical | 576 |
| 25 | Numerical | 0.40 |
| 26 | Numerical | 5.50 |
| 27 | Numerical | 18 |
| 28 | Numerical | 1.80 |
| 29 | Numerical | -7.50 |
| 30 | Numerical | -30 |
| 31 | Numerical | 57 |
| 32 | Numerical | 0.04 |
| 33 | Numerical | 372 |
| 34 | Numerical | 50 |
| 35 | Numerical | 3.60 |
| 36 | Numerical | 0.35 |
| 37 | Numerical | -163 |
| 38 | Numerical | 263 |
| 39 | Numerical | -0.18 |
| 40 | Numerical | -22 |
| 41 | Numerical | 279 |
| 42 | Numerical | 0.75 |
| 43 | Numerical | 1.80 |
| 44 | Numerical | 36 |
| 45 | Numerical | -0.40 |
| 46 | Numerical | 240 |
| 47 | Numerical | -6.76 |
| 48 | Numerical | 0.50 |
| 49 | Numerical | 58 |
| 50 | Numerical | -390 |

Every numerical answer is exact; none needs rounding.

## How the answers were checked
Every answer was recomputed independently of the hand solution. Counting questions were checked by full brute-force enumeration in Python, for example:
- set partitions of 8 (Q1); all 8! orders (Q2, Q9) and 9! orders (Q19);
- the 265 derangements (Q3); a DP path count (Q8);
- all teams and seatings (Q20); the dihedral reduction of circular orders (Q22, Q23);
- all onto functions and their sections (Q35, Q36); all 495 committees (Q46); all rectangles on the board (Q44, Q49).
Coefficient and sum questions (Q6, Q10, Q29, Q30, Q47) were checked with sympy. Q7 and Q42 were checked with exact sympy coordinates for collinearity. Q37 was checked by building one consistent Venn distribution and confirming that the asked expression equals -(e1+e2) for every distribution.

## Originality report
Every question was built on a named mechanism and checked against `known_skeletons.md`. Each one was then web-searched (WebSearch was available in this run).
- "not found" means no matching problem appeared.
- "ingredient only" means the search found the standard ingredient or a related exercise, but not this construction.
- "found: redesigned" means a close published problem was found and the question was rebuilt.
Perfect novelty cannot be guaranteed; P&C has a very large stock of textbook problems. If you recognise a question, tell me which one.

| Q | Mechanism | Web check |
|---|---|---|
| 1 | splittings of a set into unlabelled groups of size at least 2, filtered by whether two groups have equal size, so the student must enumerate the size patterns and apply the 1/k! correction only on the patterns that need it... | ingredient only |
| 2 | a partial derangement of a word in which only the vowel positions are forbidden, so inclusion-exclusion runs over 5 of the 8 positions while all 8 letters move (way 5: derangement and inclusion-exclusion linked). | not found |
| 3 | a conditional matching probability in which the sample space itself is the set of derangements and the event (a 2-cycle between two given people) leaves a smaller derangement, so the answer is the ratio D4/D6 (way 5). | ingredient only |
| 4 | a no-two-consecutive selection strengthened to 'at least two empty slots between cars' with both ends empty, converted to a beggar's-method equation with mixed lower bounds (way 5). | not found |
| 5 | a committee condition (at least two women) combined with a structural condition (contains a married couple) handled by complementary counting inside the first condition, then turned into a probability (way 5). | ingredient only |
| 6 | a weighted sum of binomial coefficients with weights C(3,k) that collapses by Vandermonde (or by Pascal's rule applied three times) into a single coefficient, then compared with a neighbouring coefficient through C(m,r) =... | not found |
| 7 | a 13-point configuration (hexagon vertices, side midpoints, centre) in which the hidden collinearities midpoint-centre-opposite midpoint must be found; the count of lines through three points is the whole difficulty (way 4: a... | found: redesigned |
| 8 | lattice paths avoiding three points, two of which are incomparable so their intersection is empty, combined with a third point that each of them precedes (way 5: inclusion-exclusion where one pairwise term vanishes for an... | ingredient only |
| 9 | exactly-k-fixed-point counting where the fixed set must be a pair of consecutive integers, so the choice of the fixed set is a combinatorial count of its own (way 5). | not found |
| 10 | a factorial sum whose polynomial weight splits as (k+1)(k+2) - 1, giving a telescoping pair two steps apart ((k+2)! - k!), so the constant term must be tracked from the two uncancelled starting terms (way 4: hidden telescoping). | found: redesigned |
| 11 | the exponent of 2 in a product of central ratios (2k)!/k!, where splitting (2k)! into even and odd parts (or Legendre's formula) shows each factor contributes exactly k, turning the problem into an arithmetic series (way 4: an... | not found |
| 12 | the gap between the exponent of 5 in n! and its 'expected' value n/4, which equals minus the base-5 digit sum over 4; the question asks for this gap at n = 2026, so a negative decimal arises naturally (way 4: an invariant... | ingredient only |
| 13 | divisibility by 11 for numbers formed with repetition from a small digit set, where the bounded digit sums force the alternating sum to be exactly 0, so the count becomes a convolution of pair-sum counts with a leading-digit... | found: redesigned |
| 14 | the mean of numbers whose digits are a 3-subset in increasing order, which needs the position-wise digit sums computed through order statistics of subsets (way 5: forming numbers and summing them, linked through how often a... | not found |
| 15 | a ratio of two divisibility counts for the same family of numbers, one decided by the digit sum (a subset problem) and one by the last two digits (a position problem), so the two counts use opposite structures (way 5). | found: redesigned |
| 16 | the mean of all integers of length 1 to 4 over the digit set {1,2,3}, where the per-length digit-sum argument produces a GP of place values inside a GP of lengths (ratio 30) (way 5: sum of formed numbers linked with a GP). | not found |
| 17 | the rank of a word with repeated letters, converted into the difference of 'before' and 'after' probabilities (2r - N - 1)/N, which is exact to two decimals only because N = 60 (way 5: rank and permutations of alike objects... | not found |
| 18 | arrangements of a word with repeated letters that are palindromes, which reduces to permuting the half-multiset with the odd-count letter forced to the middle (way 4: a hidden symmetry halves the multiset). | not found |
| 19 | the bundle and gap methods combined so that the bundle removes exactly two gaps wherever it stands (the end case looks different but is not), which decides that the novels fill the remaining gaps exactly (way 4: an invariant... | not found |
| 20 | one committee-then-seating process scored twice, once with the gap method and once with the bundle method, across the cases w = 2, 3, 4 women; the case w = 4 is impossible for one count and large for the other (way 5: four... | not found |
| 21 | a word with two different repeated letters where the gap method must be adapted: when the first repeated letter is adjacent, one copy of the second letter is forced into the gap between them (way 5: gap method and the... | found: redesigned |
| 22 | the same restricted circular arrangement (a pair together, a third object adjacent to neither) counted once as a garland and once on a fixed tray, so the answer isolates the clockwise/anticlockwise factor 2 under a restriction... | ingredient only |
| 23 | two restricted necklace counts (alternating colours, one colour in a block) compared through probabilities over the 60 necklaces, which needs the 'reflection preserves the property' argument for each count (way 5). | ingredient only |
| 24 | an alternating round-table seating with ten equally spaced seats where the 'diametrically opposite' condition is compatible with alternation only because 10/2 = 5 is odd (way 4: a parity feature of the seats). | found: redesigned |
| 25 | the same selection counted with identical and with distinguishable copies, where the identical white balls make every subset of the coloured balls give exactly one selection (2^3), compared with C(6,3) (way 5). | ingredient only |
| 26 | the mean size of a selection from a mixed collection (identical apples, identical bananas, distinct mangoes) over all selections including the empty one, which separates into independent means because the count is a product... | not found |
| 27 | strict chains of length three in the power set of a 3-element set, counted by assigning each element to one of four regions (4^n, 3^n, 2^n) and removing equalities by inclusion-exclusion (way 5: power-set counting linked with... | ingredient only |
| 28 | the mean of one variable over the integer solutions of a linear equation with mixed lower and upper bounds, which needs the distribution of that variable, not only the total count (way 5). | not found |
| 29 | a trinomial power with a fractional negative coefficient, chosen so that the three contributing terms have different signs and sizes and the coefficient is a negative decimal (way 5: counting solutions of q + 2r = 4 with weights). | ingredient only |
| 30 | a product whose factor (1 - x)(1 + x + x^2) = 1 - x^3 shortens the multinomial work to three coefficients of (1 + x + x^2)^4, each extracted by the multinomial theorem (way 4: a hidden factorisation). | ingredient only |
| 31 | placements of distinct balls into distinct boxes (empty allowed) classified by whether two boxes have equal counts; the complement is a single unequal-size pattern 0, 1, 3, while the direct count needs the equal-size patterns... | not found |
| 32 | the same 'no box empty' distribution counted for distinct and for identical balls, compared by a ratio, so the student must apply both models to one situation (way 5). | ingredient only |
| 33 | an identical-object distribution with an inequality between two recipients, settled by the symmetry a <-> b and a count of ties instead of a long case split (way 4: a hidden symmetry). | ingredient only |
| 34 | functions whose range must contain a given part of the codomain, which is an onto-type inclusion-exclusion over only the required values (way 5). | ingredient only |
| 35 | averaging the number of right inverses g of an onto f over all onto f, which equals the product of fibre sizes; the count of onto functions and of one-one sections are combined through the fibre patterns (way 5). | ingredient only |
| 36 | onto functions from a 5-set to a 4-set with no fixed point among 1..4, counted by inclusion-exclusion over the missed values where the number of allowed images depends on whether the argument is itself missed (way 5: onto... | not found |
| 37 | a signed combination of single and pairwise counts that the given 'none / exactly two / all three' data determine, although n(A), n(B), n(C) individually are not known; the student must express both sums through the exactly-j... | found: redesigned |
| 38 | factorisations of a perfect square into two factors under a parity restriction, which is removed by the substitution a = 2a', b = 2b' before the (d+1)/2 formula applies (way 5). | ingredient only |
| 39 | two probabilities on random pairs of divisors, one for 'lcm equals N' (maximum exponent conditions) and one for 'a divides b' (exponent inequalities), both computed prime by prime and compared (way 5). | not found |
| 40 | the number of ordered pairs with a given lcm M equals d(M^2), which links it to the factor-pair count of the perfect square M^2 (way 4: a hidden identity between two different counts). | ingredient only |
| 41 | the number of pieces into which the diagonals of a convex polygon are cut, found from the number of diagonals and the C(n,4) crossings by a double count (each crossing lies on two diagonals) (way 5). | found: redesigned |
| 42 | a point set in which one point is defined as a harmonic conjugate, and the triangle count depends on noticing that this conjugate lies on the line through two other given points (way 5: section formula and counting triangles... | not found |
| 43 | the split of the regions formed by lines in general position into bounded and unbounded ones, using the line-by-line region count and a large circle for the unbounded regions (way 5). | ingredient only |
| 44 | rectangles avoiding a central block, counted through the bijection rectangle = (row interval, column interval) and a complement in which the condition factorises into rows and columns (way 4: a product structure hidden in a... | not found |
| 45 | the two extreme spacing events for a random 3-subset of a row (all separated, all together) compared through their probabilities (way 5). | ingredient only |
| 46 | a committee condition (every department represented) with a refusal clause whose correction term itself needs a complement (the remaining two must supply a chemist) (way 5). | found: redesigned |
| 47 | a linear condition on the weighted sums of squares of binomial coefficients, solved by turning r C(n,r) into n C(n-1,r-1) inside a square and inside a product, then applying Vandermonde twice; n = 13 makes 2n - 1 = 25 so the... | not found |
| 48 | the triangles formed by the vertices and side-midpoints of a triangle, classified by area, where the less obvious triangles ADE (vertex with the far midpoint) also have area one-fourth (way 4: a hidden equality of areas). | not found |
| 49 | rectangles that are not squares in a board with a corner removed, counted from the full-board formulas by removing the rectangles through the corner, which are exactly those with intervals starting at the corner (way 5). | not found |
| 50 | a signed divisor sum in which the sign depends on the parity of the divisor, so the sum-of-divisors product formula must be split by the power of 2 and recombined with signs (way 4: a factorisation of a signed sum). | ingredient only |

Redesigns after the web check:
- **Q7:** 12-gon plus centre, T - L. An octagon-plus-centre T - S problem is published.
- **Q10:** the weight k^2+1, whose sum n(n+1)! is published.
- **Q13:** digits 0-5 without repetition, divisible by 12. A digits 1-5 version is published.
- **Q15:** 4-digit numbers from 1-6 divisible by 4, a published count.
- **Q21:** TATTOO, the same skeleton as the published PERMUTATION problem.
- **Q24:** a table of 7 with A, B together and C, D apart. Also, "two girls not next to a particular boy" is published.
- **Q37:** least and greatest possible number reading all three.
- **Q41:** "70 interior intersection points, find the number of diagonals" is published.
- **Q46:** built on the NCERT "at least 2 women from 6 men and 4 women" base.
- **Q18:** switched from MISSISSIPPI to SUCCESSES as a precaution.

Standard ingredients that remain on purpose: the derangement formula, inclusion-exclusion, stars and bars, C(n,4) diagonal crossings, (d(N)+1)/2 for a perfect square, the 2e+1 rule for lcm pairs, and (n-1)!/2 for necklaces.

## Difficulty
- Level distribution (calibrated scale): **level 2: 25 questions, level 3: 25 questions**. Every question is rated exactly at its blueprint target.
- Marks-weighted difficulty index (SCQ 3 marks, Numerical 4 marks): **about 2.50**. This is a JEE Main pattern paper, so the Advanced range 2.6-3.2 does not apply.
- No question is one level off target.
- Consistency pass: I read the hardest level-2 questions next to the easiest level-3 ones (Q24 and Q46 at level 2 against Q31 and Q39 at level 3) and kept the levels.
  - Q36 could be argued as level 4. Its inclusion-exclusion terms are non-standard; it is kept at 3 with Medium confidence.
  - Q18 (palindromes) is level 2 rather than 1, because the half-arrangement idea is less practised.
- No equivalence-relation adjustment and no MCQ floor apply.

## Problems found while verifying
- **Q19:** the first design (3 volumes, 3 novels, 2 dictionaries, novels adjacent neither to each other nor to the block) has answer **0** by brute force. Even at the end of the shelf, the block blocks two gaps. A third dictionary was added (answer 864).
- **Q5:** the first design (exactly two women and no couple) was a one-step level-2 count. It was replaced by "at least two women and at least one couple" (complement inside a condition) to reach level 3.
- **Q31:** the web check showed that "some two boxes contain the same number" could be read as excluding two empty boxes (54 instead of 57). The stem now says "(an empty box contains 0 balls)".
- **Q33** solution text and the **Q35** stem sentence were rephrased after the first build (see Environment).

## Rows whose concepts were hard to combine naturally
- **Q20** (4 concepts):
  - "Arrangements where no two alike objects are adjacent" is used through the M/W pattern of a seating, where "no two W adjacent" is the gap-method condition.
  - It is a genuine use, but it overlaps with the gap-method concept of the same row.
- **Q26:** "Total number of combinations (2^n and 2^n - 1 type)" enters through the count (4+1)(2+1)2^5 of all selections (the denominator), not as the asked quantity.
- **Q12:** a single-concept Legendre row with a negative-decimal plan. The question asks for E(2026) - 2026/4, which is natural through E(n) = (n - s_5(n))/4, but it is still a derived quantity.
- **Q22:** the negative-integer plan forced a difference of two counts (garland minus tray).
- **Q45:** the negative-decimal plan forced a difference of two probabilities (q - p).
- **Q32:** the decimal plan forced a ratio of two counts (b/a).

## Hindi
The Hindi is my own translation, with the terms from `hindi_terms.md`. Please review the specialised terms:
- अध्ययन-समूह (study circle), माला (garland), हार (necklace)
- आच्छादक (onto), परिसर (range), लघुत्तम समापवर्त्य (lcm)
- विकर्ण (diagonal), परिबद्ध / अपरिबद्ध क्षेत्र (bounded / unbounded region)

## Files
- Word, Master format with LaTeX:
  - `Permutations_and_Combinations_Shortened_Solutions.docx`
  - `Permutations_and_Combinations_Full_Solutions.docx`
- PDFs, English and Hindi, 2D equations:
  - `Permutations_and_Combinations_Questions_EN_HI.pdf`
  - `Permutations_and_Combinations_Questions_and_Shortened_Solutions.pdf`
  - `Permutations_and_Combinations_Questions_and_Full_Solutions.pdf`
- Internal difficulty report: `Permutations_and_Combinations_difficulty.xlsx`
- Sources for a later fix and rebuild: `_source/`, which holds `blueprint.json`, `meta.json` and `q01.json`-`q50.json`.
