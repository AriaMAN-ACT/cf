length = int(input())

numbers = list(map(int, input().split()))

uniqueNumbers = list(set(numbers))

numbersCounts = len(uniqueNumbers) * [0]

for i in range(len(uniqueNumbers)):
    for j in numbers:
        if uniqueNumbers[i] == j:
            numbersCounts[i] += 1

numbersCounts.sort(reverse=True)

print(numbersCounts[0])
