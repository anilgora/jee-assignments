# Probability: generation report

Blueprint: `qp_blueprints/Probability.xlsx`. There is no `Probability_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` ended with **no errors**. The first build gave one warning: the rupee sign (₹) in Q19 has no glyph in the PDF font. I replaced it with "Rs." in English and "रुपये" in Hindi and rebuilt; the final build has no warnings. No script was edited and no check was weakened.
- I rendered and looked at page 1 of each of the three PDFs, plus page 6 of the full-solutions PDF. The Hindi is shaped and the fractions, binomial coefficients and sums display in 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 30 questions: 6 Single Correct (Q1-Q6), then 24 Numerical (Q7-Q30).
- **Reorder (`--reorder`), old -> new:** 240->1, 242->2, 244->3, 266->4, 267->5, 268->6, 241->7, 243->8, 245->9, 246->10, 247->11, 248->12, 249->13, 250->14, 251->15, 252->16, 253->17, 254->18, 255->19, 256->20, 257->21, 258->22, 259->23, 260->24, 261->25, 262->26, 263->27, 264->28, 265->29, 269->30.
- **Answer Plans:** the blueprint had none, so the script drew all 30. Every answer matches its plan; the build checks this.
  - Q1 Option C; Q2 Option A; Q3 Option B; Q4 Option D; Q5 Option A; Q6 Option B; Q7 negative integer; Q8 positive 2-digit integer; Q9 negative decimal; Q10 decimal between 0 and 1; Q11 positive 3-digit integer; Q12 positive decimal; Q13 positive decimal; Q14 negative decimal; Q15 positive 2-digit integer; Q16 positive 3-digit integer; Q17 negative integer; Q18 decimal between 0 and 1; Q19 negative integer; Q20 negative decimal; Q21 positive 3-digit integer; Q22 decimal between 0 and 1; Q23 positive decimal; Q24 positive 2-digit integer; Q25 positive decimal; Q26 negative decimal; Q27 negative integer; Q28 positive 2-digit integer; Q29 decimal between 0 and 1; Q30 positive 3-digit integer.
- **Cells containing ";":** the check warned about six spreadsheet rows (2, 3, 9, 17, 18, 23). With no config to split them, each cell was kept as **one** concept, as you instructed:
  - "Axiomatic probability; odds in favour and against" (Q2, Q7).
  - "Independent events; pairwise vs mutual independence of three events" (Q20, Q21).
  - The other warned cells are among these same concept names, repeated in other rows.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - Rows with more than two concepts in a Main paper (kept, every concept used): Q18 (4 concepts); Q3, Q5, Q14, Q19 and Q24 (3 concepts each).
  - Concepts repeated across rows (each use has a different mechanism): Binomial probability distribution (Q4, Q5, Q21, Q29); Mean and variance of a binomial distribution (Q5, Q6, Q29); Random experiment, sample space and types of events (Q1, Q7); Axiomatic probability and odds (Q2, Q7); Addition theorem (Q3, Q8, Q15); inclusion-exclusion (Q3, Q8); Problems on coins, dice and cards (Q9, Q10); Probability computed using P&C (Q10-Q14); Complementary events and 'at least one' (Q3, Q15, Q16); Conditional probability and reduced sample space (Q4, Q17, Q18, Q19); Multiplication theorem (Q17-Q20, Q22); Law of total probability (Q18, Q19, Q23, Q24, Q25); Bayes' theorem (Q18, Q23, Q24); Probability via tree diagrams (Q24, Q25); Independent events (Q20, Q21); Mean and variance of a discrete random variable (Q5, Q27, Q28); Standard deviation and variance of ungrouped data (Q6, Q28).

