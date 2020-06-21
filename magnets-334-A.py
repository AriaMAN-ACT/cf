length = int(input())

l = 1
ml = 1

inputs = length * [0]

inputs[0] = input()

for i in range(1, length):
    inputs[i] = input()
    if inputs[i] == inputs[i - 1]:
        l += 1
    else:
        l = 1
    ml = max(l, ml)

print(ml)
