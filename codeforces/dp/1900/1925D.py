# -*- coding : utf-8 -*-
# @Time: 2024/7/6 13:58
# @Author: yefei.wang
# @File: 1925D.py
# probabilities

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007


tcn = I()
for _tcn_ in range(tcn):
    n, m, k = MI()
    p = 0
    for _ in range(m):
        a, b, f = MI()
        p = (p + f) % mod

    q = n * (n - 1) // 2
    q_inv = pow(q, mod - 2, mod)
    ans = p * k % mod * q_inv % mod
    avg_inc = 0
    comb = 1
    unpick = (q - 1) * q_inv % mod
    q1_inv = pow(q - 1, mod - 2, mod)
    unpick_k = pow(unpick, k, mod)
    inv_k = 1
    for i in range(1, k + 1):
        s = i * (i - 1) // 2  # 0, 1, 2
        comb = comb * (k - i + 1) * pow(i, mod - 2, mod) % mod
        inv_k = inv_k * q_inv % mod
        if i == k:
            unpick_k = 1
        else:
            unpick_k = unpick_k * q1_inv * q % mod
        # prob = comb * pow(q_inv, i, mod) * pow(unpick, k - i, mod)
        prob = comb * inv_k * unpick_k % mod
        avg_inc = (avg_inc + s * prob) % mod

    ans = (ans + (m * avg_inc) % mod) % mod
    print(ans)
