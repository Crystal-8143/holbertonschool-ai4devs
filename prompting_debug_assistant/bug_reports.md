# Structrued Bug Reports

This file documents the bugs found in the original code snippets, their root causes, the fixes applied, and lessons learned from debugging them.

## Bug Report - bug1.py

- **Summary**: The `calculate_average` function could not run because the function definition was missing a colon.  
- **Root Cause**: Python requires a colon (`:`) at the end of a function definition. The original code used `def calculate_average(numbers)` without the colon.
- **Resolution**: Add the missing colon after the function definition.
- **Lesson Learned**: Python syntax errors can prevent a program from running at all. When a function definition causes an error, check that the required colon and indentation are correct.

## Bug Report - bug2.py

- **Summary**: The `find_user` function did not correctly handle a user ID that was not found.
- **Root Cause**: After the loop finished without finding a matching user, the code attempted to return `user["name"]`. This did not represent a successful search result and could cause an error or incorrect behavior.without the colon.
- **Resolution**: Return `None` after the loop when no matching user is found.
- **Lesson Learned**: Functions that search for data should handle the case where the requested data does not exist. Returning `None` makes the missing result explicit and avoids accessing invalid data.

## Bug Report - bug3.js

- **Summary**: The discount was treated as a fixed dollar amount instead of a percentage.
- **Root Cause**: The original code calculated the total using `subtotal - discount`. With a 10% discount, this incorrectly removed `$10` instead of calculating 10% of the subtotal.without the colon.
- **Resolution**: Calculate the discount amount using `subtotal * (discount / 100)` before subtracting it from the subtotal.
- **Lesson Learned**: A variable's meaning is important when writing calculations. A percentage needs to be converted into a decimal or percentage amount before it can be used in a calculation.

## Bug Report - bug4.js

- **Summary**: The loop printed an extra item because it ran one iteration beyond the end of the array.
- **Root Cause**: The loop used `i <= items.length`. JavaScript arrays use indexes starting at `0`, so the final valid index is `items.length - 1`.
- **Resolution**: Change the loop condition from `i <= items.length` to `i < items.length`.
- **Lesson Learned**: Off-by-one errors are common when working with loops and arrays. Remember that `items.length` represents the number of items, not the final valid index.

## Bug Report - bug5.rb

- **Summary**: The program attempted to add price strings to an integer total.
- **Root Cause**: The prices were stored as strings such as `"10.50"`, but the code attempted to add them directly to `total`, which was an integer.
- **Resolution**: Convert each price string to a floating-point number using `to_f` before adding it to the total.
- **Lesson Learned**: Data types matter when performing calculations. Values that look like numbers may still be stored as strings and need to be converted before arithmetic operations.

## Bug Report - bug6.py

- **Summary**: A student who scored exactly 50 was incorrectly excluded from the list of passing students.
- **Root Cause**: The original code used `student["score"] > 50`, which only included scores greater than 50. The intended rule was that a score of 50 or higher should pass.
- **Resolution**: Change the comparison from `> 50` to `>= 50`.
- **Lesson Learned**: Boundary conditions are important when writing comparisons. Testing values exactly at the boundary, such as 50, can reveal logical errors that normal test cases might miss.

# Overall Lessons Learned

Working through these bugs showed that different types of errors require different debugging approaches.

- **Syntax errors** can stop a program from running
- **Runtime errors** can occur when the program reaches an invalid operation or unexpected situation
- **Logical errors** allow the program to run but produce the wrong result.
- **Off-by-one errors** are common when working with loops and array indexes.
- **Data type errors** can occur when values are stored in a different type than expected.
- **Boundary testing** is important for conditions such as passing scores and loop limits.

For this exercise, the AI suggestions were used as the starting point for all six fixes. Each suggested fix was applied and validated against the expected behavior. No additional manual code changes were required.