## Answers
| Q | Type | Answer |
|---|---|---|
| 1 | SCQ | (C) |
| 2 | SCQ | (A) |
| 3 | SCQ | (B) |
| 4 | SCQ | (D) |
| 5 | SCQ | (A) |
| 6 | SCQ | (B) |
| 7 | Numerical | -24 |
| 8 | Numerical | 26 |
| 9 | Numerical | -0.50 |
| 10 | Numerical | 0.35 |
| 11 | Numerical | 300 |
| 12 | Numerical | 3.75 |
| 13 | Numerical | 2.50 |
| 14 | Numerical | -0.55 |
| 15 | Numerical | 88 |
| 16 | Numerical | 630 |
| 17 | Numerical | -2 |
| 18 | Numerical | 0.75 |
| 19 | Numerical | -4 |
| 20 | Numerical | -0.03 |
| 21 | Numerical | 270 |
| 22 | Numerical | 0.37 |
| 23 | Numerical | 1.80 |
| 24 | Numerical | 32 |
| 25 | Numerical | 1.30 |
| 26 | Numerical | -0.25 |
| 27 | Numerical | -3 |
| 28 | Numerical | 20 |
| 29 | Numerical | 0.30 |
| 30 | Numerical | 448 |

Every numerical answer is exact; none needs rounding.

## How the answers were checked
Every answer was recomputed in Python, independently of the hand solution, using exact fractions:
- full enumeration of the 10-point sample space (Q1), all 1024 subsets (Q3), all 2^6 toss sequences (Q4), the 2^12 subset data (Q6), the 36 dice pairs (Q9, Q21), the 120 card triples (Q10), the 625 numbers (Q11), the 360 arrangements of RESIST (Q12), all 4^5 placements (Q13), the 300 solutions (Q14), all 990 pairs of lines for n = 10 (Q16), all ordered draws (Q18, Q22), all 6-round sequences (Q30);
- sympy for the systems and roots (Q2, Q5, Q15, Q17, Q24, Q26, Q27, Q29), and mpmath numerical integration for the area in Q26;
- consistency of the data: the Venn regions in Q20 are all non-negative and sum to 1; example data (five 2s and five 8s) exist for Q28; in Q15 the second root of the system gives probabilities above 1 and is rejected; in Q26 the other roots of the cubic lie outside a in (-1, 0).

## Difficulty
- Levels: **12 questions at Level 2, 18 at Level 3**, exactly as the blueprint targets. No question is one level off target.
- Marks-weighted difficulty index: **about 2.60** (no equivalence-relation or multi-correct adjustment applies). This is a Main-pattern chapter paper, so the Advanced range does not apply.
- Consistency pass (questions sorted by level, neighbours compared): Q19 is the weakest Level 3. Its mathematics alone is Level 2; the numerical format and the two-branch update keep it at 3. Q6 is the strongest Level-3 SCQ. No level was changed.

## Originality report
Every question was built on a named mechanism and checked against `known_skeletons.md`. Each one was then web-searched (WebSearch was available in this run).
- "not found" means no matching problem appeared.
- "ingredient only" means the search found the standard ingredient or a related exercise, but not this construction.
- "found: redesigned" means a close published problem was found and the question was rebuilt.

One question was redesigned before it was written into the paper. The first Q22 design (with-replacement minus without-replacement probability that three balls from 4 red and 6 blue are all one colour) turned out to be a close variant of a published exercise. It was replaced by a mixed replacement rule (red returned, blue kept aside); the search for that rule found only the general ingredient.
Perfect novelty cannot be guaranteed: probability has a very large stock of textbook problems. If you recognise a question, tell me which one.

