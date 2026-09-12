"""Curacao Cruise Excursions — Phase 17B editorial page content modules.

Each public page function returns:
  (hero_html, main_html, faq_list_or_None, meta)

meta keys: title, description, canonical_path, page_id, og_image
faq_list: list[tuple[str, str]] | None
"""
from __future__ import annotations

from html import escape
from typing import TypedDict

from curacao_config import (
    ACCENT,
    APEX,
    CRUISE_PORT,
    CRUISE_PORT_ALT,
    EMAIL,
    KLEIN,
    KLEIN_ALT,
    PRIVATE_SIGN,
    PRIVATE_SIGN_ALT,
    SITE,
    WILLEMSTAD,
    WILLEMSTAD_ALT,
)
from curacao_shell import cruise_snapshot, faq_section, hero_band, related_links


class Meta(TypedDict):
    title: str
    description: str
    canonical_path: str
    page_id: str
    og_image: str | None


PageTuple = tuple[str, str, list[tuple[str, str]] | None, Meta]


def _cta(primary_href: str, primary_label: str, secondary_href: str = "", secondary_label: str = "") -> str:
    parts = [
        f'<a href="{primary_href}" class="btn-primary inline-flex items-center justify-center gap-2 '
        f'text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{primary_label}</a>'
    ]
    if secondary_href:
        parts.append(
            f'<a href="{secondary_href}" class="btn-outline inline-flex items-center justify-center gap-2 '
            f'text-white font-semibold px-7 py-3 rounded-full text-sm">{secondary_label}</a>'
        )
    return "".join(parts)


def _section(inner: str, *, bg: str = "bg-white", pad: str = "pt-8 pb-12") -> str:
    return (
        f'<section class="{pad} {bg}">'
        f'<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">{inner}</div></section>\n'
    )


def _prose(inner: str, *, bg: str = "bg-white", narrow: bool = True) -> str:
    wrap = "max-w-3xl" if narrow else "max-w-7xl"
    return (
        f'<section class="py-14 {bg}"><div class="{wrap} mx-auto px-4 sm:px-6 lg:px-8">'
        f"{inner}</div></section>\n"
    )


def _card(
    href: str,
    title: str,
    blurb: str,
    *,
    image: str | None = None,
    alt: str = "",
    cta: str = "Read more →",
    media_label: str = "",
) -> str:
    if image:
        media = (
            f'<div class="card-media h-36">'
            f'<img src="{image}" alt="{escape(alt)}" width="600" height="288" '
            f'loading="lazy" decoding="async" /></div>'
        )
    else:
        label = media_label or title
        media = (
            f'<div class="card-media h-36 bg-ocean-800 flex items-center justify-center '
            f'text-white/80 text-sm px-4 text-center">{escape(label)}</div>'
        )
    return f"""<a href="{href}" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
  {media}
  <div class="p-5 flex flex-col flex-1">
    <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">{title}</h3>
    <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">{blurb}</p>
    <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">{cta}</span>
  </div>
</a>"""


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------


def home() -> PageTuple:
    hero = hero_band(
        eyebrow="Curacao · Willemstad cruise port",
        title_html=(
            f'Curacao Cruise <br/><span class="{ACCENT}">Excursions</span> '
            "for Ship Passengers"
        ),
        lead=(
            "A practical guide to what fits a Willemstad call: Klein Curacao sea days, "
            "snorkelling, Handelskade walking, near-port beach time, or a private plan "
            "matched to your group's pace."
        ),
        image=CRUISE_PORT,
        aria_label=CRUISE_PORT_ALT,
        actions=_cta(
            "/best-curacao-cruise-excursions",
            "Compare options",
            "/curacao-cruise-port-guide",
            "Port guide",
        ),
        tags=["Klein Curacao", "Snorkelling", "Willemstad", "Mega Pier"],
    )

    snap = cruise_snapshot(
        [
            ("Typical berths", "Often Mega Pier or Mathey Wharf — confirm your ship"),
            ("Near-port strengths", "Punda / Otrobanda walking; Handelskade colour"),
            ("Full-day water", "Klein Curacao — boat transfer + sea-state planning"),
            ("Activity level", "Varies — town walk low; Klein and west coast higher commitment"),
            ("Return window", "Leave margin before all-aboard; confirm operator policy"),
            ("This site", "Planning guides + request-to-book for the Historic Walking Tour"),
        ],
        label="Curacao cruise passenger snapshot",
    )

    faqs: list[tuple[str, str]] = [
        (
            "Where do cruise ships call in Curacao?",
            "Ships typically use Willemstad berths such as Mega Pier or Mathey Wharf. Confirm "
            "your sailing's port notes — berth and gangway arrangements can vary.",
        ),
        (
            "How long do ships usually stay?",
            "Typical Curacao calls often run several hours ashore. Always confirm gangway and "
            "all-aboard times on your sailing — schedules vary by ship and season.",
        ),
        (
            "Is Klein Curacao realistic on a cruise day?",
            "Klein is usually a full-day boat commitment. Compare the advertised return with "
            "your all-aboard time, and treat sea conditions as a planning variable — not a "
            "guaranteed ship-return product.",
        ),
        (
            "Can I request a tour on this site?",
            "Yes — you can request the Willemstad Historic Walking Tour online. Payment creates "
            "a booking request; confirmation follows separately. Other day styles remain editorial "
            "planning guides for now.",
        ),
    ]

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
  <div>
    <div class="section-label">Willemstad cruise port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 leading-snug mb-5">
      What Curacao is <br/> <span class="text-ocean-600">actually good for</span>
    </h2>
    <p class="text-gray-600 leading-relaxed mb-5">
      Cruise ships generally call at <strong>Willemstad</strong>, with passengers oriented around
      <strong>Mega Pier</strong> or <strong>Mathey Wharf</strong> — treat that as typical, not a
      guarantee for every sailing. The pastel Handelskade and the Punda / Otrobanda split across
      St Anna Bay reward a short walk; west-coast beaches and inland stops usually need a transfer.
    </p>
    <p class="text-gray-600 leading-relaxed mb-8">
      USD is commonly accepted at tourist-facing points; confirm live payment notes with taxis and
      operators. Use this site to pick a coherent theme for the day, then confirm ship times
      independently. When you want a guided near-port walk, you can request the
      <a href="/willemstad-walking-tour" class="text-ocean-600 font-medium">Willemstad Historic Walking Tour</a>
      online.
    </p>
    <p class="flex flex-wrap gap-3 mb-2">
      <a href="/best-curacao-cruise-excursions" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">
        Compare options
      </a>
      <a href="/book/historic-walking-tour" class="inline-flex items-center justify-center font-semibold px-7 py-3.5 rounded-full text-sm border border-ocean-200 text-ocean-700">
        Request walking tour
      </a>
    </p>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{CRUISE_PORT}" alt="{escape(CRUISE_PORT_ALT)}" width="800" height="600" loading="eager" decoding="async" />
  </div>
