# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def great_scientists(quotes,birth_date):
    # initialises scientist_list to store a list with quotes, year of births, and the absolute difference between these of two scientists
    scientist_list = [quotes[0], quotes[1], birth_date[0], birth_date[1], abs(birth_date[0] - birth_date[1])]
    return scientist_list


if __name__ == '__main__':
    # Test 1 - positive result
    quotes = ["Science and everyday life cannot and should not be separated.", "You should never claim perfect, or total, or 100% because you never ever get there."]
    birth_date = [1920, 1943]
    actual = great_scientists(quotes, birth_date)
    expected = ['Science and everyday life cannot and should not be separated.', 'You should never claim perfect, or total, or 100% because you never ever get there.', 1920, 1943, 23]
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - positive result
    quotes = ["Science and everyday life cannot and should not be separated.", "You should never claim perfect, or total, or 100% because you never ever get there."]
    birth_date = [1943, 1920 ]
    actual = great_scientists(quotes, birth_date)
    expected = ['Science and everyday life cannot and should not be separated.', 'You should never claim perfect, or total, or 100% because you never ever get there.', 1943, 1920, 23]
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 3 - negative result
    quotes = ["Science and everyday life cannot and should not be separated.", "You should never claim perfect, or total, or 100% because you never ever get there."]
    birth_date = [1943, 1920 ]
    actual = great_scientists(quotes, birth_date)
    expected = ['Science and everyday life cannot and should not be separated.', 'You should never claim perfect, or total, or 100% because you never ever get there.', 1920, 1943, 2]
    msg = "Test 3 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)
