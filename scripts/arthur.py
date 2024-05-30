# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def arthur(quote, name):
    full_quote = f'{quote} \n\n\n\t\t- {name}'    # Initialises a formatted string that contains a quote seperated by lines and spaces with a name
    return full_quote

if __name__ == '__main__':
    # Test 1 - positive result
    name = "Arthur C Clarke"
    quote = "I don't believe in astrology; I'm a Sagittarius and we're skeptical."
    actual = arthur(quote, name)
    expected = "I don't believe in astrology; I'm a Sagittarius and we're skeptical. \n\n\n\t\t- Arthur C Clarke"
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    name = "Arthur C Clarke"
    quote = "I don't believe in astrology; I'm a Sagittarius and we're skeptical."
    actual = arthur(quote, name)
    expected = "If it hadn't been for cotton eyed joe"
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)