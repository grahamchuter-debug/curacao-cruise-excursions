/**
 * Curacao destination booking core.
 * Product catalogue: shared/destinations/curacao-products.ts
 * Public editorial: scripts/build-curacao-site.py
 * Internal supply mapping: product.supplierReferenceNotes (never public HTML)
 */
import type { DestinationBookingCore } from "../world-booking/types";

export const curacaoBookingCore = {
  id: "curacao",
  siteName: "Curacao Cruise Excursions",
  siteHostname: "curacaocruiseexcursions.com",
  siteUrl: "https://curacaocruiseexcursions.com",
  bookingEmail: "hello@curacaocruiseexcursions.com",
  originatingSite: "curacaocruiseexcursions.com",
  originatingPort: "Willemstad, Curacao",
  bookingRefPrefix: "W2CUR",
  sessionKeyPrefix: "w2-cur-booking",
  sessionKeyVersion: 1,
  currencyCode: "USD",
  bookableWindow: {
    start: "2026-09-01",
    end: "2028-12-31",
  },
  /** No Curacao schedule import — cruise date/ship are customer-entered. */
  schedulePortSlug: "curacao",
  customShipSlug: "not-listed",
  contactPath: "/contact",
  termsPath: "/terms",
  privacyPath: "/privacy",
} as const satisfies DestinationBookingCore;
