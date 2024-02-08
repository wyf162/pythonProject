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

n = I()
S = [''] + list(input())[::-1]
m = I()
ops = []
N = 2 ** n

for _ in range(m):
    t = input()
    p, c = t.split()
    p = N - int(p)
    ops.append([p, c])

#    x=1
# 2*x, 2*x+1

dp = [0] * N

for x in range(N - 1, 0, -1):
    lc, rc = x * 2, x * 2 + 1
    if rc >= N:
        dp[x] = 2 if S[x] == '?' else 1
    else:
        if S[x] == '?':
            dp[x] = dp[lc] + dp[rc]
        elif S[x] == '0':
            dp[x] = dp[rc]
        elif S[x] == '1':
            dp[x] = dp[lc]

for x, cur in ops:
    S[x] = cur
    lc, rc = x * 2, x * 2 + 1
    if rc >= N:
        dp[x] = 2 if S[x] == '?' else 1
    else:
        if cur == '?':
            dp[x] = dp[lc] + dp[rc]
        elif cur == '0':
            dp[x] = dp[rc]
        elif cur == '1':
            dp[x] = dp[lc]

    while x >= 1:
        y = x // 2
        lc, rc = y * 2, y * 2 + 1
        if S[y] == '?':
            dp[y] = dp[lc] + dp[rc]
        elif S[y] == '0':
            dp[y] = dp[rc]
        elif S[y] == '1':
            dp[y] = dp[lc]
        x = y
    print(dp[1])
