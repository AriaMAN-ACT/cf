string = input().lower();

nvs = [s for s in string if s not in ['a', 'o', 'y', 'e', 'u', 'i']]

def addDotBefore(char):
    return '.' + char

final = ''.join(list(map(addDotBefore, nvs)))

print(final)
