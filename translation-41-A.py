berInput = input()
birInput = input()

translation = True

for i in range(len(berInput)):
    if berInput[i] == birInput[len(birInput) - i - 1]:
        continue
    translation = False

if translation:
    print('YES')
else:
    print('NO')
