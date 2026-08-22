"""Assemble the final exam JSON in the exact AGENTS.md schema order."""
import json
from pathlib import Path

from .extract import ExamData
from .taxonomy import taxonomy_list

QUESTION_KEYS = [
    "question_number",
    "subject_id",
    "question",
    "option_a",
    "option_b",
    "option_c",
    "option_d",
    "correct_answer",
    "solve_note",
    "question_image_paths",
    "solve_note_image_paths",
    "has_question_image",
    "has_solve_note_image",
    "has_image",
    "subject_en",
    "subject_bn",
]


def build_exam_json(exam: ExamData, taxonomy: dict[int, dict[str, str]]) -> dict:
    questions = []
    for q in sorted(exam.questions, key=lambda x: x["question_number"]):
        questions.append({key: q[key] for key in QUESTION_KEYS})
    return {
        "exam": {
            "title": exam.title,
            "date": exam.date,
            "total_marks": exam.total_marks,
            "set_code": exam.set_code,
            "total_questions": len(questions),
        },
        "taxonomy": taxonomy_list(taxonomy),
        "questions": questions,
    }


def write_exam_json(exam: ExamData, taxonomy: dict[int, dict[str, str]], out_path: Path) -> dict:
    payload = build_exam_json(exam, taxonomy)
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return payload


def apply_answers(exam: ExamData, answers_file: Path | None) -> int:
    """Fill blank correct_answer values from a {qnum: "A"|"B"|"C"|"D"} file.

    Only questions with a blank answer are touched. Returns number applied.
    """
    if answers_file is None or not answers_file.is_file():
        return 0
    data = json.loads(answers_file.read_text(encoding="utf-8"))
    applied = 0
    for qnum, letter in data.items():
        letter = str(letter).strip().upper() if letter is not None else ""
        if letter not in ("A", "B", "C", "D"):
            continue
        for q in exam.questions:
            if q["question_number"] == int(qnum):
                if not q["correct_answer"]:
                    q["correct_answer"] = letter
                    applied += 1
                else:
                    exam.warnings.append(f"q{qnum}: answer file ignored, source already has {q['correct_answer']}")
                break
    return applied


def apply_solve_notes(exam: ExamData, solve_notes_file: Path | None) -> int:
    """Fill blank solve_note values from a {qnum: "text"} file.

    Only questions with a blank solve_note are touched. Returns number applied.
    """
    if solve_notes_file is None or not solve_notes_file.is_file():
        return 0
    data = json.loads(solve_notes_file.read_text(encoding="utf-8"))
    applied = 0
    for qnum, text in data.items():
        text = str(text).strip() if text is not None else ""
        if not text:
            continue
        for q in exam.questions:
            if q["question_number"] == int(qnum):
                if not q["solve_note"]:
                    q["solve_note"] = text
                    applied += 1
                else:
                    exam.warnings.append(f"q{qnum}: solve-note file ignored, source already has one")
                break
    return applied
