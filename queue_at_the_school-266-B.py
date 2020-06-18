variabels = input().split()

n = int(variabels[0])
t = int(variabels[1])

string = list(input())

while t:
    t -= 1

    for i in range(n - 2, -1, -1):
        if string[i] == 'B' and string[i + 1] == 'G':
            string[i], string[i + 1] = string[i + 1], string[i]

print(''.join(string))
