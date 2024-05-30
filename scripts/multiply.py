# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def multiply(*args):
    result = 1
    # Calculates product of all arguments
    for num in args:
        result *= num
    # checks if result is an integer (i.e. a whole number)
    if isinstance(result, int):
        return "signed"
    else:
        return "unsigned"

if __name__ == '__main__':
    # Test 1 - positive test
    result = multiply(2, 3, -4)
    actual = multiply(2,3,-4)
    expected = "signed"
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - positive test
    result = multiply(0.2, 0.3, 0.4)
    actual = multiply(0.2,0.3,0.4)
    expected = "unsigned"
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)