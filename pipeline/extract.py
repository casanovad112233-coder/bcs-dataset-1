"""Parse a scraped BCS exam HTML file into exam meta, raw questions, and image specs."""
import re
from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup

from .common import clean_html_to_text, norm_stem

QUESTION_HEADER = re.compile(r"Question\s+(\d+)", re.I)
CODE_HEADER = re.compile(r"কোড\s*[:：]\s*(.+)")


@dataclass
class ImageSpec:
    question_number: int
    scope: str  # "question" | "solve"
    src: str
    index: int


@dataclass
class ExamData:
    html_path: Path
    title: str = ""
    stem: str = ""
    date: str = ""
    total_marks: int | None = None
    set_code: str = ""
    questions: list[dict] = field(default_factory=list)
    images: list[ImageSpec] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def total_questions(self) -> int:
        return len(self.questions)


def read_html(path: Path) -> str:
    data = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("cp1252", errors="replace")


def _extract_options(ul) -> dict[str, str]:
    options: dict[str, str] = {}
    for li in ul.find_all("li", recursive=False):
        label = li.find("label")
        if label is None:
            continue
        input_el = label.find("input")
        key = (input_el.get("value") or "").strip().upper() if input_el else ""
        label_tag = label.find(class_="options_label")
        if not key and label_tag is not None:
            key = label_tag.get_text(strip=True).upper()
        if key not in ("A", "B", "C", "D"):
            continue
        clone = label
        for tag in clone.find_all(class_="options_label"):
            tag.decompose()
        options[key] = clean_html_to_text(clone)
    return options


def normalize_answer(raw: str) -> tuple[str, str | None]:
    """Return (correct_answer, warning). correct_answer '' means invalid/missing in source."""
    value = (raw or "").strip()
    if len(value) == 1 and value.lower() in "abcd":
        return value.upper(), None
    return "", f"source data-answer {value!r} is not a single A-D; marked blank, needs review"


def parse_exam(path: Path) -> ExamData:
    soup = BeautifulSoup(read_html(path), "html.parser")
    exam = ExamData(html_path=path, stem=norm_stem(path))

    card = soup.select_one(".optionlist-card")
    name_el = soup.select_one(".question-name")
    date_el = soup.select_one(".question-date")
    mark_el = soup.select_one(".question-mark")
    exam.title = name_el.get_text(strip=True) if name_el else path.stem
    exam.date = date_el.get_text(strip=True) if date_el else ""
    if card is not None:
        mark = card.get("data-mark")
        if mark is not None:
            exam.total_marks = int(mark)
    if mark_el:
        m = re.search(r"(\d+)", mark_el.get_text())
        if m:
            exam.total_marks = int(m.group(1))
    for h2 in soup.select(".card-header h2"):
        m = CODE_HEADER.search(h2.get_text(" "))
        if m:
            exam.set_code = m.group(1).strip()
            break

    blocks = soup.select(".single-question")
    for block in blocks:
        h4 = block.find("h4")
        m = QUESTION_HEADER.search(h4.get_text()) if h4 else None
        if not m:
            exam.warnings.append("question block without a parseable number heading; skipped")
            continue
        number = int(m.group(1))
        raw_answer, warn = normalize_answer(block.get("data-answer", ""))
        if warn:
            exam.warnings.append(f"q{number}: {warn}")

        prompt_el = block.select_one(".p-2")
        question_imgs: list[ImageSpec] = []
        solve_imgs: list[ImageSpec] = []
        if prompt_el is not None:
            for i, img in enumerate(prompt_el.find_all("img"), 1):
                question_imgs.append(ImageSpec(number, "question", img.get("src", "").strip(), i))
            for img in prompt_el.find_all("img"):
                img.decompose()

        question_text = ""
        if prompt_el is not None:
            for h in prompt_el.find_all("h4"):
                h.decompose()
            question_text = clean_html_to_text(prompt_el)

        ul = block.select_one("ul.list-unstyled")
        options = _extract_options(ul) if ul else {}
        missing = [k for k in "ABCD" if k not in options]
        if missing:
            exam.warnings.append(f"q{number}: missing option(s) {', '.join(missing)}")

        solve_el = block.select_one(".solve-note")
        solve_text = ""
        if solve_el is not None:
            for i, img in enumerate(solve_el.find_all("img"), 1):
                solve_imgs.append(ImageSpec(number, "solve", img.get("src", "").strip(), i))
            for img in solve_el.find_all("img"):
                img.decompose()
            solve_text = clean_html_to_text(solve_el)

        # Renumber with a single per-question sequence so question and solve
        # images share one index space (question first, then solve). Without
        # this, a question image and a solve image both numbered img1 collide
        # on the same filename and the later one overwrites the earlier one.
        for k, spec in enumerate(question_imgs + solve_imgs, 1):
            spec.index = k

        q = {
            "question_number": number,
            "subject_tag": (block.get("data-subject") or "").strip(),
            "question": question_text,
            "option_a": options.get("A", ""),
            "option_b": options.get("B", ""),
            "option_c": options.get("C", ""),
            "option_d": options.get("D", ""),
            "correct_answer": raw_answer or "",
            "solve_note": solve_text,
            "question_image_paths": [],
            "solve_note_image_paths": [],
            "has_question_image": 0,
            "has_solve_note_image": 0,
            "has_image": 0,
            "exam_slug": exam.stem,
        }
        exam.questions.append(q)
        exam.images.extend(question_imgs)
        exam.images.extend(solve_imgs)
    return exam
