length = int(input())

steps = 0

steps += length // 5

steps += length % 5 // 4

steps += length % 5 % 4 // 3

steps += length % 5 % 4 % 3 // 2

steps += length % 5 % 4 % 3 % 2

print(steps)
