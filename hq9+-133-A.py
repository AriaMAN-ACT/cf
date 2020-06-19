import re

string = input()

if re.compile('\w*\s*(H|Q|9|\+)+\w*\s*').match(string):
    print('YES')
else:
    print('NO')
