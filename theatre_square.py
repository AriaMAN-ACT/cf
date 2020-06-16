w = int(input())
h = int(input())
a = int(input())

w += a - w % a
h += a - h % a

print(int((w / a) * (h / a)))
