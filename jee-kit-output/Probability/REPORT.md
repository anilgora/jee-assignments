# Probability: revision kit report

- Items in the Quick Review: 53
- Batch XII: 144 graded questions, High threshold 13 -> High 6, Medium 32, Low 15
  - High items (numbers): [4, 29, 38, 43, 50, 51]
- Batch XIII: 119 graded questions, High threshold 11 -> High 6, Medium 30, Low 17
  - High items (numbers): [4, 27, 29, 38, 50, 51]

## Added items
- 5: What conditions must the probabilities satisfy (bounds on $P(A)$, $P(A\cap B)$, $P(A\cup B)$)?  [source: J-I 6; J-M(XII) 36; J-A 30; DPP-3 5, 6]
- 45: How to find the least number of trials $n$ so that the probability of at least one (or at least $r$) success is at least $k$?  [source: J-A 11, 25; J-M(XII) 9; DPP-5 2, 12; C-II 35]
- 46: How to find the most probable number of successes in $B(n,p)$?  [source: J-I 36; J-II 37]

## Rephrased items

## Questions with no matching item
- J-M(XIII):39

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [202, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 247, 248, 249, 250, 251, 252, 253, 254, 255]

## Validation warnings
- none

## Input files used (not modified)
- chapters/Probability/Theory.pdf (theory sheet, 39 pages)
- chapters/Probability/XII.pdf (XII sheet: J-I 41, J-II 49, J-M 45, J-A 43, C-I 21, C-II 36 questions; 163 pages)
- chapters/Probability/XIII.pdf (XIII sheet; only its J-M (54 questions) was used; 173 pages)
- chapters/Probability/DPP.pdf (DPP 1-7: 13+15+15+12+13+15+17 = 100 questions; 50 pages)
- chapters/Probability/QB.pdf (JEE Main question bank, Q200-255, 56 questions; 39 pages)
- Master prompt list: .claude/skills/jee-chapter-revision-kit/references/master_index.json (Probability: 50 prompts in 17 headings, master pages 25-26)

## Item numbering
- Final item numbers in the Quick Review: 1-4 = master prompts 1-4; 5 = added item (bounds on probabilities); 6-44 = master prompts 5-43; 45 = added item (least number of trials); 46 = added item (most probable number of successes); 47-53 = master prompts 44-50.

## Graded counts and High items
- Batch XII: J-M(XII) 45 + J-A 43 + QB 56 = 144 graded questions; High threshold max(2, round(0.091 x 144)) = 13.
  High items: 4 (classical definition), 29 (meaning of independent events), 38 (identifying a Bayes question), 43 (binomial $P(X=r)$), 50 (probability distribution of a random variable), 51 (mean and variance).
- Batch XIII: J-M(XIII) 54 + J-A 43 + QB 22 new = 119 graded questions; High threshold round(0.091 x 119) = 11.
  High items: 4, 27 (multiplication theorem), 29, 38, 50, 51.
- Item 29 ("what independent means", master prompt 28) is High mainly because many questions use independence of separate tosses/draws as a further step (mapped as "other").

