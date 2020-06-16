wordsCount = int(input())

words = []

for i in range(wordsCount):
    words += [input()]

for word in words:
    if len(word) > 10:
        print("%s%d%s" % (word[0], len(word) - 2, word[-1]))
    else:
        print(word)
