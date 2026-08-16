# Difficulty Rubric

Contents:
1. The reference student
2. The five dimensions
3. Composite to level mapping
4. Level descriptors
5. Override rules
6. Question-type adjustments
7. Anchor examples
8. Justification template

---

## 1. The reference student

Every score is relative to one imagined person, not to you and not to a topper:

> A sincere Class 12 student in a good coaching programme, targeting JEE Advanced. Knows every
> formula in the syllabus. Has worked through several thousand problems. Can execute standard
> techniques reliably. Does *not* independently invent non-standard constructions. Working under
> time pressure.

When a question is hard for this student it is hard, regardless of how obvious the route looks to
you. Model-perceived ease is the single largest source of error in this task.

---

## 2. The five dimensions

Score each from 1 to 5. Fractions are not used - pick the nearer integer.

### C - Conceptual depth
How far past the plain statement of a formula must the student reason?

| C | Meaning |
|---|---|
| 1 | Direct substitution into a memorised formula. |
| 2 | Standard formula plus one routine rearrangement. |
| 3 | Requires understanding *why* a result holds, or choosing between several applicable results. |
| 4 | Rests on a property most students know but rarely use actively (e.g. behaviour of a function at the boundary of its domain, the geometric meaning of a determinant). |
| 5 | Rests on a deep or rarely-taught property; the student must reconstruct theory, not recall it. |

### L - Concept linkage
How many distinct ideas must be held together?

| L | Meaning |
|---|---|
| 1 | One concept, one chapter. |
| 2 | Two closely related concepts from the same chapter. |
| 3 | Two chapters combined in a familiar pairing (conics + straight lines, calculus + inequalities). |
| 4 | Three or more concepts, or an unfamiliar cross-chapter pairing. |
| 5 | An unusual synthesis - the student must notice that a tool from a distant chapter applies at all. |

### M - Manipulation load
Volume and delicacy of the algebra, calculus, or arithmetic.

| M | Meaning |
|---|---|
| 1 | A line or two. |
| 2 | Short, clean working; low chance of slips. |
| 3 | Sustained working of roughly 8-15 lines; a slip is plausible. |
| 4 | Long or delicate manipulation - messy surds, heavy simplification, careful case work. |
| 5 | Very heavy: extended case analysis, large systems, or algebra where one sign error destroys everything. |

### I - Insight required
Is there a step you either see or you don't?

| I | Meaning |
|---|---|
| 1 | No insight - the method is announced by the question. |
| 2 | The method is standard for this question shape; recognition is automatic with practice. |
| 3 | One non-obvious but well-drilled move (a standard substitution, adding and subtracting a term, a clever pairing). |
| 4 | A genuinely non-obvious move that many prepared students will miss under time pressure. |
| 5 | Requires constructing an idea rather than selecting one - the hallmark of Olympiad problems. |

This is the dimension that separates *tedious* from *hard*. Weight your final judgement toward it.

### T - Traps and precision
How much does the question punish carelessness?

| T | Meaning |
|---|---|
| 1 | No traps. |
| 2 | One routine check (domain, sign of a root). |
| 3 | A real trap that a hurried student falls into - extraneous roots, missing a case, ignoring a boundary. |
| 4 | Several interacting traps, or a deliberately misleading setup. |
| 5 | The question is essentially built out of its edge cases. |

---

## 3. Composite to level mapping

Composite = (C + L + M + I + T) / 5, rounded to one decimal.

| Composite | Level |
|---|---|
| 1.0 - 1.5 | 0 |
| 1.6 - 2.2 | 1 |
| 2.3 - 2.9 | 2 |
| 3.0 - 3.7 | 3 |
| 3.8 - 4.4 | 4 |
| 4.5 - 5.0 | 5 |

The composite is a starting point, not a verdict. Apply the override rules in section 5, then
sanity-check against the expected solve time below. When the composite and the time estimate
disagree by more than one level, trust the time estimate and revisit the dimension scores - the
scores are usually where the mistake is.

| Level | Expected solve time for the reference student |
|---|---|
| 0 | Under 2 minutes |
| 1 | 2 - 4 minutes |
| 2 | 4 - 7 minutes |
| 3 | 7 - 12 minutes |
| 4 | 12 - 20 minutes |
| 5 | 20+ minutes, or the student does not find the route at all |

---

## 4. Level descriptors

Use the exact label strings from `taxonomy.md` when writing the Blueprint sheet.

**Level 0 - Easier than JEE Main.** Single formula, direct substitution, no traps. Board-exam or
warm-up material. A prepared student answers on sight.

**Level 1 - JEE Main.** Standard, procedural, single-concept or a familiar two-step chain. Clear
route from the first reading. This is where the bulk of routine practice sits.

**Level 2 - A little easier than JEE Advanced.** One conceptual trap *or* one moderate calculation
beyond Main level. The route is still recognisable; the student must be careful rather than
inventive.

