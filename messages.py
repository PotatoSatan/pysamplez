import pprint

messages = 'I am under the water, please help me there is too much raining.'
char = {}

for text in messages:
    char.setdefault(text, 0)
    char[text] = char[text] + 1

print(char)

