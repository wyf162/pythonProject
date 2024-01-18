import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    dp = [0] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1] + 1
        if i + a[i] < n:
            dp[i] = min(dp[i], dp[i + a[i] + 1])
    print(dp[0])
