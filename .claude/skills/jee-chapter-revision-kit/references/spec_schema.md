# Chapter spec schema (`chapter_spec.json`) and the two companion files

```
{
 "chapter": {"en": "Quadratic Equation", "hi": "द्विघात समीकरण", "slug": "Quadratic_Equation"},
 "batches": {"XII": {"jm": "J-M(XII)"}, "XIII": {"jm": "J-M(XIII)"}},      # key = batch name, jm = key of its JM exercise in question_index.json
 "qb_overlap": {"XIII": [13,14,15,16,17,18,19,20]},                          # QB question numbers already in that batch's JM set (count once)
 "graded_sources": ["<jm>", "J-A", "QB"],                                    # optional; this is the default
 "quick_review": {"sections": [
    {"en": "Standard Form ...", "hi": "...", "items": [
       {"id": "1", "o": 1, "tag": null, "src": "",                          # id: unique string; o: original prompt number (null if added); tag: null | "rephrased" | "added"
        "q": ["English prompt", "हिन्दी प्रश्न"],
        "a": ["pure formula line $...$",                                    # a plain string is used in both languages (pure formulas only)
              ["English line with $math$", "हिन्दी पंक्ति $math$"]]}]}]},
 "notes": {"howto": ["en line", "hi line"],
           "sections": [{"en": "...", "hi": "...", "color": "blue",         # color: blue teal green orange red violet brown
                         "blocks": [["formula", [[en, hi], ...]], ["points", [...]], ["steps", [...]], ["watch", [...]]]}]},
 "formula": {"sections": [{"en": "...", "hi": "...", "lines": [[en, hi], ...]}]},   # "Label: $formula$" lines; long ones are shown as display equations
 "mindmap": {"branches": [{"en": "...", "hi": "...", "leaves": [[en, hi], ...]}]}, # 8-16 branches, 2-5 leaves, left half / right half automatically
 "flowcharts": [{"title": [en, hi], "start": [en, hi], "color": "blue",
                 "steps": [{"q": [en, hi], "a": [[en lines], [hi lines]]}],      # each step: question -> Yes: method lines; No: next step
                 "else": [[en lines], [hi lines]]}]
}
```
`question_map.json`: `{"J-I:1": "18;3", "DPP-3:5": "29", "J-A:9": "-"}` - key `SRC:number` (SRC as in `question_index.json`: `J-I, J-II, J-A, C-I, C-II, J-M(XII), J-M(XIII), DPP-<n>, QB`);
value `main` or `main;other1,other2` using item ids; `-` = no item fits.

`question_index.json`: written by `extract_questions.py` (do not edit by hand).

Text rules: LaTeX inside `$...$` only (amsmath + amssymb); `\dfrac` for display-size fractions, `\frac` inside running text; `\text{}` only with English; `$$` is not used.
`{#12}` inside a string = the final number of the item whose original number is 12.
