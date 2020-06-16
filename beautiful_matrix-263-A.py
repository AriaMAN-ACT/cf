matrix = [
        input().split(),
        input().split(),
        input().split(),
        input().split(),
        input().split()
    ]

def getIndex():
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == '1':
                return [i, j]

index = getIndex()

print(abs(2 - index[0]) + abs(2 - index[1]))
