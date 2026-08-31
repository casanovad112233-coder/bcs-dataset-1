# bcs_question_bank — BCS Question Bank Database (10th to 50th BCS) | Bangladesh Civil Service Preliminary

> **The most complete open-source BCS Question Bank database for Bangladesh.** `41` exams (10th–50th) • `5,350` questions • `10` subjects • `825` images • UTF-8 Bangla + English • Ready for Supabase/Postgres, JSON, SQLite.

[![questions](https://img.shields.io/badge/questions-5,350-blue)](Bcs_Question_Bank_Db_10th_to_50th.json) [![exams](https://img.shields.io/badge/exams-41-green)](data/processed/json) [![license](https://img.shields.io/badge/license-MIT%20%2F%20CC%20BY--4.0-lightgrey)](#license) [![source](https://img.shields.io/badge/source-uttoron.academy-orange)](#data-source--copyright-policy)

**If you search `bcs_question_bank`, `bcs question bank`, `bcs database`, `bcs preliminary question bank` — this is the dataset.**

---

## Why this exists

No single, clean, machine-readable BCS database existed. Scraped pages are HTML-only, have mojibake, missing answers, and image-only questions. This repo scrapes **uttoron.academy** (source of truth), **repairs encoding, fixes 80+ errors, curates 26 image-only questions to text, adds `exam_slug` per row**, and validates every JSON before release. Use it as a **database only** — for apps, model tests, R&D, or research.

---

## Dataset at a glance

| Exams | Questions | Subjects | Images | Format | Encoding |
|------:|----------:|---------:|-------:|--------|----------|
| 41 (10th–50th) | **5,350** | 10 (fixed) | 825 (19 MB) | JSON + images | UTF-8 |

Per-exam counts (validated `exam.total_questions == len(questions)`):

`10th:100, 11st:100, 12nd:100, 13rd:100, 14th:100, 15th:100, 16th:100, 17th:100, 18th:100, 19th:50, 20th:100, 21st:100, 22nd:100, 23rd:100, 24th:100, 25th:100, 26th:200, 27th:100, 28th:100, 29th:100, 30th:100, 31st:100, 32nd:100, 33rd:100, 34th:100, 35th:200, 36th:200, 37th:200, 38th:200, 39th:100, 40th:200, 41st:200, 42nd:100, 43rd:200, 44th:200, 45th:200, 46th:200, 47th:200, 48th:100, 49th:100, 50th:200`

**Primary file (SEO-optimized names — same content):**
* `bcs_question_bank.json` — **canonical, use this** (for `bcs_question_bank` SEO)
* `bcs-question-bank.json` — alias
* `Bcs_Question_Bank_Db_10th_to_50th.json` — original name + `data/processed/Bcs_Question_Bank_Db_10th_to_50th.json` mirror
* Per-exam: `data/processed/json/10th_bcs.json … 50th_bcs.json`

Regenerate: `python -m pipeline.merge` (see `pipeline/merge.py:24`).

---

## File structure

```
bcs_question_bank.json                          # merged DB — start here
schema.md                                       # full schema + Supabase DDL
instructions/topics_taxonomy.md                 # 10 subjects (IDs 1..10)
data/processed/json/*_bcs.json                  # 41 per-exam JSONs
images/<exam_slug>/q<N>_img<K>.(jpg|png)        # 825 images, exam-scoped
pipeline/                                       # scrape → JSON → validate
17th_bcs_math.html / 17th_bcs_frontend.html     # math-rendered frontends
manual_verification_10th_50th.html              # human-verify image-only / blank answers
```

---

## Quick start

**Python (merged DB):**
```python
import json, pathlib
db = json.loads(pathlib.Path("bcs_question_bank.json").read_text(encoding="utf-8"))
print(db["metadata"])  # total_exams 41, total_questions 5350
q = db["questions"][0] # has exam_slug, subject_id, question, option_a..d, correct_answer, solve_note, has_image...
by_17th = [q for q in db["questions"] if q["exam_slug"]=="17th_bcs"]
```

**Per-exam:**
```python
import json
data = json.loads(open("data/processed/json/50th_bcs.json", encoding="utf-8").read())
print(data["exam"]) # title/date/set_code/total_questions
```

**Node / Supabase seed:**
```js
import db from './bcs_question_bank.json' assert {type:'json'};
// db.questions is 5,350 rows ready for bulk insert
// supabase.from('questions').insert(db.questions)
```

**Verify:**
```bash
python -m pipeline validate  # via pipeline/validate.py:23
```

---

## Schema

Full spec: **`schema.md`** — question object `pipeline/build.py:8` `QUESTION_KEYS` (`question_number, subject_id, question, option_a..d, correct_answer, solve_note, question_image_paths, solve_note_image_paths, has_*_image, has_image, subject_en/bn, exam_slug`), taxonomy, validation checklist `.agent/AGENTS.md:38`, and Supabase DDL (exams/questions/subjects + `exam_slug` denormalized, `GIN` on `text[]`, `tsvector`, RLS public read).

Example row:
```json
{
  "question_number": 1,
  "subject_id": 9,
  "question": "প্রশ্নের plain text",
  "option_a": "...", "option_b": "...", "option_c": "...", "option_d": "...",
  "correct_answer": "B",
  "solve_note": "ব্যাখ্যা...",
  "question_image_paths": [],
  "solve_note_image_paths": [],
  "has_image": 0,
  "subject_en": "Mental Ability",
  "subject_bn": "মানসিক দক্ষতা",
  "exam_slug": "17th_bcs"
}
```

---

## Data source & copyright policy

**Source of truth: [uttoron.academy](https://uttoron.academy/QuestionBank) — QuestionBank / QuestionPreview pages** (`instructions/links_to_scrape.md`). This repo **scraped** those pages via Firecrawl/`scrape_questions.py` to `data/raw/html/`, then deterministically parsed to JSON.

* **Copyright belongs to the original publisher (Uttoron / PSC).** This dataset is provided **as a database only** for educational, research, and app-development use under fair use. We **do not** republish as a coaching product or claim ownership. If you are the rights holder and want a takedown or attribution change, open an issue — we comply promptly.
* **We fixed errors:** 80+ math/text fixes, mojibake repair, `q70` option restoration (17th), 26 image-only questions curated to text (image retained), 30 missing 17th questions restored (70→100 on 2026-08-31). All fixes are logged in `instructions/memory.md`.
* **This is a database, not a course.** No video/lecture content. Use freely for apps, mock tests, analytics, LLM training.

---

## Frontend

* `17th_bcs_math.html` — 14 math questions of 17th BCS rendered with **MathJax** (fractions, exponents, roots)
* `17th_bcs_frontend.html` — all 100 Q of 17th BCS
* `manual_verification_10th_50th.html` — 44 manual + 26 curated (generated by `generate_manual_html.py`)

Open any `*.html` directly or `python -m http.server 8000`.

---

## Contributing

Any contribution is welcome — especially **answer/solve-note corrections, missing images, subject fixes.**

1. Fork → branch → edit `data/processed/json/*_bcs.json` **or** fix `data/raw/html/*.html` then `python -m pipeline <html>` (see `instructions/memory.md` for per-exam quirks).
2. Run validation: `python -m pipeline.validate` and `python -m pipeline.merge`
3. PR with before/after + source link (e.g., `livepublications`, `biddabari`).

Issues: `https://github.com/<you>/bcs_question_bank/issues`

---

## Keywords (for search)

`bcs_question_bank` `bcs question bank` `bcs database` `bcs question database` `bcs preliminary` `bcs 10th to 50th` `bcs 10th-50th` `bangladesh civil service` `bcs psc` `bcs preparation` `bcs model test` `bcs json` `bcs dataset` `uttoron bcs` `bcs supabase`

---

## License

* **Code** (`pipeline/`, `*.py`, `*.html` generators): **MIT**
* **Data** (`data/processed/json/`, `bcs_question_bank.json`, `images/`): **CC BY 4.0** — free to share/adapt with attribution to this repo + original source `uttoron.academy`. If your jurisdiction requires NC, treat commercial use as needing permission.

---

## Citation

```bibtex
@dataset{bcs_question_bank_2026,
  title  = {BCS Question Bank — 10th to 50th BCS (5,350 Q, 41 exams)},
  author = {BCS Open Source Contributors},
  year   = {2026},
  url    = {https://github.com/<you>/bcs_question_bank},
  note   = {Source: uttoron.academy, scraped and cleaned; UTF-8, exam_slug per row}
}
```

**Star & share if this saved you time — it helps others find `bcs_question_bank` on GitHub.**
