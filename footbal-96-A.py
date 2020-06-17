string = input()

zp = string.split('1')
op = string.split('0')

lzp = list(map(len, zp))
lop = list(map(len, op))

lzp.sort(reverse=True)
lop.sort(reverse=True)

if lzp[0] >= 7 or lop[0] >= 7:
    print('YES')
else:
    print('NO')
