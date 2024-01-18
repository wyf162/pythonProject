import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

N = I()
A = LI()
B = [0]
for i in range(N):
    B.append(B[-1] + A[i])

dp = [[float('inf') for j in range(N)] for i in range(N)]
for i in range(N):
    dp[i][i] = 0

for L in range(1, N):
    for s in range(0, N - L, 1):
        e = s + L
        for k in range(s, e):
            dp[s][e] = min(dp[s][e], dp[s][k] + dp[k + 1][e] + B[e + 1] - B[s])

rst = dp[0][N - 1]
print(rst)

# from functools import cache

# @cache
# def dfs(i, j):
#     if i == j:
#         return 0
#     if i == j - 1:
#         ret = A[i] + A[i + 1]
#         return ret
#
#     ret = float('inf')
#     for k in range(i, j):
#         ret = min(ret, dfs(i, k) + dfs(k + 1, j))
#     ret += B[j + 1] - B[i]
#     # print(i, j, ret)
#     return ret
#
#
# rst = dfs(0, N - 1)
# print(rst)
