# Bug Snippet Descriptions

This directory contains six intentionally buggy code snippets. Each snippet demonstrates a different type of programming error.

The snippets are written in Python, JavaScript, and Ruby.

---

## Bug 1 (bug1.py)

**Intended Behaviour**: Calculate and print the average of a number list.

**Issue Type**: Syntax error.

**Notes**: Funtion definition is missing a colon (`:`) at the end of the first line. A colon is required for the syntax to work.

---

## Bug 2 (bug2.py)

**Intended Behaviour**: Find a user by their ID and return the user's name.

**Issue Type**: Runtime exception.

**Notes**: The requested user cannot be found and the function attempts to access `user["name"]` after the loop. A handle is needed for the case of no user being found.

---

## Bug 3 (bug3.js)

**Intended Behaviour**: Calculate the total price after applying a percentage discount.

**Issue Type**: Logical error.

**Notes**: The `discount` value is meant to represent a percentage. The code subtracts the discount directly from the subtotal instead of calculating the percentage. Convert the percentage into a decimal and subtract the calculated discount amount from the subtotal.