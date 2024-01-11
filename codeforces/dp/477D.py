import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

tcn, k = MI()
N = 100000 + 1
dp = [0] * N
pre_sum = [0] * N
dp[0] = 1

for i in range(1, N):
    if i < k:
        dp[i] = 1
    else:
        dp[i] += dp[i - k]
        dp[i] += dp[i - 1]
    dp[i] %= mod
    pre_sum[i] = pre_sum[i - 1] + dp[i]
    pre_sum[i] %= mod
# print(dp)

for _tcn_ in range(tcn):
    a, b = MI()
    rst = pre_sum[b] - pre_sum[a - 1] + mod
    rst %= mod
    print(rst)
