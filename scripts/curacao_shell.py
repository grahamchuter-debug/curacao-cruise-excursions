"""World 2.0 HTML shell helpers for Curacao Cruise Excursions (Phase 16B)."""
from __future__ import annotations

import json
from html import escape
from typing import Any

from curacao_config import APEX, DOMAIN, EMAIL, FONTS, HERO_GRADIENT, SITE


def canonical_url(path: str) -> str:
    """Apex HTTPS canonical: home is /; other paths are extensionless with no trailing slash (GSC form)."""
    if not path or path in ("/", "index.html"):
        return f"{APEX}/"
    p = path if path.startswith("/") else f"/{path}"
    p = p.rstrip("/")
    if p.endswith(".html"):
        # Keep explicit file paths such as /404.html
        return f"{APEX}{p}"
    return f"{APEX}{p}"


def nav_html() -> str:
    return f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-ocean-100 shadow-sm" aria-label="Primary">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="/" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Curacao Cruise<br/><span class="text-[10px] font-body font-normal text-pr-500 tracking-widest uppercase">Excursions</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="/" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="/best-curacao-cruise-excursions" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="/klein-curacao-day-trip" data-nav="klein" class="text-gray-600 hover:text-ocean-600 transition-colors">Klein Curacao</a>
        <a href="/curacao-snorkeling-tours" data-nav="snorkeling" class="text-gray-600 hover:text-ocean-600 transition-colors">Snorkelling</a>
        <a href="/curacao-cruise-port-guide" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
        <a href="/contact" data-nav="contact" class="text-gray-600 hover:text-ocean-600 transition-colors">Contact</a>
      </div>
      <a href="/best-curacao-cruise-excursions" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare options
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" id="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
  <div class="mobile-menu lg:hidden" id="mobile-menu" data-mobile-panel="true" hidden>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex flex-col gap-3 text-sm font-medium border-t border-ocean-50 bg-white">
      <a href="/">Home</a>
      <a href="/best-curacao-cruise-excursions">Excursions</a>
      <a href="/klein-curacao-day-trip">Klein Curacao</a>
      <a href="/curacao-snorkeling-tours">Snorkelling</a>
      <a href="/willemstad-walking-tour">Willemstad</a>
      <a href="/private-curacao-tours">Private tours</a>
      <a href="/curacao-cruise-port-guide">Port Guide</a>
      <a href="/contact">Contact</a>
      <a href="/about">About</a>
    </div>
  </div>
</nav>
"""


def footer_html() -> str:
    return f"""<footer class="bg-gray-900 text-gray-400 py-14">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
      <div class="sm:col-span-2 lg:col-span-1">
        <a href="/" class="font-display font-semibold text-white text-lg">{SITE}</a>
        <p class="mt-3 text-sm leading-relaxed">Independent planning guide for cruise passengers calling at Willemstad, Curacao. Editorial advice only. Not affiliated with any cruise line.</p>
        <p class="mt-3 text-sm"><a href="mailto:{EMAIL}" class="hover:text-white transition-colors">{EMAIL}</a></p>
      </div>
      <div>
        <h2 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Decide</h2>
        <ul class="space-y-2 text-sm">
          <li><a href="/best-curacao-cruise-excursions" class="hover:text-white transition-colors">Compare options</a></li>
          <li><a href="/klein-curacao-day-trip" class="hover:text-white transition-colors">Klein Curacao</a></li>
          <li><a href="/curacao-snorkeling-tours" class="hover:text-white transition-colors">Snorkelling</a></li>
          <li><a href="/willemstad-walking-tour" class="hover:text-white transition-colors">Willemstad walking</a></li>
          <li><a href="/private-curacao-tours" class="hover:text-white transition-colors">Private tours</a></li>
        </ul>
      </div>
      <div>
        <h2 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Plan</h2>
        <ul class="space-y-2 text-sm">
          <li><a href="/curacao-cruise-port-guide" class="hover:text-white transition-colors">Cruise port guide</a></li>
          <li><a href="/best-curacao-cruise-excursions" class="hover:text-white transition-colors">Excursion hub</a></li>
          <li><a href="/methodology" class="hover:text-white transition-colors">Methodology</a></li>
        </ul>
      </div>
      <div>
        <h2 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Trust</h2>
        <ul class="space-y-2 text-sm">
          <li><a href="/about" class="hover:text-white transition-colors">About</a></li>
          <li><a href="/contact" class="hover:text-white transition-colors">Contact</a></li>
          <li><a href="/privacy" class="hover:text-white transition-colors">Privacy</a></li>
          <li><a href="/terms" class="hover:text-white transition-colors">Terms</a></li>
        </ul>
      </div>
    </div>
    <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
      <p>&copy; 2026 {SITE} · <a href="{APEX}/" class="hover:text-white">{DOMAIN}</a> · Confirm live schedules and operator details before you travel. Editorial planning only.</p>
    </div>
  </div>
