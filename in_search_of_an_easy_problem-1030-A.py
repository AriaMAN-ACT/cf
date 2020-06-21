import re

length = int(input())
opinions = input()

hardOpinions = re.compile('1').findall(opinions)

if len(hardOpinions) >= 1:
    print('HARD')
else:
    print('EASY')
