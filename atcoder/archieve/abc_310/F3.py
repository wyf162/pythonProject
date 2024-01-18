import sys
sys.stdin = open('../../input.txt', 'r')

MOD = 998244353
N = int(input())
A = list(map(int, input().split()))

D = 12
D2 = 1 << D
dp = [0] * D2
dp[1 << 0] = 1
for a in A:
    pre = [0] * D2
    dp, pre = pre, dp

    for s in range(D2):
        if pre[s] == 0:
            continue

        for i in range(1, a + 1):
            ns = s
            for r in range(D):
                if (s >> r) & 1:
                    if r + i <= 10:
                        ns |= 1 << (r + i)
                    else:
                        ns |= 1 << 11

            if i <= 10:
                dp[ns] += pre[s]
                dp[ns] %= MOD
            else:
                dp[ns] += pre[s] * (a - 10)
                break

ans = 0
for s in range(D2):
    if (s >> 10) & 1:
        ans += dp[s]
        ans %= MOD

All = 1
for a in A:
    All *= a
    All %= MOD

# ans *= pow(All, -1, MOD)
ans *= pow(All, MOD-2, MOD)
ans %= MOD
print(ans)
