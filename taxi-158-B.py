import math

length = int(input())

groups = list(map(int, input().split()))

taxis = 0;

while 4 in groups:
    taxis += 1
    groups.remove(4)

while 3 in groups:
    taxis += 1
    groups.remove(3)
    if 1 in groups:
        groups.remove(1)

while 2 in groups:
    taxis += 1
    groups.remove(2)
    if 2 in groups:
        groups.remove(2)
        continue
    if 1 in groups:
        groups.remove(1)
    if 1 in groups:
        groups.remove(1)

taxis += math.ceil(len(groups) / 4)

print(taxis)
