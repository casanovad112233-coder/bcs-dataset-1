# 45th BCS - pipeline report

- Source HTML: `45th_bcs.html`
- Output JSON: `45th_bcs.json`
- Date: 2023-05-19 | Marks: 200 | Set code: মনপুরা
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

Answers filled directly in `45th_bcs.json` (not re-run from HTML, to preserve math edits):

- q186 = D (ময়মনসিংহ) — solve_note updated. At exam time (May 2023) the largest solar plant was Mymensingh's Sutiyakhali; Teesta Solar (Gaibandha, 200 MW) opened 2024 and is not an option. Verified vs. banglanewsexpress/myexaminer.
- q197 = C (১১টি) — solve_note updated. 11 GI products as of May 2023 (11th = Rajshahi Fazli mango, 2022); 4 more (Bogura curd, Sherpur Tulsimala rice, Chapainawabganj Langra & Ashwina mango) registered 2023-07-05 → 15. Verified vs. banglanewsexpress (answer ১১টি).
- q38 = A (solve note written) — all spellings in (ক) শিরশ্ছেদ/দরিদ্রতা/সমীচীন are correct; the other options each contain an incorrect spelling.
- q42 = D (solve note written) — 'এ' is the high-mid front vowel; 'অ', 'আ', 'ও' are not.

Corresponding template files updated: `output/45th_bcs_answers.json`, `output/45th_bcs_solve_notes.json`.

## Manual / human check (image options not extracted)

The pipeline does not extract option images, so these questions have empty option text in the JSON and their correctness must be verified against the source HTML images:

- q121 (ans A): "কোনটি ভারসাম্যপূর্ণ অবস্থা?" — options are images `19.jpg`, `119.jpg`, `20.jpg`, `21.jpg`. solve_note references "‘গ’ চিত্র" which conflicts with ans A; verify against the actual option images and correct the solve_note if needed.
- q126 (ans C): "ROSE এর আয়নায় প্রতিবিম্ব কোনটি হবে?" — options A/B/C are images `122/123/124.jpg`, D = text "কোনোটিই নয়". Verify mirror-image option against solve image `125.jpg`.
- q127 (ans B): fully image-based question (option images `127–130.jpg`, question+solve images `131.jpg`). Verify image paths and answer.
- q123 (ans D): question is an image (`q123_img1.jpg`), text options ১/৩/২/৪. Verify the image path renders correctly.

## Math formatting

Deferred (handled later in a separate pass).

## Image questions (verify manually)

These questions have no text - the prompt lives in the image(s). Please verify that the images and their paths are correct:

- q123: question=[images/45th_bcs/q123_img1.jpg], solve=[-]
- q127: question=[images/45th_bcs/q127_img1.jpg], solve=[images/45th_bcs/q127_img2.jpg]

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 2 | English Language & Literature | 35 |
| 1 | Bangla Language & Literature | 35 |
| 4 | International Affairs | 21 |
| 5 | Geography, Environment & Disaster Management | 9 |
| 8 | Mathematical Reasoning | 15 |
| 9 | Mental Ability | 15 |
| 10 | Ethics, Values & Good Governance | 10 |
| 6 | General Science | 15 |
| 7 | Computer & Information Technology | 15 |
| 3 | Bangladesh Affairs | 30 |

## Classification

- Mapped from source tags: 200
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q121: option_a is empty (option images not extracted - see Manual/human check)
- q121: option_d is empty (option images not extracted - see Manual/human check)
- q123: image-only question (empty text) - verify image paths manually
- q126: option_a is empty (option images not extracted - see Manual/human check)
- q127: image-only question (empty text) - verify image paths manually
- q127: option_a is empty (option images not extracted - see Manual/human check)
- q127: option_d is empty (option images not extracted - see Manual/human check)

## Validation

All hard checks passed.
