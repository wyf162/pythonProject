import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

N = I()
A = LI()

dp = [[float('-inf') for j in range(N)] for i in range(N)]
for i in range(N):
    dp[i][i] = A[i]

for L in range(1, N):
    for s in range(0, N - L, 1):
        e = s + L
        dp[s][e] = max(A[s] - dp[s + 1][e], A[e] - dp[s][e - 1])


# @lru_cache(None)
# def dfs(i, j):
#     if i == j:
#         return A[i]
#     return max(A[i] - dfs(i + 1, j), A[j] - dfs(i, j - 1))


ret = dp[0][N-1]
print(ret)
