function calculateTotal(price, quantity, discount) {
    const subtotal = price * quantity;
    const discountAmount = subtotal * (discount / 100);
    const total = subtotal - discountAmount;

    return total;
}

const price = 25;
const quantity = 4;
const discount = 10;

const total = calculateTotal(price, quantity, discount);

console.log("Total:", total);