</div>
''')}
{_section(f'''
<div class="text-center mb-12">
  <div class="section-label justify-center">Decision spine</div>
  <h2 class="text-3xl font-display font-bold text-gray-900">Five useful starting points</h2>
  <p class="mt-4 text-gray-500 max-w-2xl mx-auto">Pick the page that matches your question — not a ranking of “bestsellers”.</p>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
  {_card("/klein-curacao-day-trip", "Klein Curacao", "Uninhabited island sea day — boat transfer, full-day timing, sea-state honesty.", image=KLEIN, alt=KLEIN_ALT, cta="Plan Klein day →")}
  {_card("/curacao-snorkeling-tours", "Snorkelling", "Reef and turtle possibilities, boat vs shore, and cruise-day practicality.", media_label="Snorkel day", cta="Read snorkelling guide →")}
  {_card("/willemstad-walking-tour", "Willemstad", "Punda, Otrobanda and Handelskade colour — often the lowest-transfer option.", image=WILLEMSTAD, alt=WILLEMSTAD_ALT, cta="Willemstad guide →")}
  {_card("/best-curacao-cruise-excursions", "Beach / island day", "Near-port beach time versus longer west-coast or island commitments.", media_label="Beach day", cta="Compare options →")}
  {_card("/private-curacao-tours", "Private", "Custom pacing when mobility, ages or timing differ within one group.", image=PRIVATE_SIGN, alt=PRIVATE_SIGN_ALT, cta="Private guide →")}
</div>
''', bg="bg-pr-50", pad="py-16")}
{_section(f'''
<div class="text-center mb-10">
  <div class="section-label justify-center">Equity routes</div>
  <h2 class="text-2xl font-display font-bold text-gray-900">All planning guides</h2>
</div>
<div class="flex flex-wrap justify-center gap-3 text-sm">
  <a href="/best-curacao-cruise-excursions" class="text-ocean-600 font-medium hover:text-ocean-800">Excursions hub</a>
  <span class="text-gray-300">·</span>
  <a href="/curacao-cruise-port-guide" class="text-ocean-600 font-medium hover:text-ocean-800">Port guide</a>
  <span class="text-gray-300">·</span>
  <a href="/klein-curacao-day-trip" class="text-ocean-600 font-medium hover:text-ocean-800">Klein Curacao</a>
  <span class="text-gray-300">·</span>
  <a href="/curacao-snorkeling-tours" class="text-ocean-600 font-medium hover:text-ocean-800">Snorkelling</a>
  <span class="text-gray-300">·</span>
  <a href="/willemstad-walking-tour" class="text-ocean-600 font-medium hover:text-ocean-800">Willemstad</a>
  <span class="text-gray-300">·</span>
  <a href="/private-curacao-tours" class="text-ocean-600 font-medium hover:text-ocean-800">Private tours</a>
