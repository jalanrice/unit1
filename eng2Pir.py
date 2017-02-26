def translate(text):

    eng2Pir = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie', 'boy': 'matey', 'madam': 'proud beauty', 'professor': 'foul blaggart', 'restaurant': 'galley', 'your': 'yer', 'excuse': 'arr', 'students': 'swabbies', 'are': 'be', 'lawyer': 'foul blaggart', 'the': 'th\'', 'restroom': 'head', 'my': 'me', 'hello': 'avast', 'is': 'be', 'man': 'matey'}
    text = str.lower(text)
    textList = text.split()
    pirateList = []

    for word in textList:
        if word in eng2Pir:
            pirateList.append(eng2Pir[word])
        else:
            pirateList.append(word)
    glue = " "
    pirateText = glue.join(pirateList)


    return pirateText
