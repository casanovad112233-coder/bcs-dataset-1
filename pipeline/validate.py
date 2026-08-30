"""Validation checklist per AGENTS.md, run on a produced exam JSON."""
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from .common import MOJIBAKE_MARKERS
from .taxonomy import load_taxonomy

VALID_ANSWERS = {"A", "B", "C", "D"}


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_json_file(path: Path, taxonomy_path: Path, expected_stem: str | None = None) -> ValidationResult:
    taxonomy = load_taxonomy(taxonomy_path)
    result = ValidationResult()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        result.errors.append(f"{path.name}: file is not valid UTF-8")
        return result
    except json.JSONDecodeError as exc:
        result.errors.append(f"{path.name}: JSON does not parse: {exc}")
        return result

    exam_meta = data.get("exam", {})
    questions = data.get("questions", [])
    stem = expected_stem or re.sub(r"\s+", "_", path.stem).lower().strip("_")

    if exam_meta.get("total_questions") != len(questions):
        result.errors.append(
            f"exam.total_questions={exam_meta.get('total_questions')} but questions array has {len(questions)}"
        )

    seen_numbers = set()
    for i, q in enumerate(questions, 1):
        where = f"q{q.get('question_number', i)}"

        if not isinstance(q.get("question_number"), int):
            result.errors.append(f"{where}: question_number is not an integer")
        n = q.get("question_number")
        if n in seen_numbers:
            result.errors.append(f"{where}: duplicate question_number")
        seen_numbers.add(n)
        if n != i:
            result.errors.append(f"{where}: sequence gap (expected {i})")

        if not (isinstance(q.get("question"), str) and q["question"].strip()):
            q_imgs = q.get("question_image_paths") or []
            s_imgs = q.get("solve_note_image_paths") or []
            if q_imgs:
                result.warnings.append(f"{where}: image-only question (empty text) - verify image paths manually")
            elif s_imgs:
                result.errors.append(f"{where}: question text is empty and no question image; "
                                     "an image exists only in the solve note (misplaced?)")
            else:
                result.errors.append(f"{where}: question text is empty and no question image")

        if "question_html" in q:
            result.errors.append(f"{where}: stray question_html field present")
        if "image_paths" in q:
            result.errors.append(f"{where}: stray generic image_paths field present")

        for field_name in OPTION_FIELDS:
            if field_name not in q or not isinstance(q[field_name], str):
                result.errors.append(f"{where}: option field {field_name} missing or not a string")
                continue
            if not q[field_name].strip() and field_name in ("option_a", "option_d"):
                result.warnings.append(f"{where}: {field_name} is empty")

        ca = q.get("correct_answer")
        if ca in VALID_ANSWERS:
            pass
        elif ca == "":
            result.warnings.append(f"{where}: correct_answer is blank (source had no valid answer)")
        else:
            result.errors.append(f"{where}: correct_answer {ca!r} is not A-D or ''")

        sid = q.get("subject_id")
        if sid is None:
            result.errors.append(f"{where}: subject_id is null - needs LLM classification (fill classification file)")
        elif not isinstance(sid, int) or sid not in taxonomy:
            result.errors.append(f"{where}: subject_id {sid!r} not in taxonomy")
        else:
            info = taxonomy[sid]
            if q.get("subject_en") != info["subject_en"]:
                result.errors.append(f"{where}: subject_en {q.get('subject_en')!r} != taxonomy {info['subject_en']!r}")
            if q.get("subject_bn") != info["subject_bn"]:
                result.errors.append(f"{where}: subject_bn mismatch with taxonomy")

        blob = " ".join(
            str(q.get(key, ""))
            for key in ("question", "option_a", "option_b", "option_c", "option_d",
                        "solve_note", "subject_en", "subject_bn")
        )
        for marker in MOJIBAKE_MARKERS:
            if marker in blob:
                result.errors.append(f"{where}: mojibake marker {marker!r} found in text")
                break

        q_imgs = q.get("question_image_paths")
        s_imgs = q.get("solve_note_image_paths")
        if not isinstance(q_imgs, list) or not isinstance(s_imgs, list):
            result.errors.append(f"{where}: image path arrays missing or not lists")
            continue
        for p in list(q_imgs) + list(s_imgs):
            if not (Path(".") / p).exists():
                result.errors.append(f"{where}: referenced image does not exist: {p}")
            if not p.startswith(f"images/{stem}/"):
                result.warnings.append(f"{where}: image path {p} is not exam-scoped under images/{stem}/")

        if not q.get("solve_note") and not s_imgs:
            result.warnings.append(f"{where}: solve_note empty and no solve images (no solution in source)")

        hq = 1 if q_imgs else 0
        hs = 1 if s_imgs else 0
        hi = 1 if (hq or hs) else 0
        if q.get("has_question_image") != hq:
            result.errors.append(f"{where}: has_question_image flag mismatch")
        if q.get("has_solve_note_image") != hs:
            result.errors.append(f"{where}: has_solve_note_image flag mismatch")
        if q.get("has_image") != hi:
            result.errors.append(f"{where}: has_image flag mismatch")

        # exam_slug must be the canonical exam stem (e.g. "50th_bcs") and match the file
        exam_slug = q.get("exam_slug")
        if not isinstance(exam_slug, str) or not exam_slug:
            result.errors.append(f"{where}: exam_slug missing or not a string")
        elif exam_slug != stem:
            result.errors.append(f"{where}: exam_slug {exam_slug!r} != file stem {stem!r}")
        elif not re.fullmatch(r"\d+(?:st|nd|rd|th)_bcs", exam_slug):
            result.errors.append(f"{where}: exam_slug {exam_slug!r} does not match pattern N(th)_bcs")

    return result


OPTION_FIELDS = ("option_a", "option_b", "option_c", "option_d")
