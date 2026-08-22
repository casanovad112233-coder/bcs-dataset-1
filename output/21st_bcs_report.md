# 21st BCS - pipeline report

- Source HTML: `21st_bcs.html`
- Output JSON: `21st_bcs.json`
- Date: 1999-12-24 | Marks: 100 | Set code: সুরমা
- Questions: 100

## Needs LLM classification

None.

## Needs answers

None.

## Needs solve notes

None.

## Image questions (verify manually)

These questions have no text - the prompt lives in the image(s). Please verify that the images and their paths are correct:

- q21: question=[images/21st_bcs/q21_img1.jpg], solve=[images/21st_bcs/q21_img2.jpg]

## Subject distribution

| subject_id | subject_en | count |
|---|---|---|
| 1 | Bangla Language & Literature | 20 |
| 2 | English Language & Literature | 20 |
| 8 | Mathematical Reasoning | 10 |
| 5 | Geography, Environment & Disaster Management | 17 |
| 3 | Bangladesh Affairs | 5 |
| 4 | International Affairs | 18 |
| 6 | General Science | 10 |

## Classification

- Mapped from source tags: 100
- Classified from file: 0
- Still need LLM classification: 0

## Warnings (review these)

- q21: image-only question (empty text) - verify image paths manually

## Validation

All hard checks passed.

## What has been done (LLM pass)

Exam date verified 1999-12-24 (metadata; Set সুরমা). Sources: biddabari 21st (`https://biddabari.com/bcs-question-bank/21th-BCS-Question-Solution`), chakribangla 21-bcs, TI CPI archives, contemporary 1998-2001 news. Note: biddabari AND chakribangla both present-day-doctored the income & cadre questions (21st-bcs income key=২৭৯৩ present-day, cadre keyless with note "১৯৮৫=২৯ / ২০১৮=২৬"; chakribangla variant answers cadre=২৬). Era facts used where sources diverge from the exam window.

Filled from `output/21st_bcs_answers.json` (7):

- **q51 = D** (`২৫টি`) — option_d restored `৫টি`→`২৫টি` (uttoron corrupted; biddabari's pristine 21st shows D=২৫টি); era-era count ~25 cadres by late 1990s. DISPUTED: chakribangla's variant paper lists D=২৬টি and biddabari left it keyless.
- **q66 = D** (`৪০০ ডলার`) — era: Bangladesh per-capita income ~$370-400 around FY1999-2000 (WB Atlas ~$370 in 1999). biddabari + chakribangla both doctored option D → '২৭৯৩' and keyed the present-day value; restored era value $400 (option D). DISPUTED: no pristine-era source confirmed the exact letter, but $400 is the era-appropriate figure and the only value among our options in that range.
- **q69 = C** (`শ্রীলংকা`) — SAARC literacy rate circa 1999: Sri Lanka ~91% (highest among our four options {India, Bangladesh, Sri Lanka, Nepal}). NOTE: biddabari/chakribangla show a doctored 4th option 'মালদ্বীপ' (Maldives) as the present-day answer, but our paper's option D = 'নেপাল', which had ~29% literacy in 1999 — lowest. Era-correct among our actual options = C.
- **q70 = B** (`১১টি`) — OPEC membership Dec 1999 = 11 (Gabon withdrew Jan 1996; USA still member until Dec 2002). biddabari + chakribangla both key "১২টি" — the pre-1996 count (anachronistic). Era-correct = 11 (option B).
- **q75 = C** (`আবদুর রহমান ওয়াহিদ`) — Abdur Rahman Wahid elected Indonesia president 20 October 1999; exam 24 Dec 1999 ("নতুন রাষ্ট্রপতি"). biddabari/chakribangla doctored option D (বিরান্তো→present-day name) but key letter D; era-correct letter C.
- **q76 = C** (`পাকিস্তান`) — Pakistan suspended from Commonwealth councils after Pervez Musharraf's 12 Oct 1999 coup (suspension announced at Durban CHOGM Nov 1999). Nigeria had rejoined in May 1999, so "সম্প্রতি বহিষ্কার" at Dec 1999 = Pakistan. Era-certain.
- **q90 = A** (`বাংলাদেশ`) — only option where (per 1991-census-era data still cited in 1990s) male life expectancy exceeded female (BD male ~54.6 vs female ~53.4); Japan/Sweden/Singapore all have female > male by wide margins even in 1999. Era-reasoned: A.

Solve note filled for q31 (English reading passage "true learning leads to ...") — key = 'better expressive powers' per biddabari; note written generically since the passage text is not embedded in our HTML.

Image question q21 (and the q22–q31 reading block it carries) remains under manual/human check — image not viewable by the model this session.
