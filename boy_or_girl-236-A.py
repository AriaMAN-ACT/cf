username = input()

letters = set(list(username))

if len(letters) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
