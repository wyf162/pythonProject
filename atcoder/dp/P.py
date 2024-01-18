import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

n = I()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

dp = [[0, 0] for _ in range(n)]

stk = [[0, -1]]
sstk = []
while stk:
    x, fa = stk.pop()
    dp[x][0] = dp[x][1] = 1
    for y in g[x]:
        if y == fa:
            continue
        stk.append([y, x])
        sstk.append([y, x])

while sstk:
    y, x = sstk.pop()
    dp[x][1] = dp[x][1] * dp[y][0] % mod
    dp[x][0] = dp[x][0] * (dp[y][0] + dp[y][1]) % mod

# def dfs(x, fa):
#     dp[x][0] = dp[x][1] = 1
#     for y in g[x]:
#         if y == fa:
#             continue
#         dfs(y, x)
#         dp[x][1] = dp[x][1] * dp[y][0] % mod
#         dp[x][0] = dp[x][0] * (dp[y][0] + dp[y][1]) % mod
#
#
# dfs(0, -1)
rst = sum(dp[0]) % mod
print(rst)
