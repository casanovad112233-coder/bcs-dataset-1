# 43rd BCS - pipeline report

- Source HTML: `43rd_bcs.html`
- Output JSON: `43rd_bcs.json`
- Date: 2021-10-29 | Marks: 200 | Set code: নীলকণ্ঠ
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

q68 already answered in `43rd_bcs.json` (from the math/mental audit) = **B (S∞=3/20)**: 1/4 − 1/6 + 1/9 − 2/27 + … is a GP with a=1/4, r=−2/3, so S∞ = a/(1−r) = (1/4)/(5/3) = 3/20. The report's "Needs answers" was stale — the JSON already had the answer. Template `output/43rd_bcs_answers.json` filled for consistency. Do NOT re-run pipeline from HTML (would overwrite math edits).

## Manual / human check (image / empty options)

- q65, q76, q79, q85, q90: image-only questions (prompt in image) — verify image paths (`q65_img1`, `q76_img1/2`, `q79_img1/2`, `q85_img1/2`, `q90_img1`) against source HTML.
- q76 (ans?): option_a and option_d are empty (option images not extracted). Verify against source.
- q90 (ans?): option_a and option_d are empty (option images not extracted). Verify against source.

## Image questions (verify manually)

These questions have no text - the prompt lives in the image(s). Please verify that the images and their paths are correct:

- q65: question=[images/43rd_bcs/q65_img1.jpg], solve=[-]
- q76: question=[images/43rd_bcs/q76_img1.jpg], solve=[images/43rd_bcs/q76_img2.jpg]
- q79: question=[images/43rd_bcs/q79_img1.png], solve=[images/43rd_bcs/q79_img2.jpg]
- q85: question=[images/43rd_bcs/q85_img1.jpg], solve=[images/43rd_bcs/q85_img2.jpg]
- q90: question=[images/43rd_bcs/q90_img1.png], solve=[-]

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 4 | International Affairs | 20 |
| 5 | Geography, Environment & Disaster Management | 10 |
| 6 | General Science | 12 |
| 7 | Computer & Information Technology | 18 |
| 8 | Mathematical Reasoning | 15 |
| 9 | Mental Ability | 15 |
| 10 | Ethics, Values & Good Governance | 10 |
| 1 | Bangla Language & Literature | 35 |
| 2 | English Language & Literature | 35 |
| 3 | Bangladesh Affairs | 30 |

## Classification

- Mapped from source tags: 200
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q65: image-only question (empty text) - verify image paths manually
- q76: image-only question (empty text) - verify image paths manually
- q76: option_a is empty (option images not extracted - see Manual/human check)
- q76: option_d is empty (option images not extracted - see Manual/human check)
- q79: image-only question (empty text) - verify image paths manually
- q85: image-only question (empty text) - verify image paths manually
- q90: image-only question (empty text) - verify image paths manually
- q90: option_a is empty (option images not extracted - see Manual/human check)
- q90: option_d is empty (option images not extracted - see Manual/human check)

## Validation

All hard checks passed.
