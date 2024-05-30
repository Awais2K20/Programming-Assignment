# A function name (DO NOT RENAME) is provided below. 
# Implement the function according to the description document. 
# ------ 

def lyric_frequencies(lyrics):
    day_counter = ["", "", "", "", "", "", ""]  # Initialises an empty list that will be used to store how many times a day is mentioned
    counter = 0
    # For loop iterates through lyrics to count how many times a day is mentioned using count()
    for i in days_of_week:
        day_counter[counter] = lyrics.count(i)
        counter += 1
    days_said = zip(days_of_week, day_counter)  # days_of_week and day_counter are "zipped" using tuples
    days_said = dict(days_said)  # Converts days_said into a data dictionary
    return days_said


if __name__ == '__main__':

    # Test 1 - positive result
    lyrics = '''
        I don’t care if Monday blue
        Tuesday grey and Wednesday too
        Thursday I don’t care about you
        It’s Friday I’m in love

        Monday you can fall apart
        Tuesday Wednesday break my heart
        Thursday doesn’t even start
        It’s Friday I’m in love

        Saturday wait
        And Sunday always comes too late
        But Friday never hesitate…

        I don’t care if Monday black
        Tuesday Wednesday heart attack
        Thursday never looking back
        It’s Friday I’m in love

        Monday you can hold your head
        Tuesday Wednesday stay in bed
        Or Thursday watch the walls instead
        It’s Friday I’m in love

        Saturday wait
        And Sunday always comes too late
        But Friday never hesitate…

        Dressed up to the eyes
        It’s a wonderful surprise
        To see your shoes and your spirits rise
        Throwing out your frown
        And just smiling at the sound
        And as sleek as a shriek
        Spinning round and round
        Always take a big bite
        It’s such a gorgeous sight
        To see you eat in the middle of the night
        You can never get enough
        Enough of this stuff
        It’s Friday
        I’m in love
        '''
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    actual = lyric_frequencies(lyrics)
    expected = {'Monday': 4, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 4, 'Friday': 7, 'Saturday': 2, 'Sunday': 2}
    msg = "Test 1 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)

    # Test 2 - negative result
    lyrics = '''
        I don’t care if Monday blue
        Tuesday grey and Wednesday too
        Thursday I don’t care about you
        It’s Friday I’m in love

        Monday you can fall apart
        Tuesday Wednesday break my heart
        Thursday doesn’t even start
        It’s Friday I’m in love

        Saturday wait
        And Sunday always comes too late
        But Friday never hesitate…

        I don’t care if Monday black
        Tuesday Wednesday heart attack
        Thursday never looking back
        It’s Friday I’m in love

        Monday you can hold your head
        Tuesday Wednesday stay in bed
        Or Thursday watch the walls instead
        It’s Friday I’m in love

        Saturday wait
        And Sunday always comes too late
        But Friday never hesitate…

        Dressed up to the eyes
        It’s a wonderful surprise
        To see your shoes and your spirits rise
        Throwing out your frown
        And just smiling at the sound
        And as sleek as a shriek
        Spinning round and round
        Always take a big bite
        It’s such a gorgeous sight
        To see you eat in the middle of the night
        You can never get enough
        Enough of this stuff
        It’s Friday
        I’m in love
        '''
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    actual = lyric_frequencies(lyrics)
    expected = {'Monday': 4, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 4, 'Friday': 7, 'Saturday': 2, 'Sunday': 2}
    msg = "Test 2 has "
    if actual == expected:
        msg += "passed"
    else:
        msg += "failed"
    print(msg)