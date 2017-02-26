import string

def alphabet_position(char):
    """accept an alpha character, return a position in the alphabet"""

    if str.isupper(char):
        index = string.ascii_uppercase.find(char)

    elif str.islower(char):
        index = string.ascii_lowercase.find(char)

    return index




def rotate_character(char, rot):
    """receives a character and a number instructing how far to rotate
    from that character. Returns new, encrypted character"""

    if str.isupper(char):
        index = alphabet_position(char)
        newChar = string.ascii_uppercase[(index + rot) % 26]

    elif str.islower(char):
        index = alphabet_position(char)
        newChar = string.ascii_lowercase[(index + rot) % 26]

    elif str.isspace(char):
        newChar = char

    elif str.isdigit(char):
        newChar = char

    elif char in string.punctuation:
        newChar = char

    return newChar
