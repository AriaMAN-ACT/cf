import re

length = int(input())
matches = input()

A = re.compile('A').findall(matches)

if len(A) > length / 2:
    print('Anton')
elif len(A) < length / 2:
    print('Danik')
else:
    print('Friendship')
