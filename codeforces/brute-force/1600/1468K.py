import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    x, y = 0, 0
    coords = []
    for c in s:
        if c == 'L':
            x -= 1
        if c == 'R':
            x += 1
        if c == 'D':
            y -= 1
        if c == 'U':
            y += 1
        coords.append((x, y))
    xr, yr = 0, 0
    for obstacle in coords:
        xo, yo = obstacle
        x, y = 0, 0
        for c in s:
            if c == 'L':
                x -= 1
            if c == 'R':
                x += 1
            if c == 'D':
                y -= 1
            if c == 'U':
                y += 1
            if x == xo and y == yo:
                if c == 'L':
                    x += 1
                if c == 'R':
                    x -= 1
                if c == 'D':
                    y += 1
                if c == 'U':
                    y -= 1

        if x == 0 and y == 0:
            xr, yr = xo, yo
            break
    print(xr, yr)
