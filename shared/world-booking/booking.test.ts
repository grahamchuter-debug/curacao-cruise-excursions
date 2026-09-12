/**
 * Shared booking engine tests — Curacao Phase 17D (Willemstad Historic Walking Tour only).
 */
import assert from "node:assert/strict";
import { test } from "node:test";
import {
  CURACAO_BOOKABLE_PRODUCTS,
  CURACAO_CANCELLATION_COPY,
  findCuracaoBookingProduct,
} from "../destinations/curacao-products";
import { curacaoBookingCore } from "../destinations/curacao";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  createBookingReference,
  destinationBrandFromCore,
  requestedCustomerEmail,
  statusAfterPaymentSuccess,
  supplierRequestEmail,
  validateCruise,
  validateCustomer,
} from "./index";

const brand = destinationBrandFromCore(curacaoBookingCore);
const walking = findCuracaoBookingProduct("historic-walking-tour");
assert.ok(walking);

test("single Curacao product ID present", () => {
  assert.equal(CURACAO_BOOKABLE_PRODUCTS.length, 1);
  assert.equal(CURACAO_BOOKABLE_PRODUCTS[0]!.id, "historic-walking-tour");
});

test("quantity-only USD 57; no invented child/infant rates", () => {
  assert.equal(walking!.pricing.model, "flat_per_guest");
  assert.equal(walking!.pricing.pricePerGuest, 57);
  assert.equal(walking!.pricing.adultAmount, 57);
  assert.equal(walking!.pricing.childAmount, null);
  assert.equal(walking!.pricing.childPricingStatus, "not_sold");
  assert.equal(walking!.pricing.infantAmount, null);
  assert.equal(walking!.pricing.infantPricingStatus, "not_sold");
  assert.equal(calculateBookingQuote(walking!, { adults: 1, children: 0, infants: 0 }).amountCents, 5700);
  assert.equal(calculateBookingQuote(walking!, { adults: 2, children: 0, infants: 0 }).amountCents, 11400);
  assert.equal(calculateBookingQuote(walking!, { adults: 10, children: 0, infants: 0 }).amountCents, 57000);
  assert.throws(() => calculateBookingQuote(walking!, { adults: 0, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(walking!, { adults: 11, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(walking!, { adults: -1, children: 0, infants: 0 }));
});

test("client total must match server quote", () => {
  const quote = calculateBookingQuote(walking!, { adults: 1, children: 0, infants: 0 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 5700));
  assert.throws(() => assertClientTotalMatches(quote, 8900));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("booking references use Curacao W2CUR prefix", () => {
  assert.match(createBookingReference(curacaoBookingCore), /^W2CUR-/);
  assert.equal(curacaoBookingCore.bookingRefPrefix, "W2CUR");
});

test("customer and cruise validation", () => {
  assert.equal(
    validateCustomer({ name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" }),
    null,
  );
  assert.ok(validateCustomer({ name: "A", email: "x", phone: "1" }));
  assert.ok(
    validateCruise({
      date: "2020-01-01",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
  );
  assert.equal(
    validateCruise({
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
    null,
  );
});

test("cancellation copy covers 14-day policy and full refund", () => {
  assert.match(CURACAO_CANCELLATION_COPY.customerCancellation, /outside 14 days/i);
  assert.match(CURACAO_CANCELLATION_COPY.customerCancellation, /14th day/i);
  assert.match(CURACAO_CANCELLATION_COPY.unableToConfirm, /full refund/i);
  assert.match(CURACAO_CANCELLATION_COPY.paymentNotConfirmation, /confirm.*separately|separately.*confirm/i);
});

test("customer email never exposes SEG or internal codes", () => {
  const mail = requestedCustomerEmail({
    brand,
    product: walking!,
    reference: "W2CUR-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 0 },
    amountLabel: "USD $57.00",
    customerName: "Alex Traveller",
  });
  const blob = JSON.stringify(mail);
  assert.doesNotMatch(blob, /\bSEG\b|cacucurcolhis|Shore Excursions Group|info@wowatour/i);
  assert.match(blob, /request|confirm/i);
});

test("ops email includes internal supply notes for Graham", () => {
  const mail = supplierRequestEmail({
    product: walking!,
    reference: "W2CUR-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 0 },
    amountLabel: "USD $57.00",
    customer: {
      name: "Alex Traveller",
      email: "alex@example.com",
      phone: "+447700900123",
    },
    destinationLabel: "Curacao Cruise Excursions — new booking request",
  });
  const blob = JSON.stringify(mail);
  assert.match(blob, /cacucurcolhis|SEG_MANUAL/i);
});

test("reject foreign destination product lookup", () => {
  assert.equal(findCuracaoBookingProduct("grenadas-spice-route"), null);
  assert.equal(findCuracaoBookingProduct("classic-beach-day"), null);
  assert.equal(findCuracaoBookingProduct("doctors-cave-beach"), null);
  assert.equal(findCuracaoBookingProduct("belize-cave-tubing"), null);
});
