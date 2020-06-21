nh = input().split()
n = int(nh[0])
h = int(nh[1])

heights = list(map(int, input().split()))

final = 0

for i in heights:
    if i <= h:
        final += 1
    else:
        final += 2

print(final)
