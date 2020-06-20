n = int(input())

friendsGivenGifts = list(map(int, input().split()))

friendsGifts = n * [0]

for i in range(n):
    friendsGifts[friendsGivenGifts[i] - 1] = i + 1

print(' '.join(list(map(str, friendsGifts))))