</div>
''', pad="pb-8 pt-4")}
{_section(snap + related_links([
    ("/curacao-cruise-port-guide", "Port guide"),
    ("/klein-curacao-day-trip", "Plan Klein day"),
    ("/best-curacao-cruise-excursions", "Compare options"),
    ("/contact", "Contact"),
]), pad="pb-16 pt-4")}
{faq_section(faqs, heading="Curacao shore day FAQ")}
"""

    meta: Meta = {
        "title": "Curacao Cruise Excursions | Willemstad Shore Day Planning",
        "description": (
            "Plan Curacao cruise excursions from Willemstad — Klein Curacao, snorkelling, "
            "Handelskade walking, beach days and realistic return-window planning."
        ),
        "canonical_path": "/",
        "page_id": "home",
        "og_image": CRUISE_PORT,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# KLEIN CURACAO (highest equity)
# ---------------------------------------------------------------------------


def klein() -> PageTuple:
    hero = hero_band(
        eyebrow="Full-day sea commitment",
        title_html=f'Klein Curacao <br/> <span class="{ACCENT}">day trip planning</span>',
        lead=(
            "Honest cruise-day framing for Curacao's uninhabited outer island: boat transfer, "
            "full-day nature, sea conditions, and comparing timing to your ship's all-aboard — "
            "not a guaranteed return product."
        ),
        image=KLEIN,
        aria_label=KLEIN_ALT,
        breadcrumb="Klein Curacao",
        actions=_cta(
            "/curacao-cruise-port-guide",
            "Port guide",
            "/best-curacao-cruise-excursions",
            "Compare options",
        ),
        tags=["Boat transfer", "Full day", "Sea state", "Lighthouse island"],
    )

    snap = cruise_snapshot(
        [
            ("Day shape", "Typically a full-day boat outing from Curacao"),
            ("Transfer", "Open-water crossing — duration varies with operator and sea"),
            ("On island", "Pale sand, shallow turquoise water, lighthouse landmark"),
            ("Sea conditions", "Can delay or reshape the day — confirm live"),
            ("Cruise fit", "Only if advertised return clears your all-aboard with margin"),
            ("This site", "Editorial planning — no booking checkout"),
        ],
        label="Klein Curacao cruise snapshot",
    )

    faqs: list[tuple[str, str]] = [
        (
            "Is Klein Curacao a half-day option?",
            "Treat Klein as a full-day commitment. Crossing time, beach hours and the return sail "
            "usually consume most of a cruise call — confirm the operator's published schedule "
            "against your all-aboard.",
        ),
        (
            "Can sea conditions change the day?",
            "Yes. Open-water crossings depend on sea state. Operators may adjust, delay or cancel. "
            "Plan with that uncertainty in mind rather than assuming a fixed clock.",
        ),
        (
            "Will I get back to the ship on time?",
            "No website can guarantee ship return. Compare the operator's advertised return with "
            "your all-aboard, leave conservative margin, and confirm cancellation / weather policy "
            "before you travel.",
        ),
        (
            "Can I book Klein Curacao here?",
            "No. This page is editorial planning only. We do not process bookings, payments or "
            "availability checks on this site.",
        ),
    ]

    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  <strong>Klein Curacao</strong> is the island's signature uninhabited sandbar day: pale beach,
  turquoise shallows and a lonely lighthouse — reached by boat, not by a short taxi from
  Mega Pier. For cruise passengers, the decision is rarely “is it pretty?” and almost always
  “does the full-day boat schedule still leave honest margin before all-aboard?”
</p>
''' + snap)}
{_section('''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">What the day is</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Boat first, island second</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Expect an open-water transfer to an uninhabited island with limited facilities compared with
      Willemstad. Snorkelling and beach time are the usual focus; inclusions (lunch, gear, shade)
      vary by operator — confirm them live rather than assuming a standard package.
    </p>
    <p class="text-gray-600 leading-relaxed">
      If your priority is a short walk and Handelskade colour, start with the
      <a href="/willemstad-walking-tour" class="text-ocean-600 font-medium">Willemstad walking</a>
      guide instead. Klein is a different time budget.
    </p>
  </div>
  <div>
    <div class="section-label">Cruise-day honesty</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Timing vs all-aboard</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Line up the operator's advertised departure and return against your ship's published
      all-aboard. Leave margin for pier queues, tender or berth quirks, and sea-state delays.
      A beautiful island day is not worth a missed sailing.
    </p>
    <p class="text-gray-600 leading-relaxed">
      Read the
      <a href="/curacao-cruise-port-guide" class="text-ocean-600 font-medium">port guide</a>
      for Mega Pier / Mathey Wharf orientation, then
      <a href="/best-curacao-cruise-excursions" class="text-ocean-600 font-medium">compare options</a>
      if Klein's duration feels too tight.
    </p>
  </div>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Sea state and planning language</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Treat weather and swell as first-class planning inputs. Operators often publish soft language
  about conditions; ask what happens if the crossing is rough or delayed. This guide does not
  invent schedules, prices or “guaranteed back on board” claims.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Shorter water days — boat or shore snorkelling nearer Curacao — may fit tighter calls better.
  See the
  <a href="/curacao-snorkeling-tours" class="text-ocean-600 font-medium">snorkelling guide</a>
  when Klein's full-day shape is the wrong tool.
</p>
''' + related_links([
    ("/curacao-cruise-port-guide", "Port guide"),
    ("/curacao-snorkeling-tours", "Read snorkelling guide"),
    ("/best-curacao-cruise-excursions", "Compare options"),
    ("/contact", "Contact"),
]))}
{faq_section(faqs, heading="Klein Curacao FAQ")}
"""

    meta: Meta = {
        "title": "Klein Curacao Day Trip | Cruise Passenger Planning Guide",
        "description": (
            "Plan a Klein Curacao day trip from a Willemstad cruise call — boat transfer, "
            "full-day timing, sea conditions and honest return-window planning."
        ),
        "canonical_path": "/klein-curacao-day-trip",
        "page_id": "klein",
        "og_image": KLEIN,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# SNORKELLING
# ---------------------------------------------------------------------------


def snorkeling() -> PageTuple:
    hero = hero_band(
        eyebrow="Reef &amp; water days",
        title_html=f'Curacao <br/> <span class="{ACCENT}">snorkelling tours</span>',
        lead=(
            "Reef context, turtle possibilities (not guarantees), boat versus shore choices, "
            "and what usually fits a Willemstad cruise call."
        ),
        image=None,
        aria_label="Curacao snorkelling for cruise passengers",
        css_only=True,
        breadcrumb="Snorkelling",
        actions=_cta(
            "/klein-curacao-day-trip",
            "Plan Klein day",
            "/best-curacao-cruise-excursions",
            "Compare options",
        ),
        tags=["Reef", "Turtles possible", "Boat or shore", "Cruise timing"],
    )

    snap = cruise_snapshot(
        [
            ("Boat snorkel", "Often includes transfers and timed water stops"),
            ("Shore snorkel", "Needs beach access + gear plan; west coast usually longer drive"),
            ("Wildlife", "Turtles sometimes seen — never promised"),
            ("Conditions", "Clarity and swell vary — confirm live"),
            ("Klein overlap", "Klein is a full-day island sail, not a short reef hop"),
            ("This site", "Editorial only — no booking checkout"),
        ],
        label="Snorkelling cruise snapshot",
    )

    faqs: list[tuple[str, str]] = [
        (
            "Will I see turtles on a Curacao snorkel day?",
            "Turtles are possible in places, not guaranteed. Treat wildlife sightings as a bonus, "
            "not a contractual highlight, and confirm what the operator actually includes.",
        ),
        (
            "Boat snorkel or shore snorkel?",
            "Boat days package water time with transfers; shore days need beach access and your own "
            "timing discipline. West-coast beaches often need a longer road transfer from Willemstad.",
        ),
        (
            "Is Klein Curacao the same as a snorkel tour?",
            "No. Klein is typically a full-day outer-island boat commitment. Many snorkel products "
            "stay nearer Curacao and fit shorter calls more easily — compare durations carefully.",
        ),
        (
            "Do you sell snorkelling tours here?",
            "No. This is an editorial planning guide. We do not process bookings or payments.",
        ),
    ]

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Curacao's underwater appeal is real: fringing reef, clear water on good days, and occasional
  turtle encounters. For cruise passengers the useful split is <strong>boat-organised water time</strong>
  versus <strong>shore access</strong> — plus whether you are accidentally shopping for a
  <a href="/klein-curacao-day-trip" class="text-ocean-600 font-medium">Klein Curacao</a>
  full-day sail when a nearer reef stop would do.
</p>
''' + snap)}
{_section('''
<div class="max-w-3xl">
  <div class="section-label">Cruise practicality</div>
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Match water time to the call</h2>
  <p class="text-gray-600 leading-relaxed mb-4">
    Shorter calls favour organised boat snorkels with clear return windows, or a near-port beach
    such as the Mambo Beach area when swimming matters more than remote reef. Longer calls can
    stretch toward west-coast names such as Kenepa — still a road commitment, still needing margin.
  </p>
  <p class="text-gray-600 leading-relaxed">
    Ask operators about gear, swimming ability expectations, and what happens if sea conditions
    deteriorate. Soft claims beat hard promises.
  </p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  Inland or coastal stops such as Shete Boka's wave-cut cliffs are scenic context, not snorkel
  substitutes. Keep the day to one water theme unless your call is unusually long.
</p>
''' + related_links([
    ("/klein-curacao-day-trip", "Plan Klein day"),
    ("/curacao-cruise-port-guide", "Port guide"),
    ("/best-curacao-cruise-excursions", "Compare options"),
    ("/willemstad-walking-tour", "Willemstad walking"),
]))}
{faq_section(faqs, heading="Curacao snorkelling FAQ")}
"""

    meta: Meta = {
        "title": "Curacao Snorkelling Tours | Cruise Day Reef Planning",
        "description": (
            "Plan Curacao snorkelling from a cruise call — reef context, turtle possibilities, "
            "boat versus shore choices and realistic timing."
        ),
        "canonical_path": "/curacao-snorkeling-tours",
        "page_id": "snorkeling",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# PORT GUIDE
# ---------------------------------------------------------------------------


def port_guide() -> PageTuple:
    hero = hero_band(
        eyebrow="Port logistics",
        title_html=f'Curacao <br/> <span class="{ACCENT}">cruise port guide</span>',
        lead=(
            "Mega Pier and Mathey Wharf orientation, Punda and Otrobanda walkability, "
            "beach versus west-coast trade-offs, and return planning without invented guarantees."
        ),
        image=CRUISE_PORT,
        aria_label=CRUISE_PORT_ALT,
        breadcrumb="Port guide",
        actions=_cta(
            "/best-curacao-cruise-excursions",
            "Compare options",
            "/klein-curacao-day-trip",
            "Plan Klein day",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Typical berths", "Mega Pier or Mathey Wharf — confirm your ship"),
            ("Near-port", "Punda / Otrobanda; Handelskade colour"),
            ("Bridge link", "Queen Emma pontoon bridge often connects the two sides"),
            ("Near beach", "Mambo Beach area usually needs a short transfer"),
            ("West coast", "Kenepa and similar — longer drive commitment"),
            ("Return planning", "Leave margin; queues and traffic vary"),
        ],
        label="Willemstad port snapshot",
    )

    faqs: list[tuple[str, str]] = [
        (
            "Where do cruise ships dock in Curacao?",
            "Calls typically use Mega Pier or Mathey Wharf in the Willemstad area. Confirm berth "
            "notes for your sailing — arrangements can vary.",
        ),
        (
            "Can I walk around Willemstad from the pier?",
            "Often yes for Handelskade, Punda and Otrobanda, depending on berth and walking comfort. "
            "Treat west-coast beaches and inland stops as transfer-based, not casual strolls.",
        ),
        (
            "How far is Mambo Beach from the cruise port?",
            "The Mambo Beach area is typically a short taxi or organised transfer from Willemstad "
            "berths — not a waterfront stroll. Agree return pickup and leave margin before all-aboard.",
        ),
        (
            "Should I attempt Klein Curacao on every call?",
            "No. Klein is usually a full-day boat commitment. Use this port guide plus the Klein "
            "page to compare timing honestly against your all-aboard.",
        ),
    ]

    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Curacao's cruise gateway is <strong>Willemstad</strong>. Ships generally dock at
  <strong>Mega Pier</strong> or <strong>Mathey Wharf</strong> — treat that as typical planning
  guidance, not a guarantee that every sailing uses the same berth or passenger flow. Confirm your
  ship's port notes for the call.
</p>
''' + snap)}
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Near the pier</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Punda, Otrobanda and walkability</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      The pastel <strong>Handelskade</strong> façades and the Punda / Otrobanda split across
      St Anna Bay reward an unhurried walk. The Queen Emma pontoon bridge often links the two
      sides when it is closed to water traffic — confirm live if you are timing photos around it.
    </p>
    <p class="text-gray-600 leading-relaxed">
      For a structured town focus, see the
      <a href="/willemstad-walking-tour" class="text-ocean-600 font-medium">Willemstad walking</a> guide.
    </p>
  </div>
  <div>
    <div class="section-label">Further out</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Beach vs west coast</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Near-port beach time (often the <strong>Mambo Beach</strong> area) usually needs a short
      transfer. West-coast names such as <strong>Kenepa</strong> typically need a longer drive —
      beautiful water, higher road commitment. We do not publish fares; agree return pickup clearly.
    </p>
    <p class="text-gray-600 leading-relaxed">
      Inland context stops such as Hato caves, Shete Boka or Christoffel add duration. Stacking
      them onto a beach morning or a Klein sail usually squeezes the return window.
    </p>
  </div>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Currency and return planning</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  USD is commonly accepted at tourist-facing points; local currency notes appear in change.
  Carry small notes for taxis where appropriate, and confirm payment expectations before you depart.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Ship-sold tours and independent arrangements both have trade-offs. Neither approach guarantees
  you will make the ship — leave margin, watch queues, and treat traffic as a variable.
</p>
''' + related_links([
    ("/best-curacao-cruise-excursions", "Compare options"),
    ("/klein-curacao-day-trip", "Plan Klein day"),
    ("/willemstad-walking-tour", "Willemstad walking"),
    ("/contact", "Contact"),
]))}
{faq_section(faqs, heading="Curacao port FAQ")}
"""

    meta: Meta = {
        "title": "Curacao Cruise Port Guide | Mega Pier & Willemstad",
        "description": (
            "Willemstad cruise port guide for Mega Pier and Mathey Wharf — Punda and Otrobanda "
            "walkability, beach versus west-coast transfers, and return planning."
        ),
        "canonical_path": "/curacao-cruise-port-guide",
        "page_id": "port",
        "og_image": CRUISE_PORT,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# BEST EXCURSIONS (decision hub)
# ---------------------------------------------------------------------------


def best_excursions() -> PageTuple:
    hero = hero_band(
        eyebrow="Decision hub",
        title_html=f'Compare Curacao <br/> <span class="{ACCENT}">cruise day styles</span>',
        lead=(
            "Klein, snorkelling, Willemstad walking, beach or island time, and private pacing — "
            "grouped by how they fit a cruise call, not by invented popularity rankings."
        ),
        image=None,
        aria_label="Curacao cruise excursion comparison for passengers",
        css_only=True,
        breadcrumb="Excursions",
        actions=_cta(
            "/curacao-cruise-port-guide",
            "Port guide",
            "/klein-curacao-day-trip",
            "Plan Klein day",
        ),
    )

    snap = cruise_snapshot(
        [
            ("How to use this page", "Choose a theme, then open the matching guide"),
            ("Highest commitment", "Klein Curacao — full-day boat + sea state"),
            ("Water nearer island", "Snorkel boat or shore — confirm duration"),
            ("Lowest transfer", "Willemstad walking around Punda / Otrobanda"),
            ("Custom pace", "Private — still confirm return time in writing"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Curacao shore days become clearer once you decide how far you are willing to travel from
  Willemstad and how much open-water risk you accept. Stay in town for Handelskade colour;
  commit a short transfer for near-port beach time; reserve a full day — and honest sea-state
  language — for Klein. Mixing every highlight on a short call usually produces rushed photos
  and a tense return window.
</p>
''' + snap)}
{_section(f'''
<div class="text-center mb-10">
  <div class="section-label justify-center">Five decision themes</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900">Start with the question you actually have</h2>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
  {_card("/klein-curacao-day-trip", "Klein Curacao", "Full-day uninhabited island sail — compare timing to all-aboard before you commit.", image=KLEIN, alt=KLEIN_ALT, cta="Plan Klein day →")}
  {_card("/curacao-snorkeling-tours", "Snorkelling", "Reef and turtle possibilities; boat versus shore; cruise-day practicality.", media_label="Snorkel day", cta="Read snorkelling guide →")}
  {_card("/willemstad-walking-tour", "Willemstad", "Punda, Otrobanda and Handelskade — request the guided walking tour online when you are ready.", image=WILLEMSTAD, alt=WILLEMSTAD_ALT, cta="Willemstad guide →")}
  {_card("/curacao-cruise-port-guide", "Beach / island day", "Mambo-area beach time versus longer west-coast or island commitments — port logistics first.", image=CRUISE_PORT, alt=CRUISE_PORT_ALT, cta="Port guide →")}
  {_card("/private-curacao-tours", "Private", "Custom sequencing when ages, mobility or timing differ within one group.", image=PRIVATE_SIGN, alt=PRIVATE_SIGN_ALT, cta="Private guide →")}
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  Most pages here are planning guides. You can
  <a href="/book/historic-walking-tour" class="text-ocean-600 font-medium">request the Willemstad Historic Walking Tour</a>
  online — payment creates a booking request, and confirmation is emailed separately.
  For other day styles, confirm inclusions, pickup logistics and timing with any independent
  operator and your cruise line before you travel. Leave margin before all-aboard.
</p>
''' + related_links([
    ("/book/historic-walking-tour", "Request walking tour"),
    ("/willemstad-walking-tour", "Willemstad guide"),
    ("/curacao-cruise-port-guide", "Port guide"),
    ("/contact", "Contact"),
]))}
"""

    meta: Meta = {
        "title": "Best Curacao Cruise Excursions | Compare Day Styles",
        "description": (
            "Compare Curacao cruise excursion styles from Willemstad — Klein Curacao, "
            "snorkelling, Willemstad walking, beach days and private pacing."
        ),
        "canonical_path": "/best-curacao-cruise-excursions",
        "page_id": "excursions",
        "og_image": None,
    }
    return hero, main, None, meta


