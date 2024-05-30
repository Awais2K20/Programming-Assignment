# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def decimal_mapping(shift_pressed, keys_pressed):
    # Initialise a data dictionary with numbers and their corresponding shift press
    keys_dict = {0: ")", 1: "!", 2: "@", 3: "#", 4: "$", 5: "%", 6: "^", 7: "&", 8: "*", 9: "("}

    #Initialise an empty list to store characters
    key_output = []

    #Initialise a loop for the individual key presses in the keys_pressed list
    for key in keys_pressed:
        if shift_pressed == "True":
            key_output.append(keys_dict[key])   #Append the key_output list with the value of the key
        else:
            key_output.append(key)  #Append the key_output with the key
    return key_output

if __name__ == '__main__':

    # Test 1 - Positive test
    shift_pressed = "True"
    keys_pressed = [5, 2, 1]
    expected = ['%', '@', '!']
    actual = decimal_mapping(shift_pressed, keys_pressed)
    msg = "Test 1 has "
    if expected == actual:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - Positive test
    shift_pressed = "False"
    keys_pressed = [5, 2, 1]
    expected = [5, 2, 1]
    actual = decimal_mapping(shift_pressed, keys_pressed)
    msg = "Test 2 has "
    if expected == actual:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - Negative test
    shift_pressed = "True"
    keys_pressed = [5, 2, 1]
    expected = ['%', '@', '']
    actual = decimal_mapping(shift_pressed, keys_pressed)
    msg = "Test 3 has "
    if expected == actual:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)