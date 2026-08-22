# 44th BCS - pipeline report

- Source HTML: `44th_bcs.html`
- Output JSON: `44th_bcs.json`
- Date: 2022-05-27 | Marks: 200 | Set code: হেমন্ত
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

Answers filled directly in `44th_bcs.json` (not re-run from HTML, to preserve math edits):

- q156 = B (৪৮) — number of small ethnic groups at exam time (May 2022); gazette then in force said 48, later 2022 census reports list 50. Verified vs. bissoy 44th BCS answer key / biddabari.
- q11 = defective — correct answer is "সেপ্টেম্বর মাসের তৃতীয় মঙ্গলবার" (UNGA annual session traditionally starts the 3rd Tuesday of September), which is NOT among the given options. correct_answer left blank; solve note documents it. Biddabari solution notes "অপশনে সঠিক উত্তর ছিল না".

Corresponding template updated: `output/44th_bcs_answers.json`.

## Defective questions (no valid option - left blank)

- q11: জাতিসংঘ সাধারণ পরিষদের বার্ষিক অধিবেশন প্রথাগতভাবে সেপ্টেম্বর মাসের তৃতীয় মঙ্গলবার শুরু হয়; অপশনগুলোর (প্রথম সোমবার/প্রথম মঙ্গলবার/শেষ সোমবার) কোনোটি সঠিক নয়। বাকি solve note q11-এ সংরক্ষিত।

## Manual / human check (image / empty options)

- q186, q190, q191, q195 (all answered B/D/B/C): image-only questions (prompt in image) — verify image paths `q186_img1`, `q190_img1/2`, `q191_img1/2`, `q195_img1/2` against source HTML.
- q194 (ans B): 'MEMORY' mirror image — all 4 option texts empty (option images not extracted); solve image `q194_img1.jpg` present. Verify option images.
- q190/q191/q195 have empty solve_notes but solve images exist — verify.

## Image questions (verify manually)

These questions have no text - the prompt lives in the image(s). Please verify that the images and their paths are correct:

- q186: question=[images/44th_bcs/q186_img1.jpg], solve=[-]
- q190: question=[images/44th_bcs/q190_img1.jpg], solve=[images/44th_bcs/q190_img2.jpg]
- q191: question=[images/44th_bcs/q191_img1.jpg], solve=[images/44th_bcs/q191_img2.jpg]
- q195: question=[images/44th_bcs/q195_img1.jpg], solve=[images/44th_bcs/q195_img2.jpg]

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 4 | International Affairs | 19 |
| 3 | Bangladesh Affairs | 29 |
| 1 | Bangla Language & Literature | 37 |
| 2 | English Language & Literature | 35 |
| 8 | Mathematical Reasoning | 15 |
| 5 | Geography, Environment & Disaster Management | 10 |
| 6 | General Science | 15 |
| 7 | Computer & Information Technology | 15 |
| 10 | Ethics, Values & Good Governance | 10 |
| 9 | Mental Ability | 15 |

## Classification

- Mapped from source tags: 200
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q11: correct_answer is blank (defective - no valid option; see Defective questions)
- q186: image-only question (empty text) - verify image paths manually
- q190: image-only question (empty text) - verify image paths manually
- q191: image-only question (empty text) - verify image paths manually
- q194: option_a is empty (option images not extracted - see Manual/human check)
- q194: option_d is empty (option images not extracted - see Manual/human check)
- q195: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.
