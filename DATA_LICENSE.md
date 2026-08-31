# DATA LICENSE — BCS Preliminary Question Bank

**This file covers the dataset. The code is under `LICENSE` (MIT). The dataset is NOT MIT.**

## 1. What this covers

* `bcs_preliminary_question_bank.json` (merged DB, `5,350` questions)
* `data/processed/json/*_bcs.json` (41 per-exam JSONs)
* `data/raw/html/*.html` (scraped HTML snapshots)
* `images/<exam_slug>/q*_img*` (825 images)
* Question text, options (`option_a..d`), `correct_answer`, `solve_note` and other question-level fields

It **does not** cover `pipeline/`, `scripts/`, validation code, HTML generators, and other tooling — those are MIT per `LICENSE`.

## 2. Source and ownership

* **Source of truth:** `https://uttoron.academy/QuestionBank` (QuestionPreview pages). See `instructions/links_to_scrape.md` and `topics_taxonomy.md` at root for scrape list and taxonomy.
* **Copyright in the underlying questions, explanations, and images remains with the original publisher(s)** — primarily Uttoron and/or the Bangladesh Public Service Commission (PSC) and other exam-content owners. **We do not claim ownership and we do not have a separate license from the publisher to re-license that content.**
* **We do not grant MIT (or any other open license) to the dataset itself.** The `LICENSE` (MIT) in this repository applies **only to code** as stated in `README.md#license`.

## 3. Why the dataset is not MIT

GitHub's docs note that when you upload third-party content you are responsible for having the right to post it, and that a repository license grants rights according to its terms. Because the questions/images are third-party copyrighted works, we cannot — by adding a `LICENSE` file — give you MIT rights to that third-party content unless we hold those rights.

Stating `MIT` for the dataset would imply we are licensing someone else's copyrighted material, which we are not.

## 4. Basis for distribution and limits

* This repository distributes a **structured database / compilation** of facts and exam materials for **educational, research, data-analysis, and application-development** purposes. We have cleaned the data (mojibake repair, 80+ math/text fixes, 26 image-only questions curated to text, `exam_slug` added) and validated it (`pipeline/validate.py:23`).
* We provide the compilation **as-is** under a **fair-use / fair-dealing** rationale for scholarship and research. **Labeling a use as "fair use" in a README does not itself make it fair use** — whether a particular downstream use qualifies depends on purpose, amount, market effect, nature of the work, and applicable law (which varies by jurisdiction).
* **Database / compilation copyright** (in selection, arrangement, cleaning) may exist separately from copyright in individual items. We do not assert a database right to restrict your non-commercial research use, but we also do not use a database right to grant you rights to the underlying third-party content.

## 5. What you may do — with your own legal assessment

You must make your own determination whether your intended use is permitted under applicable law (fair use/fair dealing, quotation, or with permission from the rights holder).

If you proceed, we ask (as a community norm, not as a license grant):

* Use for **educational, research, personal study, or non-commercial app prototyping** with attribution to this repository **and** the original source (`uttoron.academy`).
* **Do not** republish the full dataset as a paid coaching product, book, or paywalled course without permission from the rights holder.
* Do not misrepresent the source or claim endorsement by Uttoron/PSC.

This request does not change the legal status of the underlying rights.

## 6. Uploader responsibility (GitHub)

Per GitHub's guidance, the uploader is responsible for having the right to post content and a repository license only grants rights the uploader can grant. We have described our source and cleaning, but **we do not warrant that we have a license to grant MIT (or other) rights to the dataset**.

## 7. Takedown and correction

If you are a rights holder and believe content should be removed or attributed differently, open an issue or contact the maintainers — we will review promptly and remove or amend as appropriate. For corrections (wrong answer, missing image, subject fix), PRs with a source link are welcome (see `README.md#contributing`).

## 8. No warranty

The dataset is provided **as-is**, without warranty of accuracy, completeness, or fitness. Use at your own risk. We do not guarantee that any particular use will be considered fair use.

---

**In short:** `LICENSE` → MIT → `pipeline/`, `scripts/`, validation/tooling. `DATA_LICENSE.md` → this file → question data, solve notes, images. **Do not treat the dataset as MIT unless you have independently secured rights to do so.**