# ---------------------------------------------------------------------------
# WILLEMSTAD WALKING
# ---------------------------------------------------------------------------


def walking() -> PageTuple:
    hero = hero_band(
        eyebrow="Near-port colour",
        title_html=f'Willemstad <br/> <span class="{ACCENT}">walking tour</span>',
        lead=(
            "Punda and Otrobanda orientation, Handelskade façades, and a low-transfer cruise day "
            "when you want Willemstad itself rather than a long road or boat commitment."
        ),
        image=WILLEMSTAD,
        aria_label=WILLEMSTAD_ALT,
        breadcrumb="Willemstad",
        actions=_cta(
            "/book/historic-walking-tour",
            "Book now",
            "/curacao-cruise-port-guide",
            "Port guide",
        ),
        tags=["Punda", "Otrobanda", "Handelskade", "Low transfer"],
    )

    snap = cruise_snapshot(
        [
            ("Best for", "Architecture, waterfront colour, shorter calls"),
            ("Typical focus", "Punda shops / streets; Otrobanda views; Handelskade photos"),
            ("Bridge", "Queen Emma pontoon — status can change with shipping"),
            ("Activity", "Walking on uneven historic streets — pace yourself"),
            ("Request online", "$57 per participant · confirmation emailed separately"),
        ]
    )

    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  A Willemstad walking day keeps you close to the cruise berths: pastel Dutch Caribbean façades,
  harbour edges, and the lived-in split between <strong>Punda</strong> and <strong>Otrobanda</strong>.
  It is often the lowest-transfer option on a Curacao call — and the right answer when Klein's
  full-day boat clock feels too aggressive.
