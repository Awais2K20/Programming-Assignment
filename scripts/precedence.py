# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def precedence(a,b,c,d,e,f,g):
    #  Calculates result using BODMAS
    result = (((a + b) * c * d / e - f + g)/f) -g
    return result

if __name__ == '__main__':
    # Test 1 - positive test
    a,b,c,d,e,f,g = 1,2,3,4,5,6,8
    actual = precedence(a,b,c,d,e,f,g)
    expected = -6.466666666666667
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative test
    a,b,c,d,e,f,g = 1,2,3,4,5,6,9
    actual = precedence(a,b,c,d,e,f,g)
    expected = -5.633333333333334
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)