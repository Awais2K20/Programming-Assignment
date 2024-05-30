# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def multiplies(list1,list2):
    # Calculates the product of all elements in list 1
    list1_product = 1
    for num in list1:
        list1_product *= num
    # Multiplies each value in list 2 by the product of list 1
    list2_product = []
    for value in list2:
        list2_product.append(value * list1_product)
    # Calculates the sum of the elements in list2_product
    list2_total = sum(list2_product)
    # Multiplies list2_total by the approximate value of pi
    result = list2_total * 3.1

    return result

if __name__ == '__main__':
    # Test 1 - positive result
    list1 = [2, 3, 4]
    list2 = [5, 6, 7]
    actual = multiplies(list1, list2)
    expected = 1339.2
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    list1 = []
    list2 = [5, 6, 7]
    actual = multiplies(list1, list2)
    expected = 1339.2
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)