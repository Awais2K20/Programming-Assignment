# A function name (DO NOT RENAME) is provided below.
# Implement the function according to the description document.
# ------

def binary_multiply(binary_list1, binary_list2):
    total = [0, 0]
    counter = [0,0,0]
    for binary1, binary2 in zip(binary_list1.reverse(), binary_list2.reverse()):
        while counter[0] != len(binary_list1):
            if binary[counter[1]] == 1:
                decimal_binary = 2 ** (counter[0])
            else:
                decimal_binary = 0
            total[counter[2]] += decimal_binary
            counter[0] += 1
        counter[1] += 1
    print("hello")
    return total


if __name__ == '__main__':
    binary_list1 = [0, 1, 1, 0]
    binary_list2 = [0, 1, 1, 1]
    result = binary_multiply(binary_list1, binary_list2)
    print(result)
    # Implement your tests here.
    # Any test code not inside the main block WILL BE PENALISED
