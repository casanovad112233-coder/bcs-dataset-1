"""Merge 41 per-exam JSONs into bcs_preliminary_question_bank.json

Usage:
    python -m pipeline.merge
    python -m pipeline.merge --out bcs_preliminary_question_bank.json
"""
import json
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "data" / "processed" / "json"
DEFAULT_OUT = ROOT / "bcs_preliminary_question_bank.json"  # canonical SEO name for bcs preliminary question bank

def exam_num(slug: str) -> int:
    m = re.match(r"(\d+)", slug)
    return int(m.group(1)) if m else 0

def merge(out_path: Path = DEFAULT_OUT):
    files = sorted([p for p in SRC_DIR.glob("*_bcs.json") if p.name != out_path.name])
    # also exclude merged file itself if it lives in same dir (legacy names)
    files = [p for p in files if p.name not in ("Bcs_Question_Bank_Db_10th_to_50th.json", "bcs_question_bank.json", "bcs_preliminary_question_bank.json")]

    taxonomy = None
    exams = []
    all_q = []
    for p in files:
        data = json.loads(p.read_text(encoding="utf-8"))
        exam = data.get("exam", {})
        if taxonomy is None and data.get("taxonomy"):
            taxonomy = data["taxonomy"]
        qs = data.get("questions", [])
        slug = p.stem
        for q in qs:
            q.setdefault("exam_slug", slug)
            all_q.append(q)
        exams.append({
            "slug": slug,
            "title": exam.get("title", slug),
            "date": exam.get("date", ""),
            "total_marks": exam.get("total_marks"),
            "set_code": exam.get("set_code", ""),
            "total_questions": exam.get("total_questions", len(qs)),
            "actual_questions": len(qs),
        })

    exams = sorted(exams, key=lambda x: exam_num(x["slug"]))
    all_q = sorted(all_q, key=lambda q: (exam_num(q["exam_slug"]), q["question_number"]))

    merged = {
        "metadata": {
            "title": "BCS Preliminary Question Bank Database 10th to 50th",
            "name": "bcs_preliminary_question_bank",
            "version": "1.0",
            "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "total_exams": len(exams),
            "total_questions": len(all_q),
            "source": "data/processed/json/*_bcs.json",
            "taxonomy_source": "instructions/topics_taxonomy.md",
        },
        "taxonomy": taxonomy or [],
        "exams": exams,
        "questions": all_q,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Merged {len(exams)} exams, {len(all_q)} questions -> {out_path} ({out_path.stat().st_size/1024:.1f} KB)")
    return out_path

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()
    merge(args.out)
