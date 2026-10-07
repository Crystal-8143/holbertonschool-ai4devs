# Fix Validation

This file records the tests performed on each AI-generated code fix.

Each corrected file was run to verify that the original bug was resolved and that the code produced the intended result

## Bug 1 - bug1_fixed.py

- **Input**: `[10,20,30,40]` 
- **Expected Output**: `Average: 25.0`  
- **Actual Output**: `Average: 25.0` ✅
- **Test Results**: Pass
- **Manual Tweaks**: The AI-suggested fix of adding the missing colon worked as expected.

## Bug 2 - bug2_fixed.py

- **Input**: User ID `5` with users having IDs `1`, `2`, and `3`
- **Expected Output**: `User: None`
- **Actual Output**: `User: None` ✅
- **Test Results**: Pass
- **Manual Tweaks**: Returning `None` when no matching user is found fixed the runtime error.

## Bug 3 - bug3_fixed.js

- **Input**: Price `$25`, quantity `4`, discount`10%`
- **Expected Output**: `Total: 90`
- **Actual Output**: `Total: 90` ✅
- **Test Results**: Pass
- **Manual Tweaks**: The percentage discount calculation worked as expected.

## Bug 4 - bug4_fixed.js

- **Input**: `["Apple", "Banana", "Orange", "Mango"]`  
- **Expected Output**: Each of the four items printed exactly once.
- **Actual Output**: 
    - Item: Apple
    - Item: Banana
    - Item: Orange
    - Item: Mango
- **Test Results**: Pass
- **Manual Tweaks**: Changing `<=` to `<` fixed the off-by-one error.

## Bug 5 - bug5_fixed.rb

- **Input**: `["10.50", "20.25", "5.75"]` 
- **Expected Output**: `$36.50`  
- **Actual Output**: `$36.50` ✅
- **Test Results**: Pass
- **Manual Tweaks**: Converting each price using `to_f` allowed the values to be added correctly. Ruby displayed the result as `$36.5`, which is numerically equivalent to `$36.50`.

## Bug 6 - bug6_fixed.py

- **Input**: Students with scores `80`, `50`, `65`, and `45` 
- **Expected Output**: `['Alice', 'Bob', 'Charlie']`  
- **Actual Output**: `['Alice', 'Bob', 'Charlie']` ✅
- **Test Results**: Pass
- **Manual Tweaks**: Changing `> 50` to `>= 50` correctly included students scoring exactly 50.