/**
 * Public commercial status for Curacao Cruise Excursions (Phase 17D).
 * Internal supply references must never appear on customer pages.
 */
window.CUR_COMMERCIAL = {
  bookingsApiUrl: "https://curacao-bookings-prod.dark-violet-8d91.workers.dev",
  email: "hello@curacaocruiseexcursions.com",
  siteName: "Curacao Cruise Excursions",
  defaultPublicBookingStatus: "PRODUCTION_READY_LOCKED",
  cancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  meetingInstructions:
    "Meeting instructions will be provided with your confirmed excursion details. Expect approximately a 2–10 minute walk from the cruise pier.",
  overTenGuidance:
    "For groups larger than 10, email hello@curacaocruiseexcursions.com before requesting.",
  products: {
    "historic-walking-tour": {
      productId: "historic-walking-tour",
      slug: "historic-walking-tour",
      name: "Willemstad Historic Walking Tour",
      shortTitle: "Historic Walking Tour",
      productPath: "/willemstad-walking-tour",
      bookingPath: "/book/historic-walking-tour",
      receivedPath: "/book/historic-walking-tour/received",
      adultUsd: 57,
      childUsd: null,
      infantUsd: null,
      guestModel: "quantity_only",
      durationLabel: "2 hours 30 minutes",
      maxGuests: 10,
      publicBookingStatus: "PRODUCTION_READY_LOCKED",
      displayPrice: "$57 per participant · maximum 10 online",
    },
  },
};
