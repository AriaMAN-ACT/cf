input1 = input().lower()
input2 = input().lower()

final = 0

for i in range(len(input1)):
    if input1[i] > input2[i]:
        final += 1
    elif input1[i] < input2[i]:
        final -= 1

print(final)
