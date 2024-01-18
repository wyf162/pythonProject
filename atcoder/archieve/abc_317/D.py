import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n = I()
xyz = [LI() for i in range(n)]

taka = 0
aoki = 0

invert = []

for i in range(n):
    x, y, z = xyz[i]
    if x < y:
        aoki += z
        invert.append([(y - x + 1) // 2, z])
    else:
        taka += z

if taka > aoki:
    exit(print(0))

diff = (aoki - taka + 1) // 2

# knapsack dp
# cost, value
# select some thing, let sum(value)>=diff and min(cost)
N = 10 ** 5 + 5
MX = 10 ** 12
f = [MX] * N
f[0] = 0

for cost, value in invert:
    for x in range(N-1, value-1, -1):
        f[x] = min(f[x], f[x-value] + cost)

rst = MX
for v in range(diff, N):
    rst = min(rst, f[v])
print(rst)


