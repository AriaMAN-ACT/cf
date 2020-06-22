import math

inputs = input().split()

n = int(inputs[0])
k = int(inputs[1])

if k <= math.ceil(n / 2):
    print(k * 2 - 1)
else:
    print((k - math.ceil(n / 2)) * 2)
