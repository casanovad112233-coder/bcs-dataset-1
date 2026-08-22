# 39th BCS - pipeline report

- Source HTML: `39th_bcs.html`
- Output JSON: `39th_bcs.json`
- Date: 2018-08-03 | Marks: 100 | Set code: সুরমা
- Questions: 100

## Needs LLM classification

None.

## What has been done (LLM pass)

Answers filled directly in `39th_bcs.json` (verified vs biddabari 39th BCS solution / bdmcq):

- q33 = A (১৪.৭৯%) — agriculture share of GDP (FY2017-18) at exam time (Aug 2018).
- q53 = A (মন্টিনিগ্রো) — NATO's latest member at exam time (joined June 2017); Finland 2023 & Sweden 2024 came later.

## Defective questions (no valid option - left blank)

- q58: C={x: x ঋণাত্মক পূর্ণসংখ্যা এবং x²<18} → {-4,-3,-2,-1}; all options are positive integers. Biddabari: "অপশনে সঠিক উত্তর নেই".
- q76: ঘড়িতে ৮টা → কোণ = ১২০°; options are ৯০/৯৫/১০৫/১১০ — ১২০° absent.
- q99: স্বাধীনতা পদক প্রাপ্ত ব্যক্তিত্ব — all four listed (যতীন সরকার ২০১০, সৈয়দ শামসুল হক ২০০০, শামসুর রাহমান ১৯৯১, সৈয়দ আলী আহসান ১৯৮৭) received it; multiple correct answers, source notes option typos ('সতীন'→'যতীন', 'রহমান'→'রাহমান'). Biddabari: "অপশনে সঠিক উত্তর নেই".

Defect explanations written into the solve notes; `output/39th_bcs_answers.json` = {33:A, 53:A, 58:null, 76:null, 99:null}.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 8 | Mathematical Reasoning | 10 |
| 1 | Bangla Language & Literature | 24 |
| 2 | English Language & Literature | 21 |
| 5 | Geography, Environment & Disaster Management | 1 |
| 3 | Bangladesh Affairs | 15 |
| 4 | International Affairs | 20 |
| 9 | Mental Ability | 9 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q58: correct_answer is blank (defective - negative integer set, options all positive)
- q76: correct_answer is blank (defective - 8 o'clock angle 120°, not in options)
- q99: correct_answer is blank (defective - all 4 options are award recipients)

## Validation

All hard checks passed.
