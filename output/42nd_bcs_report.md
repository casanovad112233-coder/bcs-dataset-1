# 42nd BCS - pipeline report

- Source HTML: `42nd_bcs.html`
- Output JSON: `42nd_bcs.json`
- Date: 2021-02-26 | Marks: 100 | Set code: সুরমা
- Questions: 100

## Needs LLM classification

None.

## Needs answers

None.

## What has been done (LLM pass)

Solve notes filled directly in `42nd_bcs.json` (answers were already present; not re-run from HTML):

- q47 = A (উদ্বাসন = বাসভূমি থেকে বিতাড়িত হওয়া) — solve note written.
- q63 = A (Caesarean) — solve note written (named after Julius Caesar).
- q85 = image-only, cannot be solved without the image — left for manual/human check (see below).

Corresponding template updated: `output/42nd_bcs_solve_notes.json`.

## Manual / human check (image / empty options)

- q85 (ans B): image-only question (prompt lives in `q85_img1.jpg`); all 4 option texts empty (option images not extracted). Needs human verification of the image and its options.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 2 | English Language & Literature | 20 |
| 1 | Bangla Language & Literature | 19 |
| 9 | Mental Ability | 7 |
| 3 | Bangladesh Affairs | 21 |
| 4 | International Affairs | 20 |
| 8 | Mathematical Reasoning | 13 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q85: image-only question (empty text) - verify image paths manually
- q85: option_a is empty (option images not extracted - see Manual/human check)
- q85: option_d is empty (option images not extracted - see Manual/human check)

## Validation

All hard checks passed.
