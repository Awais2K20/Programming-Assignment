# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def is_palindrome(word):
    list = []   # Initialises and empty list to append letter in word to
    # Iterates through each letter in the word appending it to the list
    for letter in word:
        list.append(letter)

    reverse_list = list
    reverse_list.reverse()  # Reverses the elements in the list i.e. [apple, car, bus] to [bus, car, apple]
    reverse_word = "".join(reverse_list)    # Converts reversed list into a string using join()

    # Checks if word is a palindrome
    if word == reverse_word:
        true_false = "True"
    else:
        true_false = "False"
    return true_false


if __name__ == '__main__':
    # Test 1 - positive result
    word = "racecar"
    actual = is_palindrome(word)
    expected = "True"
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - positive result
    word = "a"
    actual = is_palindrome(word)
    expected = "True"
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - negative result
    word = "racecar"
    actual = is_palindrome(word)
    expected = "False"
    msg = "Test 3 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)