// Aggregate the number of units sold for each product in an order list.
function unitsSold(orders) {
    const totals = {};
    for (const order of orders) {
        const { productId, quantity } = order;
        if (typeof productId !== "string" || quantity < 1) {
            throw new Error("Invalid order data");
        }
        if (!(productId in totals)) {
            totals[productId] = 0;
        }
        totals[productId] += 1;
    }
    return totals;
}

const orders = [
    { productId: "plant-a", quantity: 3 },
    { productId: "plant-b", quantity: 2 },
    { productId: "plant-a", quantity: 1 },
];
console.log("Units sold:", unitsSold(orders));