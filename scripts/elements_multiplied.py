# A function name (DO NOT RENAME) is provided below.
# Implement the function according to the description document. 
# ------ 

def elements_multiplied(list1, list2, n):
    result = []     # Initialises an empty list to store result
    # Check if the sizes of the lists are compatible
    try:
        if len(list1) != (len(list2) / n):
            return []
    except:
        return []

     # Multiply list element at index i of list 1 by element at index i * n of list 2
    for i in range(len(list1)):
        result.append(list1[i] * list2[i * n])  # Appends product of list1[i] * list2[i * n]
    counter = len(result) - 1
    total_result = result[counter]  # Sets total_result to equal last element of results list

    # While counter != 0 counter is used to iterate through results taking away element at index counter from total_result
    while counter != 0:
        counter -= 1
        total_result -= result[counter]
    return result, total_result

if __name__ == '__main__':
    # Test 1 - positive result
    list1 = [1, 2, 4]
    list2 = [10, 20, 30, 40, 50, 60]
    n = 2
    actual = elements_multiplied(list1, list2, n)
    expected = ([10, 60, 200], 130)
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    list1 = [1, 2, 4]
    list2 = [10, 20, 30, 40, 50, 60]
    n = 0
    actual = elements_multiplied(list1, list2, n)
    expected = ([10, 60, 200], 130)
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - negative result
    list1 = [1, 2, 4]
    list2 = [10, 20, 30, 40, 50, 60]
    n = -1
    actual = elements_multiplied(list1, list2, n)
    expected = ([10, 60, 200], 130)
    msg = "Test 3 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 4 - negative result
    list1 = [1, 2, 4]
    list2 = [10, 20, 30, 40, 50, 60]
    n = "pizza"
    actual = elements_multiplied(list1, list2, n)
    expected = ([10, 60, 200], 130)
    msg = "Test 4 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)