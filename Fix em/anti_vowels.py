def anti_vowel(text):
    worked_on = ""
    for letter in text:
        for vowel in "ieaouIEAOU":
            if letter== vowel:
                letter=""
            else:
                letter = letter
        worked_on = worked_on + letter
    return worked_on
