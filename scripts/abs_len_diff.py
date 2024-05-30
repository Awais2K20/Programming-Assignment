# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def abs_len_diff(list1, list2, power):

    # The length difference of the lists are calculated
    len_diff = (len(list1) - len(list2))
    len_diff = abs(len_diff)    # Retrieves the absolute value of the length difference
    total = len_diff ** power
    return total

    

if __name__ == '__main__':

    # Test 1 - Positive result
    list1 = [5,5,5,5,5,4]
    list2 = [2,3,4,5]
    power = 2
    actual = abs_len_diff(list1, list2, power)
    expected = 4
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - Positive result
    list1 = [5, 5, 5, 5]
    list2 = [2, 3, 4, 5]
    power = 3
    actual = abs_len_diff(list1, list2, power)
    expected = 0
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - Negative result
    list1 = [5, 5, 5, 5, 5, 4]
    list2 = [2, 3, 4, 5]
    power = 2
    actual = abs_len_diff(list1, list2, power)
    expected = 5
    msg = "Test 3 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)