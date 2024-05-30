# A function name (DO NOT RENAME) is provided below.
# Implement the function according to the description document. 
# ------ 

def smooth(list):
    length = len(list)  # Calculates length of list
    smoothed_list = []
    # Calcuates left index and right index of element whilst also accounting for wrap
    for i in range(length):
        left_index = (i - 1) % length
        right_index = (i + 1) % length

        # Calculate the average of the element and its adjacent neighbors
        average_value = (list[left_index] + list[i] + list[right_index]) / 3
        smoothed_list.append(average_value)

    return smoothed_list

if __name__ == '__main__':
    # Test 1 - positive result
    list = [1, 2, 3, 4, 5]
    actual = smooth(list)
    expected = [2.6666666666666665, 2.0, 3.0, 4.0, 3.3333333333333335]
    msg = "Test 1 has "
    print("Original List:", list)
    print("Smoothed List:", actual)
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - positive result
    list = [1, 2, 3, 4]
    actual = smooth(list)
    expected = [2.3333333333333335, 2.0, 3.0, 2.6666666666666665]
    msg = "Test 2 has "
    print("Original List:", list)
    print("Smoothed List:", actual)
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - negative result
    list = [1, 2, 3, 4]
    actual = smooth(list)
    expected = [2.3333333333333335, 2.0, 3.0, 3.9]
    msg = "Test 3 has "
    print("Original List:", list)
    print("Smoothed List:", actual)
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)
