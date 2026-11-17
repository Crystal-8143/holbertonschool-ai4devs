"use strict";
const assert = require("node:assert/strict");
const { invoiceTotal } = require("../bug2_fixed.js");
const { unitsSold } = require("../bug5_fixed.js");
let passed = 0;

function test(name, fn) {
  fn();
  passed++;
  console.log(`PASS ${name}`);
}

test("bug2 discount before tax", () => assert.equal(invoiceTotal(100, 20, 10), 88));
test("bug2 no discount", () => assert.equal(invoiceTotal(100, 0, 10), 110));
test("bug2 full discount", () => assert.equal(invoiceTotal(100, 100, 10), 0));
test("bug2 cent rounding", () => assert.equal(invoiceTotal(19.99, 15, 10), 18.69));
test("bug2 zero subtotal", () => assert.equal(invoiceTotal(0, 20, 10), 0));
test("bug2 invalid discount", () => assert.throws(() => invoiceTotal(100, 101, 10), /invalid discount/));

test("bug5 sums repeated quantities", () => assert.deepEqual(unitsSold([
  { productId: "plant-a", quantity: 3 },
  { productId: "plant-b", quantity: 1 },
  { productId: "plant-a", quantity: 2 },
]), { "plant-a": 5, "plant-b": 1 }));
test("bug5 empty orders", () => assert.deepEqual(unitsSold([]), {}));
test("bug5 single order", () => assert.deepEqual(unitsSold([{ productId: "a", quantity: 7 }]), { a: 7 }));
test("bug5 rejects fractional quantity", () => assert.throws(() => unitsSold([{ productId: "a", quantity: 1.5 }]), /invalid order/));
test("bug5 rejects missing quantity", () => assert.throws(() => unitsSold([{ productId: "a" }]), /invalid order/));
test("bug5 special product key", () => assert.deepEqual(unitsSold([{ productId: "__proto__", quantity: 2 }]), Object.fromEntries([["__proto__", 2]])));

console.log(`JavaScript assertions passed: ${passed}`);
