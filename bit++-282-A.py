n = int(input())

value = 0

for i in range(n):
    line = input()
    if 'x' in line:
        if '++' in line:
            value += 1
        elif '--' in line:
            value -= 1

print(value)
