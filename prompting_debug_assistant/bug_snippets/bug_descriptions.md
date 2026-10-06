# Bug Snippet Descriptions

This directory contains six intentionally buggy code snippets. Each snippet demonstrates a different type of programming error.

The snippets are written in Python, JavaScript, and Ruby.

---

## Bug 1 - bug1.py

**Intended Behaviour**: Calculate and print the average of a list of numbers.

**Issue Type**: Syntax error.

**Notes**: Funtion definition is missing a colon (`:`) at the end of the first line. Python requires a colon after a function definition.

---

## Bug 2 - bug2.py

**Intended Behaviour**: Find a user by their ID and return the user's name.

**Issue Type**: Runtime exception.

**Notes**: If the requested user cannot be found, the function attempts to access `user["name"]` after the loop. The function should handle the case where no matching user is found.

---

## Bug 3 - bug3.js

**Intended Behaviour**: Calculate the total price after applying a percentage discount.

**Issue Type**: Logical error.

**Notes**: The `discount` value represents a percentage. The code subtracts the discount directly from the subtotal instead of calculating the percentage first.

## Bug 4 - bug4.js

**Intended Behaviour**: Print every item in an array exactly once.

**Issue Type**: Off-by-one error.

**Notes**: JavaScript arrays use zero-based indexes. The loop uses `<= items.length`, causing it to run one additional time and attempt to access an index that does not exist.

## Bug 5 - bug5.rb

**Intended Behaviour**: Add a list of prices together and print the total rounded to two decimal places.

**Issue Type**: Data type misuse.

**Notes**: The prices are stored as strings instead of numbers. The code attempts to add the strings directly to an integer total, which causes a Ruby type error.

## Bug 6 - bug6.py

**Intended Behaviour**: Returns the names of all students who have a score of 50 or higher.

**Issue Type**: Logical error.

**Notes**: The code uses `> 50`, which excludes students who score exactly 50. The comparison should use `>= 50` so that a score of 50 is considered passing.