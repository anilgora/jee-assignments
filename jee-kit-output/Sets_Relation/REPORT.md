# Sets & Relation: revision kit report

- Items in the Quick Review: 45
- Batch XII: 69 graded questions, High threshold 6 -> High 8, Medium 14, Low 23
  - High items (numbers): [3, 11, 31, 34, 37, 39, 40, 44]
- Batch XIII: 89 graded questions, High threshold 8 -> High 8, Medium 14, Low 23
  - High items (numbers): [3, 11, 31, 34, 37, 39, 40, 44]

## Added items
- 1: What is a set? What is its cardinal number?  [source: J-I:1]
- 2: How is a set written in roster form and in set-builder form?  [source: theory sheet (no question needs it directly)]
- 3: A set is given by an equation or inequality. How do you list or count its elements?  [source: J-I:2, J-I:7, J-I:10, J-I:12, QB:1, QB:7 (+11 more)]
- 4: Define finite, infinite, singleton and null sets.  [source: J-I:2, J-I:4, J-I:5, J-I:10]
- 5: What is the difference between equal sets and equivalent sets?  [source: theory sheet (no question needs it directly)]
- 6: What is a subset and a proper subset? How many subsets does a set with $n$ elements have?  [source: J-I:3, J-I:11, QB:1, QB:21, J-M(XIII):22, J-M(XIII):57]
- 9: How do you count subsets (or pairs of subsets) that satisfy a condition?  [source: QB:25, J-M(XIII):9, J-M(XIII):10, J-M(XIII):31, J-M(XIII):32, J-M(XIII):43 (+1 more)]
- 10: What are the universal set and the complement of a set?  [source: J-I:17, J-I:22, J-M(XIII):22]
- 11: Define union, intersection, difference and symmetric difference of two sets.  [source: J-I:7, J-I:8, J-I:12, J-I:22, QB:8, QB:35 (+8 more)]
- 12: When are two sets disjoint?  [source: J-I:15, J-I:16]
- 13: State the laws of algebra of sets.  [source: J-I:17, J-I:19, J-M(XIII):5]
- 14: State De Morgan's laws.  [source: J-I:17, J-I:18, J-I:19]
- 15: How do you read a statement in a Venn diagram?  [source: J-M(XIII):15]
- 16: Write the formulas for the number of elements in the union, difference and complement of two sets.  [source: J-I:15, J-I:16, J-I:18, J-I:21, QB:17, J-M(XIII):45 (+1 more)]
- 17: Write the formula for $n(A\cup B\cup C)$. How do you find "exactly one" and "exactly two"?  [source: J-I:14, QB:28, QB:31, J-M(XIII):49, J-M(XIII):62, J-M(XIII):72]
- 18: How do you find the greatest and least possible values of $n(A\cap B)$ or $n(A\cup B)$?  [source: J-I:13, J-I:20, QB:28, QB:31, J-M(XIII):20, J-M(XIII):62 (+1 more)]
- 19: How do you count (or add) the multiples of given numbers in a range?  [source: J-I:9, QB:17, J-M(XIII):12, J-M(XIII):19, J-M(XIII):26, J-M(XIII):45 (+1 more)]
- 23: Which identities hold for the cartesian product?  [source: J-I:23, J-I:24, J-I:25, J-M(XIII):10, J-M(XIII):46]
- 30: How many relations are there from A to B, and on A?  [source: J-I:28]
- 31: A relation is given by a rule. How do you count its elements?  [source: QB:2, QB:3, QB:4, QB:5, QB:6, QB:16 (+16 more)]
- 32: What are the void relation and the universal relation? Which properties do they have?  [source: J-II:2]
- 43: How many reflexive, symmetric and equivalence relations can be defined on a set of $n$ elements?  [source: QB:9, QB:26, QB:27, QB:32, J-M(XIII):53, J-M(XIII):63]
- 44: What is the least number of pairs to add so that a relation becomes reflexive / symmetric / transitive / an equivalence?  [source: J-I:35, J-I:36, QB:3, QB:4, QB:5, QB:10 (+14 more)]

## Rephrased items

## Questions with no matching item

## Question Bank questions counted once (overlap with a batch JM set)
- Batch XIII: QB [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35]

## Validation warnings
- none

## Run details (added by hand)

Built on 2026-10-30 on the owner's direct request ("There is one chapter sets and relation. I want you to do it"), although the chapter is not in the skill's master_index.json.

### Input files used (unchanged)
- Theory: `chapters/01_Sets_&_Relation/THEORY SHEET.pdf` (15 pages)
- XII sheet: `chapters/01_Sets_&_Relation/XII.pdf` (67 pages; Key Concept + Exercise -I, -II, -III)
- XIII sheet: `chapters/01_Sets_&_Relation/XIII.pdf` (69 pages; Exercise -I, -II, -III)
- Question Bank: `chapters/01_Sets_&_Relation/QB.pdf` (23 pages, "Sets and Relations" from the Differential Calculus JEE Main bank)
- DPP: none in the folder (optional, skipped)

