# BCS Question JSON Agent Instructions

This repo builds a BCS question bank from scraped HTML sources. The HTML files are temporary sources only. The final JSON must be self-contained and ready for database import.

## Source Of Truth

- Treat each exam HTML file as the source for the exam's questions, options, correct answers, solve notes, and image placement.
- Treat `topics_taxonomy.md` as the ground truth taxonomy for all exams from 10th BCS through 50th BCS.
- Do not invent, rename, reorder, or remove taxonomy subjects.
- `subject_id` must always be an integer from `1` to `10`.
- Every question must include `subject_id`, `subject_en`, and `subject_bn` matching the taxonomy.

## Encoding

- All repo text outputs must be UTF-8.
- Repair mojibake before extracting JSON. Broken markers such as `à¦`, `à§`, `â€`, `Â`, or `�` should not appear in final JSON.
- Preserve Bangla text as real Unicode Bangla, not escaped mojibake and not transliteration.

## JSON Shape

Each exam JSON file should use this top-level shape:
For example:

```json
{
  "exam": {
    "title": "50th BCS",
    "date": "2026-01-30",
    "total_marks": 200,
    "set_code": "ধরলা",
    "total_questions": 200
  },
  "taxonomy": [],
  "questions": []
}
```

Each question object must use this schema:

```json
{
  "question_number": 1,
  "subject_id": 9,
  "question": "প্রশ্নের plain text",
  "option_a": "A option text",
  "option_b": "B option text",
  "option_c": "C option text",
  "option_d": "D option text",
  "correct_answer": "B",
  "solve_note": "ব্যাখ্যার plain text, empty string allowed only when solution is image-only",
  "question_image_paths": [],
  "solve_note_image_paths": [],
  "has_question_image": 0,
  "has_solve_note_image": 0,
  "has_image": 0,
  "subject_en": "Mental Ability",
  "subject_bn": "মানসিক দক্ষতা",
  "exam_slug": "50th_bcs"
}
```

Rules:

- Use `question`, not `question_html`.
- Do not include raw HTML tags in `question`, options, or `solve_note`.
- Do not use a generic `image_paths` field. Always split images by purpose.
- `question_image_paths` contains images that appear inside the question prompt before the options.
- `solve_note_image_paths` contains images that appear inside the solve/explanation area.
- `has_question_image` is `1` when `question_image_paths` is non-empty, otherwise `0`.
- `has_solve_note_image` is `1` when `solve_note_image_paths` is non-empty, otherwise `0`.
- `has_image` is `1` when either image array is non-empty, otherwise `0`.
- `exam_slug` is the canonical exam stem (e.g. `"50th_bcs"`, `"10th_bcs"`) and must match the JSON file name `data/processed/json/<exam_slug>.json` and the pattern `N(th)_bcs`.
- `correct_answer` must be uppercase `A`, `B`, `C`, or `D`.
- `question_number` must be an integer.

## HTML Extraction Rules

- Parse each `.single-question` block as one question.
- Read the question number from the block heading, such as `Question 1`.
- Read the correct answer from the block's `data-answer` attribute and normalize it to uppercase `A-D`.
- Extract the prompt text from the content between the heading and the options list.
- Extract options from the option labels, not from visible layout text outside the question block.
- Extract solve note text from `.solve-note`.
- Convert HTML entities and non-breaking spaces to normal text.
- Preserve meaningful math symbols where possible.
- Ignore page chrome, navbar, footer, ads, unrelated promotional images, and external marketing images.

## Image Handling

Be careful: an image can belong to the question prompt or to the solve note.

- If an `<img>` appears before the options list in the question block, save/reference it in `question_image_paths`.
- If an `<img>` appears inside `.solve-note`, save/reference it in `solve_note_image_paths`.
- If `solve_note` text is empty but `solve_note_image_paths` is non-empty, that is valid: the solution is image-only.
- Do not move solve-note images into `question_image_paths`.
- Store local paths like `images/50th_bcs/q14_img1.png`.
- Keep image filenames stable and exam-scoped, for example `images/50th_bcs/q{question_number}_img{index}.png`.
- Image index is a single per-question sequence that runs across both scopes: question images first (`q173_img1`), then solve-note images (`q173_img2`). A question image and a solve-note image must never share the same `img{index}` filename, or the later write overwrites the earlier one.

## Validation Checklist

Before finishing an exam JSON:

- JSON parses successfully.
- Question count equals `exam.total_questions`.
- Every question has a non-empty `question`, unless the question is image-only: then `question` may be empty but `question_image_paths` must be non-empty, and the question must be reported for manual image/path verification.
- No question has `question_html`.
- No question has generic `image_paths`.
- All `subject_id` values are integers in the taxonomy.
- All `subject_en` and `subject_bn` values match the taxonomy for that `subject_id`.
- No broken encoding markers remain.
- `solve_note` may be empty only if `solve_note_image_paths` is non-empty.
- Every image path referenced in JSON exists on disk.
- Image flags match the image arrays.
- Every question has `exam_slug` equal to the file stem (e.g. `"50th_bcs"`) and matching `^\d+(st|nd|rd|th)_bcs$`.
