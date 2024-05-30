# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def repeat(word, n):
    # Multiplies repeated word n number of times
    repeated_word = word * n
    # Returns repeated_word to n places
    return repeated_word[:n]

if __name__ == '__main__':
    # Test 1 - positive result
    word = "Hello"
    n = 12
    actual = repeat(word, n)
    expected = "HelloHelloHe"
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    if __name__ == '__main__':
        word = "He"
        n = 12
        actual = repeat(word, n)
        expected = "HelloHelloHe"
        msg = "Test 2 has "
        if actual == expected:
            msg += "passed"
        else:
            msg += "failed"
        print(msg)