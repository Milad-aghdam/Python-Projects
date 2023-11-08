# Happy Number Checker
This script contains a function `is_happy` that determines whether a number is happy or not.

### Function Description

The `is_happy` function takes a positive integer as input and follows the following process to determine if the number is happy:
1. Starting with the given positive integer, it replaces the number by the sum of the squares of its digits.
2. It repeats this process until the number equals 1 or it loops endlessly in a cycle that does not include 1.
3. If the number equals 1, it is considered a happy number. Otherwise, it is not.

## Usage
To use the `is_happy` function, call it with a positive integer as the argument. It will return True if the number is happy and False otherwise.


### Example:
``` python
is_happy(19)
# Output: True
```

### Testing

The script includes two assertions to test the `is_happy` function:
```python

assert is_happy(7) is True
assert is_happy(44) is True
```
These assertions verify that the function correctly identifies 7 and 44 as happy numbers.

Note: The script can also be run as a standalone program. The assertions will be executed when the script is run directly.