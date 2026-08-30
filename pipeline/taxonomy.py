"""Taxonomy (ground truth from instructions/topics_taxonomy.md) and source subject-tag mapping."""
import re
from pathlib import Path

TABLE_ROW = re.compile(r"^\|\s*`(\d+)`\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$")


def load_taxonomy(path: Path) -> dict[int, dict[str, str]]:
    taxonomy: dict[int, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = TABLE_ROW.match(line.strip())
        if m:
            taxonomy[int(m.group(1))] = {"subject_en": m.group(2), "subject_bn": m.group(3)}
    if sorted(taxonomy) != list(range(1, len(taxonomy) + 1)):
        raise ValueError(f"taxonomy ids in {path} are not 1..N contiguous: {sorted(taxonomy)}")
    return taxonomy


def taxonomy_list(taxonomy: dict[int, dict[str, str]]) -> list[dict]:
    return [
        {"id": sid, "subject_en": info["subject_en"], "subject_bn": info["subject_bn"]}
        for sid, info in sorted(taxonomy.items())
    ]


SUBJECT_TAG_MAP = {
    "bangla-language": 1,
    "bangla-literature": 1,
    "bangla": 1,
    "english-language": 2,
    "english-literature": 2,
    "english": 2,
    "bangladesh-affairs": 3,
    "international-affairs": 4,
    "geography-environment-and-disaster-management": 5,
    "geography-environment-and-digester-management": 5,
    "geography": 5,
    "general-science": 6,
    "science": 6,
    "computer-and-information-technology": 7,
    "computer": 7,
    "mathematical-reasoning": 8,
    "mathematics": 8,
    "mental-ability": 9,
    "ethics-values-good-governance": 10,
    "ethics": 10,
}


def map_subject_tag(tag: str) -> int | None:
    key = (tag or "").strip().lower()
    if not key:
        return None
    return SUBJECT_TAG_MAP.get(key)