</p>
''' + snap)}
{_section('''
<div class="max-w-3xl">
  <div class="section-label">Request online</div>
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Willemstad Historic Walking Tour</h2>
  <p class="text-gray-600 leading-relaxed mb-4">
    Request a guided historic walking experience for <strong>$57 per participant</strong>
    (maximum 10 online). Payment creates a booking request — confirmation is emailed separately.
    If we cannot confirm, you receive a full refund.
  </p>
  <p class="mb-6">
    <a href="/book/historic-walking-tour" class="btn-ocean inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Book now</a>
  </p>
  <div class="section-label">How to shape the walk</div>
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">One side, then the other — with margin</h2>
  <p class="text-gray-600 leading-relaxed mb-4">
    Start with Handelskade views, then decide whether you have time to cross into the other
    neighbourhood. Heat, uneven paving and shopping queues all eat time. Leave a clear buffer
    to re-enter the terminal area before all-aboard.
  </p>
  <p class="text-gray-600 leading-relaxed">
    If you still want water after town, prefer a short transfer toward the Mambo Beach area over
    inventing a west-coast marathon. For reef focus, open the
    <a href="/curacao-snorkeling-tours" class="text-ocean-600 font-medium">snorkelling guide</a>;
    for island ambition, read
    <a href="/klein-curacao-day-trip" class="text-ocean-600 font-medium">Klein Curacao</a> first.
  </p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
