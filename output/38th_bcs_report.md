# 38th BCS - pipeline report

- Source HTML: `38th_bcs.html`
- Output JSON: `38th_bcs.json`
- Date: 2017-12-29 | Marks: 200 | Set code: সুরমা
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

- q151 = B (input-reader bus) — no such bus exists (address/data/control are the 3 system buses; 'dat bus' is a typo of data bus). Verified vs kgc.ac.bd 38th BCS key.
- q152 = B (firmware) — ROM-based program; option b is 'irmware' (typo). Verified vs kgc.ac.bd.
- q182: solve note written (UNFARE mirror → answer A); option texts are empty (option images not extracted) — see Manual/human check.

## Defective questions (no valid option - left blank)

- q6: 'কোনটি শুদ্ধ বানান?' — all 4 options misspelled; correct form স্বায়ত্তশাসন absent. (Source's own note confirms.)
- q83: Bangladesh Economic Review 2016 → child mortality = 30 per 1000; options are ২৫/২৭/২৯/৩১, so 30 absent. kgc.ac.bd 38th key confirms answer was ৩০.

Templates updated: `output/38th_bcs_answers.json` = {6:null, 83:null, 151:B, 152:B}; `output/38th_bcs_solve_notes.json` = {182: ...}.

## Manual / human check (image / empty options)

- q175, q181, q184, q186, q188: image-only questions (prompt lives in the images) — verify images and paths.
- q182: option_a & option_d empty (option images not extracted) — verify mirror-image options against source images.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 36 |
| 2 | English Language & Literature | 34 |
| 3 | Bangladesh Affairs | 30 |
| 4 | International Affairs | 20 |
| 5 | Geography, Environment & Disaster Management | 10 |
| 6 | General Science | 15 |
| 7 | Computer & Information Technology | 15 |
| 8 | Mathematical Reasoning | 15 |
| 9 | Mental Ability | 15 |
| 10 | Ethics, Values & Good Governance | 10 |

## Classification

- Mapped from source tags: 200
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q6: correct_answer is blank (defective - correct form স্বায়ত্তশাসন not in options)
- q83: correct_answer is blank (defective - Economic Review 2016 says 30, not in options)
- q175: image-only question (empty text) - verify image paths manually
- q181: image-only question (empty text) - verify image paths manually
- q182: option_a is empty (option images not extracted - see Manual/human check)
- q182: option_d is empty (option images not extracted - see Manual/human check)
- q184: image-only question (empty text) - verify image paths manually
- q186: image-only question (empty text) - verify image paths manually
- q188: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.
