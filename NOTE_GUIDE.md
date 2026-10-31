# BCS Question Bank Note Guide

This guide explains how to navigate, use, and maintain the BCS preliminary question-bank repository. It reflects the files and pipeline currently in the repository; use the linked schema, taxonomy, and license documents as the authoritative detailed references.

## What is in this repository?

The project contains Bangla and English BCS preliminary exam questions, their four answer options, source-provided answers and solution notes, subject labels, and related images. The README describes the dataset as covering 10th through 50th BCS, with 41 exams and 5,350 questions. The stored question text is UTF-8; Bangla characters are kept as Unicode.

| Location | Purpose |
| --- | --- |
| `bcs_preliminary_question_bank.json` | Root-level merged dataset; convenient for importing or querying all exams together. |
| `data/processed/json/<exam_slug>.json` | One structured JSON file per exam; inputs used by the merge pipeline. |
| `data/raw/html/<exam_slug>.html` | Scraped HTML snapshots used as source material for extraction. |
| `images/<exam_slug>/` | Local question and solution images referenced by the JSON records. |
| `output/` | Per-exam reports and auxiliary answer, classification, and solve-note files, where present; also contains `defective.json` and `manual_check_queue.json`. |
| `pipeline/` | Python parsing, classification, image, JSON build, merge, reporting, and validation modules. |
| `scrape_questions.py` | Optional Firecrawl-based source-page downloader. |
| `topics_taxonomy.md` | Fixed subject IDs and bilingual subject names. |
| `schema.md` | Detailed JSON structure, field constraints, and import notes. |
| `instructions/links_to_scrape.md` | Source and reference URLs used by the project. |
| `instructions/memory.md` | Historical correction and maintenance notes. |

Exam slugs are canonical identifiers used in filenames, image directories, and question records (for example, `50th_bcs`). Some historical ordinals in this repository use the existing slugs `11st_bcs`, `12nd_bcs`, and `13rd_bcs`; keep the exact repository slug rather than normalizing it.

## Which data file should I use?

Use the root-level `bcs_preliminary_question_bank.json` when you need one combined dataset. Its top-level fields are `metadata` (dataset name/version, generation time, and totals), `taxonomy` (the 10 subject definitions), `exams` (one summary record for each exam), and `questions` (all questions, including `exam_slug` for filtering).

Use `data/processed/json/<exam_slug>.json` when you need a single exam. Each file contains `exam`, `taxonomy`, and `questions`. The merge command reads these per-exam JSON files and regenerates the root-level combined file.

```python
import json
from pathlib import Path

database = json.loads(
    Path("bcs_preliminary_question_bank.json").read_text(encoding="utf-8")
)
print(database["metadata"]["total_exams"])
questions_for_exam = [
    question
    for question in database["questions"]
    if question["exam_slug"] == "50th_bcs"
]
```

## Question and exam data

An exam record has a title, date, total marks, set code, and declared question count. Its `questions` array is sorted by `question_number`; the declared count should equal the array length.

Every question record includes:

| Field | Meaning |
| --- | --- |
| `question_number` | Exam-local question number. |
| `subject_id`, `subject_en`, `subject_bn` | Subject ID and its English/Bangla names from the taxonomy. |
| `question` | Plain-text prompt, with Bangla and mathematical text preserved where possible. |
| `option_a` through `option_d` | The four answer options as text. |
| `correct_answer` | `A`, `B`, `C`, `D`, or an empty string when the source has no valid answer. A blank is not an invitation to guess. |
| `solve_note` | Plain-text explanation; it may be empty when an explanation image is present or the source has no explanation. |
| `question_image_paths` | Local image paths belonging to the prompt. |
| `solve_note_image_paths` | Local image paths belonging to the explanation. |
| `has_question_image`, `has_solve_note_image`, `has_image` | Integer flags (`0` or `1`) derived from the image-path arrays. |
| `exam_slug` | Canonical exam identifier, matching the per-exam filename stem. |

Image paths are repository-relative strings such as `images/50th_bcs/q14_img1.png`; image bytes are stored in `images/`, not embedded in JSON. For a question that has both prompt and solution images, filenames use one sequence per question: prompt images first, followed by solution images. The `has_image` flag is `1` when either image array is non-empty.

An empty `correct_answer` is preserved for defective or unanswered source questions. `output/defective.json` records known defective cases; do not infer or fill an answer merely to make the data look complete. `output/` may also contain exam reports and work files used to fill missing answers, subjects, or solution notes. The report and auxiliary files are not replacements for the per-exam JSON or the merged dataset.

## Subject taxonomy

The taxonomy is fixed at 10 IDs and defined in `topics_taxonomy.md`. It covers Bangla Language & Literature, English Language & Literature, Bangladesh Affairs, International Affairs, Geography/Environment/Disaster Management, General Science, Computer & Information Technology, Mathematical Reasoning, Mental Ability, and Ethics/Values/Good Governance.

Every question must carry an integer `subject_id` from 1 to 10 and matching `subject_en` and `subject_bn` values. Do not invent, rename, reorder, or remove taxonomy entries. Update the JSON labels from the taxonomy rather than editing the names ad hoc.

## Install and run the pipeline

The code requires Python and the packages listed in `requirements.txt`:

```console
python -m pip install -r requirements.txt
```

To process an existing scraped exam page, run the module with its HTML path:

```console
python -m pipeline data/raw/html/50th_bcs.html
```

The pipeline extracts exam metadata, questions, options, source answer values, subject tags, solution text, and image references; writes the per-exam JSON; validates it; and writes a Markdown report under `output/`. Relative input paths are accepted, and the runner also checks `data/raw/html/` for the supplied filename.

