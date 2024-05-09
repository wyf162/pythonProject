# -*- coding : utf-8 -*-
# @Time: 2024/5/8 23:31
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 998244353

N = 5 * 10 ** 5
fact = [1]
for i in range(1, N + 1):
    fact.append(fact[-1] * i % mod)

fact_inv = [pow(fact[-1], mod - 2, mod)]
for i in range(N, 0, -1):
    fact_inv.append(fact_inv[-1] * i % mod)

fact_inv.reverse()


def comb(a, b):
    if 0 <= b <= a:
        return fact[a] * fact_inv[b] % mod * fact_inv[a - b] % mod
    else:
        return 0


tcn = I()
for _tcn_ in range(tcn):
    N, M = MI()
    A = LI()

    next_dup = [N] * (N + 1)
    last_seen = [N] * (M + 1)
    for i in reversed(range(N)):
        if A[i] == 0:
            next_dup[i] = next_dup[i + 1]
        else:
            next_dup[i] = min(next_dup[i + 1], last_seen[A[i]])
            last_seen[A[i]] = i

    st = set()
    pre_sum = [0]
    for i, a in enumerate(A):
        if a == 0:
            pre_sum.append(pre_sum[-1] + 1)
            continue
        st.add(a)
        pre_sum.append(pre_sum[-1])
    x = len(st) if len(st) > 0 else 1

    ans = 0
    for k in range(x, min(N, M) + 1):
        f1 = comb(M - len(st), k - len(st))

        for i in range(0, N, k):
            R = min(N, k + i)
            if next_dup[i] < R:
                f1 = 0
                break

            if i + k <= N:
                zero = pre_sum[i + k] - pre_sum[i]
                # zero = A[i:i + k].count(0)
                f1 *= fact[zero]
                f1 %= mod
            else:
                tot = N - i
                zero = pre_sum[N] - pre_sum[i]
                non_zero = tot - zero
                n1 = k - non_zero
                n2 = k - tot
                f1 *= fact[n1] * fact_inv[n2]
                f1 %= mod
        ans += f1
        ans %= mod
    print(ans)
