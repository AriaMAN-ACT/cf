inputs = input().split()

n = int(inputs[0])
k = int(inputs[1])

while k:
    k -= 1
    if n % 10 == 0:
        n = n // 10
    else:
        n = n - 1

print(n)
