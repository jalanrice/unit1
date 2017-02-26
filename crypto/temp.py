import string

def rot13(mess):
    # Your code here
    newChar = ""
    ciphered = ""

    for char in mess:


        if str.isupper(char):
            index = string.ascii_uppercase.find(char)
            newChar = string.ascii_uppercase[(index + 13) % 26]

        elif str.islower(char):
            index = string.ascii_lowercase.find(char)
            newChar = string.ascii_lowercase[(index + 13) % 26]

        elif str.isspace(char):
            newChar = char

        elif str.isdigit(char):
            index = string.digits.find(char)
            newChar = string.digits[(index + 13) % 10]

        elif char in string.punctuation:
            newChar = char

        else:
            return "invalid character"

        ciphered = ciphered + newChar

    return ciphered

print(rot13(input("Give me a secret: ")))