import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    a = LI()
    dp = dict()

    fa = ca = 0
    for i in range(n):
        if a[i] in dp:
            ca += dp[a[i]]
        else:
            dp[a[i]] = 0
        dp[a[i]] += i+1
        fa += ca
    print(fa)

