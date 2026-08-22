# 34th BCS - pipeline report

- Source HTML: `34th_bcs.html`
- Output JSON: `34th_bcs.json`
- Date: 2013-05-24 | Marks: 100 | Set code: সুরমা
- Questions: 100

## What has been done (LLM pass)

Filled the 4 missing answers against external keys (kgc.ac.bd, eduaidbd, sattacademy, bcstarget, bdmcq):

- q6 = C (ঈশ্বরচন্দ্র বিদ্যাসাগর) — kgc.ac.bd and eduaidbd both give ঈশ্বরচন্দ্র বিদ্যাসাগর for this exact question; strictly he is 'বাংলা গদ্যের জনক', but that is the expected exam answer.
- q57 = A (নেপাল) — DISPUTED: kgc key says ভারত, bdmcq argues "none" (Nepal secular since 2006); however eduaidbd + sattacademy + bcstarget all say নেপাল, matching the exam-era convention (Nepal declared Hindu state by the 1962 constitution). Went with majority.
- q65 = A (অগ্ন্যাশয় হতে) — options A/B are near-synonyms (অগ্ন্যাশয় = pancreas); kgc key picks A.
- q100 = A ("T, X") — image-only question; kgc key explicitly answers "T, X" for this exact option set. Earlier flagged defective because the source note (EY → ASSEMBLY) fits no option; overturned on kgc evidence.

Solve notes appended to q6, q57, q65, q100 in `34th_bcs.json` (also mirrored in `output/34th_bcs_solve_notes.json`).

## Defective questions (no valid option - left blank)

None.

## Manual / human check (image / empty options)

- q100: question text lives in `images/34th_bcs/q100_img1.png` (this session could not view images). Answer filled as A per kgc key — please eyeball the image to confirm it matches a "T, X"-type puzzle rather than the ASSEMBLY/EY note from the source site.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 20 |
| 2 | English Language & Literature | 5 |
| 3 | Bangladesh Affairs | 12 |
| 6 | General Science | 23 |
| 4 | International Affairs | 16 |
| 8 | Mathematical Reasoning | 12 |
| 7 | Computer & Information Technology | 1 |
| 9 | Mental Ability | 11 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q100: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.
