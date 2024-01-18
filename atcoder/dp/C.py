import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
mtx = [LI() for _ in range(n)]

cur = mtx[0]
nex = [0, 0, 0]
for i in range(1, n):
    nex[0] = max(cur[1], cur[2]) + mtx[i][0]
    nex[1] = max(cur[0], cur[2]) + mtx[i][1]
    nex[2] = max(cur[1], cur[0]) + mtx[i][2]

    cur[0], cur[1], cur[2] = nex
    nex[1], nex[0], nex[2] = 0, 0, 0

print(max(cur))
