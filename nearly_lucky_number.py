import re

n = input()

if re.compile("^(4|7)+$").match(n):
    print('YES')
else:
    print('No')
