# -*- coding : utf-8 -*-
# @Time: 2024/1/11 20:28
# @Author: yefei.wang
# @File: 1633D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

N = 10 ** 3 + 5
f = [N] * N
f[1] = 0
for i in range(2, N):
    for j in range(1, i):
        k = i - j
        x = j // k
        if x > 0 and j // x == k:
            f[i] = min(f[i], f[j] + 1)
        if x + 1 > 0 and j // (x + 1) == k:
            f[i] = min(f[i], f[j] + 1)
        if x - 1 > 0 and j // (x - 1) == k:
            f[i] = min(f[i], f[j] + 1)
print(f[:10])
# 最大值就是12。所以k的最大12*1000.复杂度最大值12*1000*1000
print(max(f[1:1001]))

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    b = LI()
    c = LI()
    W = [0] * n
    for i in range(n):
        W[i] = f[b[i]]
    # 从数据范围优化
    if sum(W) < k:
        print(sum(c))
        continue

    dp = [0] * (k + 1)
    for i in range(n):
        for w in range(k, W[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - W[i]] + c[i])
    rst = max(dp)
    print(rst)
