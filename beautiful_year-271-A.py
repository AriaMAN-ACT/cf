year = str(int(input()) + 1)

while len(list(year)) != len(set(year)):
    year = str(int(year) + 1)

print(year)
