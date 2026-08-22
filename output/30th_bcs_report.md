# 30th BCS - pipeline report

- Source HTML: `30th_bcs.html`
- Output JSON: `30th_bcs.json`
- Date: 2010-07-30 | Marks: 100 | Set code: সুরমা
- Questions: 100

## Needs LLM classification

None.

## Needs answers

None — all filled in the LLM pass (see below).

## Needs solve notes

None — notes written for q19, q57, q90 in the LLM pass.

## What has been done (LLM pass)

Filled directly in `30th_bcs.json` (do not re-run the pipeline from HTML for this exam):

- **q19 → C** (শামসুর রাহমান) [disputed]: strictly none of the four was born in 'পাহাড়তলী' — Shamsur Rahman was born in Mahutuli, Dhaka; ancestral home পাড়াতলী, Narsingdi (name confusion). biddabari 30th: "no correct option; most acceptable = গ"; kgc's compilation instead shows option ঘ as "উপরের কোনটি সঠিক নয়". Filled C per exam-era convention.
- **q57 → D**: real exam option ঘ was '১৮৬৩ সালে' (Red Cross/ICRC founded 1863); source HTML corrupted it to '১৮৬১'. Restored `option_d` = '১৮৬৩ সালে', answer D (kgc #92 — first three options match ours exactly; biddabari 30th also answers 1863).
- **q90 → B**: printed exam question had mixed signs (a−1/a=3, find a³+1/a³) — defective as printed (biddabari note: "if a+1/a=3 then খ is correct"). kgc #25 presents it as a+1/a=3 with answer 18. Question corrected to "a+1/a=3 হলে a³+1/a³ এর মান কত?", answer B (18). Supersedes an earlier math-audit fill of D=36 (all-minus reading).

## Manual / human check (image / empty options)

These questions have no text - the prompt lives in the image(s). Please verify that the images and their paths are correct:

- q32: question=[images/30th_bcs/q32_img1.jpg], solve=[-]
- q35: question=[images/30th_bcs/q35_img1.jpg], solve=[-]
- q39: question=[images/30th_bcs/q39_img1.jpg], solve=[-]

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 20 |
| 2 | English Language & Literature | 20 |
| 3 | Bangladesh Affairs | 10 |
| 4 | International Affairs | 11 |
| 6 | General Science | 17 |
| 5 | Geography, Environment & Disaster Management | 1 |
| 7 | Computer & Information Technology | 1 |
| 8 | Mathematical Reasoning | 20 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q19: disputed — no strictly correct option; C filled per exam-era convention (see LLM pass)
- q32: image-only question (empty text) - verify image paths manually
- q35: image-only question (empty text) - verify image paths manually
- q39: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.
