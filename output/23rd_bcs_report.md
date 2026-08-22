# 23rd BCS - pipeline report

- Source HTML: `23rd_bcs.html`
- Output JSON: `23rd_bcs.json`
- Date: 2001-03-23 | Marks: 100 | Set code: সুরমা
- Questions: 100

## Needs LLM classification

None.

## Needs answers

- q25: বাংলাদেশ সিভিল সার্ভিসের (BCS) ক্যাডার কতটি?

Send these to the LLM (external call), then fill and rerun with `--answers`:

```json
{
  "25": null
}
```

## Needs solve notes

None.

## Image questions (verify manually)

None.

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 6 | General Science | 25 |
| 7 | Computer & Information Technology | 1 |
| 3 | Bangladesh Affairs | 4 |
| 4 | International Affairs | 20 |
| 8 | Mathematical Reasoning | 10 |
| 1 | Bangla Language & Literature | 20 |
| 2 | English Language & Literature | 20 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q25: correct_answer blank (source had no valid A-D answer)
- q25: correct_answer is blank (source had no valid answer)

## Validation

All hard checks passed.

## What has been done (LLM pass)

Exam date verified: **২৩ মার্চ ২০০১** (livemcq, w3classroom, jobprotidin; chakribangla's "১ জুন ২০০১" is an outlier). Filled via biddabari full solution (content-matched; their ordering differs from ours) plus era-certain reasoning:

- **q6 = D** (`সোডিয়াম মনোগ্লুটামেট`) — testing salt is MSG; biddabari keys "মনো সোডিয়াম গ্লুটামেট".
- **q27 = C** (`আব্দুর রহমান ওয়াহিদ`) — exam held 23 Mar 2001, before Megawati Sukarnoputri's 23 Jul 2001 takeover; Wahid was president Oct 1999–Jul 2001. Era-certain.
- **q45 = B** (`ফ্রাংক`) — Belgian franc circulated until euro cash (Jan 2002); era-certain. Note: biddabari's copy answers "ইউরো", a doctored present-day edit — original key was ফ্রাংক.
- Solve note added for q75 ('রামগরুড়ের ছানা' = গোমড়ামুখো লোক, B per biddabari).

Left blank as defective:

- **q25** — "BCS ক্যাডার কতটি?" Original options were {২৯, ২২, ২১, **২৬**} with keyed answer ২৬টি (biddabari reproduces the original set); uttoron corrupted option D `২৬টি`→`৫টি`, so the keyed value no longer exists among our options. Kept blank rather than attach a false value to D.

Validation PASSED (1 warning, intended).

