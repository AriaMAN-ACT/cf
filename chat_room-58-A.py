import re

string = input()

if re.compile('\w*h+\w*e+\w*l+\w*l+\w*o+\w*').match(string):
    print('YES')
else:
    print('NO')
