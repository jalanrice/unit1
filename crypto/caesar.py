from helpers import rotate_character
from sys import argv, exit

def user_input_is_valid(cl_args):
#    cl_args = argv
#    if argv[-1] == __file__ and len(argv) <= 1 and not argv[1].isdigit():
#        return True
    if len(cl_args) == 2 and cl_args[1].isdigit():
        return True
    else:
        return False
#    elif argv not in str.digits
#        return false


def encrypt(text, rot):
    """Receives a string and a number telling how far to rotate. Returns
    new, encrypted string"""

    char = ""
    ciphered = ""
    newChar = ""

    for char in text:
        newChar = rotate_character(char, rot)
        ciphered += newChar

    return ciphered


def main():
    if user_input_is_valid(argv):

        phrase = input("Type a message:")
        rotate = int(argv[1])
        print(encrypt(phrase, rotate))
    else:
        print("usage: python3 caesar.py n")
        exit()


if __name__ == '__main__':
    main()
