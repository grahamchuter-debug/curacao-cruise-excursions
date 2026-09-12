#!/usr/bin/env python3
"""Build Curacao Cruise Excursions World 2.0 static HTML (Phase 17B)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from curacao_config import APEX, PROTECTED_ROUTES, ROOT as SITE_ROOT  # noqa: E402
from curacao_pages import (  # noqa: E402
    about,
    best_excursions,
    contact,
    home,
    klein,
    methodology,
    not_found,
    port_guide,
    privacy,
    private_tours,
    snorkeling,
    terms,
    walking,
)
from curacao_shell import page_shell  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"  wrote {path.relative_to(SITE_ROOT)}")


def render(builder, *, robots: str | None = None, include_trust: bool = True) -> str:
    hero, main, faqs, meta = builder()
    return page_shell(
        meta["title"],
        meta["description"],
        meta["canonical_path"],
        meta["page_id"],
        hero,
        main,
        meta.get("og_image"),
        faq_entities=faqs,
        robots=robots,
        include_trust=include_trust,
    )


PAGES: list[tuple[str, object, dict]] = [
    ("index.html", home, {}),
    ("klein-curacao-day-trip/index.html", klein, {}),
    ("curacao-snorkeling-tours/index.html", snorkeling, {}),
    ("curacao-cruise-port-guide/index.html", port_guide, {}),
    ("best-curacao-cruise-excursions/index.html", best_excursions, {}),
    ("willemstad-walking-tour/index.html", walking, {}),
    ("private-curacao-tours/index.html", private_tours, {}),
    ("contact/index.html", contact, {}),
    ("about/index.html", about, {}),
    ("privacy/index.html", privacy, {}),
    ("terms/index.html", terms, {}),
    ("methodology/index.html", methodology, {}),
]


def build_pages() -> None:
    for rel, builder, opts in PAGES:
        write(SITE_ROOT / rel, render(builder, **opts))
    write(
        SITE_ROOT / "404.html",
        render(not_found, robots="noindex, follow", include_trust=False),
    )


def build_sitemap() -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for route in PROTECTED_ROUTES:
        if route.get("sitemap") is False:
            continue
        path = route["path"]
        loc = f"{APEX}/" if path == "/" else f"{APEX}{path}"
        kind = route.get("kind", "")
        if path == "/":
            pri, freq = "1.0", "weekly"
        elif kind in {"hub", "guide", "attraction", "decision"}:
            pri, freq = "0.9", "monthly"
        else:
            pri, freq = "0.5", "yearly"
        lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <changefreq>{freq}</changefreq>",
                f"    <priority>{pri}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    write(SITE_ROOT / "sitemap.xml", "\n".join(lines) + "\n")


def build_robots() -> None:
    write(
        SITE_ROOT / "robots.txt",
        f"User-agent: *\nAllow: /\n\nSitemap: {APEX}/sitemap.xml\n",
    )


def build_protected_manifest() -> None:
    write(
        SITE_ROOT / "protected_routes.json",
        json.dumps(PROTECTED_ROUTES, indent=2) + "\n",
    )


def main() -> None:
    print("Building Curacao Cruise Excursions (Phase 17B)…")
    build_pages()
    build_sitemap()
    build_robots()
    build_protected_manifest()
    print("Done.")


if __name__ == "__main__":
    main()
