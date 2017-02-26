text = input("Please enter a sentence:")
text = str.lower(text)
#textList = list(text)
alphaCount = {}

for letter in text:
    alphaCount[letter] = 0

for letter in text:
    alphaCount[letter] = alphaCount[letter] + 1

keylist = list(alphaCount.items())
keylist.sort()

for akey in keylist:
    if akey[0] != " ":
        print(akey[0], "   ", akey[1])

#print(keylist[])

#for akey in alphaCount.keys():
#    print(akey, "   ", alphaCount[akey])
