# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------

def do_the_dog(dog_list, specific_dog):
    dog_list = " ".join(str(x) for x in dog_list)   # Converts the input list of dog names into a string
    for dog in specific_dog:
        if dog_list.find(dog) >= 0:   # Searches through dog_list string to find dog name position
            is_dog = "True"
        else:
            return "dinnae do the dog"  # Returns string if list of dog names aren't found

    if is_dog == "True":
        return lyrics   # If list of dog names are found returns song lyrics


if __name__ == '__main__':

    # Test 1 - positive result
    lyrics = '''
        Do the do the do the do the dog
        Everybody's doing the dog
        '''
    dog_list = ["Eeezy", "Rover", "Ben", "Kepler", "Charlie", "Smudge", "Mandy"]
    specific_dog = ["Eeezy", "Rover", "Ben", "Kepler", "Charlie", "Smudge", "Mandy"]
    actual = do_the_dog(dog_list, specific_dog)
    expected = lyrics
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    lyrics = '''
            Do the do the do the do the dog
            Everybody's doing the dog
            '''
    dog_list = ["Eeezy", "Rover", "Ben", "Kepler", "Charlie", "Smudge", "Mandy"]
    specific_dog = ["Eeezy", "Rover", "Ben", "Kepler", "Charlie", "Smudge", "Grover"]
    actual = do_the_dog(dog_list, specific_dog)
    expected = lyrics
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)