''' + related_links([
    ("/book/historic-walking-tour", "Book walking tour"),
    ("/curacao-cruise-port-guide", "Port guide"),
    ("/best-curacao-cruise-excursions", "Compare options"),
    ("/contact", "Contact"),
]))}
"""

    meta: Meta = {
        "title": "Willemstad Walking Tour | Punda & Otrobanda Cruise Guide",
        "description": (
            "Plan a Willemstad walking day from a cruise call — Punda, Otrobanda, Handelskade "
            "colour and low-transfer return-window planning."
        ),
        "canonical_path": "/willemstad-walking-tour",
        "page_id": "willemstad",
        "og_image": WILLEMSTAD,
    }
    return hero, main, None, meta


# ---------------------------------------------------------------------------
# PRIVATE TOURS (editorial only)
# ---------------------------------------------------------------------------


def private_tours() -> PageTuple:
    hero = hero_band(
        eyebrow="Custom pacing",
        title_html=f'Private Curacao <br/> <span class="{ACCENT}">tours</span>',
        lead=(
            "Editorial guidance for private shore days: custom pacing, mixed mobility within "
            "a group, and confirming return time in writing — without booking on this site."
        ),
        image=PRIVATE_SIGN,
        aria_label=PRIVATE_SIGN_ALT,
        breadcrumb="Private tours",
        actions=_cta(
            "/best-curacao-cruise-excursions",
            "Compare options",
            "/curacao-cruise-port-guide",
            "Port guide",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Best for", "Mixed ages, mobility needs, custom stop lists"),
            ("Advantage", "Pace control — not automatic schedule safety"),
            ("Must do", "Confirm return time in writing before paying"),
            ("Still true", "Leave margin before all-aboard"),
            ("This site", "Editorial only — no booking checkout"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Private tours help when one shared package will not fit everyone: different walking speeds,
  limited stairs tolerance, or a wish to blend Willemstad colour with a short beach stop without
  joining a fixed coach script. Flexibility is the point — it is not a substitute for written
  timing discipline.
</p>
''' + snap)}
{_section('''
<div class="max-w-3xl">
  <div class="section-label">Before you pay</div>
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Return time in writing</h2>
  <p class="text-gray-600 leading-relaxed mb-4">
    Agree the latest pier return, what happens if traffic builds, and whether the driver waits at
    beach or viewpoint stops. Keep the plan shorter than the maximum hours available. Confirm
    payment method and cancellation terms without sharing card details on casual email threads
    you do not trust.
  </p>
  <p class="text-gray-600 leading-relaxed">
    Use the theme guides —
    <a href="/willemstad-walking-tour" class="text-ocean-600 font-medium">Willemstad</a>,
    <a href="/curacao-snorkeling-tours" class="text-ocean-600 font-medium">snorkelling</a>,
    <a href="/klein-curacao-day-trip" class="text-ocean-600 font-medium">Klein</a> —
    to choose ingredients, then ask a private operator to sequence only what fits. West-coast
    beaches, Shete Boka or Christoffel each add road time; do not treat them as free add-ons.
  </p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
''' + related_links([
    ("/best-curacao-cruise-excursions", "Compare options"),
    ("/curacao-cruise-port-guide", "Port guide"),
    ("/contact", "Contact"),
]))}
"""

    meta: Meta = {
        "title": "Private Curacao Tours | Custom Cruise Shore Days",
        "description": (
            "Plan private Curacao tours from a cruise call — custom pacing, mixed mobility, and "
            "confirming return time in writing. Editorial guidance only."
        ),
        "canonical_path": "/private-curacao-tours",
        "page_id": "private",
        "og_image": PRIVATE_SIGN,
    }
    return hero, main, None, meta


# ---------------------------------------------------------------------------
# TRUST / LEGAL
# ---------------------------------------------------------------------------


def contact() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'Contact <br/> <span class="{ACCENT}">{SITE}</span>',
        lead="Editorial questions about this Curacao cruise planning guide.",
        image=None,
        aria_label="Contact Curacao Cruise Excursions",
        css_only=True,
        breadcrumb="Contact",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Email <a href="mailto:{EMAIL}" class="text-ocean-600 font-semibold">{EMAIL}</a>
  for questions about this guide or a Historic Walking Tour booking request.
  You can also <a href="/book/historic-walking-tour" class="text-ocean-600 font-medium">request the walking tour online</a>.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Please include your ship’s scheduled Willemstad / Curacao date if you are asking about planning
  logic — we still will not invent fares or guarantee operator inventory beyond confirmed bookings.
</p>
<p class="text-sm text-gray-500">Do not send payment card details by email.</p>
''')}
"""
    meta: Meta = {
        "title": f"Contact | {SITE}",
        "description": (
            f"Contact {SITE} at {EMAIL} for editorial questions about this Curacao cruise "
            "planning guide."
        ),
        "canonical_path": "/contact",
        "page_id": "contact",
        "og_image": None,
    }
    return hero, main, None, meta


