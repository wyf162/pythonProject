import bisect
import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

s = input()
n = len(s)
# 标识 '(' - ')'
m = n // 2 + 2
dp = [[0 for j in range(m)] for i in range(n)]
if s[0] == ')' or n % 2 == 1:
    exit(print(0))
dp[0][1] = 1
for i in range(1, n):
    if s[i] == '(':
        for j in range(m - 1):
            dp[i][j + 1] += dp[i - 1][j]
            dp[i][j + 1] %= mod2
    elif s[i] == ')':
        for j in range(1, m):
            dp[i][j - 1] += dp[i - 1][j]
            dp[i][j - 1] %= mod2
    else:
        for j in range(m - 1):
            dp[i][j + 1] += dp[i - 1][j]
            dp[i][j + 1] %= mod2
        for j in range(1, m):
            dp[i][j - 1] += dp[i - 1][j]
            dp[i][j - 1] %= mod2
print(dp[n - 1][0] % mod2)
