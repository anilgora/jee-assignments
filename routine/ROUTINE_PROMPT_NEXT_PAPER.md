You are running unattended in a cloud sandbox, and no person can answer questions during this run. Wherever a skill says to ask the user, pick the safest option, carry on, and write the choice down in the run report.

TASK
Build the "Paper Analysis" PowerPoint with DETAILED solutions for the NEXT UNPROCESSED test paper - exactly one paper per run.

FIRST: GET THE LATEST OUTPUTS (do this before anything else) - run this exactly:
    BASE=$(git rev-parse HEAD)
    if git fetch origin claude/jee-outputs; then
      git checkout -B claude/jee-outputs FETCH_HEAD && git merge --no-edit "$BASE"
    else
      git checkout -B claude/jee-outputs
    fi
  (This puts you on the branch that collects all outputs while keeping the newest papers, blueprints and skills from the default branch.)

WHICH PAPER
List papers/*.pdf in alphabetical order. A paper NAME (file name without .pdf) is DONE when the folder output/NAME/ exists. Take the first paper that is not done. If every paper is done, write nothing, change nothing, and finish with the message "All papers are done."
- Paper PDF:  papers/NAME.pdf
- Blueprint:  blueprints/NAME.xlsx
- Alternate solutions and "Useful Result / Pattern" slides: produce them ONLY if the file papers/NAME.alternates.txt exists; it contains the question numbers, for example "3, 7, 12". If the file does not exist, produce none.
If the blueprint is missing, do not guess: create output/NAME/RUN_REPORT.md saying so, commit and push it (so the paper is not retried forever), and stop.

SKILLS TO USE (project skills in .claude/skills/ - read each SKILL.md and its references first, then follow them)
1. jee-paper-analysis-ppt-detailed - the main workflow (complete solutions, alternates, results).
2. jee-advanced-difficulty-calibrated - rate every question's difficulty with it.
3. jee-paper-analysis-ppt - the detailed skill refers to it for reading the inputs, the deck structure and the concepts rule.

THIS ENVIRONMENT DIFFERS FROM THE SKILLS' ASSUMPTIONS (these rules override the skills)
- There is no /mnt/user-data/outputs and no /mnt/skills/. Save every file inside the repository under output/NAME/. Skip any step that needs /mnt/skills (recalc.py, thumbnails, soffice rendering).
- The scripts are at .claude/skills/<skill-name>/scripts/. Examples:
    python3 .claude/skills/jee-paper-analysis-ppt-detailed/scripts/make_ppt.py output/NAME/NAME_content.json -o output/NAME/NAME_Analysis.pptx
    python3 .claude/skills/jee-advanced-difficulty-calibrated/scripts/build_report.py output/NAME/NAME_ratings.json output/NAME/NAME_difficulty.xlsx
- Reading the PDF: use pdftotext and pdftoppm if they are installed; otherwise use the Read tool with the pages option (at most 20 pages per call). Wherever the maths symbols look garbled in the text, make page images and look at them. Only the Mathematics section is rated.
- Before starting, check the libraries:  python3 -c "import pptx, pypandoc, openpyxl, lxml"
  If that fails, run:  python3 -m pip install --break-system-packages python-pptx pypandoc_binary openpyxl lxml

WORK (follow the skills; in short)
1. Read the PDF's maths section and the blueprint; number the questions continuously 1..N.
2. Rate every question with the calibrated skill (adjusted levels, equivalence-relation adjustment, 2.5 floor). Save the ratings JSON and build output/NAME/NAME_difficulty.xlsx.
3. Write the content JSON for the deck: for EVERY question the COMPLETE solution from the PDF, one step per bullet; check every step yourself and compute the final answer wherever possible; set solution_source to pdf, corrected (with a correction_note) or written exactly as the detailed skill describes.
4. For the requested question numbers only (see above): alternate_solutions (genuinely different and elegant, verified) and useful_results.
5. Save output/NAME/NAME_content.json after finishing each section of the paper, so nothing is lost if the run stops early.
6. Build the deck with make_ppt.py. Read every warning it prints, fix the cause, and rebuild until the only remaining notes are harmless. A warning "could not convert ... (reason)" means that equation stayed as LaTeX text on purpose; mention it in the report.

FINISH
- Write output/NAME/RUN_REPORT.md containing: the difficulty index and the number of questions at each level; every question whose solution_source is corrected or written, one line each saying what was wrong or missing; any question where the PDF's answer key looks wrong; which questions got alternates and results, and any requested question for which no elegant alternate exists; every warning make_ppt.py printed and how it was resolved; anything you skipped, assumed or guessed.
- Commit ONLY the folder output/NAME/ and push:
    git add output/NAME && git commit -m "NAME: detailed analysis deck" && git push -u origin claude/jee-outputs
- Your final message: three or four sentences (paper, index, number of corrections, branch name).
