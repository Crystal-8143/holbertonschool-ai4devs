# Fix Validation

This file records the tests performed on each AI-generated code fix.

Each corrected file was run to verify that the original bug was resolved and that the code produced the intended result

## Bug 1 - bug1_fixed.py

- **Input**: `[10,20,30,40]` 
- **Expected Output**: `Average: 25.0`  
- **Actual Output**: `Average: 25.0` ✅
- **Test Results**: Pass
- **AI Fix Applied**: Added the missing colon to the Python function definition.
- **Validation**: The corrected code ran successfully and produced the expected average.

## Bug 2 - bug2_fixed.py

- **Input**: User ID `5` with users having IDs `1`, `2`, and `3`
- **Expected Output**: `User: None`
- **Actual Output**: `User: None` ✅
- **Test Results**: Pass
- **AI Fix Applied**: Changed the return statement after the loop to `return None` when no matching user is found.
- **Validation**: The corrected code ran successfully and handled a missing user without raising an exception.

## Bug 3 - bug3_fixed.js

- **Input**: Price `$25`, quantity `4`, discount`10%`
- **Expected Output**: `Total: 90`
- **Actual Output**: `Total: 90` ✅
- **Test Results**: Pass
- **AI Fix Applied**: Calculated the discount as a percentage of the subtotal before subtracting it.
- **Validation**: The corrected code calculated the 10% discount correctly and returned a total of 90.

## Bug 4 - bug4_fixed.js

- **Input**: `["Apple", "Banana", "Orange", "Mango"]`  
- **Expected Output**: Each of the four items printed exactly once.
- **Actual Output**: 
    - Item: Apple
    - Item: Banana
    - Item: Orange
    - Item: Mango
- **Test Results**: Pass
- **AI Fix Applied**: Changed the loop condition from i <= items.length to i < items.length.
- **Validation**: The corrected loop printed each array item exactly once and did not attempt to access an index beyond the end of the array.

## Bug 5 - bug5_fixed.rb

- **Input**: `["10.50", "20.25", "5.75"]` 
- **Expected Output**: `$36.50`  
- **Actual Output**: `$36.50` ✅
- **Test Results**: Pass
- **AI Fix Applied**: Converted each price string to a floating-point number using to_f before adding it to the total.
- **Validation**: The corrected code successfully converted the strings and calculated the correct total of 36.5.

## Bug 6 - bug6_fixed.py

- **Input**: Students with scores `80`, `50`, `65`, and `45` 
- **Expected Output**: `['Alice', 'Bob', 'Charlie']`  
- **Actual Output**: `['Alice', 'Bob', 'Charlie']` ✅
- **Test Results**: Pass
- **AI Fix Applied**: Changed the comparison from > 50 to >= 50 so that a score of exactly 50 is considered passing.
- **Validation**: The corrected code included students scoring 50 or higher and excluded the student scoring 45.