## Added items (why)
- 5 Bounds on probabilities ($0\le P\le1$, sum of exclusive events $\le1$, $P(A)+P(B)-1\le P(A\cap B)\le\min$): needed by J-I 6, J-M(XII) 36, J-A 30, DPP-3 5, 6; search_master found no prompt on bounds/range of probability in any chapter.
- 45 Least number of trials: J-A 11, 25, J-M(XII) 9, DPP-5 2, 12 (C-II 35 is Challenger); "minimum number of trials" has no match in the master.
- 46 Most probable number of successes: J-I 36, J-II 37; "most probable" / "mode" have no match in the master (Binomial Theorem's greatest-term prompts are about coefficients, not probabilities).

## Candidates not added because another chapter of the master covers them
- Derangements (J-A 19, J-M(XIII) 6 / at-least-3 correct T-shirts): covered in Permutations & Combinations / De-arrangement. Mapped to the classical definition (item 4).
- Counting words, functions, matrices, relations, integer solutions, distributions into boxes (many J-M questions): covered in Permutations & Combinations; mapped to item 4 (with item 9 where alike objects matter).
- Real / equal roots of a random quadratic (J-M(XII) 2, 34, J-M(XIII) 42, 43, 54, QB 221, 222, 252): covered in Quadratic Equation / nature of roots. Mapped to item 4.
- Unique solution of a random linear system / singular random matrix (J-M(XIII) 1, J-M(XII) 4, 28, QB 214, 219, 241): covered in Determinant / Matrices. Mapped to item 4 (or 50/51 for the variance of a determinant).
- "Toss until first success" (geometric distribution, $q^{k-1}p$, mean $1/p$): covered by the master's item 33 (infinite GP pattern in independent events) - that item's model answer states $q^{k-1}p$ and $P(X>k)=q^k$; mean questions go to item 51 with 34 as other. Not added as a separate item.
- Number of defectives drawn without replacement (hypergeometric): written into the model answer of item 50 (probability distribution), not a separate item.
- Mathematical expectation of a game (J-I 34, 35): theory sheet 10.3; mapped to mean (item 51), whose model answer includes $\sum p_iM_i$.
- search_master.py was run for: minimum number of trials, least number, most probable, greatest term, mode, derangement, dearrangement, expectation, range of probability, maximum value of probability, hypergeometric, geometric distribution, random variable, number of tosses, inclusion exclusion, units digit, maximum, minimum, greatest, least, bound, union, nature of roots, discriminant, distribution, mean, envelope, arrangement, real root.

## Questions with no matching item / outside the chapter
- J-M(XIII) 39: a differential-equation question printed in the probability J-M set (Jan 2024); mapped "-". It is still counted in the XIII graded total by the renderer.

## Items not used by any question
- Final numbers 26 (conditional probability of disjoint events), 36 (tree diagram for total probability), 37 (board method), 42 (meaning of X and q in BPD): never chosen as main or other, because the questions that use them were mapped to the item carrying the working method (conditional definition, total probability, binomial formula). Low = not tested in these questions.

## Uncertain decisions and notes
- The master PDF (jee-inputs/quick_review_all_chapters.pdf) is not in the repo, so the 50 prompts come from the saved OCR index; OCR noise ("Howto", "| How", "probablities", "Baye's", "\"C_ method" read as the ${}^nC_r$ method) was cleaned by hand. No prompt was rephrased in meaning.
- Question extraction: the sheets print "Exercise J-1 / J-2", so a patterns file was passed to extract_questions.py. J-II question 47 is printed without its full stop; a small wrapper around the skill's script (same output format) accepts a number without a full stop when it is the next in sequence. Counts were checked against the "Ans." lines of every exercise and the highest question numbers (J-I 41, J-II 49, J-M 45 / 54, J-A 43, C-I 21, C-II 36, DPP 13/15/15/12/13/15/17, QB 200-255). J-M(XII) and J-A have one extra "Ans." line each (a repeated answer line under one question), not an extra question.
- QB overlap: the 34 QB questions 202, 220-243, 247-255 are the J-M(XIII) questions 19, 41-48, 28, 30, 31, 34-37, 20-25, 1-3, 49-54, 38, 26, 27 (detect_overlaps.py, all "LIKELY SAME", checked by eye) and are counted once in batch XIII. No QB question equals a J-M(XII) question. QB 216 (3 defective oranges, 2 drawn) is similar to but different from J-M(XIII) 5 (4 apples drawn) and was kept.
- J-M(XIII) 6 is marked "Drop" in the sheet; it was still mapped (item 4 with complement) and counted as graded.
- Paragraph / comprehension questions (J-II 23-25, 26-28, 29-30; J-A 6-7, 8-9, 15-16, 19-20, 28-29, 37-38; C-II 23-25, 26-27, 28, 29-31, 32-33; DPP-6 9-11; DPP-7 14-16) were mapped from the question text; the shared paragraph is not in the extracted stem, so DPP-6 9 ("which event is most probable") and C-II 28 were mapped by best guess (binomial / conditional).
- Figure questions (J-I 21 butterfly on T-shaped board, J-M(XII) 15 and QB 212 chessboard squares, DPP-4 10 bird cages) were mapped from their wording.
- Match-the-column questions (J-II 48, 49; C-II 34-36) are mapped to the main concept of their first rows with the others as "other".
- Mapping judgement: questions that are mainly counting with a probability wrapper were given item 4 as main; questions on "repeat until" games were given item 34 (infinite GP); mean / variance of a hypergeometric count were given item 51 with 50 as other.
- Model answers come from the theory sheet; every example was checked with sympy or by enumeration (counting, complements, dice sums, inclusion-exclusion 21/50, conditional, Bayes 45/122, 1/2, 11/14, binomial 625/3888, least trials $n=4$, modes 49 and 50 for 99 tosses, units-digit formulas by enumeration for $n=1,2,3$, geometric 3/4).
- Source errors found: theory sheet Venn note writes $d=(1-P_2)(1-P_2)$ for "neither" of two independent events; the correct product $(1-P_1)(1-P_2)$ is used. Theory 10.5 prints the "2, 4, 6, 8" units-digit probability as $\frac{4^n-2^n}{5^n}$, equal to $\frac{8^n-4^n}{10^n}$ used here (checked).

## New Hindi terms
- See hindi_glossary_additions.md.
