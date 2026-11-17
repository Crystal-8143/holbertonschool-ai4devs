// Calculate a discounted invoice total with tax added afterward.
function invoiceTotal(subtotal, discountPercent, taxPercent) {
    if (subtotal < 0) {
        throw new Error("Subtotal cannot be negative");
    }
    if (discountPercent < 0 || discountPercent > 100) {
        throw new Error("Discount percent must be a value between 0 and 100");
    }
    if (taxPercent < 0) {
        throw new Error("Tax percent cannot be negative");
    }

    const discount = subtotal * (discountPercent / 100);
    const discountedSubtotal = subtotal - discount;
    const tax = subtotal * (taxPercent / 100);
    return Math.round((discountedSubtotal + tax) * 100) / 100; // Round to two decimal places
}

const result = invoiceTotal(100, 20, 10);
console.log("Invoice Total: $" + result); // Expected output: Invoice Total: $90.00
