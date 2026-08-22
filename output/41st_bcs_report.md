# 41st BCS - pipeline report

- Source HTML: `41st_bcs.html`
- Output JSON: `41st_bcs.json`
- Date: 2021-03-19 | Marks: 200 | Set code: হাসনাহেনা
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

- q171: DEFECTIVE — left blank. All 4 options give May 1972 (২০/২১/২২/২৩ মে ১৯৭২), but the correct date is ২৩ মে ১৯৭৩ (per biddabari 41st answer key and the source's own solve note: "প্রদত্ত প্রশ্নের অপশনগুলোর সাল ভুল দেওয়া আছে"). The World Peace Council announced the award on 10 Oct 1972 and presented it 23 May 1973; neither date is among the options. Kept `output/41st_bcs_answers.json` as `{"171": null}`.
- q81: solve note written in `41st_bcs.json` (answer B, Encyclopedia). Template updated in `output/41st_bcs_solve_notes.json`.

## Defective questions (no valid option - left blank)

- q171: বঙ্গবন্ধুকে কখন 'জুলিও কুরী' শান্তি পুরস্কার প্রদান করা হয়? — correct answer ২৩ মে ১৯৭৩ absent from options (all options are May 1972).

## Manual / human check (image / empty options)

- q87 (ans B): image-only question — prompt lives in `q87_img1.jpg`, solve image `q87_img2.jpg`. Needs human verification of the image and options.
- q88 (ans A): 'RELATION'-এর আয়নায় প্রতিবিম্ব — option texts empty (option images not extracted); solve note present. Needs human verification of the option images.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 4 | International Affairs | 20 |
| 5 | Geography, Environment & Disaster Management | 10 |
| 6 | General Science | 15 |
| 7 | Computer & Information Technology | 15 |
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

- q87: image-only question (empty text) - verify image paths manually
- q88: option_a is empty (option images not extracted - see Manual/human check)
- q88: option_d is empty (option images not extracted - see Manual/human check)
- q171: correct_answer is blank (defective - correct date 23 May 1973 absent from options)

## Validation

All hard checks passed.
