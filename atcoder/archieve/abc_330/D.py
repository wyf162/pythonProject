import math
import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
mtx = [input() for _ in range(n)]

row = [0] * n
col = [0] * n
for i in range(n):
    for j in range(n):
        if mtx[i][j] == 'o':
            row[i] += 1
            col[j] += 1

ans = 0
for i in range(n):
    for j in range(n):
        if mtx[i][j] == 'o':
            ans += (row[i] - 1) * (col[j] - 1)
print(ans)
