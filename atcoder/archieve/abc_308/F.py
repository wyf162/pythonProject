import sys
from heapq import heappop, heappush

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N, M = MI()
P = LI()
L = LI()
D = LI()

LD = [[x, y] for x, y in zip(L, D)]
LD.sort()
P.sort()

h = []
rst = 0
j = 0
for i in range(N):
    while j < M and LD[j][0] <= P[i]:
        heappush(h, -LD[j][1])
        j += 1
    rst += P[i]
    if h:
        rst += heappop(h)

print(rst)
