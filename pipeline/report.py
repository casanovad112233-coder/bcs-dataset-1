"""Markdown run report for one exam."""
import json
from pathlib import Path

from .extract import ExamData
from .validate import ValidationResult


def write_report(exam: ExamData, summary: dict, validation: ValidationResult,
                 report_path: Path, json_path: Path, payload: dict) -> None:
    q_by_num = {q["question_number"]: q for q in payload["questions"]}
    lines: list[str] = []
    lines.append(f"# {exam.title} - pipeline report\n")
    lines.append(f"- Source HTML: `{exam.html_path.name}`")
    lines.append(f"- Output JSON: `{json_path.name}`")
    lines.append(f"- Date: {exam.date or 'n/a'} | Marks: {exam.total_marks or 'n/a'} | Set code: {exam.set_code or 'n/a'}")
    lines.append(f"- Questions: {len(payload['questions'])}\n")

    lines.append("## Needs LLM classification\n")
    if summary["needs_list"]:
        for n in summary["needs_list"]:
            lines.append(f"- q{n}: {q_by_num[n]['question'][:90]}")
        lines.append("\nSend these to the LLM (external call), then fill and rerun with `--classifications`:\n")
        lines.append("```json")
        lines.append(json.dumps({str(n): None for n in summary["needs_list"]}, ensure_ascii=False, indent=2))
        lines.append("```\n")
    else:
        lines.append("None.\n")

    lines.append("## Needs answers\n")
    blank = [q["question_number"] for q in payload["questions"] if not q["correct_answer"]]
    if blank:
        for n in blank:
            lines.append(f"- q{n}: {q_by_num[n]['question'][:90]}")
        lines.append("\nSend these to the LLM (external call), then fill and rerun with `--answers`:\n")
        lines.append("```json")
        lines.append(json.dumps({str(n): None for n in blank}, ensure_ascii=False, indent=2))
        lines.append("```\n")
    else:
        lines.append("None.\n")

    lines.append("## Needs solve notes\n")
    no_solve = [q["question_number"] for q in payload["questions"]
                if not q["solve_note"] and not q["solve_note_image_paths"]]
    if no_solve:
        for n in no_solve:
            lines.append(f"- q{n}: {q_by_num[n]['question'][:90]}")
        lines.append("\nSend these to the LLM (external call), then fill and rerun with `--solve-notes`:\n")
        lines.append("```json")
        lines.append(json.dumps({str(n): None for n in no_solve}, ensure_ascii=False, indent=2))
        lines.append("```\n")
    else:
        lines.append("None.\n")

    lines.append("## Image questions (verify manually)\n")
    img_q = [q for q in payload["questions"] if not q["question"] and q["question_image_paths"]]
    if img_q:
        lines.append("These questions have no text - the prompt lives in the image(s). "
                     "Please verify that the images and their paths are correct:\n")
        for q in img_q:
            qp = ", ".join(q["question_image_paths"]) or "-"
            sp = ", ".join(q["solve_note_image_paths"]) or "-"
            lines.append(f"- q{q['question_number']}: question=[{qp}], solve=[{sp}]")
        lines.append("")
    else:
        lines.append("None.\n")

    lines.append("## Subject distribution\n")
    lines.append("| subject_id | subject_en | count |")
    lines.append("|---|---|---|")
    dist: dict[int | None, int] = {}
    for q in payload["questions"]:
        dist[q["subject_id"]] = dist.get(q["subject_id"], 0) + 1
    for sid in sorted(dist, key=lambda x: x is not None):
        if sid is None:
            lines.append("| (unclassified) | needs LLM | {0} |".format(dist[sid]))
            continue
        q0 = next(q for q in payload["questions"] if q["subject_id"] == sid)
        lines.append(f"| {sid} | {q0['subject_en']} | {dist[sid]} |")

    lines.append("\n## Classification\n")
    lines.append(f"- Mapped from source tags: {summary['mapped'] - summary['file']}")
    lines.append(f"- Classified from file: {summary['file']}")
    lines.append(f"- Still need LLM classification: {summary['needs_classification']}")
    if summary["unknown_tags"]:
        lines.append(f"- Untagged source values: {', '.join(repr(t) for t in summary['unknown_tags'])}")

    lines.append("\n## Warnings (review these)\n")
    warnings: list[str] = []
    for q in payload["questions"]:
        if q["correct_answer"] == "":
            warnings.append(f"- q{q['question_number']}: correct_answer blank (source had no valid A-D answer)")
    for w in exam.warnings:
        if "data-answer" in w:
            continue
        warnings.append(f"- {w}")
    for w in validation.warnings:
        if w not in warnings:
            warnings.append(f"- {w}")
    if warnings:
        lines.extend(warnings)
    else:
        lines.append("None.")

    lines.append("\n## Validation\n")
    if validation.ok:
        lines.append("All hard checks passed.\n")
    else:
        lines.append("FAILED hard checks:\n")
        lines.extend(f"- ERROR: {e}" for e in validation.errors)
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")