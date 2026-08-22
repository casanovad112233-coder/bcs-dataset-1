# 46th BCS - pipeline report

- Source HTML: `46th_bcs.html`
- Output JSON: `46th_bcs.json`
- Date: 2024-04-26 | Marks: 200 | Set code: কপোতাক্ষ
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

Answers filled directly in `46th_bcs.json` (not re-run from HTML, to preserve math edits):

- q45 = A (Injured) — "Injured, he lay on the ground groaning" (reduced clause from "As he was injured"; 'Being' omitted). Solve note updated. Verified vs. bissoy/babarenglish/reddit.
- q64 = B (quit) — 'quit' is a typo for 'quiet', the antonym of boisterous. Intended answer B. Solve note updated. Verified vs. biddabari/chakribangla/lxmcq.
- q170 = D (খরা) — solve note written: drought is the agro-meteorological hazard; earthquake/landslide/tsunami are not weather-related.

Corresponding template files updated: `output/46th_bcs_answers.json`, `output/46th_bcs_solve_notes.json`.

## Defective questions (no valid option - left blank)

These were flagged by BPSC / have no correct answer among the given options. correct_answer left blank in JSON; flagged for review.

- q9: ১৬ by ৩০ divisible but not ১৬ → actual count 29 (1000/30 = 33, minus 1000/LCM(30,16)=240 → 4, so 33−4=29). Options 33/35/37/41 — none match. Question cancelled by PSC (chakribangla).
- q28: ratio ৩:২, women 25 → men = 25×3/2 = 37.5. Options 30/35/40/45 — none match (not an integer).
- q30: 5 consecutive integers avg 15 → 13,14,15,16,17, largest = 17. Options 18/20/22/24 — none match.
- q145: G-77 has 134 members (last: South Sudan). Options 105/115/125/135 — none match.

## Manual / human check (image / empty options)

The pipeline does not extract option images and some questions are image-only. Verify against source HTML/images:

- q17 (ans B): image-based dictionary-order question; option text present (৪৩৫২১/৩৫৪২১/৩৪৫১২/৪৩৫১২), solve_note present. Verify q17_img1/2.jpg paths.
- q22 (ans C): "যদি একটি কামান থেকে..." — options are images (all 4 empty in JSON), solve_note present. Verify option images.
- q25 (ans A): fully image-based question, all options empty. Verify q25_img1/2.jpg.
- q26 (ans C): question is an image (q26_img1.jpg), text options present (৮০/১১৪/১০৮/কোনোটিই নয়), solve_note empty. Verify image.
- q92 (ans A): 'শূন্যপূরাণের' রচয়িতা = রামাই পন্ডিত; option_d is empty in source. Verify source had only 3 options.

## Math formatting

Deferred (handled later in a separate pass).

## Image questions (verify manually)

These questions have no text - the prompt lives in the image(s). Please verify that the images and their paths are correct:

- q17: question=[images/46th_bcs/q17_img1.jpg], solve=[images/46th_bcs/q17_img2.jpg]
- q25: question=[images/46th_bcs/q25_img1.jpg], solve=[images/46th_bcs/q25_img2.jpg]
- q26: question=[images/46th_bcs/q26_img1.jpg], solve=[images/46th_bcs/q26_img2.jpg]

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 8 | Mathematical Reasoning | 15 |
| 9 | Mental Ability | 15 |
| 10 | Ethics, Values & Good Governance | 10 |
| 2 | English Language & Literature | 35 |
| 1 | Bangla Language & Literature | 35 |
| 6 | General Science | 15 |
| 7 | Computer & Information Technology | 15 |
| 4 | International Affairs | 20 |
| 5 | Geography, Environment & Disaster Management | 10 |
| 3 | Bangladesh Affairs | 30 |

## Classification

- Mapped from source tags: 200
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q9: correct_answer is blank (defective - no valid option; see Defective questions)
- q17: image-only question (empty text) - verify image paths manually
- q22: option_a is empty (option images not extracted - see Manual/human check)
- q22: option_d is empty (option images not extracted - see Manual/human check)
- q25: image-only question (empty text) - verify image paths manually
- q25: option_a is empty (option images not extracted - see Manual/human check)
- q25: option_d is empty (option images not extracted - see Manual/human check)
- q26: image-only question (empty text) - verify image paths manually
- q28: correct_answer is blank (defective - no valid option; see Defective questions)
- q30: correct_answer is blank (defective - no valid option; see Defective questions)
- q92: option_d is empty (source had only 3 options - see Manual/human check)
- q145: correct_answer is blank (defective - no valid option; see Defective questions)

## Validation

All hard checks passed.
