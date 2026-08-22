"""Download / decode images referenced in exam HTML into exam-scoped local paths."""
import base64
import re
from pathlib import Path

import requests

from .extract import ExamData

DATA_URI = re.compile(r"^data:(image/[a-z0-9.+-]+);base64,(.+)$", re.S)
BASE_URL = "https://uttoron.academy"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

MIME_EXT = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/gif": ".gif",
    "image/webp": ".webp",
}


def _ext_for(src: str) -> str:
    m = DATA_URI.match(src)
    if m:
        return MIME_EXT.get(m.group(1).lower(), ".png")
    m = re.search(r"\.(png|jpe?g|gif|webp)(?:$|[?#])", src, re.I)
    if not m:
        return ".jpg"
    ext = m.group(1).lower()
    return ".jpg" if ext in ("jpg", "jpeg") else f".{ext}"


def save_images(exam: ExamData, dry_run: bool = False) -> None:
    """Save every referenced image locally and fill path arrays + flags on exam.questions."""
    for q in exam.questions:
        q["question_image_paths"] = []
        q["solve_note_image_paths"] = []

    session = requests.Session()
    session.headers["User-Agent"] = UA

    for spec in exam.images:
        data = None
        if spec.src.startswith("data:"):
            m = DATA_URI.match(spec.src)
            if not m:
                exam.warnings.append(f"q{spec.question_number}: unparseable data URI, image skipped")
                continue
            data = base64.b64decode(m.group(2))
        else:
            src = spec.src
            if src.startswith("/"):
                src = BASE_URL + src
            elif not src.startswith(("http://", "https://")):
                src = f"{BASE_URL}/{src.lstrip('/')}"
            try:
                resp = session.get(src, timeout=20, allow_redirects=True)
                resp.raise_for_status()
                data = resp.content
            except requests.RequestException as exc:
                exam.warnings.append(
                    f"q{spec.question_number}: failed to download {src} ({exc.__class__.__name__})"
                )
                continue

        out_dir = Path("images") / exam.stem
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"q{spec.question_number}_img{spec.index}{_ext_for(spec.src)}"
        rel = out_path.as_posix()
        if not dry_run:
            out_path.write_bytes(data)

        for q in exam.questions:
            if q["question_number"] == spec.question_number:
                (q["question_image_paths"] if spec.scope == "question"
                 else q["solve_note_image_paths"]).append(rel)
                break

    _update_flags(exam)


def _update_flags(exam: ExamData) -> None:
    for q in exam.questions:
        q["has_question_image"] = 1 if q["question_image_paths"] else 0
        q["has_solve_note_image"] = 1 if q["solve_note_image_paths"] else 0
        q["has_image"] = 1 if (q["has_question_image"] or q["has_solve_note_image"]) else 0
