import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

n, m = MI()
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = MI()
    g[u].append(v)
    g[v].append(u)
