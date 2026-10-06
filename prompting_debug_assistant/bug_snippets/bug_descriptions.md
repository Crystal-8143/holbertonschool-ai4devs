# Bug Snippet Descriptions

This file describes the intended behavior and known issue type for each buggy code snippet in the `bug_snippets` directory.


## Bug 1 - bug1.py

### Intended Behaviour

Calculate the average of a list of numbers and print the result.

### Issue type

Syntax error.

### Notes

The function definition is missing a colon (`:`) after `def calculate_average(numbers)`. Python requires a colon at the end of a function definition.


## Bug 2 - bug2.py

### Intended Behaviour

Search a list of users for a specific user ID and return that user's name. If the user does not exist, the function should handle that situation without causing an exception.

### Issue type

Runtime exception.

### Notes

When the requested user cannot be found, the function reaches `return user["name"]` after the loop. This can cause an error because there is no matching user to return. The function should handle the case where no matching user exists.


## Bug 3 - bug3.js

### Intended Behaviour

Calculate the total price of several items after applying a percentage discount.

For example, if the subtotal is $100 and the discount is 10%, the final total should be $90.

### Issue type

Logical error.

### Notes

The `discount` value represents a percentage, but the code subtracts the discount value directly from the subtotal. The code should calculate the percentage amount before subtracting it.

## Bug 4 - bug4.js

### Intended Behaviour

Print every item in an array exactly once.

### Issue type

Off-by-one error.

### Notes

JavaScript arrays use zero-based indexes. The loop uses `i <= items.length`, which causes the loop to run one time too many. When `i` reaches `items.length`, there is no item at that index. The loop should use `i < items.length`.

## Bug 5 - bug5.rb

### Intended Behaviour

Add a list of prices together and print the total rounded to two decimal places.

### Issue type

Data type misuse.

### Notes

The prices are stored as strings, such as `"10.50"`, rather than numeric values. The code attempts to add these strings to an integer total, which causes a Ruby type error. The price strings should be converted to numbers before performing the addition.

## Bug 6 - bug6.py

### Intended Behaviour

Return the names of all students who have a score of 50 or higher.

### Issue type

Logical error.

### Notes

The code uses `> 50`, which excludes students who have exactly 50 points. A score of 50 should count as a passing score, so the comparison should use `>= 50`.