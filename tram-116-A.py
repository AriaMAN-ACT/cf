n = int(input())

c = 0
m = 0

while n:
    n -= 1
    inputs = input().split()
    a = int(inputs[0])
    b = int(inputs[1])
    c -= a
    c += b

    if c > m:
        m = c

print(m)
