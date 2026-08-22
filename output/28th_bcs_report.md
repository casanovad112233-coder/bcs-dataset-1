# 28th BCS - pipeline report

- Source HTML: `28th_bcs.html`
- Output JSON: `28th_bcs.json`
- Date: 2008-11-28 | Marks: 100 | Set code: সুরমা
- Questions: 100

## Needs LLM classification

None.

## Needs answers

None — all filled in the LLM pass (see below).

## Needs solve notes

None — notes written/clarified for q47, q48, q50, q53, q56, q62, q91 in the LLM pass.

## What has been done (LLM pass)

Filled directly in `28th_bcs.json` (do not re-run the pipeline from HTML for this exam):

- **q47 → D**: real exam option ঘ was '৩৫.১৩৫ বর্গমাইল' (~91 km² ≈ 35 sq mi); source HTML corrupted it to '৯০ ব.মা.'. Restored `option_d`, answer D (kgc #81).
- **q48 → D**: real option ঘ was '৮৭,৩৭২টি'; source had '৮৩৯০০টি'. Restored `option_d`, answer D (kgc #80). Source note's 87,391 figure is from the 2022 census.
- **q50 → A** (সেন্টমার্টিন): kgc #78 + exam-era convention. Source note (হাজীপুর/দৌলতখান) is 2022-census data, variable over time.
- **q53 → A**: real option ক was 'ওয়াশিংটন' (NASA HQ); source HTML corrupted it to 'ফ্লোরিডা' (our B/C/D match kgc #91 exactly). Restored `option_a`, answer A.
- **q56 → A** (নিকোলাস সার্কোজি): exam held Nov 2008 — Sarkozy was president (2007–2012). Source note about Macron is anachronistic; kgc #95's compilation adds 'ওঁলান্দ' as the answer which cannot be right at exam time (Hollande elected 2012).
- **q62 → A**: real option ক was '১০ ক্যালরি'; source HTML dropped the zero → '১ ক্যালরি'. Heat = 1 g × 1 cal/g°C × 10°C = 10 cal. Restored `option_a`, answer A (kgc #29). The earlier "no correct option" reading was caused by the corrupted option.
- **q91 → D**: real option ঘ was '20' (digit count: ten unit-place 5s + eleven in 50–59 incl. two in 55); source HTML corrupted it to '19'. Restored `option_d`, answer D (kgc #96 + ExamDao 28th). Supersedes the earlier math-audit fill of D=19.

## Manual / human check (image / empty options)

None.

## Image questions (verify manually)

None.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 20 |
| 2 | English Language & Literature | 24 |
| 3 | Bangladesh Affairs | 10 |
| 4 | International Affairs | 10 |
| 6 | General Science | 19 |
| 7 | Computer & Information Technology | 1 |
| 5 | Geography, Environment & Disaster Management | 3 |
| 9 | Mental Ability | 7 |
| 8 | Mathematical Reasoning | 6 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q47/q48/q53/q62/q91: source-HTML option corruption restored from kgc/ExamDao keys (see LLM pass)
- q50/q56: "সবচেয়ে ছোট"/"বর্তমান" questions — answered per exam era (2008), see LLM pass

## Validation

All hard checks passed.
