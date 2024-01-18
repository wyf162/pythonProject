from itertools import product
import math

N, A, B, C = map(int, input().split())
dp = [0] * (8 * A * B * C)
dp[0] = 1

for i in range(63, 0, -1):
    new_dp = [0] * (8 * A * B * C)
    for p, q, r in product(range(A), range(B), range(C)):
        for s0, s1, s2 in product(range(2), repeat=3):
            for t0, t1, t2 in [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]:
                ni = (N >> (i - 1)) & 1
                if not ni and ((not s0 and t0) or (not s1 and t1) or (not s2 and t2)): continue
                ss0 = s0 or (ni and not t0)
                ss1 = s1 or (ni and not t1)
                ss2 = s2 or (ni and not t2)
                s = s0 + s1 * 2 + s2 * 4
                ss = ss0 + ss1 * 2 + ss2 * 4
                pp = (p * 2 + t0) % A
                qq = (q * 2 + t1) % B
                rr = (r * 2 + t2) % C
                new_dp[((ss * A + pp) * B + qq) * C + rr] += dp[((s * A + p) * B + q) * C + r]
                new_dp[((ss * A + pp) * B + qq) * C + rr] %= 998244353
    dp = new_dp

ans = sum(dp[s * A * B * C] for s in range(8))
ans -= N // math.lcm(A, B)
ans -= N // math.lcm(B, C)
ans -= N // math.lcm(C, A)
ans -= 1
print(ans % 998244353)
