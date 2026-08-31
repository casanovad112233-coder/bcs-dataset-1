"""CLI entry point.

No LLM is ever called by this pipeline. Parsing, subject mapping (from the HTML
`data-subject` tag), JSON build, image download and validation are all
deterministic. Questions the pipeline cannot finish are listed in the report so
you can classify / answer them in an external LLM pass, then rerun.

Usage:
    python -m pipeline 49th_bcs.html
    python -m pipeline 48th_bcs.html --classifications output/48th_bcs_classification.json
    python -m pipeline 48th_bcs.html --answers output/48th_bcs_answers.json
    python -m pipeline <html> --dry-run          # parse only; write nothing

Workflow:
    1. Run once. The pipeline writes <stem>.json, images, and a report listing
       (a) questions needing subject classification, (b) questions with no answer,
       and (c) questions with no solve note. Empty {qnum: null} template files are
       written to output/ for each.
    2. Send those questions to an LLM (your own call), fill the templates with
       {qnum: <subject_id>}, {qnum: "A"|"B"|...} and {qnum: "<solve note>"}.
    3. Rerun with --classifications / --answers / --solve-notes. The JSON is
       completed and validation passes.
"""
import argparse
import json
import sys
from pathlib import Path

from .build import apply_answers, apply_solve_notes, write_exam_json
from .classify import classify
from .extract import parse_exam
from .images import save_images
from .report import write_report
from .taxonomy import load_taxonomy
from .validate import validate_json_file

ROOT = Path(__file__).resolve().parent.parent
# Canonical location is topics_taxonomy.md at root; keep legacy instructions fallback
_TAXONOMY_CANDIDATE = ROOT / "topics_taxonomy.md"
TAXONOMY_PATH = _TAXONOMY_CANDIDATE if _TAXONOMY_CANDIDATE.exists() else ROOT / "instructions" / "topics_taxonomy.md"
OUTPUT_DIR = ROOT / "output"
# Minimal tidy layout: raw HTML under data/raw/html, processed JSON under data/processed/json
RAW_HTML_DIR = ROOT / "data" / "raw" / "html"
PROCESSED_JSON_DIR = ROOT / "data" / "processed" / "json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="BCS exam HTML -> JSON pipeline (no LLM calls)")
    parser.add_argument("html", type=Path, help="scraped exam HTML file")
    parser.add_argument("--classifications", type=Path, default=None,
                        help="filled {question_number: subject_id} JSON "
                             "(default: output/<stem>_classification.json)")
    parser.add_argument("--answers", type=Path, default=None,
                        help="filled {question_number: \"A\"..\"D\"} JSON "
                             "(default: output/<stem>_answers.json)")
    parser.add_argument("--solve-notes", type=Path, default=None,
                        help="filled {question_number: \"text\"} JSON "
                             "(default: output/<stem>_solve_notes.json)")
    parser.add_argument("--out", type=Path, default=None, help="output JSON path (default <stem>.json)")
    parser.add_argument("--dry-run", action="store_true", help="parse only; write nothing")
    args = parser.parse_args(argv)

    # Resolve HTML path: support both old flat `49th_bcs.html` and new `data/raw/html/49th_bcs.html`
    html_path = args.html
    if not html_path.is_absolute():
        # Try as given, then fallback to RAW_HTML_DIR
        candidate = (Path.cwd() / html_path).resolve()
        if candidate.is_file():
            html_path = candidate
        elif (RAW_HTML_DIR / html_path.name).is_file():
            html_path = (RAW_HTML_DIR / html_path.name).resolve()
        else:
            html_path = candidate
    else:
        html_path = html_path.resolve()
    if not html_path.is_file():
        print(f"error: {html_path} not found (also tried {RAW_HTML_DIR / args.html.name})", file=sys.stderr)
        return 1

    taxonomy = load_taxonomy(TAXONOMY_PATH)
    exam = parse_exam(html_path)
    print(f"Parsed {exam.title}: {exam.total_questions} questions, "
          f"{len(exam.images)} image refs, {len(exam.warnings)} warnings")

    stem = exam.stem
    clf_path = (args.classifications or OUTPUT_DIR / f"{stem}_classification.json").resolve()
    ans_path = (args.answers or OUTPUT_DIR / f"{stem}_answers.json").resolve()
    sol_path = (args.solve_notes or OUTPUT_DIR / f"{stem}_solve_notes.json").resolve()
    summary = classify(exam, taxonomy, clf_path)
    print(f"Subjects: {summary['mapped']} mapped, "
          f"{summary['file']} from file, {summary['needs_classification']} need LLM classification")

    n_answers = apply_answers(exam, ans_path)
    print(f"Answers: {n_answers} filled from file, "
          f"{sum(1 for q in exam.questions if not q['correct_answer'])} still missing")

    n_solve = apply_solve_notes(exam, sol_path)
    print(f"Solve notes: {n_solve} filled from file, "
          f"{sum(1 for q in exam.questions if not q['solve_note'])} still missing")

    save_images(exam, dry_run=args.dry_run)

    if args.dry_run:
        print("Dry run: no JSON/report written")
        return 0

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if summary["needs_list"] and not clf_path.is_file():
        clf_path.write_text(
            json.dumps({str(n): None for n in summary["needs_list"]}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Needs classification -> {clf_path.relative_to(ROOT)} (fill and rerun)")
    blank_answers = [q["question_number"] for q in exam.questions if not q["correct_answer"]]
    if blank_answers and not ans_path.is_file():
        ans_path.write_text(
            json.dumps({str(n): None for n in blank_answers}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Needs answers -> {ans_path.relative_to(ROOT)} (fill and rerun)")
    blank_solve = [q["question_number"] for q in exam.questions if not q["solve_note"]]
    if blank_solve and not sol_path.is_file():
        sol_path.write_text(
            json.dumps({str(n): None for n in blank_solve}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Needs solve notes -> {sol_path.relative_to(ROOT)} (fill and rerun)")

    out_path = (args.out or PROCESSED_JSON_DIR / f"{stem}.json").resolve()
    report_path = OUTPUT_DIR / f"{out_path.stem}_report.md"

    payload = write_exam_json(exam, taxonomy, out_path)
    validation = validate_json_file(out_path, TAXONOMY_PATH)
    write_report(exam, summary, validation, report_path, out_path, payload)

    print(f"Wrote {out_path.relative_to(ROOT)}")
    print(f"Wrote {report_path.relative_to(ROOT)}")
    if validation.ok:
        n_warn = len(validation.warnings)
        print(f"Validation: PASSED ({n_warn} warnings)")
    else:
        print(f"Validation: FAILED ({len(validation.errors)} errors)", file=sys.stderr)
        for e in validation.errors:
            print(f"  ERROR: {e}", file=sys.stderr)
        return 1
    for w in validation.warnings:
        print(f"  warn: {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())