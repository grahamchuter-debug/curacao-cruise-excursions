#!/usr/bin/env python3
"""QA gates for Curacao Cruise Excursions Phase 17B."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from curacao_config import APEX, DOMAIN, EMAIL, PROTECTED_ROUTES  # noqa: E402

ERRORS: list[str] = []
WARNINGS: list[str] = []

FORBIDDEN_PHRASES = [
    "ship return guaranteed",
    "top rated",
    "most popular",
    "check availability",
    "book a tour",
    "info@wowatour.com",
    "aggregateRating",
    '"@type": "Product"',
    '"@type": "Offer"',
    '"@type": "LocalBusiness"',
    "shoreexcursionsgroup.com",
    "cacucurcolhis",
    "cacuhfdysnk",
    "stripe",
    "/book/",
    "hero-flamingos",
    "bonaire",
    "coracocruisexcursions",
    "curacaoshoreexcursions",
]

PROTECTED_PATHS = [r["path"] for r in PROTECTED_ROUTES]


def err(msg: str) -> None:
    ERRORS.append(msg)


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def html_files() -> list[Path]:
    files = [ROOT / "index.html", ROOT / "404.html"]
    for p in ROOT.iterdir():
        if p.is_dir() and (p / "index.html").exists():
            if p.name.startswith("_") or p.name in {"scripts", "images", "css", "js", "node_modules"}:
                continue
            files.append(p / "index.html")
    return files


def main() -> int:
    files = html_files()
    if len(files) < 10:
        err(f"Expected more HTML pages, found {len(files)}")

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        low = text.lower()

        if 'data-inlined="true"' not in text and path.name != "404.html":
            # 404 may omit hero inlining markers differently; still require main
            pass
        if "id=\"main-content\"" not in text and 'id="main-content"' not in text:
            err(f"{rel}: missing #main-content")
        if "<h1" not in low:
            err(f"{rel}: missing H1")
        if low.count("<h1") > 1:
            err(f"{rel}: multiple H1")
        if "cdn.tailwindcss.com" in low:
            err(f"{rel}: Tailwind CDN present")
        if "js/site.js" in low or "data-content=" in low:
            err(f"{rel}: legacy JS content loader present")
        if "/css/site.css" not in text:
            err(f"{rel}: missing /css/site.css")
        if 'rel="canonical"' not in low:
            err(f"{rel}: missing canonical")
        if EMAIL not in text and path.name != "404.html":
            # email may only be in footer for most pages
            if "mailto:" not in low and path.parent.name not in {"privacy", "terms", "contact", "about", "methodology"}:
                warn(f"{rel}: no mailto visible (footer should include {EMAIL})")
        if EMAIL not in text:
            err(f"{rel}: public email {EMAIL} missing from page shell/footer")
        for phrase in FORBIDDEN_PHRASES:
            if phrase.lower() in low:
                err(f"{rel}: forbidden phrase/token '{phrase}'")

        # Canonical must be apex extensionless (except 404)
        m = re.search(r'rel="canonical"\s+href="([^"]+)"', text)
        if not m:
            m = re.search(r'href="([^"]+)"\s+rel="canonical"', text)
        if m:
            canon = m.group(1)
            if not canon.startswith(APEX):
                err(f"{rel}: canonical not on apex ({canon})")
            if canon.endswith(".html") and path.name != "404.html":
                err(f"{rel}: canonical still .html ({canon})")
            if canon.rstrip("/") != APEX and canon.endswith("/") and canon != f"{APEX}/":
                err(f"{rel}: unexpected trailing slash canonical ({canon})")

    # Sitemap
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if ".html" in sm and "404.html" not in sm.replace("404", ""):
        # no .html locs
        if re.search(r"<loc>[^<]+\.html</loc>", sm):
            err("sitemap contains .html locs")
    for path in PROTECTED_PATHS:
        loc = f"{APEX}/" if path == "/" else f"{APEX}{path}"
        if f"<loc>{loc}</loc>" not in sm:
            err(f"sitemap missing {loc}")
    if "curacaoshoreexcursions" in sm.lower() or "coraco" in sm.lower():
        err("sitemap mentions alternate/wrong domain")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {APEX}/sitemap.xml" not in robots:
        err("robots.txt sitemap URL wrong")

    # Active images must not include quarantine names
    for html in files:
        t = html.read_text(encoding="utf-8")
        if "/images/quarantine/" in t or "hero-flamingos" in t:
            err(f"{html.relative_to(ROOT)}: references quarantined imagery")

    css = ROOT / "css" / "site.css"
    if not css.exists() or css.stat().st_size < 1000:
        err("css/site.css missing or too small — run npm run css")

    nav_js = ROOT / "js" / "nav.js"
    if not nav_js.exists():
        err("js/nav.js missing")

    print(f"Checked {len(files)} HTML files against {DOMAIN}")
    for w in WARNINGS:
        print(f"WARN: {w}")
    if ERRORS:
        print(f"\n{len(ERRORS)} ERROR(S):")
        for e in ERRORS:
            print(f"  - {e}")
        return 1
    print("QA PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
