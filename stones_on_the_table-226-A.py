stringLen = input()
string = input()

finalString = string[0]

for i in range(1, len(string)):
    if string[i] != finalString[-1]:
        finalString += string[i]

print(len(string) - len(finalString))
