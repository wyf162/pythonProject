import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N, D = MI()
A = LI()

dp = [[0 for _ in range(D + 1)] for _ in range(1 << N)]

ave = sum(A) / D

for i in range(1 << N):
    y = 0
    for j in range(N):
        if i & (1 << j):
            y += A[j]

    dp[i][1] = pow(y - ave, 2)
    for j in range(2, D + 1):
        dp[i][j] = dp[i][j - 1] + dp[0][1]
        x = i
        while x > 0:
            dp[i][j] = min(dp[i][j], dp[i - x][j - 1] + dp[x][1])
            x = (x - 1) & i

rst = dp[-1][D] / D
print('%.15f' % rst)
