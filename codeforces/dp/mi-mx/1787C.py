import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, s = MI()
    a = LI()
    x = [0] * n
    y = [0] * n
    for i in range(n):
        if i == 0 or i == n-1:
            x[i] = y[i] = a[i]
        elif a[i] <= s:
            x[i] = 0
            y[i] = a[i]
        else:
            x[i] = s
            y[i] = a[i] - s

    dp = [[0, 0] for _ in range(n)]
    for i in range(1, n, 1):
        dp[i][0] = min(dp[i - 1][0] + y[i - 1] * x[i], dp[i - 1][1] + x[i - 1] * x[i])
        dp[i][1] = min(dp[i - 1][0] + y[i - 1] * y[i], dp[i - 1][1] + x[i - 1] * y[i])

    print(dp[-1][0])