def about() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'About <br/> <span class="{ACCENT}">{SITE}</span>',
        lead="Independent cruise-passenger planning for Curacao, from Willemstad.",
        image=CRUISE_PORT,
        aria_label=CRUISE_PORT_ALT,
        breadcrumb="About",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  {SITE} helps cruise passengers decide what is genuinely practical from a Willemstad call —
  Klein Curacao sea days, snorkelling, Handelskade walking, near-port beach time, and private
  pacing — without pretending every highlight fits every ship schedule.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  We are not a cruise line and not a pier operator. Most pages are editorial planning guides.
  The Willemstad Historic Walking Tour can be requested online as a paid booking request —
  confirmation is separate.
</p>
<p class="text-gray-600 leading-relaxed">
  Read our <a href="/methodology" class="text-ocean-600 font-medium">methodology</a>
  and <a href="/contact" class="text-ocean-600 font-medium">contact</a> pages for how we work.
</p>
''')}
"""
    meta: Meta = {
        "title": f"About | {SITE}",
        "description": (
            f"About {SITE} — an independent cruise passenger planning guide for Curacao "
            "from Willemstad."
        ),
        "canonical_path": "/about",
        "page_id": "about",
        "og_image": CRUISE_PORT,
    }
    return hero, main, None, meta


def privacy() -> PageTuple:
    hero = hero_band(
        eyebrow="Legal",
        title_html=f'Privacy <br/> <span class="{ACCENT}">policy</span>',
        lead="How this editorial website handles information.",
        image=None,
        aria_label="Privacy policy",
        css_only=True,
        breadcrumb="Privacy",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  {SITE} is an editorial planning website. If you email us at
  <a href="mailto:{EMAIL}" class="text-ocean-600 font-medium">{EMAIL}</a>,
  we use your message only to respond. We do not sell personal information.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Standard server and security logs may record technical data such as IP address, user agent and
  requested URLs. Analytics, if enabled by the hosting platform, may collect aggregated traffic
  statistics.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Payment card details for the Historic Walking Tour request are collected by a hosted payment
  checkout page, not on this website's editorial pages. Editorial pages do not ask for card details.
</p>
<p class="text-sm text-gray-500">Questions: <a href="mailto:{EMAIL}" class="text-ocean-600">{EMAIL}</a>.</p>
''')}
"""
    meta: Meta = {
        "title": f"Privacy Policy | {SITE}",
        "description": (
            f"Privacy policy for {SITE} — how this Curacao cruise planning website handles "
            "information."
        ),
        "canonical_path": "/privacy",
        "page_id": "privacy",
        "og_image": None,
    }
    return hero, main, None, meta


def terms() -> PageTuple:
    hero = hero_band(
        eyebrow="Legal",
        title_html=f'Terms of <br/> <span class="{ACCENT}">use</span>',
        lead="Editorial information only — not a booking contract.",
        image=None,
        aria_label="Terms of use",
        css_only=True,
        breadcrumb="Terms",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  Content on {SITE} is general planning information for cruise passengers. It is not a ticket,
  voucher, insurance policy or contract with any tour operator. Attraction access, sea conditions
  and ship schedules change — confirm live details before you travel.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  We are not affiliated with cruise lines calling at Willemstad, Curacao. Mentions of Klein Curacao,
  reefs, beaches or town landmarks do not imply partnership.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  To the fullest extent permitted by law, we disclaim liability for decisions made solely on the
  basis of editorial planning pages. Online booking requests for the Historic Walking Tour create
  a paid request relationship as described at checkout — payment is not instant confirmation.
</p>
<p class="text-sm text-gray-500">Contact: <a href="mailto:{EMAIL}" class="text-ocean-600">{EMAIL}</a>.</p>
''')}
"""
    meta: Meta = {
        "title": f"Terms of Use | {SITE}",
        "description": (
            f"Terms of use for {SITE} — editorial cruise planning information, not a booking "
            "marketplace."
        ),
        "canonical_path": "/terms",
        "page_id": "terms",
        "og_image": None,
    }
    return hero, main, None, meta