</footer>
"""


def trust_strip_html() -> str:
    return """<section class="trust-strip" aria-label="Curacao cruise excursion planning highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item">
        <span class="trust-strip__check" aria-hidden="true">✔</span>
        Cruise-aware timing
      </li>
      <li class="trust-strip__item">
        <span class="trust-strip__check" aria-hidden="true">✔</span>
        Plan your return window
      </li>
      <li class="trust-strip__item">
        <span class="trust-strip__check" aria-hidden="true">✔</span>
        Klein, snorkel &amp; Willemstad choices
      </li>
    </ul>
  </div>
</section>
"""


def hero_wave() -> str:
    return (
        '<div class="absolute bottom-0 left-0 right-0">'
        '<svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" '
        'preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true">'
        '<path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/>'
        "</svg></div>"
    )


def hero_band(
    *,
    eyebrow: str,
    title_html: str,
    lead: str,
    image: str | None,
    aria_label: str,
    actions: str = "",
    breadcrumb: str | None = None,
    tags: list[str] | None = None,
    css_only: bool = False,
) -> str:
    if css_only or not image:
        bg = (
            f'style="background-image: {HERO_GRADIENT}; '
            'background-color: #0f172a;"'
        )
    else:
        bg = (
            f'style="background-image: {HERO_GRADIENT}, url(\'{image}\'); '
            'background-position: center 40%; background-size: cover;"'
        )

    bc = ""
    if breadcrumb:
        bc = f"""<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="/" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""

    act = (
        f'<div class="site-hero__actions flex flex-col sm:flex-row gap-3">{actions}</div>'
        if actions
        else ""
    )

    tag_html = ""
    if tags:
        pills = "".join(
            f'<span class="inline-flex items-center bg-white/10 border border-white/25 '
            f'rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{escape(t)}</span>'
            for t in tags
        )
        tag_html = (
            f'<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t '
            f'border-white/20">{pills}</div>'
        )

    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" {bg} role="img" aria-label="{escape(aria_label)}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-pr-400"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{escape(eyebrow)}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title_html}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      {act}
      {tag_html}
    </div>
  </div>
  {hero_wave()}
</section>
"""


def cruise_snapshot(items: list[tuple[str, str]], *, label: str = "Cruise passenger snapshot") -> str:
    rows = "".join(
        f'<div class="cruise-snapshot__item"><dt>{escape(k)}</dt><dd>{v}</dd></div>'
        for k, v in items
    )
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="{escape(label)}">
  <h2 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise passenger snapshot</h2>
  <dl class="cruise-snapshot__grid">{rows}</dl>
</aside>
"""


def faq_section(faqs: list[tuple[str, str]], *, heading: str) -> str:
    blocks = []
    for q, a in faqs:
        blocks.append(
            f"""<details class="faq-item rounded-2xl border border-ocean-100 p-5 group bg-white">
        <summary class="font-semibold text-gray-900 cursor-pointer list-none flex items-center justify-between gap-4">{escape(q)}<span class="text-ocean-400 group-open:rotate-90 transition-transform text-xl flex-shrink-0" aria-hidden="true">›</span></summary>
        <p class="mt-4 text-sm text-gray-500 leading-relaxed">{a}</p>
      </details>"""
        )
    return f"""<section id="faq" class="py-16 bg-sand-50 scroll-mt-20">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-2xl font-display font-bold text-gray-900 text-center mb-8">{escape(heading)}</h2>
    <div class="space-y-4">
      {"".join(blocks)}
    </div>
  </div>
</section>
"""


def related_links(links: list[tuple[str, str]], *, label: str = "Plan your port day") -> str:
    parts: list[str] = []
    for i, (href, text) in enumerate(links):
        if i:
            parts.append('<span class="text-gray-300">·</span>')
        parts.append(
            f'<a href="{href}" class="text-ocean-600 hover:text-ocean-800 font-medium">{text}</a>'
        )
    return f"""<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Curacao guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">{escape(label)}</p>
  <div class="flex flex-wrap gap-3 text-sm">{"".join(parts)}</div>
</nav>
"""


