# 47th BCS - pipeline report

- Source HTML: `47th_bcs.html`
- Output JSON: `47th_bcs.json`
- Date: 2025-09-19 | Marks: 200 | Set code: রক্তকমল
- Questions: 200

## Needs LLM classification

None.

## What has been done (LLM pass)

Answers filled directly in `47th_bcs.json` (not re-run from HTML, to preserve math edits):

- q27 = D (তোহ্ফা) — আলাওল wrote his personal life story in the last part of 'তোহ্ফা' (family, war-captivity, Arakan refuge). Verified vs. sattacademy 47th-BCS answer key.
- q139 = C — the false statement about ether is "এ মাধ্যম ছাড়া তাড়িৎ চৌম্বক তরঙ্গ সঞ্চালন সম্ভব নয়" (EM waves propagate without ether; Michelson–Morley). Solve note already present.
- q110, q146 = defective, no valid option — left blank (see Defective questions below).

Corresponding template files updated: `output/47th_bcs_answers.json`, `output/47th_bcs_solve_notes.json`.

## Defective questions (no valid option - left blank)

These were reported by media / have no correct answer among the given options. correct_answer left blank in JSON; flagged for review.

- q110: ফার্দো (Fordow) সমৃদ্ধকরণ কেন্দ্রটি 'কোম' প্রদেশে অবস্থিত, কিন্তু অপশনে কোম নেই (ইসফাহান/ইলাম/বুমেহর/আলবোজ)। Question named in sabahbd news article (set-1 Q110).
- q146: ক্লক স্পিড ৪.০০ GHz → cycle time = 1/4 GHz = 0.25 ns, কিন্তু অপশনে নেই (২.৫ ns/২.৫ µs/৪ ms/৪ ns)। Question named in sabahbd news article (set-1 Q146).

## Manual / human check (image / empty options)

- q180 (ans D): all 4 option texts empty (option images not extracted); Mental Ability image question with solve image `q180_img1.jpg`. Verify option images against source HTML.

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

- q110: correct_answer is blank (defective - no valid option; see Defective questions)
- q146: correct_answer is blank (defective - no valid option; see Defective questions)
- q180: option_a is empty (option images not extracted - see Manual/human check)
- q180: option_d is empty (option images not extracted - see Manual/human check)

## Validation

All hard checks passed.
