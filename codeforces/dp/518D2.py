import sys

sys.stdin = open('../input.txt', 'r')

n, p, t = input().split()
n = int(n)
p = float(p)
t = int(t)

dp = [[0 for _ in range(n + 1)] for _ in range(t + 1)]

dp[0][0] = 1
for i in range(t):
    dp[i + 1][n] += dp[i][n]
    for j in range(n):
        dp[i + 1][j + 1] += dp[i][j] * p
        dp[i + 1][j] += dp[i][j] * (1 - p)

ans = 0
for i in range(n + 1):
    ans += i * dp[t][i]

print(ans)
