"""Scrape BCS question pages from uttoron.academy one at a time via Firecrawl.

Reads URLs from links_to_scrape.md, scrapes each page's HTML with the
`html` format (Firecrawl), and saves it as <stem>_bcs.html in the repo root
(already-scraped files are skipped so reruns are resumable).
"""
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from firecrawl import V1FirecrawlApp

ROOT = Path(__file__).resolve().parent
# Canonical location is instructions/links_to_scrape.md; keep legacy root fallback
_LINKS_CANDIDATE = ROOT / "instructions" / "links_to_scrape.md"
LINKS_FILE = _LINKS_CANDIDATE if _LINKS_CANDIDATE.exists() else ROOT / "links_to_scrape.md"
RAW_HTML_DIR = ROOT / "data" / "raw" / "html"

URL_RE = re.compile(r"https://uttoron\.academy/QuestionBank/QuestionPreview/([0-9]+(?:st|nd|rd|th)-bcs)")


def _seconds_to_wait(error) -> float:
    """Extract the Firecrawl 'retry after Ns' hint from an HTTPError message."""
    text = str(error)
    m = re.search(r"retry after (\d+)s", text, re.I)
    if m:
        return float(m.group(1)) + 1.0
    return 60.0


def scrape_with_retry(app, url: str, attempts: int = 4) -> str | None:
    """Scrape one page, retrying on 429 rate-limit errors with backoff."""
    for n in range(attempts):
        try:
            resp = app.scrape_url(url, formats=["html"])
            if not getattr(resp, "success", False) or not resp.html:
                print(f"  ERROR: success={getattr(resp, 'success', None)} "
                      f"html_len={len(resp.html or '')}", file=sys.stderr)
                return None
            return resp.html
        except Exception as exc:
            wait = _seconds_to_wait(exc)
            if n < attempts - 1:
                print(f"  rate-limited ({exc.__class__.__name__}); retrying in {wait:.0f}s "
                      f"[attempt {n + 2}/{attempts}]", file=sys.stderr)
                time.sleep(wait)
            else:
                print(f"  ERROR scraping: {exc.__class__.__name__}: {exc}", file=sys.stderr)
    return None


def read_links() -> list[tuple[str, str]]:
    """Return [(url, output_stem)] pairs in file order."""
    pairs: list[tuple[str, str]] = []
    for line in LINKS_FILE.read_text(encoding="utf-8").splitlines():
        m = URL_RE.search(line)
        if m:
            slug = m.group(1)                # e.g. 44th-bcs
            stem = slug.replace("-", "_")    # e.g. 44th_bcs
            pairs.append((line.strip(), stem))
    return pairs


def main(argv: list[str] | None = None) -> int:
    parser = argparse_()
    args = parser.parse_args(argv)

    load_dotenv(ROOT / ".env")
    api_key = os.getenv("FIRECRAWL_API_KEY") or os.getenv("FIREWORKS_API_KEY")
    if not api_key:
        print("error: FIRECRAWL_API_KEY not set in .env", file=sys.stderr)
        return 1

    links = read_links()
    print(f"{len(links)} links found in {LINKS_FILE.name}")
    if args.only is not None:
        keep = [p for p in links if args.only.lower() in p[0]]
        print(f"Filtered to {len(keep)} link(s) matching {args.only!r}")
        links = keep

    todo = [(url, stem) for url, stem in links if not (RAW_HTML_DIR / f"{stem}.html").is_file() and not (ROOT / f"{stem}.html").is_file()]
    skipped = len(links) - len(todo)
    if skipped:
        print(f"Skipping {skipped} already-scraped page(s)")
    if not todo:
        print("Nothing to scrape")
        return 0

    app = V1FirecrawlApp(api_key=api_key)
    min_html_len = 10_000  # below this the page is almost certainly an empty shell

    RAW_HTML_DIR.mkdir(parents=True, exist_ok=True)
    for i, (url, stem) in enumerate(todo, 1):
        out_path = RAW_HTML_DIR / f"{stem}.html"
        print(f"[{i}/{len(todo)}] {stem} <- {url} ...", flush=True)
        html = scrape_with_retry(app, url)
        if html is None:
            print(f"  ERROR: could not scrape {url}", file=sys.stderr)
            continue
        if len(html) < min_html_len:
            print(f"  ERROR: response too small ({len(html):,} bytes); not saved "
                  f"(likely an empty/error page)", file=sys.stderr)
            continue
        out_path.write_text(html, encoding="utf-8")
        print(f"  saved {out_path.name} ({len(html):,} bytes)")
        if i < len(todo):
            time.sleep(args.delay)

    done = sum(1 for _, s in todo if (RAW_HTML_DIR / f"{s}.html").is_file() or (ROOT / f"{s}.html").is_file())
    print(f"Done: {done}/{len(todo)} saved")
    return 0


def argparse_():
    import argparse
    p = argparse.ArgumentParser(description="Scrape BCS question pages (one at a time) via Firecrawl")
    p.add_argument("--only", default=None, help="only scrape links containing this substring (e.g. '44th')")
    p.add_argument("--delay", type=float, default=1.0, help="seconds to sleep between pages")
    return p


if __name__ == "__main__":
    raise SystemExit(main())
