length = int(input())
sells = list(map(int, input().split()))

l = 1
ml = 1

for i in range(1, length):
    if sells[i] > sells[i - 1]:
        l += 1
        ml = max(ml, l)
    else:
        l = 1

print(ml)
