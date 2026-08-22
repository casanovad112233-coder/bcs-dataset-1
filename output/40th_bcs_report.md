# 40th BCS - pipeline report

- Source HTML: `40th_bcs.html`
- Output JSON: `40th_bcs.json`
- Date: 2019-05-03 | Marks: 200 | Set code: সুরমা
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

Answers filled directly in `40th_bcs.json` (verified vs biddabari 40th answer key / livemcq):

- q33 = B (১৯২১ সন) — 'বিদ্রোহী' first published in মাসিক 'মোসলেম ভারত' কার্তিক ১৩২৮ (Oct-Nov 1921) per রফিকুল ইসলামের নজরুল নির্দেশিকা; also the exam answer. (Note: it later appeared in সাপ্তাহিক বিজলী 6 Jan 1922.)
- q79 = A (২ কোটি ৪০ লক্ষ একর) — biddabari 40th key. (Note: source's solve note quotes ৮৮.২৯ লক্ষ হেক্টর ≈ ২ কোটি ১৮ লক্ষ একর, which is NOT an option; official exam answer is A.)
- q81 = B ($ ১,৭৫১) — 2018 Bangladesh per capita GDP (nominal) per BBS.
- q105 = C (ফেব্রুয়ারি, ২০১৯) — Munich Security Conference is held each February; latest before the May 2019 exam was Feb 2019.
- q161 = D (√48) and q183 = D (১১০) were already filled from the math audit.

Corresponding template updated: `output/40th_bcs_answers.json`.

## Manual / human check (image / empty options)

- q172, q184, q185, q186, q188: image-only questions (prompt lives in the images) — verify images and paths.
- q180: option_a & option_d empty (option images not extracted) — verify against source images.

## Subject distribution

| subject_id | subject_en                                   | count |
| ---------- | -------------------------------------------- | ----- |
| 1          | Bangla Language & Literature                 | 35    |
| 2          | English Language & Literature                | 35    |
| 3          | Bangladesh Affairs                           | 30    |
| 4          | International Affairs                        | 20    |
| 5          | Geography, Environment & Disaster Management | 10    |
| 6          | General Science                              | 15    |
| 7          | Computer & Information Technology            | 15    |
| 8          | Mathematical Reasoning                       | 15    |
| 9          | Mental Ability                               | 15    |
| 10         | Ethics, Values & Good Governance             | 10    |

## Classification

- Mapped from source tags: 200
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q172: image-only question (empty text) - verify image paths manually
- q180: option_a is empty (option images not extracted - see Manual/human check)
- q180: option_d is empty (option images not extracted - see Manual/human check)
- q184: image-only question (empty text) - verify image paths manually
- q184: option_a is empty (option images not extracted - see Manual/human check)
- q184: option_d is empty (option images not extracted - see Manual/human check)
- q185: image-only question (empty text) - verify image paths manually
- q185: option_a is empty (option images not extracted - see Manual/human check)
- q185: option_d is empty (option images not extracted - see Manual/human check)
- q186: image-only question (empty text) - verify image paths manually
- q186: option_a is empty (option images not extracted - see Manual/human check)
- q186: option_d is empty (option images not extracted - see Manual/human check)
- q188: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.
