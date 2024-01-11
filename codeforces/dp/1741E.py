import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()

    dp = [False] * (n + 1)
    dp[0] = True
    for i, a in enumerate(A):
        if i + a + 1 <= n and dp[i]:
            dp[i + a + 1] = True
        if i - a >= 0 and dp[i - a]:
            dp[i + 1] = True
    YN(dp[-1])