Before rerunning a processed exam, note that the normal command writes the per-exam JSON and report again, and saves referenced image files. Preserve any manual work you need before regenerating those outputs. The command can also write missing-answer, classification, and solve-note templates under `output/`.

### Classification and missing information

Subject classification first maps the HTML `data-subject` tag using the known tag map in `pipeline/taxonomy.py`. Unrecognized or missing tags are left unclassified and listed in the report. The pipeline does not call an LLM.

For unresolved questions, the report and generated JSON templates identify the question numbers to review. Fill a classification file as a JSON object mapping question numbers to taxonomy IDs, for example:

```json
{
  "12": 8
}
```

Then rerun with the corresponding options:

```console
python -m pipeline data/raw/html/50th_bcs.html --classifications output/50th_bcs_classification.json --answers output/50th_bcs_answers.json --solve-notes output/50th_bcs_solve_notes.json
```

Answer files map question numbers to `A`–`D`; solve-note files map them to non-empty explanatory text. These files only fill values that are blank in the source-derived question. Existing source values are retained, and invalid or blank template entries are not applied. Review the report and source references before adding a correction.

`--dry-run` skips writing the exam JSON and report. It still parses the page and executes the image-processing path with dry-run enabled; it should not be treated as a general guarantee that no network request or filesystem directory is touched.

### Merge the per-exam JSON files

After updating per-exam JSON files, rebuild the root dataset with:

```console
python -m pipeline.merge
```

An alternate destination can be supplied with `--out`:

```console
python -m pipeline.merge --out path/to/combined.json
```

The merge reads `data/processed/json/*_bcs.json`, orders exams numerically, and orders questions by exam and question number. It updates the generated timestamp and combined counts each time. Do not hand-edit the merged file as the sole change: a later merge will replace those edits.

### Validation

Normal pipeline processing runs `pipeline.validate.validate_json_file` after writing the per-exam JSON. A successful validation has no hard errors; warnings can still indicate blank answers, image-only prompts that need visual checking, or absent solution text.

The current package has no `validate` subcommand. To validate a file directly from Python:

```python
from pathlib import Path
from pipeline.validate import validate_json_file

result = validate_json_file(
    Path("data/processed/json/50th_bcs.json"),
    Path("topics_taxonomy.md"),
)
print("OK" if result.ok else "\n".join(result.errors))
print("\n".join(result.warnings))
```

Validation checks JSON/UTF-8 readability, sequential question numbering, required option string fields, answer values, taxonomy agreement, known mojibake markers, image paths and flags, and `exam_slug` consistency. It allows blank answers as warnings rather than supplying a guess. A generated report helps find questions requiring human review.

## Optional scraping

`scrape_questions.py` downloads source HTML for URLs in `instructions/links_to_scrape.md` using Firecrawl and writes snapshots under `data/raw/html/`. It skips pages that already have a saved snapshot, supports `--only` to filter by a URL substring, and can wait between pages with `--delay`. Scraping requires network access and a Firecrawl API key supplied through `.env` (`FIRECRAWL_API_KEY`; the script also accepts `FIREWORKS_API_KEY`). Do not commit credentials.

The scraper is optional when using the HTML snapshots already stored in the repository. The HTML extraction and JSON-processing pipeline is deterministic and does not itself call an LLM.

## Supplementary practice-app references

The supplied `BCS Preliminary Question Bank.html` is a standalone bilingual
question-bank interface, and `BCS_Preliminary_Merged.html` combines a question
bank with five timed practice sets. The `BCS_Final_Review_5_Sets` references
focus on five sets of 200 questions each, with subject distribution, answer
feedback, review marking, and result summaries. These HTML files are interface
references; they are not generated by the repository's Python pipeline and are
not the canonical question data.

Before adapting one of these pages, verify its data source and intended schema.
The supplied practice-page code fetches its merged JSON from
`SangbitDas/bcs-dataset`, which is not this repository
(`casanovad112233-coder/bcs-dataset-1`). Update the endpoint deliberately if the
page should load data from this project, and confirm the fetched JSON includes
the fields the page expects. The references also state that the dataset is
compiled secondary material and that answers have not all been independently
checked against official BPSC keys; keep that limitation visible and verify
important answers against authoritative sources.

## Review and maintenance checklist

Before treating a changed exam as ready:

1. Confirm the question count matches `exam.total_questions` and numbering is sequential.
2. Check subject IDs and bilingual names against `topics_taxonomy.md`.
3. Keep source answer gaps blank unless verified by a trustworthy reference; investigate known defective questions instead of forcing an option.
4. Confirm image paths exist, belong to the correct exam, and point to the correct prompt or solution. Check image-only prompts visually.
5. Review the generated report for missing classifications, answers, notes, warnings, and validation errors.
6. If per-exam JSON changed, regenerate the merged root JSON and confirm that its counts reflect the per-exam files.
7. Record significant manual corrections in `instructions/memory.md`, and provide a source reference for corrections where possible.

The exact field requirements and validator behavior are documented in `schema.md`, and the repository-specific extraction guidance is in `.agent/AGENTS.md`.

## Source, attribution, and licenses

The repository identifies Uttoron Academy's QuestionBank/QuestionPreview pages as the primary source for the HTML snapshots. `instructions/links_to_scrape.md` also lists answer-verification references. Attribution and any downstream use must respect the rights of the original publishers and exam-content owners.

The code license and dataset terms are different:

- `LICENSE` applies to the project's code and tooling.
- `DATA_LICENSE.md` covers the dataset, question text, answers, solution notes, HTML snapshots, and images. The dataset is **not** MIT-licensed by this repository, and the repository does not claim ownership of the underlying third-party content.

Read `DATA_LICENSE.md` before redistributing or using the dataset in a product. The data is provided as-is; the repository does not warrant completeness or accuracy. Rights holders can request corrections or removal through the maintainer contact/issue process described there.