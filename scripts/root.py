# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------
import math

def root(number):
    # Calculates square root of sqaure_root using math.sqrt
    square_root = math.sqrt(number)
    return square_root

if __name__ == '__main__':
    # Test 1 - positive test
    number = 4
    actual = root(number)
    expected = 2
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative test
    number = 4
    actual = root(number)
    expected = 3
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)