### Exercise names
The sheets are titled "Exercise -I / -II / -III" instead of J-I / J-II / J-M. Custom patterns were given to extract_questions.py and the exercises are keyed as follows (numbers kept exactly as printed):
- Exercise -I (39 Q, same in XII and XIII; checked stem by stem) -> `J-I`
- Exercise -II (17 Q, same in XII and XIII) -> `J-II`
- Exercise -III = previous-year JEE Main / AIEEE questions -> `J-M(XII)` (34 Q, 2004 to July 2022) and `J-M(XIII)` (73 Q; Q1-34 identical to XII, Q35-73 are Jan 2023 to April 2024)
- No JEE Advanced exercise and no Challenger exercise in either sheet, so J-A, C-I, C-II are absent. Graded sources are therefore J-M + QB only.
- QB: 35 questions. Total indexed: 198 (39 + 17 + 34 + 73 + 35).

### Grading
- XII: 34 JM + 35 QB = 69 graded questions (no overlap), High threshold max(2, round(0.091 x 69)) = 6.
- XIII: 73 JM + 35 QB - 19 overlaps = 89 graded questions, High threshold 8.
- QB overlap with J-M(XIII), checked by eye: QB 15-24 = JM 67, 68, 69, 70, 71, 56, 57, 58, 59, 60; QB 27 = JM 53; QB 28-35 = JM 72, 73, 61, 62, 63, 64, 65, 66. QB 26 ("at most 6 elements including (1,2)") is NOT the same as JM 53, although the detector called it "possible". No QB question is in J-M(XII).

### Prompt list (master Quick Review) - uncertain, please check
- The saved master index has no "Sets & Relation" chapter. Its Sets & Relations prompts were filed by the OCR split inside "Vector 3D" as prompts #31-52 (the Vector 3D kit already left them out for that reason). Those 22 prompts are used here with their master numbers (`o` = 31..52) and master headings: Cartesian Product of two sets, Relation, Types of a relation, Inverse of a relation.
- Prompts 31 ("Define superset") and 32 ("Power set") sat under the garbled heading "Coordinate System in 3D"; they are placed under the heading "Subsets and Power Set" here.
- The master's Sets prompts before #31 (sets, types of sets, subsets, operations, Venn diagrams, counting formulas) are missing from the index, most likely on the page the split lost. They were rebuilt as 23 added items (tag "added") under headings taken from the theory sheet. **The wording of the added items is mine, not the master's.** To replace them with the master's own prompts, put `quick_review_all_chapters.pdf` in `jee-inputs/` and re-split.
- jee-inputs/master_index.json was NOT created or changed (that would change the prompt source for all chapters); Sets & Relation remains outside the automatic chapter order.

### Cross-chapter check (search_master.py)
- Venn diagrams / union formula: Probability > Venn Diagram (#16-18) covers the probability version. The set-count items (16-18) were still added because they are this chapter's own baseline (lost from the index), not new concepts. Uncertain decision.
- Bell numbers: covered in Permutations & Combinations > Extra Reading Material #9, so no separate item; they are mentioned as one line in item 43.
- Modulus equations / inequalities (JM 11, 17, 22, 23, 40): covered in Logarithm > Modulus Equation; no new item. These questions are mapped to item 3 ("set given by an equation or inequality").
- "Numbers divisible by 3/4" in P&C is about forming numbers from digits; counting multiples in a range ([N/k], lcm) was not found anywhere, so item 19 was added.
- Not found anywhere and added: null/singleton/roster/set-builder, De Morgan, symmetric difference, disjoint sets, counting relations, least pairs to add (closures).

### Mapping decisions
- "Classify the relation" questions (reflexive / symmetric / transitive / equivalence) are mapped main = 49 (equivalence relation) with also-used = 43, 46, 48 (the three check methods). This is why 43, 46, 48, 49 are all High. The definition items 42, 45, 47 are therefore Low.
- JM 8 and 14 (similar matrices) and JM 4 / QB 11 (relations as subsets of R x R) are kept in this chapter (equivalence relation) - the matrix / coordinate part is routine.
- JM 33 (sums of 4, 6, 9) and JM 34 / QB 1 / QB 8 (integer points in regions) -> item 3 (set given by a condition). JM 57 / QB 21 (2^m - 2^n = 56, then a distance) -> item 6.
- Items with no question at all (Low = "not tested in these questions"): 2 (How is a set written in roster form and ); 5 (What is the difference between equal set); 7 (Define superset.); 20 (How is the cartesian product of sets A a); 26 (What do you mean by pre-image and image ); 28 (What is the co-domain of a relation?); 33 (Define reflexive relation.); 35 (Define identity relation.); 36 (Define symmetric relation.); 38 (Define transitive relation.); 41 (Define anti-symmetric relation.); 45 (What is inverse of a relation?).
- No question was left unmapped (`-`).

### Source errors found
- XIII Exercise -III Q53 (JEE Main April 2023): the sheet prints Ans. 4. The correct answer is **3** (brute-force check of all 512 relations on {1,2,3}; NTA's official answer is also 3, as printed in the theory sheet Ex.9 and QB 27). The sheet's R4 is the symmetric full relation and should not be counted.
- Theory sheet Section 11, Ex.9: the listed R2 and R3 omit the forced pair (1,3); the count 3 is right.
- XIII Exercise -III Q49: Ans. printed as "21", which is option (D); confirmed (exactly two = 21).
- Printed answers were not all re-solved. Only the answers used in model-answer examples were checked (by direct computation).

### Hindi
New terms are in `hindi_glossary_additions.md`.

### Limits
Mapping is a judgement call. The text extraction loses symbols (∈, ⊂, ∪, ∩), so stems in Question_Mapping.xlsx look garbled. Word equations are pandoc-converted OMML (schema-valid; preview only in Word).
