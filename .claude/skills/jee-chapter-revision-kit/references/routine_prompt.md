# Ready-to-paste routine prompt (one chapter per run)

Run the **jee-chapter-revision-kit** skill for the chapter **<CHAPTER NAME>**.
Inputs are in `chapters/<CHAPTER_NAME>/` (theory sheet, XII sheet, XIII sheet, and DPP / Question Bank if present). The master Quick Review is `jee-inputs/quick_review_all_chapters.pdf`
(use `jee-inputs/master_index.json` if it exists, otherwise the index saved in the skill). Run unattended - do not ask questions; record every uncertain decision in REPORT.md.
Write all outputs to `chapters/<CHAPTER_NAME>/kit/` and commit them to branch `claude/jee-outputs`. If anything required is missing or a tool is unavailable, write `RUN_FAILED.md` there instead and stop.

(To process the next unfinished chapter automatically, replace the first line with: "Run the jee-chapter-revision-kit skill for the first folder in `chapters/` that has no `kit/` folder.")
