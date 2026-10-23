# Choosing concepts: natural synergy, not random

Concepts come only from the `Concepts` sheet of `input_config.xlsx` (`chapter_concepts.json` lists the ones
for the paper's chapters). Pairing is decided from your knowledge of real JEE Main and JEE Advanced papers
and public question banks. It is never random.

## Rules (user's instructions, 18-Oct-2026)
0. **Both concepts come from the Concepts sheet** (text copied exactly). The pairing itself comes from your knowledge
   of JEE Main and Advanced papers, never from random choice.
1. **Concept 1 is the main concept.** It belongs to the slot's chapter (the Chapter column). The question is
   "about" Concept 1; the other concept(s) support or extend it.
2. **Concept 2 (and 3) must come from a chapter that is in the paper's Chapters sheet.** The old "earlier
   chapter only" rule is dropped. A partner may come from any of those chapters, in any order.
3. **Prefer concepts that matter.** Among the sheet's concepts, favour those that recur in JEE Main / Advanced
   papers (standard, high-frequency ideas) over rare or purely technical ones. Use the rarer ones only
   when they are the natural link. Do not use a concept twice in one paper (the script enforces this).
4. **Chapter classification.** Vector and 3D are one chapter. Matrices and Determinants are different
   chapters. A DE or Area question that needs an integration technique counts as different chapters.
5. **Same chapter** means every extra concept sits in Concept 1's chapter. **Different chapters** means at
   least one extra concept sits in another chapter.

## Patterns
**JEE Main** (`--pattern main`): one or two concepts per question. Target 20% single / 40% same chapter /
40% different chapters. Rounding is your judgement (each within +-1 of target). Choose which slots are
single-concept to suit the type and level (an easy L1 question or an INT question is a natural single-concept slot; an
L4 question rarely is). Two concepts only, never three.

**JEE Advanced** (`--pattern advanced`): every question is multi-concept, two or three concepts, and **at least two
questions must have three concepts**. **At least 40% of the questions must mix different chapters** (the script
enforces both); the rest may be same-chapter. Three-concept questions need a real chain of ideas, so give them to
the higher-level or MCQ / Paragraph slots.
The paper should feel like an actual Advanced paper: the second and third concepts are real parts of
the solution path (an extra lemma, a constraint, a different representation), never decoration.

## What "natural" means
A pair is natural when a competent setter could write one clean problem in which both are needed and the
link is part of the idea, the way it happens in real papers. Typical links (examples, not a closed list):
- a curve found by solving a differential equation, then its area / tangent / normal;
- a definite integral whose evaluation needs a symmetry property or a limit of a sum;
- a function defined by an integral, then its monotonicity, extrema or a functional equation;
- a quadratic whose roots form an AP/GP, or whose root locations are given by a graph condition;
- binomial coefficients combined with complex numbers (roots of unity) or with counting;
- a conic with a line or circle (tangent, chord, normal, common tangent) or with vectors/locus;
- a determinant or matrix condition that settles the consistency of a linear system;
- probability built on a counting argument; a recurrence/progression feeding a limit or a sum.
Look for the "same object seen two ways" (a curve as a DE solution and as an area boundary).

## Earlier papers of the same phase
When the user supplies earlier blueprints (oldest first), fresh concepts are used first. If a chapter has no fresh
concept left, reuse the **earliest-used** ones first (`reuse_order.json`). If a chapter has more questions than
concepts, a concept may repeat within the paper. Whenever you reuse, do not repeat the same *combination* of concepts
(pair) used before: change the partner concept, and keep the link natural. Also avoid repeating the same link pattern.
Say in the reply which concepts were reused.

## Avoid
- **Glued pairs:** two unrelated tasks welded into one stem ("find X, then separately Y").
- **Shell pairs:** Concept 2 is only a routine computation wrapped around Concept 1.
- Pairs whose link needs a third idea outside the sheet, or a level above the slot's difficulty.
- The same pair (or the same link pattern) in two questions of one paper.
- Cross-chapter partners that force an unnatural link just to meet the percentage. If a chapter in the
  paper has no natural partner among the paper's chapters, use a same-chapter pair or a single concept
  and say so in the reply.

## Link Note column
One line per question: what the link is, for example "Solve the DE for the curve, then find the area it
encloses with the axes." You write it; the user reads it during blueprint review.
