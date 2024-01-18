import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N, M = MI()
dp = [[0, 1] for _ in range(N)]
for i in range(1, N):
    dp[i][0] = dp[i - 1][0] * (M - 2) + dp[i - 1][1] * (M - 1)
    dp[i][0] %= mod2
    dp[i][1] = dp[i - 1][0]
    dp[i][1] %= mod2

rst = M * dp[N - 1][0] % mod2
print(rst)
