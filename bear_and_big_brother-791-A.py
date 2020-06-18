inputs = input().split()

limak = int(inputs[0])
bob = int(inputs[1])

years = 0

while bob >= limak:
    years += 1
    limak *= 3
    bob *= 2

print(years)
