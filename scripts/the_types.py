# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def the_types(input_list):
    element_type = []
    # Iterates though each element in input_list finding it's object class and appending to element_type
    for element in input_list:
        element_type.append(type(element))
    return element_type

if __name__ == '__main__':
    # Test 1 - positive result
    input_list = [5, "cat", 0.16, "a"]
    actual = the_types(input_list)
    expected = ["<class 'int'>, <class 'str'>, <class 'float'>, <class 'str'>"]
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)