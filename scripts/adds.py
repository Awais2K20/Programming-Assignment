# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def adds(list1):
    # Initialises total to equal 0
    total = 0
    # Initialises a loop to add elements at odd indices together
    for i in range(0, len(list1), 2):
        total += list1[i]   # Adds the total to the number at the odd indice
    return total



if __name__ == '__main__':
    # Test 1 - positive test
    list1 = [5,3,5,6]
    actual = adds(list1)
    expected = 10
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - positive result
    list1 = [5, 3, 3]
    actual = adds(list1)
    expected = 8
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - negative result
    list1 = [5, 3, 3, 5]
    actual = adds(list1)
    expected = 10
    msg = "Test 3 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)
