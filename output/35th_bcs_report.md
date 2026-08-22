# 35th BCS - pipeline report

- Source HTML: `35th_bcs.html`
- Output JSON: `35th_bcs.json`
- Date: 2015-03-06 | Marks: 200 | Set code: চামেলি
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

Answers filled directly in `35th_bcs.json` (verified vs kgc.ac.bd 35th BCS key, biddabari 35th solution PDF, bdmcq.com 35th full solve):

- q10 = B (লবণাক্ত) — exam question was 'বিশেষণ' (source HTML typo'd 'বিশেষ্য'; question text corrected). bdmcq + source's own note confirm লবণাক্ত.
- q23 = A (খুলনার দক্ষিণ ডিহি) — পূর্বপুরুষের আদি নিবাস রূপসার পিঠাভোগ গ্রাম; biddabari key confirms.
- q74 = D (২৮) — kgc + biddabari keys say ২৮ (exam-era, 2015); eduaidbd's ২৬ is an outlier.
- q78 = B (৪৫৫০) — kgc key (options match ours exactly); eduaidbd's ৪৫৬২ is not among the exam options.
- q161 = left blank (defective, see below).

Solve notes written for q2 (মনীষী), q4 (ভোগ্যপণ্য), q10, q23, q74, q78, q127 (ধান-প্রধান নিবিড় স্বয়ংভোগী), q128 (পরিবেশগত), q161.

## Defective questions (no valid option - left blank)

- q161: correct answer ১.২০ টাকা not among options (1.50/2.50/3.00/4.00). Math: ১২ টাকার ২০% = ২.৪০ = ২টি কলার বর্তমান দাম → ১টি = ১.২০. Option A (1.50) is the pre-discount price. biddabari note: "অপশনে সঠিক উত্তর নেই"। Previously filled A from math audit — cleared to blank.

`output/35th_bcs_answers.json` = {10:B, 23:A, 74:D, 78:B, 161:null}.

## Manual / human check (image / empty options)

- q1, q178, q179, q183, q185: image-only questions (prompt lives in images) — verify images and paths.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 35 |
| 2 | English Language & Literature | 35 |
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

- q1: image-only question (empty text) - verify image paths manually
- q161: correct_answer is blank (defective - correct answer ১.২০ not in options)
- q178: image-only question (empty text) - verify image paths manually
- q179: image-only question (empty text) - verify image paths manually
- q183: image-only question (empty text) - verify image paths manually
- q185: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.
