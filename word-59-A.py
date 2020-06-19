import re

word = input()

uppers = re.compile('[A-Z]').findall(word)

if len(uppers) > len(word) / 2:
    print(word.upper())
else:
    print(word.lower())
