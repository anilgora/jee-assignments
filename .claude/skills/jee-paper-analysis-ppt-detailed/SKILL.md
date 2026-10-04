---
name: "jee-paper-analysis-ppt-detailed"
description: Build the user's "Paper Analysis" PowerPoint (title slide, section dividers, question slides with calibrated difficulty level, difficulty table, summary, difficulty profile, comparison with JEE Advanced papers) with COMPLETE step-by-step solutions copied from the paper's PDF (verified, and corrected where the PDF is wrong) instead of concise ones, plus optional "Alternate Solution" slides and "Useful Result / Pattern" slides for the specific question numbers the user asks for. Produces a content JSON and a Python script the user runs from the terminal. Use whenever the user wants the paper-analysis PPT with detailed, complete or full solutions, or with alternate/elegant solutions, shortcuts, results or patterns for chosen questions. For the standard deck with concise solutions use jee-paper-analysis-ppt instead.
---

# JEE Paper Analysis PPT - detailed solutions edition

Same deck, same design and same workflow as **jee-paper-analysis-ppt**, with exactly two differences
in the solution part:

1. **Complete solution.** The primary solution contains *every step of the PDF's working*, not a
   condensed version. If the PDF's solution is wrong it is corrected; if the PDF has none, one is written.
2. **Alternate solutions, only on request.** For the question numbers the user lists, an elegant
   alternate method follows the primary solution on slides tagged **Alternate Solution**, then a
   **Useful Result / Pattern** slide. If the user gives no list, there are no alternate solutions
   and no result/pattern slides at all.

Everything else - difficulty rating with the calibrated skill, 24 pt Arial text, key-idea strip,
level badges, native editable equations, section dividers, difficulty table, summary, profile
chart, comparison slide - is identical, because it is the same script with the solution
renderer extended.

Always deliver: the content JSON, the built `.pptx` (build it here too) and `scripts/make_ppt.py`
(tell the user it is the detailed edition; if they already have the concise `make_ppt.py`, offer
it under the name `make_ppt_detailed.py` so the two do not overwrite each other).

## Files in this skill

- `scripts/make_ppt.py` - deck builder (`python-pptx` + `pypandoc_binary`). Do not restyle per paper.
- `references/content_schema.md` - JSON schema, type labels, LaTeX rules, concept rule and the
  rules for complete solutions, alternates and results. **Read it before writing any JSON.**
- `references/example_PRT_06_detailed_content.json` - a working excerpt (Q4, Q10, Q11 of PRT 06)
  showing a complete solution, two alternates and a results slide. It is an excerpt, not a whole paper.

## Inputs

