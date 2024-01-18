import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

N, X, Y = MI()
pt = [LI() for _ in range(N - 1)]
Q = I()
qs = [I() for _ in range(Q)]

MX_P = 840

dp = list(range(MX_P))
for i, s in enumerate(dp):
    for j in range(N - 1):
        p, t = pt[j]
        if s % p == 0:
            s += t
        else:
            s += t + p - s % p
    dp[i] = s

for st in qs:
    st += X
    i = st % MX_P
    st = dp[i] + Y + (st // MX_P * MX_P)
    print(st)
