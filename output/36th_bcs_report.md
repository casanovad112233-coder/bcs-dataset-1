# 36th BCS - pipeline report

- Source HTML: `36th_bcs.html`
- Output JSON: `36th_bcs.json`
- Date: 2016-01-08 | Marks: 200 | Set code: দোলনচাঁপা
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

Answers filled directly in `36th_bcs.json` (verified vs kgc.ac.bd 36th BCS answer key):

- q36 = B (of) — "a scholar of repute" (source question typo'd 'refute' for 'repute'; the source's own note explains 'of' works with repute).
- q90 = A (৯ মে, ১৯৫৪) — Pak Constituent Assembly recognized Bangla on 9 May 1954.
- q93 = D (১৯টি) — kgc 36th key: "বাংলাদেশের বৃহত্তম জেলা" answer ১৯টি.
- q147 = C (Assembly Language) — 3G language ≠ low-level; kgc key: Assembly Language.
- q186 = A (কুসংস্কার) — already filled from math audit.

## Defective questions (no valid option - left blank)

- q113: NAM members = ১২০ (kgc key), but options here are ৩৩/১৫/৭৭/২১ — ১২০ absent.
- q120: Mother Teresa born in Macedonia (kgc key), but options here are ভারত/আলজেরিয়া/আলবেনিয়া/ফ্রান্স — Macedonia absent.
- q182: parallel lines meet 0 times; options are ৪/২/৮/১৬ — ০ absent.

`output/36th_bcs_answers.json` = {36:B, 90:A, 93:D, 113:null, 120:null, 147:C, 182:null, 186:A}.

## Manual / human check (image / empty options)

- q174, q177, q178, q184, q190: image-only questions (prompt lives in images) — verify images and paths.
- q183: image-only (answer B present, solve note empty) + option_a/option_d empty — verify against source images.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 35 |
| 2 | English Language & Literature | 35 |
| 3 | Bangladesh Affairs | 31 |
| 4 | International Affairs | 20 |
| 5 | Geography, Environment & Disaster Management | 10 |
| 6 | General Science | 14 |
| 7 | Computer & Information Technology | 15 |
| 8 | Mathematical Reasoning | 15 |
| 9 | Mental Ability | 15 |
| 10 | Ethics, Values & Good Governance | 10 |

## Classification

- Mapped from source tags: 200
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q113: correct_answer is blank (defective - NAM=120 not in options)
- q120: correct_answer is blank (defective - born in Macedonia, not in options)
- q174: image-only question (empty text) - verify image paths manually
- q177: image-only question (empty text) - verify image paths manually
- q178: image-only question (empty text) - verify image paths manually
- q182: correct_answer is blank (defective - parallel lines meet 0 times, not in options)
- q183: image-only question (empty text) - verify image paths manually
- q183: option_a is empty (option images not extracted - see Manual/human check)
- q183: option_d is empty (option images not extracted - see Manual/human check)
- q184: image-only question (empty text) - verify image paths manually
- q186: (already answered A - কুসংস্কার)
- q190: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.
