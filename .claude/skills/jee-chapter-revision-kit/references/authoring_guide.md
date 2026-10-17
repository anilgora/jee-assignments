# Authoring guide (what Claude writes into the spec)

## Quick Review items
- One item per numbered prompt of the user's Quick Review list; keep its heading and order. Prompts are tests of understanding ("Can you ...?"), the item adds the model answer.
- Model answer = short and printing-friendly: 1-3 lines of the rule/formula, then (when useful) one `Ex:` line with a small worked example. Source = the theory sheet; if the sheet is wrong or garbled, correct it and note it in the report.
- Every number in an example is checked with sympy before it goes in. Never copy garbled PDF maths.
- Rephrase only prompts that are ambiguous (tag `rephrased`, keep `o`). Say in the report which and why.
- A line that is only a formula can be a plain string (shown centred as a display equation); otherwise give `[English, Hindi]`.

## Mapping questions to items
- `main` = the item the question is mainly about; `others` = items the solution genuinely needs as a further step. Do not pad `others`.
- Consistent choices: "one root common" -> main = the one-common-root condition, other = elimination method; recurrences S_n -> Newton item; "range of a Q/Q" -> the Q/Q range item; etc.
- Use the section header of the exercise/DPP as a hint, but read the stem. Figure or paragraph questions: look at the page image.
- DPP sets are often one concept repeated (e.g. 40 rational inequalities) - map them all to that item; check a few pages visually for modulus / double inequalities.
- Challenger (C-I, C-II), J-I, J-II and DPP are mapped too (they show in the practice map) even though they are not graded.
- `-` for a question outside the chapter (logs, linear systems, word problems) or with an empty stem; the report lists them.

## Coverage check (exclude Challenger)
Go through J-I, J-II, J-M (both batches), J-A, DPP, QB. If a method or fact is needed and no item covers it, add an item (tag `added`, `src` = question ids) under the matching heading, else in Miscellaneous.
A one-off trick that appears once is still added if it is a standard JEE method (e.g. pairing four linear factors). Examples from Quadratic Equation: solution set of one inequality inside another;
equation homogeneous in two expressions; product of four linear factors; composite p(p(x)); integer roots; modulus of a quadratic; positive-definite form; biquadratic location of roots.

## Short notes (spec.notes)
- One section per Quick Review heading (merge small neighbours; about 15-18 sections). Colour per section from the fixed list.
- Blocks, in this order when present: `formula` (centred equations), `points` (one idea per line), `steps` (numbered), `watch` (common mistakes). No worked examples.
- Keep all key points the chapter needs; one short line each; the last section is a "common mistakes" checklist (use `steps`).

## Formula sheet (spec.formula)
- Pure formulas with a 2-5 word label: `"Sum: $\alpha+\beta=-\dfrac ba$"`. Group by topic. No explanations, no examples. Include the conditions tables (special cases, location of roots) as one line each.

## Mind map (spec.mindmap)
- Branch = one Quick Review heading (merged to <= 16). 2-4 leaves, each one line: the key formula or the method in a few words.

## Method flowcharts (spec.flowcharts)
- 5-8 charts, each answering "which method do I use?" for a type of problem (conditions on coefficients, questions on alpha-beta, non-standard equations, common roots, range, location of roots, inequalities...).
- A chart is a chain of recognisable features of the question ("It contains a modulus?") -> the method (<= 2 short lines), ending with an "otherwise" line. At most ~8 steps per chart (the page scales to fit).

## Hindi
- Use `references/hindi_glossary.md`. Same formulas; Hindi sentences; Devanagari digits are not used. Keep "JM, JA, DPP, QB" in Latin. New terms go to `hindi_glossary_additions.md` in the output folder.

## Things that went wrong before (check for them)
- Answers printed in the PDFs can contradict their own solutions; recompute.
- Strict vs non-strict inequalities in printed answers; "equal roots" vs "distinct roots".
- Minus signs lost in the PDF text (e.g. e^{4x}+8e^{3x}+13e^{2x}-8e^{x}+1): compare with the page image when an answer does not match.
