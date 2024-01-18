import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, W = MI()
nv = [LI() for _ in range(N)]
f = [0] * (W + 1)
for w, v in nv:
    for x in range(W, w - 1, -1):
        f[x] = max(f[x], f[x - w] + v)

print(max(f))
