a = int(input())
b = int(input())
c = int(input())

exp1 = a + b + c
exp2 = a * b * c
exp3 = a + b * c
exp4 = a * b + c
exp5 = a * (b + c)
exp6 = (a + b) * c

print(max(exp1, exp2, exp3, exp4, exp5, exp6))
