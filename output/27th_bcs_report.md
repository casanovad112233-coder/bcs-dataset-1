# 27th BCS - pipeline report

- Source HTML: `27th_bcs.html`
- Output JSON: `27th_bcs.json`
- Date: 2005-11-18 | Marks: 100 | Set code: সুরমা
- Questions: 100

## Needs LLM classification

None.

## Needs answers

None — all filled in the LLM pass (see below).

## Needs solve notes

None — note written for q53; notes added for q54, q61, q97, q100.

## What has been done (LLM pass)

Filled directly in `27th_bcs.json` (do not re-run the pipeline from HTML for this exam):

- **q53** solve note written: UNDP HDR 2005 per capita income $1,770 is PPP-based (nominal then ~$444). Answer was already D — consistent with kgc #21.
- **q54 → D** (৪২৬ জন): source note itself confirms 426 Bir Protik (7 Birshreshtha, 68 Bir Uttom, 175 Bir Bikrom); kgc #22 agrees.
- **q61 → D**: real exam option ঘ was '৫.৫৮' কিমি (the proposed Padma Bridge length at exam time); source HTML corrupted it to '৬.৮'. Restored `option_d`, answer D (kgc #29's other three options match ours exactly; biddabari kept '৬.৮' but gave no answer).
- **q97 → D (২৬)** [disputed]: ARF had 25 members at exam time (Nov 2005) — Bangladesh became the 26th in July 2006 — so strictly no option matched. Neither kgc nor biddabari marks an answer. Filled ২৬ as most acceptable: the setter evidently built options around Bangladesh's pending accession.
- **q100 → C** (কুর্দি): Talabani was Kurdish; kgc #68 + biddabari #100 agree. Source note about Rashid is current-day data.

## Manual / human check (image / empty options)

None.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 20 |
| 2 | English Language & Literature | 20 |
| 8 | Mathematical Reasoning | 10 |
| 3 | Bangladesh Affairs | 20 |
| 6 | General Science | 10 |
| 4 | International Affairs | 20 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q61: source-HTML option corruption restored from kgc key (see LLM pass)
- q97: disputed — exam-era count (25) not among options; D=26 filled as most acceptable (see LLM pass)
- q100: "বর্তমান" question — answered per exam era (2005), see LLM pass

## Validation

All hard checks passed.
