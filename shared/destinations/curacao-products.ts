import { curacaoBookingCore } from "./curacao";
import type { AgeBand, BookableProductConfig, ProductCapacity, ProductPricing } from "../world-booking/types";

/**
 * Operational routing: Wow A Tour ops mailbox for Graham’s manual fulfilment.
 * Public customers never see SEG. Graham places corresponding bookings via his
 * established SEG affiliate / white-label account using INTERNAL supply refs only.
 */
const OPERATIONS = {
  id: "wow-a-tour-operations",
  displayName: "Wow A Tour",
  notificationEmail: "info@wowatour.com",
  routingStatus: "production_ready" as const,
};

const REQUEST_SETTLEMENT = "charge_refund" as const;

/** Graham online max — never describe as supplier / vehicle / boat capacity. */
const CUR_CAPACITY: ProductCapacity = {
  minGuests: 1,
  maxGuestsPerBooking: 10,
  maxGuestsPerBookingSource: "approved",
  supplierGroupSize: null,
  maxGuestsPerGuide: null,
};

/**
 * Phase 17D Graham-approved:
 * Quantity-only USD 57 per participant.
 * Do NOT invent child/infant bands or minimum ages.
 * UI maps all participants into the adults count field.
 */
const PARTICIPANT_BANDS: readonly AgeBand[] = [
  { id: "adult", label: "Participants", minAge: null, maxAge: null, pricingStatus: "priced" },
  { id: "child", label: "Children", minAge: null, maxAge: null, pricingStatus: "not_sold" },
  { id: "infant", label: "Infants", minAge: null, maxAge: null, pricingStatus: "not_sold" },
];

function flatPerGuestUsd(amount: number): ProductPricing {
  return {
    model: "flat_per_guest",
    currency: "USD",
    pricePerGuest: amount,
    adultAmount: amount,
    childAmount: null,
    childPricingStatus: "not_sold",
    infantAmount: null,
    infantPricingStatus: "not_sold",
    pricingNeedsConfirmation: false,
  };
}

const SHARED_PENDING = [
  "Customer cancellation APPROVED: free outside 14 days before excursion; from the 14th day non-refundable.",
  "Unable to confirm after payment: full refund to original payment method.",
  "Meeting: approximately 2–10 minute walk from the cruise pier; exact instructions after confirmation / on source e-ticket.",
  "Fulfilment: Graham places corresponding booking via established SEG affiliate / white-label route (INTERNAL).",
  "Payment received ≠ excursion confirmed.",
  "Online max 10 participants per booking (Graham online limit — not supplier capacity).",
  "Quantity-only pricing USD 57 per participant — do not invent child/infant rates.",
  "commercial_status=SEG_FULFILMENT_READY · fulfilment_mode=SEG_MANUAL · supplier=UNKNOWN · direct_supplier_status=NOT_CONTACTED · net_cost=UNKNOWN · margin=UNKNOWN",
] as const;

export const CURACAO_CANCELLATION_COPY = {
  customerCancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable. If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  freeWindow: "Free cancellation outside 14 days before your excursion.",
  insideWindow: "From the 14th day before your excursion, bookings are non-refundable.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  meetingInstructions:
    "Meeting instructions will be provided with your confirmed excursion details. Expect approximately a 2–10 minute walk from the cruise pier.",
  overTenGuidance: "For groups larger than 10, email hello@curacaocruiseexcursions.com before requesting.",
} as const;

const HISTORIC_WALKING: BookableProductConfig = {
  id: "historic-walking-tour",
  destinationId: curacaoBookingCore.id,
  slug: "historic-walking-tour",
  name: "Willemstad Historic Walking Tour",
  durationLabel: "2 hours 30 minutes",
  bookingMode: "request",
  availability: "live",
  bookingPath: "/book/historic-walking-tour",
  receivedPath: "/book/historic-walking-tour/received",
  confirmedPath: "/book/historic-walking-tour/received",
  productPath: "/willemstad-walking-tour",
  pricing: flatPerGuestUsd(57),
  ageBands: PARTICIPANT_BANDS,
  capacity: CUR_CAPACITY,
  requiredCustomerFields: ["name", "email", "phone"],
  supplier: OPERATIONS,
  paymentSettlement: REQUEST_SETTLEMENT,
  schedulePortSlug: "curacao",
  pendingCommercialRules: [
    ...SHARED_PENDING,
    "Paying participant USD 57 · quantity-only · require ≥1 participant",
    "Themes (source-supported): Riffort, Otrobanda, Queen Emma Bridge, Fort Amsterdam, Handelskade, Punda, Mikve Israel-Emanuel Synagogue, rum tasting at AnnaBay Club Rum Distillery",
    "Inclusions: walking tour, bottled water, rum tasting",
    "Moderate activity · historic streets · Queen Emma Bridge · steps / uneven terrain may occur",
    "NOT wheelchair accessible · not recommended for pregnancy, back/neck injuries, heart conditions, or limited mobility",
    "Do NOT claim guaranteed ship return, instant confirmation, or invented meeting landmarks",
  ],
  supplierReferenceNotes: [
    "INTERNAL SUPPLY: SEG_MANUAL · cacucurcolhis",
    "INTERNAL CODE: cacucurcolhis",
    "Supplier contact: UNKNOWN · NOT_CONTACTED · net/margin UNKNOWN",
    "Fulfilment: place via established SEG affiliate / white-label route (manual — do not automate).",
    "Selling: USD 57 per participant (quantity-only).",
    "Customer cancellation: Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
    "Unable to confirm after payment: full refund to original payment method.",
  ],
};

export const CURACAO_BOOKABLE_PRODUCTS: readonly BookableProductConfig[] = [HISTORIC_WALKING];

export function findCuracaoBookingProduct(productId: string): BookableProductConfig | null {
  return CURACAO_BOOKABLE_PRODUCTS.find((p) => p.id === productId || p.slug === productId) ?? null;
}