def _faq_entities(faqs: list[tuple[str, str]]) -> list[dict[str, Any]]:
    return [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in faqs
    ]


def _breadcrumb_entities(canonical_path: str, title: str) -> dict[str, Any]:
    """Breadcrumb item URLs omit trailing slash except home (GSC form)."""
    path = canonical_path if canonical_path.startswith("/") else f"/{canonical_path}"
    path = path.rstrip("/") if path not in ("/", "") else "/"
    name = title.split("|")[0].strip()
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{APEX}/"},
            {
                "@type": "ListItem",
                "position": 2,
                "name": name,
                "item": canonical_url(path),
            },
        ],
    }


def page_shell(
    title: str,
    description: str,
    canonical_path: str,
    page_id: str,
    hero_html: str,
    main_html: str,
    og_image: str | None,
    faq_entities: list[tuple[str, str]] | None = None,
    extra_schema: list[dict[str, Any]] | None = None,
    *,
    robots: str | None = None,
    include_trust: bool = True,
) -> str:
    canon = canonical_url(canonical_path)
    if og_image:
        og_abs = og_image if og_image.startswith("http") else f"{APEX}{og_image}"
        preload = (
            f'  <link rel="preload" as="image" href="{og_image if og_image.startswith("/") else "/" + og_image}" fetchpriority="high" />\n'
        )
        og_image_meta = f'  <meta property="og:image" content="{og_abs}" />\n'
        tw_image = f'  <meta name="twitter:image" content="{og_abs}" />\n'
    else:
        preload = ""
        og_image_meta = ""
        tw_image = ""

    graph: list[dict[str, Any]] = [
        {
            "@type": "WebSite",
            "name": SITE,
            "url": f"{APEX}/",
            "description": (
                "Independent cruise-passenger planning guide for Curacao "
                "shore excursions from Willemstad."
            ),
            "inLanguage": "en-GB",
            "publisher": {
                "@type": "Organization",
                "name": SITE,
                "url": f"{APEX}/",
                "email": EMAIL,
            },
        },
        {
            "@type": "Organization",
            "name": SITE,
            "url": f"{APEX}/",
            "email": EMAIL,
            "description": (
                f"{SITE} provides cruise-focused excursion information and "
                "independent destination advice for passengers visiting Curacao. "
                "Not affiliated with any cruise line."
            ),
        },
    ]

    path_norm = canonical_path if canonical_path.startswith("/") else f"/{canonical_path}"
    if path_norm not in ("/", "", "/404.html", "404.html"):
        graph.append(_breadcrumb_entities(path_norm, title))

    if faq_entities:
        graph.append({"@type": "FAQPage", "mainEntity": _faq_entities(faq_entities)})

    if extra_schema:
        graph.extend(extra_schema)

    schema_block = (
        '  <script type="application/ld+json">\n'
        + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2)
        + "\n  </script>\n"
    )

    robots_meta = f'  <meta name="robots" content="{escape(robots)}" />\n' if robots else ""
    trust = (
        f'  <div id="page-trust-strip" data-inlined="true">\n{trust_strip_html()}  </div>\n'
        if include_trust
        else ""
    )

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}" />
{robots_meta}  <link rel="canonical" href="{canon}" />
{preload}  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{escape(title)}" />
  <meta property="og:description" content="{escape(description)}" />
{og_image_meta}  <meta property="og:site_name" content="{SITE}" />
  <meta property="og:locale" content="en_GB" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{escape(title)}" />
  <meta name="twitter:description" content="{escape(description)}" />
{tw_image}  <meta name="geo.region" content="CW" />
  <meta name="geo.placename" content="Willemstad, Curacao" />
{schema_block}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
<body class="bg-white text-gray-800 antialiased" data-page="{escape(page_id)}">
  <a class="skip-link" href="#main-content">Skip to content</a>
  <div id="site-nav" data-inlined="true">
{nav_html()}  </div>
  <div id="page-hero" data-inlined="true">
{hero_html}  </div>
{trust}<main id="main-content" tabindex="-1" data-inlined="true">
{main_html}
</main>
  <div id="site-footer" data-inlined="true">
{footer_html()}  </div>
  <script src="/js/nav.js" defer></script>
</body>
</html>
"""
