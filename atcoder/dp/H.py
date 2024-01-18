import sys
from collections import deque

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

h, w = MI()
grid = [input() for _ in range(h)]

cur = [0] * w
cur[0] = 1
for i in range(h):
    nex = [0] * w
    for j in range(w):
        if grid[i][j] == '.':
            if j >= 1:
                nex[j] = nex[j - 1] + cur[j]
            else:
                nex[j] = cur[j]
            nex[j] %= mod

    cur = nex

print(cur[-1])
