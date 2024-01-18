import math
import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n = I()
xys = [LI() for _ in range(n)]


def dist(i, j):
    dx = xys[j][0] - xys[i][0]
    dy = xys[j][1] - xys[i][1]
    return math.sqrt(dx * dx + dy * dy)


penalty = [0] + [(1 << i) for i in range(17)]


f = [[float('inf') for j in range(17)] for i in range(n)]
f[0][0] = 0
for i, xy in enumerate(xys):
    x, y = xy
    if i == 0:
        continue

    for j in range(max(0, i - 16), i):
        d = i - j - 1
        for k, v in enumerate(f[j]):
            if k + d > 16:
                continue
            f[i][k + d] = min(f[i][k + d], f[j][k] + dist(j, i) + penalty[k+d] - penalty[k])


rst = min(f[-1])
print(rst)