def methodology() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'Methodology <br/> <span class="{ACCENT}">&amp; sourcing</span>',
        lead="How we organise Curacao cruise-day guidance without inventing commercial claims.",
        image=CRUISE_PORT,
        aria_label=CRUISE_PORT_ALT,
        breadcrumb="Methodology",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  {SITE} prioritises cruise-passenger decisions: call length, transfer burden, and whether a stop
  sits in Willemstad’s local orbit or requires a longer west-coast or open-water commitment.
</p>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-6">
  <li>Preserve equity URLs that already attract search interest (extensionless, no trailing slash).</li>
  <li>Treat Klein Curacao as highest-equity full-day sea planning — never as a guaranteed ship return.</li>
  <li>Use soft claims (“often”, “typically”, “confirm live”) instead of invented schedules or fares.</li>
  <li>Image policy: cruise-port, Klein, Willemstad and private-sign assets only when themed; CSS-only heroes otherwise.</li>
  <li>Mention Mambo Beach, Kenepa, Hato, Shete Boka and Christoffel only as contextual duration cues — no standalone pages.</li>
  <li>No ship schedules imported as facts; only the Willemstad Historic Walking Tour is offered as an online request-to-book product.</li>
  <li>Avoid review-aggregate, product-offer and local-business schema types; no fake popularity language.</li>
</ul>
<p class="text-gray-600 leading-relaxed">
  See <a href="/about" class="text-ocean-600 font-medium">about</a> and
  <a href="/contact" class="text-ocean-600 font-medium">contact</a>. Site apex:
  <a href="{APEX}/" class="text-ocean-600 font-medium">{APEX}/</a>.
</p>
''')}
"""
    meta: Meta = {
        "title": f"Methodology | {SITE}",
        "description": (
            f"How {SITE} researches and organises Curacao cruise shore excursion planning guides."
        ),
        "canonical_path": "/methodology",
        "page_id": "methodology",
        "og_image": CRUISE_PORT,
    }
    return hero, main, None, meta


def not_found() -> PageTuple:
    hero = ""
    main = f"""
<section class="pt-28 pb-24 bg-white">
  <div class="max-w-xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="section-label justify-center">404</p>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Page not found</h1>
    <p class="text-gray-600 leading-relaxed mb-8">
      That URL is not part of the {SITE} guide. Try the excursions hub or port guide.
    </p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="/" class="btn-ocean inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Home</a>
      <a href="/best-curacao-cruise-excursions" class="inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm border border-ocean-200 text-ocean-700">Compare options</a>
      <a href="/curacao-cruise-port-guide" class="inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm border border-ocean-200 text-ocean-700">Port guide</a>
    </div>
  </div>
</section>
"""
    meta: Meta = {
        "title": f"Page not found | {SITE}",
        "description": f"The requested page was not found on {SITE}.",
        "canonical_path": "/404.html",
        "page_id": "not-found",
        "og_image": CRUISE_PORT,
    }
    return hero, main, None, meta
