import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
cd = [LI() for _ in range(n)]

Level = 1900
mi, mx = -10 ** 9, 10 ** 9
s = 0
for i in range(n):
    ci, di = cd[i]

    if di == 1:
        mi = max(mi, Level)
    else:
        mx = min(mx, Level - 1)
    s += ci
    mi += ci
    mx += ci

if mi > mx:
    print('Impossible')
elif mx > 10 ** 8:
    print('Infinity')
else:
    print(mx)