| Q | Mechanism | Web check |
|---|---|---|
| 1 | a two-branch experiment whose branches have different lengths, so 'at least two tails' and 'at least one head' are decided by the branch structure; the true statement needs the single outcome TTT to be placed in E3 (way 5: sample space construction linked with types of events). | ingredient only |
| 2 | a probability assignment with a quadratic term, where the odds condition and P(S) = 1 give two candidate assignments and the non-negativity axiom (not the algebra) rejects one of them (way 5: odds linked with the axioms). | not found |
| 3 | a random subset required to hit three overlapping blocks, so the pairwise intersections of the complementary events have unequal probabilities (shared element versus disjoint blocks) and inclusion-exclusion has to track the overlap structure (way 5: complement, addition theorem for three events and inclusion-exclusion linked). | not found |
| 4 | conditioning a biased binomial experiment on a tail event (at least 4 heads) and asking about one specified trial; inside each level X = k the bias cancels and the answer is the weighted average of k/6 (way 5: binomial distribution linked with the reduced sample space). | not found |
| 5 | a count of ordered success-failure pairs of trials, which equals X(n - X), so its mean needs E(X^2) recovered from the binomial mean and variance (way 5: binomial parameters, mean of a function of a random variable and variance linked). | ingredient only |
| 6 | a data set indexed by all subsets of a 12-element set, whose frequency table is the binomial coefficients, so the standard deviation of the data is read off from the variance of B(12, 1/2) and then rescaled (way 5: binomial mean and variance linked with the variance of ungrouped data). | not found |
| 7 | the odds in favour of an unspecified event fix only its size, and the counts of events mutually exclusive with it and exhaustive with it are complementary powers of 2 (way 5: odds linked with counting types of events). | not found |
| 8 | three divisors chosen so that every pairwise lcm equals the triple lcm, so all four intersection terms are the same set and the inclusion-exclusion collapses to n(A)+n(B)+n(C) - 2*3 (way 4: a hidden coincidence of intersections). | ingredient only |
| 9 | two dice events linked by number theory: a coprime pair can never have its product divisible by its sum, so the first count is done only over non-coprime pairs and the two events are disjoint (way 5: a dice count linked with a gcd argument). | not found |
| 10 | a card selection whose values split into unequal residue classes (3, 4, 3), so the familiar answer 1/3 fails and the count has to be done by classes (way 5: cards linked with combinations by residue classes). | ingredient only |
| 11 | comparing a formed number with its own reversal, which pairs the numbers up so that only the self-reverse numbers need counting (way 4: a hidden symmetry). | not found |
| 12 | two anagrams with a repeated letter (RESIST and SISTER) bound a dictionary interval, and the probability that a random arrangement falls inside it needs both ranks (way 5: rank of a word linked with a probability over alike-letter arrangements). | not found |
| 13 | comparing the two leading occupancy events (none empty versus exactly one empty) for 5 balls in 4 boxes, which needs two different onto counts (way 5: probability linked with distributions into distinct boxes with and without empty boxes). | ingredient only |
| 14 | one uniform model on the solutions of x + y + z = 23 scored by an upper-bound event and a lower-bound event, so the beggar's method is used three ways (total, shifted lower bound, excess over an upper bound) (way 5). | not found |
| 15 | only the three pairwise unions of independent events are given; the complements turn them into three products whose product is a perfect square, so the 'at least one' probability follows without solving for each event first (way 4: a hidden product structure). | not found |
| 16 | the probability that two random lines of a complete point configuration meet at one of the given points simplifies to 4/(n+1); its complement determines n and then the number of new intersection points (way 4: a hidden clean formula). | not found |
| 17 | a two-stage experiment (die, then that many coins) feeding the coefficients of a quadratic; conditioning on 'distinct integer roots' gives a reduced sample space with unequal weights from the multiplication theorem, and the most probable smaller root is asked (way 5: conditional probability linked with multiplication theorem and a root condition). | not found |
| 18 | an urn whose composition is set by a die roll, observed through two white draws without replacement, and asked for the next draw; the posterior on the composition is proportional to k(k - 1) (way 5: multiplication theorem, total probability and Bayes linked in one prediction). | not found |
| 19 | an urn whose update rule differs by colour (red removed, green returned with two more), so the second draw is computed from two different reduced urns and turned into the value of a bet (way 5: conditional probability, multiplication theorem and total probability in one game). | ingredient only |
| 20 | pairwise independence fixes all pair terms, and the 'none' probability then fixes the triple term through the addition theorem, measuring exactly how far the events are from mutual independence (way 5: pairwise versus mutual independence linked with the multiplication theorem). | not found |
| 21 | the 'none of three' probability of a pairwise-but-not-mutually independent triple is the success probability of a binomial experiment, so assuming mutual independence (1/8) instead of the true 1/4 changes the answer (way 5: pairwise versus mutual independence linked with a binomial distribution). | ingredient only |
| 22 | a mixed sampling rule (red with replacement, blue without), so the three orders of the same colour count have three different products (way 5: drawing with and without replacement in one process, linked by the multiplication theorem). | found: redesigned |
| 23 | one test raises the posterior from 0.1 to 0.5 and a second conditionally independent test to 0.9, and the question compares the two posteriors (way 5: total probability and Bayes applied twice with conditional independence). | ingredient only |
| 24 | the number of tosses is itself random (set by a die), so the likelihood of 'all heads' for a fair coin is a finite geometric average 21/128, and the posterior condition is inverted to find the number of fair coins (way 5: tree diagram, total probability over the die and Bayes linked). | not found |
| 25 | an urn reinforced on red and depleted on black, so the second draw is more likely red than the first (0.7 against 0.6), and the expected red count is read from a two-level tree (way 5: tree diagram linked with total probability). | ingredient only |
| 26 | the favourable region of a geometric probability is the region between a sign-changing parabola and the axis, and the given probability is inverted to find the parameter through a cubic in sqrt(-a) (way 5: geometrical probability linked with area under sign changes). | not found |
| 27 | a three-point distribution recovered from its mean and variance only, then used for the third moment, whose sign shows the asymmetry of the values (way 5: distribution of a random variable linked with mean and variance conditions). | not found |
| 28 | the mean squared difference of a random pair drawn without replacement from a data set equals n^2 sigma^2 / C(n,2), so the given sums fix it without knowing the data (way 4: a hidden identity linking a random variable to the data variance). | ingredient only |
| 29 | the binomial variance gives two symmetric values of p, and an inequality between two binomial probabilities (not the mean) selects one of them (way 5: variance of a binomial linked with comparison of binomial probabilities). | ingredient only |
| 30 | a repeated matching experiment in which each round is a miss with the derangement probability 1/3, and the 'no two consecutive misses' probability is computed by a weighted Fibonacci-type recursion c_n = 2c_{n-1} + 2c_{n-2} (way 5: derangement probability linked with a recursion). | not found |

## Problems found while verifying
- Q15: the system for P(A'), P(B'), P(C') has a second solution (from the negative square root) that gives probabilities above 1. The solution says why it is rejected.
- Q26: the area equation is a cubic with three real roots in c = sqrt(-a). The stated condition a in (-1, 0) leaves only c = 1/2. Without that condition, c = (1+sqrt3)/2 would also fit, which is why the condition is in the stem.
- Q17: a student who forgets the case c = 0 still gets -2. The answer is robust, but the full solution includes c = 0.
- Q7 (stem review): I added "that is, A ∪ B = S" so that "exhaustive" has only one reading.
- Q19: the rupee sign was replaced as described under Environment.

## Rows whose concepts were hard to combine naturally
- Q18 (four concepts: conditional, multiplication, total probability, Bayes). All four are used in one urn-prediction problem. Bayes appears as the posterior on the urn composition; the direct ratio of total probabilities also gives the answer.
- Q19 asks for an expected gain (a negative integer plan). The expectation is computed from the total-probability value, which is the substance of the question.
- Q12 and Q30 ask for 1/p and k in "k/3^6": the plans (positive decimal, 3-digit integer) made a derived quantity necessary, as the skill allows.

The Hindi text is my own translation; please review the specialised terms.
