import re

word = input()

def changeCase(char):
    if char.isupper():
        return char.lower()
    else:
        return char.upper()

if re.compile('^[a-z]{0,1}[A-Z]+$').fullmatch(word):
    print(''.join(list(map(changeCase, list(word)))))
else:
    print(word)
