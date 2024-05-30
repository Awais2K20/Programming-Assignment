# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def lyric_count(lyric, lyric_word):
    # Counts the number of times a word occurs in lyric
    word_occurs = lyric.count(lyric_word)
    return word_occurs


if __name__ == '__main__':
    # Test 1 - positive result
    lyric = "never gonna give you up, never gonna let you down"
    lyric_word = "never"
    actual = lyric_count(lyric, lyric_word)
    expected = 2
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    lyric = "never gonna give you up, never gonna let you down"
    lyric_word = "never, gonna"
    actual = lyric_count(lyric, lyric_word)
    expected = 2
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)