"""Curaçao Cruise Excursions — World 2.0 Phase 17B site configuration."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN = "curacaocruiseexcursions.com"
APEX = f"https://{DOMAIN}"
SITE = "Curacao Cruise Excursions"
EMAIL = "hello@curacaocruiseexcursions.com"
DATE = "2026-09-12"
ACCENT = "text-pr-400"

FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)

HERO_GRADIENT = (
    "linear-gradient(140deg, rgba(15, 23, 42, 0.78) 0%, "
    "rgba(30, 64, 175, 0.62) 42%, rgba(249, 115, 22, 0.38) 72%, "
    "rgba(0, 0, 0, 0.22) 100%)"
)

# Active assets only (see images/ATTRIBUTION.md). Quarantine/review must not be referenced.
CRUISE_PORT = "/images/cruise-port.png"
CRUISE_PORT_ALT = (
    "Cruise ship alongside Willemstad waterfront with colourful Handelskade façades"
)

KLEIN = "/images/klein-curacao.png"
KLEIN_ALT = "Aerial view of Klein Curacao with pale sand and turquoise shallows"

WILLEMSTAD = "/images/willemstad-walking-tour.png"
WILLEMSTAD_ALT = (
    "Colourful Dutch colonial façades along Willemstad's Handelskade waterfront"
)

PRIVATE_SIGN = "/images/private-curacao-tours.png"
PRIVATE_SIGN_ALT = "Large outdoor CURACAO lettering landmark on Curaçao"

# Extensionless, NO trailing slash — matches live GSC preferred form.
PROTECTED_ROUTES: list[dict] = [
    {"path": "/", "file": "index.html", "kind": "home"},
    {
        "path": "/klein-curacao-day-trip",
        "file": "klein-curacao-day-trip/index.html",
        "kind": "attraction",
    },
    {
        "path": "/curacao-snorkeling-tours",
        "file": "curacao-snorkeling-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/curacao-cruise-port-guide",
        "file": "curacao-cruise-port-guide/index.html",
        "kind": "guide",
    },
    {
        "path": "/best-curacao-cruise-excursions",
        "file": "best-curacao-cruise-excursions/index.html",
        "kind": "hub",
    },
    {
        "path": "/willemstad-walking-tour",
        "file": "willemstad-walking-tour/index.html",
        "kind": "attraction",
    },
    {
        "path": "/private-curacao-tours",
        "file": "private-curacao-tours/index.html",
        "kind": "attraction",
    },
    {"path": "/contact", "file": "contact/index.html", "kind": "trust"},
    {"path": "/about", "file": "about/index.html", "kind": "trust"},
    {"path": "/privacy", "file": "privacy/index.html", "kind": "trust"},
    {"path": "/terms", "file": "terms/index.html", "kind": "trust"},
    {"path": "/methodology", "file": "methodology/index.html", "kind": "trust"},
]
