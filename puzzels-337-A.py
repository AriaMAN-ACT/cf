numbers = input().split()

n = int(numbers[0])
m = int(numbers[1])

prices = list(map(int, input().split()))

prices.sort()

print(prices[0])
