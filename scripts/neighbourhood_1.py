# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def neighbourhood_1():
    neighborhood_offsets = []
    # Returns a 1D moore neighbourhood offsets
    for offset in range(-1, 2):
        neighborhood_offsets.append([offset])
    return neighborhood_offsets


if __name__ == '__main__':
    actual = neighbourhood_1()
    print(actual)
    expected = [[-1], [0], [1]]
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative test
    actual = neighbourhood_1()
    print(actual)
    expected = [[-1], [0], [2]]
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)
