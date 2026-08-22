"""Subject classification: deterministic data-subject tag map + optional external file.

The pipeline never calls an LLM. Questions with no `data-subject` tag (or an
unmappable one) are left with subject_id=None and listed in the report so the
user can classify them in an external LLM pass, save `{qnum: subject_id}` to a
file, and rerun with `--classifications`.
"""
import json
from pathlib import Path

from .extract import ExamData


def classify(exam: ExamData, taxonomy: dict[int, dict[str, str]],
             classifications_file: Path | None = None) -> dict:
    """Assign subject_id/subject_en/subject_bn to every question.

    Priority: source data-subject tag -> classifications_file (if provided and present).
    Questions still unmapped get subject_id=None and are reported for an external LLM pass.

    Returns summary dict:
        {"mapped": int, "file": int, "needs_classification": int,
         "needs_list": [qnum, ...], "unknown_tags": [..], "assigned": {qnum: sid}}
    """
    from .taxonomy import map_subject_tag

    unknown: list[int] = []
    unknown_tags: list[str] = []
    for q in exam.questions:
        sid = map_subject_tag(q["subject_tag"])
        if sid is None:
            unknown.append(q["question_number"])
            tag = q["subject_tag"] or "(empty)"
            if tag not in unknown_tags:
                unknown_tags.append(tag)
        else:
            q["subject_id"] = sid

    file_assigned: dict[int, int] = {}
    if unknown and classifications_file is not None and classifications_file.is_file():
        data = json.loads(classifications_file.read_text(encoding="utf-8"))
        for qnum, sid in data.items():
            try:
                sid = int(sid)
            except (TypeError, ValueError):
                continue  # null / unfilled template entry
            if sid not in taxonomy:
                raise ValueError(f"classifications file: invalid subject_id {sid} for q{qnum}")
            if int(qnum) not in unknown:
                exam.warnings.append(f"q{qnum}: classification file entry ignored (tag already mapped)")
                continue
            file_assigned[int(qnum)] = sid

    for q in exam.questions:
        qnum = q["question_number"]
        if "subject_id" not in q:
            q["subject_id"] = file_assigned.get(qnum)
        if q["subject_id"] is None:
            q["subject_en"] = ""
            q["subject_bn"] = ""
        else:
            info = taxonomy[q["subject_id"]]
            q["subject_en"] = info["subject_en"]
            q["subject_bn"] = info["subject_bn"]

    needs_list = [n for n in unknown if n not in file_assigned]
    return {
        "mapped": sum(1 for q in exam.questions if q["subject_id"] is not None),
        "file": len(file_assigned),
        "needs_classification": len(needs_list),
        "needs_list": needs_list,
        "unknown_tags": unknown_tags,
        "assigned": file_assigned,
    }