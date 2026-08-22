# 22nd BCS - pipeline report

- Source HTML: `22nd_bcs.html`
- Output JSON: `22nd_bcs.json`
- Date: 2001-02-02 | Marks: 100 | Set code: চামেলী
- Questions: 100

## Needs LLM classification

None.

## Needs answers

- q23: রাশিয়ার কুরস্ক নামক সাবমেরিনটির ওজন কত টন?

Send these to the LLM (external call), then fill and rerun with `--answers`:

```json
{
  "23": null
}
```

## Needs solve notes

None.

## Image questions (verify manually)

These questions have no text - the prompt lives in the image(s). Please verify that the images and their paths are correct:

- q61: question=[images/22nd_bcs/q61_img1.jpg], solve=[-]
- q62: question=[images/22nd_bcs/q62_img1.jpg], solve=[-]
- q63: question=[images/22nd_bcs/q63_img1.jpg], solve=[-]
- q64: question=[images/22nd_bcs/q64_img1.jpg], solve=[-]
- q65: question=[images/22nd_bcs/q65_img1.jpg], solve=[-]
- q70: question=[images/22nd_bcs/q70_img1.jpg], solve=[-]
- q71: question=[images/22nd_bcs/q71_img1.jpg], solve=[-]
- q72: question=[images/22nd_bcs/q72_img1.jpg], solve=[-]
- q73: question=[images/22nd_bcs/q73_img1.jpg], solve=[-]
- q74: question=[images/22nd_bcs/q74_img1.jpg], solve=[-]
- q75: question=[images/22nd_bcs/q75_img1.jpg], solve=[-]

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 3 | Bangladesh Affairs | 21 |
| 4 | International Affairs | 19 |
| 1 | Bangla Language & Literature | 20 |
| 2 | English Language & Literature | 20 |
| 8 | Mathematical Reasoning | 10 |
| 6 | General Science | 10 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q23: correct_answer blank (source had no valid A-D answer)
- q23: correct_answer is blank (source had no valid answer)
- q61: image-only question (empty text) - verify image paths manually
- q62: image-only question (empty text) - verify image paths manually
- q63: image-only question (empty text) - verify image paths manually
- q64: image-only question (empty text) - verify image paths manually
- q65: image-only question (empty text) - verify image paths manually
- q70: image-only question (empty text) - verify image paths manually
- q71: image-only question (empty text) - verify image paths manually
- q72: image-only question (empty text) - verify image paths manually
- q73: image-only question (empty text) - verify image paths manually
- q74: image-only question (empty text) - verify image paths manually
- q75: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.

## What has been done (LLM pass)

Exam date verified as 2 February 2001 (metadata; Set চামেলী). Sources: biddabari 22nd (`https://biddabari.com/bcs-question-bank/22th-BCS-Question-Solution-Biddabari`), TI CPI archives, contemporary NAM reporting. Note: biddabari's own copy of the 22nd is present-day doctored (UN=১৯৩, Kursk=২৪,০০০, TI=সোমালিয়া, NAM=১২০, Dhaka-districts=১৩টি) — none of its keys were used where era facts differ.

Filled from `output/22nd_bcs_answers.json` (5):

- **q14 = C** (`ঢাকা`) — era-certain: at Durban 1998 Bangladesh was chosen to host the 13th NAM Summit in 2001 and only withdrew its offer on **16 October 2001** (after this exam), whereupon Jordan, then Malaysia, took over → KL Feb 2003. Contemporary confirmation: Lim Kit Siang media statement, limkitsiang.com/archive/2003/feb03/lks2114.htm.
- **q18 = B** (`১৮৯`) — UN membership was 189 between Tuvalu's admission (Sep 2000) and Switzerland's (Sep 2002); exam sat in that window. biddabari's "১৯৩" is a present-day figure not present among our options.
- **q24 = B** (`নাইজেরিয়া`) — TI CPI 2000: Nigeria ranked last (90/90, score 1.2); Bangladesh first entered the CPI only with the 2001 index, published after this exam ("second-most corrupt, second only to Bangladesh" per CPI 2001). biddabari's "সোমালিয়া" is present-day data.
- **q33 = B** (`১৭টি`) — Dhaka division had 17 districts until the Mymensingh division split (2015); biddabari's keyed "১৩টি" is post-split.
- **q36 = C** (`১১৪`) — NAM had 113 members at the Durban summit (Sep 1998) and 114 through early 2003 (KL summit: "114 member nations", Lim Kit Siang, 24 Feb 2003); Belarus joined in 1998 making 114 by exam time. 118 was reached only 2006–2011, 120 since May 2011.

Solve notes filled from `output/22nd_bcs_solve_notes.json` (2): q31 (সোনালী আঁশ = পাট → বাংলাদেশ), q60 ('ঢাকের কাঠি' = তোষামুদে).

Defective blank (1):

- **q23** — "কুরস্ক সাবমেরিনের ওজন": both uttoron and biddabari key **২৪,০০০** টন, but our paper's option D reads `১৫,০০০` — the keyed value does not exist among our options (option set corrupted). Left blank rather than attach the key to a value it never named. Image-only questions q61–65, q70–75 still need manual image verification.
