print('Enter an english sentence to convert into Pig Latin')
messages = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []

for word in messages.split():
    prefixnonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixnonletters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixnonletters)
        continue

    suffixnonletters = ''
    while not word[-1].isalpha():
        suffixnonletters += word[-1]
        word = word[:-1]

    wasupper = word.isupper()
    wastitle = word.istitle()

    word = word.lower()

    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    if wasupper:
        word = word.upper()
    if wastitle:
        word = word.title()

    pigLatin.append(prefixnonletters + word + suffixnonletters)

print (' '.join(pigLatin))