#### initials.py ####

def get_initials(fullname):
    """ Given a person's name, return the person's initials (uppercase) """
    nameList = fullname.split()
    initials = ""
    for name in nameList:
        initials = initials + name[0]
    initials = initials.upper()

    return initials

def main():
    userName = input("What is your full name?")
    get_initials(userName)
    print("The initials of", userName, "are", get_initials(userName))

if __name__ == '__main__':
    main()
