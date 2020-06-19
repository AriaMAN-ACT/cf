rooms = int(input())

gaa = 0

while rooms:
    rooms -= 1
    roomAndAcc = list(map(int, input().split()))
    if roomAndAcc[1] - roomAndAcc[0] >= 2:
        gaa += 1

print(gaa)
