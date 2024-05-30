# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------
import math
def is_overlap(circle_1, circle_2):
    distance = math.sqrt(((circle_1[0] - circle_2[0]) ** 2) + ((circle_1[1] - circle_2[1]) ** 2))   # Calculates distance between circles
    if distance <= circle_1[2] + circle_2[2]:   # Checks to see if distance <= total circle radii
        return "True"   # Circles overlap
    else:
        return "False"  # Circles don't overlap

if __name__ == '__main__':
    # Test 1 - positive test
    circle_1 = [-10, 8, 30]
    circle_2 = [14, 10, 10]
    actual = is_overlap(circle_1, circle_2)
    expected = "True"
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - positive test
    circle_1 = [0, 0, 10]
    circle_2 = [20, 0, 10]
    actual = is_overlap(circle_1, circle_2)
    expected = "True"
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - negative test
    circle_1 = [0, 1000, 10]
    circle_2 = [20, 0, 10]
    actual = is_overlap(circle_1, circle_2)
    expected = "True"
    msg = "Test 3 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)
    # Implement your tests here. 
    # Any test code not inside the main block WILL BE PENALISED 