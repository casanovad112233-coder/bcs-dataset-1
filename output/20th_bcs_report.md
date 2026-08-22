# 20th BCS - pipeline report

- Source HTML: `20th_bcs.html`
- Output JSON: `20th_bcs.json`
- Date: 1998-12-11 | Marks: 100 | Set code: পদ্ম
- Questions: 100

## Needs LLM classification

None.

## Needs answers

None.

## Needs solve notes

None.

## Image questions (verify manually)

None.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 20 |
| 2 | English Language & Literature | 20 |
| 3 | Bangladesh Affairs | 20 |
| 4 | International Affairs | 20 |
| 6 | General Science | 10 |
| 8 | Mathematical Reasoning | 10 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

None.

## Validation

All hard checks passed.

## What has been done (LLM pass)

Exam date verified: **11 December 1998** (metadata; biddabari header "২০তম বিসিএস প্রিলিমিনারি পরীক্ষা-১৯৯৮ / পরীক্ষার তারিখ: ১১-১২-১৯৯৮"). Set: পদ্ম. Sources: biddabari 20th (`https://biddabari.com/bcs-question-bank/-20th-BCS-Question-Solution-Biddabari`) — notably the 20th biddabari copy is *not* present-day-doctored (it keys era-correct values), unlike the 21st/22nd/23rd copies.

Filled from `output/20th_bcs_answers.json` (2):

- **q49 = C** (`৩০টি`) — reserved women's seats in Jatiya Sangsad. Era-correct for Dec 1998 = 30 (raised to 50 only by the 15th Amendment 2011). biddabari keys ৩০ and adds a note about the 2011 change, but the *answer* remains the era value. Our source left it blank.
- **q58 = C** (`৬৮ জন`) — Bir Uttom recipients. 68 freedom fighters awarded Bir Uttom (7 Bir Shreshtho + 68 Bir Uttom + 175 Bir Bikram + 426 Bir Protik). Era-certain. Our source left it blank.

Solve notes filled from `output/20th_bcs_solve_notes.json` (10): q2 (spelling শুশ্রূষা), q12 (ব্যাঙের সর্দি = impossible/fictional), q19 (কাক ভূষণ্ডি = long-lived person), q34 (dilly dally = waste time), q36 (passive 'was being helped'), q37 (rumour as primitive man's newspaper — note: source value A overridden, see below), q38 (rumors hardy in growth), q39 (wartime news = limited information), q40 (author's attitude = philosophical interest — note: source value overridden, see below), q60 (Hitler quote).

Post-pipeline **source-error corrections** (edited directly in `20th_bcs.json` because the pipeline only fills *blanks*; these questions arrived non-blank but with wrong answers from our HTML source — biddabari's pristine 20th page overrules them):

- **q37: 'A' → 'C'** — "The author is mainly concerned with" on the rumour passage. Our source keyed (A) the nature of rumour; correct per passage's literal opening ("Rumour is the most primitive way ... primitive man's newspaper") and biddabari key = (C) 'rumour as primitive man's newspaper'.
- **q40: 'C' → 'B'** — "author's personal attitude toward rumor". Our source keyed (C) 'Acute indignation'; the author's tone is analytical/observational (notes fears, suspicions, hopes, daydreams without condemnation) → biddabari key = (B) 'Philosophical interest'.

These are the first *answer-value* overrides on this exam (not option-text fixes as in 28th/36th); flagged in notes for reviewer visibility. No defective-blank questions on the 20th; 15 image-only questions (q-suffixed) remain under manual review.
