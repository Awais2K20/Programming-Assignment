# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def move(graphic, speed, acceleration):
    position_index = graphic.find('P')  # Finds the index of P in "graphic"

    # Returns the "graphic" if P isn't found
    if position_index == -1:
        return graphic

    new_position = position_index + speed + acceleration    # Calculates new position of P
    if new_position >= len(graphic):
        new_position = 0  # Moves position to 0 if P moves off the edge

    updated_graphics = list(graphic)    # Converts graphic string into a list
    updated_graphics[position_index] = '#'  # Sets old position of P TO #
    updated_graphics[new_position] = 'P'    # Updates P's position to new position

    return ''.join(updated_graphics)    # Returns updated_graphics value as a string


if __name__ == '__main__':
    # Test 1 - positive result
    graphic = "##P########################"
    speed = 3
    acceleration = 5
    result = move(graphic, speed, acceleration)
    print(result)
    actual = result
    expected = "##########P################"
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    graphic = "###P#######################"
    speed = -3
    acceleration = 5
    result = move(graphic, speed, acceleration)
    print(result)
    actual = result
    expected = "####P######################"
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)