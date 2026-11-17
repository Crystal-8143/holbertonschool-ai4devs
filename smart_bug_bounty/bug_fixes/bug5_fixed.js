// Aggregate the number of units sold for each product in an order list.
function unitsSold(orders) {
  const totals = Object.create(null);
  for (const order of orders) {
    const { productId, quantity } = order;
    if (
      typeof productId !== "string" ||
      !Number.isSafeInteger(quantity) ||
      quantity < 1
    ) {
      throw new Error("invalid order");
    }
    if (!(productId in totals)) {
      totals[productId] = 0;
    }
    // Add the number of units, not just one per order record.
    totals[productId] += quantity;
  }
  return { ...totals };
}

if (require.main === module) {
  const orders = [
    { productId: "plant-a", quantity: 3 },
    { productId: "plant-b", quantity: 1 },
    { productId: "plant-a", quantity: 2 },
  ];
  console.log("Units sold:", unitsSold(orders));
}

module.exports = { unitsSold };
