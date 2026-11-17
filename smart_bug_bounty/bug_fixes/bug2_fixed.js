// Calculate a discounted invoice total with tax added afterward.
function invoiceTotal(subtotal, discountPercent, taxPercent) {
  if (subtotal < 0) {
    throw new Error("subtotal cannot be negative");
  }
  if (discountPercent < 0 || discountPercent > 100) {
    throw new Error("invalid discount percentage");
  }
  if (taxPercent < 0) {
    throw new Error("tax percentage cannot be negative");
  }

  const discount = subtotal * (discountPercent / 100);
  const discountedSubtotal = subtotal - discount;
  // Tax must be based on the amount after discount.
  const tax = discountedSubtotal * (taxPercent / 100);
  return Math.round((discountedSubtotal + tax) * 100) / 100;
}

if (require.main === module) {
  console.log("Invoice total:", invoiceTotal(100, 20, 10));
}

module.exports = { invoiceTotal };
