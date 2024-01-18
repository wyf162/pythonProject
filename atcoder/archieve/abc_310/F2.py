import sys
sys.stdin = open('../../input.txt', 'r')
N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
SIZE = 10

dp = [0] * (1 << SIZE)
dp[1] = 1
total = 1
MASK = (1 << SIZE) - 1
for i, a in enumerate(A):
    dpn = [0] * (1 << SIZE)
    for frm in range(1, 1 << SIZE):
        for v in range(1, a + 1):
            if v == 10:
                dpn[frm] += dp[frm] * (a - 10)
                dpn[frm] %= MOD
                break
            to = frm | (frm << v)
            if to >> 10 & 1:
                continue
            to &= MASK
            dpn[to] += dp[frm]
            dpn[to] %= MOD

    dp = dpn
    total *= a
    total %= MOD

ans = (total - sum(dp)) * pow(total, -1, MOD) % MOD

print(ans)
