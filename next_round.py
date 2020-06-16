k = int(input().split()[1])

def parseInt(val):
    return int(val)

scores = list(map(parseInt, input().split()))

print(len([score for score in scores if score > k]))
