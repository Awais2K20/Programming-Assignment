# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def descriptions(string1, string2):
    # Split the strings into words then finds word count
    string_length1 = len(string1.split())
    string_length2 = len(string2.split())

    if string_length1 <= 5 or string_length2 <= 5:  # Checks word count > 5
        return 0.0
    else:
        return string_length1 / string_length2



if __name__ == '__main__':
    # Test 1 - positive result
    string1 = "I am a computer system hehe hehe"
    string2 = "No you are not a computer system"
    actual = descriptions(string1,string2)
    expected = 1
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - positive result
    string1 = "I am a computer system hehe"
    string2 = "you are not a computer system hehe hehe hehe hehe hehe hehe"
    actual = descriptions(string1, string2)
    expected = 0.5
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - negative result
    string1 = "I am a computer system hehe hehe"
    string2 = "nuh uh"
    actual = descriptions(string1, string2)
    expected = 1
    msg = "Test 3 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)