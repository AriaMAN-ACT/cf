n = int(input())

sum = 0

for i in range(n):
    row = input()
    for j in row.split():
        sum += int(j)

if sum == 0:
    print('YES')
else:
    print('NO')