**Level 3 - JEE Advanced (default).** Multi-concept linking, substantial manipulation, and
analytical endurance. The student must choose an approach rather than be handed one. This is the
centre of gravity for a genuine Advanced paper.

**Level 4 - A little more difficult than JEE Advanced.** High abstraction or a key insight that a
majority of well-prepared students will miss in the exam hall. Often combines an unusual pairing
of chapters with a demanding execution.

**Level 5 - Very difficult.** RMO/INMO-grade reasoning wrapped in an objective format. Requires
constructing a non-standard argument. Rare in coaching assignments - if you are assigning several
of these, re-check them against Level 4.

---

## 5. Override rules

These beat the composite arithmetic.

1. **Grind is not difficulty.** If M is 4 or 5 but I is 2 or less, cap at Level 3. Long boring
   algebra with an obvious route is a stamina test, not a hard problem.
2. **Insight is difficulty.** If I is 5 and the route is genuinely non-standard, assign Level 4 or
   5 even when M and L are low. Short, brutal problems exist.
3. **Level 5 requires I of at least 4.** No exceptions. Without it, the ceiling is Level 4.
4. **Level 0 and 1 require L of at most 2.** A question spanning two chapters is at minimum
   Level 2, however easy each piece is.
5. **A single hidden case can lift a level.** If the question is routine but silently requires
   splitting into cases the student will not think of, add one level.
6. **Answer format never changes difficulty by more than one level**, and only via the adjustments
   in section 6.
7. **Rate what is asked, not what is nearby.** A question set in an intimidating context but
   answered by one line is easy. Presentation is not difficulty.

---

## 6. Question-type adjustments

Apply after the composite, and never more than +1 in total.

- **One or More Than One Correct** - +0.5 composite. Every option must be verified independently,
  and partial marking punishes uncertainty. Add the full +1 if the options are near-misses of each
  other.
- **Matrix Match** - +0.5 composite when the list items are genuinely different sub-problems, since
  the student is effectively solving four small problems.
- **Numerical Type** - +0.5 composite when the arithmetic is heavy, because there is no option list
  to check against and no way to back-solve.
- **Integer Type (0 to 9)** - no adjustment, and consider -0.5 if the tiny answer range lets the
  student verify or guess-check cheaply.
- **Single Correct** - no adjustment, but consider -0.5 if the options can be eliminated by
  substitution or a limiting case without solving the problem properly. Note this in the
  justification; it is useful feedback on paper quality.
- **Paragraph based** - rate each sub-question independently. A shared passage only raises
  difficulty if the passage itself is hard to parse; in that case add +0.5 to the first
  sub-question only.

---

## 7. Anchor examples

Calibrate against these before rating.

**Level 0** - "If the roots of `x^2 - 5x + 6 = 0` are a and b, find a + b."
C1 L1 M1 I1 T1, composite 1.0. Direct formula recall.

**Level 1** - "Find the equation of the tangent to `y = x^3 - 2x` at the point where `x = 1`."
C2 L2 M2 I1 T1, composite 1.6. Fully procedural: differentiate, evaluate, point-slope form.

**Level 2** - "Find the number of real solutions of `|x - 1| + |x - 3| = 2x`."
C2 L2 M3 I3 T4, composite 2.8. The method is standard but the case boundaries are the whole point,
and students routinely lose the case where no solution exists.

**Level 3** - "Let `f` be twice differentiable with `f(0) = f(1) = 0` and `f''(x) + 2f'(x) > 0` on
`(0,1)`. Determine the sign of `f` on `(0,1)`."
C4 L3 M2 I4 T3, composite 3.2. The student must think of multiplying by an integrating factor to
make the hypothesis usable - a standard trick, but only for those who have met it.

**Level 4** - A locus problem where the point moves on a conic, the condition involves the angle
subtended at a variable focal chord, and the answer requires eliminating two parameters through a
non-obvious symmetric substitution.
C4 L4 M4 I4 T3, composite 3.8. Cross-chapter, long, and the elimination is the hard part.

**Level 5** - "Find all polynomials `P` with real coefficients such that
`P(x)P(x+1) = P(x^2 + x + 1)` for all real x, and report the degree of the unique non-constant
solution."
C5 L5 M3 I5 T3, composite 4.2 but overridden upward by rule 2. Functional equations over
polynomials with a root-mapping argument - INMO territory, translated into a numerical answer.

Note the last two: the composite alone would have put both at Level 4. The override rules did the
real work. Expect this often.

---

## 8. Justification template

Two to four sentences, in this order:

1. What the question actually demands - name the concepts, not the chapter.
2. The specific step that determines the level - the insight, the trap, or the calculation.
3. Why it is not the level above or below, when the call is close.

Name concrete mathematics. "Requires the student to see that the constraint forces the discriminant
to be a perfect square" is useful. "Tests conceptual clarity" is not.