1. The question paper PDF **with solutions** (the PDF's solutions are the source of the primary solution).
2. The blueprint / concept Excel (chapter, Concept1, Concept 2, Q Type; ignore its Difficulty column).
3. **Optionally a list of question numbers for alternates**, e.g. "alternate solutions for Q3, Q7, Q12".
   Numbers are the continuous deck numbers 1..N (the same as `q_no`). If a number is outside the
   paper, ask. If no list is given, do not produce alternates and do not ask for one - just mention
   in the final reply that they can name questions to get alternates.

- `references/test_matrix_content.json` - regression sample with matrices, determinants and `cases`. After any change to the
  equation code, build it and open the result in PowerPoint: there must be no "repair" prompt and no empty slide.

## Workflow

### 1-2. Read the inputs and rate difficulty
Exactly as in jee-paper-analysis-ppt: read the PDF with the file-reading skills (rasterize pages
whenever the text layer garbles maths), number questions continuously, rate every question with the
**jee-advanced-difficulty-calibrated** skill (adjusted level, including the equivalence-relation
adjustment and the 2.5 floor for multi-concept one-or-more-correct questions), and apply the
concepts rule from the schema.

### 3. Primary solution - complete, verified, corrected if needed
For **every** question:

1. **Copy the PDF's working in full.** Keep its method, its order and its intermediate numbers.
   One step per bullet; do not summarise, merge steps or drop "obvious" lines. A bullet may be
   longer than in the concise edition (up to about 250 characters of converted text); a question
   normally ends up with 6-15 bullets. Rewrite only the notation, into `$...$` LaTeX.
2. **Verify every step independently** - re-derive it, and check the final answer by computation
   wherever possible (sympy, brute-force counting, numerical evaluation). Do not assume the PDF is right.
3. **Decide the source** and set `solution_source`:
   - `pdf` - the working is correct; it is reproduced as it is.
   - `corrected` - the working (or an intermediate value, a sign, a case, a final answer) was wrong.
     Fix it with the **smallest change that makes it correct**, keeping the PDF's structure, and write
     `correction_note`: which step was wrong, what the PDF said, what is correct. The note goes into
     the speaker notes of the first solution slide; the slide itself shows only the corrected working.
   - `written` - the PDF has no usable solution for that question (missing, cut off, unreadable):
     write a complete solution yourself.
   If the PDF's *answer key* disagrees with the correct answer, keep the correct answer in `answer`
   and tell the user which question and why.
4. Write the `key_idea` (decisive step) exactly as in the concise edition.

### 4. Alternate solutions - only for the requested numbers
For each requested question add `alternate_solutions` (a list; usually one, two at most unless asked):

- **Genuinely different and elegant.** A different idea - symmetry, geometry instead of algebra,
  a substitution, an identity, a counting bijection, a limiting case, a shortcut formula - not the same
  steps reworded or reordered. Prefer methods that are shorter, avoid heavy computation, or show
  why the answer is what it is.
- **Complete.** Still a full chain of reasoning, one step per bullet, ending at the same answer
  (the deck shows "Same answer" under it).
- **Verified.** Check that it reaches the same answer, numerically if possible; check that each general
  claim it uses is true for the conditions of the question.
- Give each alternate a one-sentence `idea` (shown in an amber "Idea" strip).
- **If no genuinely different elegant method exists, say so** in the final reply instead of
  inventing one (you may leave the field out for that question). Do not pad.

### 5. Useful result / pattern - only for the requested numbers
For each requested question add `useful_results`, 2-5 bullets of **general** facts that help with this
kind of question: formulas, identities, standard patterns, recognition cues, a generalisation of what the
question shows, and (where it adds value) the instance in this question. Rules: correct and stated with
their conditions; not a restatement of the solution; verified (for formulas, check one numerical case).
They appear on one slide tagged **Useful Result / Pattern** after the alternates.

### 6. Build and check
```bash
pip install python-pptx pypandoc_binary --break-system-packages    # if needed in the sandbox
python scripts/make_ppt.py /mnt/user-data/outputs/<Paper>_content.json -o /mnt/user-data/outputs/<Paper>_Analysis.pptx
```
Read every note the script prints. It warns about: missing or invalid `solution_source`; `corrected`
without a `correction_note`; a primary solution with fewer than 4 bullets (probably not complete);
LaTeX that did not convert or was kept as plain text for PowerPoint-safety (the note gives the reason); missing answers or key ideas. Fix and rebuild. Then render the deck and look
at the longest solution slides and at one alternate and one results slide.

### 7. Deliver and report
Present the JSON, the deck and `make_ppt.py`. In the chat reply include:
- the difficulty index and spread (as in the concise edition);
- **a short list of questions whose PDF solution was `corrected` or `written`**, one line each on what
  changed - this is the most important thing for the user to see;
- any question where the paper's answer key looked wrong;
- which questions got alternates / results, and any requested question for which you found no elegant
  alternate;
- the terminal command, first time only.

## Order of slides for a question (what the script produces)
1. Question slide (level badge, question box, info box).
2. Primary solution slides: amber **Key idea** strip, bullets (at most 6 per slide, spread evenly),
   green **Correct Answer** box on the last slide. Speaker notes on the first slide state the source
   (pdf / corrected + what changed / written).
3. For each alternate: slides with the header tag **Alternate Solution** (numbered when there are
   several), amber **Idea** strip, bullets, green **Same answer** box.
4. One **Useful Result / Pattern** slide set (blue tag), bullets only.

The paper-level slides (section dividers, difficulty table, summary, difficulty profile, optional AIR
marks, comparison with JEE Advanced 2021-2026) are unchanged. Defaults for the level descriptions are
the same as in the concise edition.
