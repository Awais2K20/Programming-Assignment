# A function name (DO NOT RENAME) is provided below.
# Implement the function according to the description document. 
# ------ 

def square_and_sum(list1):
    square_list = []
    # Iterates through each element in list; squaring it, multiplying it by the approximate value of gamma then appending it to square_list
    for element in list1:
        square = element ** 2
        square *= gamma_approx
        square_list.append(square)
    return square_list

if __name__ == '__main__':
    # Test 1 - positive result
    expected = [40.0, 40.0, 40.0]
    gamma_approx = 1.6
    list1 = [5,5,5]
    actual = square_and_sum(list1)
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    expected = [40.0, 40.0]
    gamma_approx = 1.6
    list = [5,5,5]
    actual = square_and_sum(list1)
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)