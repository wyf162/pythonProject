import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N = I()
A = LI()

g = [[] for i in range(N + 1)]
for i, x in enumerate(A):
    g[x].append(i)

b = []
for x in range(1, N + 1):
    b.append([x, g[x][1]])
b.sort(key=lambda x: x[1])
c = [x for x, _ in b]
print(*c)
