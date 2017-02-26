from helpers import alphabet_position, rotate_character
import string        
        
def encrypt(text, key):
    """Receives a message and a key word telling how far to rotate. Returns
    new, encrypted string"""
    
    char = ""
    ciphered = ""
    newChar = ""
    keyLength = len(key)
    textLength = len(text)
    i = 0
    keyChar = ""
    rot = 0
    
    for char in text:
        keyChar = key[i % keyLength]
        rot = alphabet_position(keyChar)
        newChar = rotate_character(char, rot)
        ciphered += newChar
        if char in string.ascii_uppercase or char in string.ascii_lowercase:
            i += 1
        
    return ciphered
    

def main():
    phrase = input("Type a message:")
    rotate = input("Encryption key:")

    print(encrypt(phrase, rotate))
    
if __name__ == '__main__':
    main()
