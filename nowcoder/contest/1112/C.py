# -*- coding : utf-8 -*-
# @Time: 2023/11/12 19:51
# @Author: yefei.wang
# @File: C.py

N = 10 ** 1 + 5
# latest prime factor
lpf = list(range(N + 1))
# 最小质因数 埃式筛法 初始化过程
for x in range(2, int(N ** .5) + 1):
    if lpf[x] == x:
        for y in range(x * x, N + 1, x):
            lpf[y] = x


# lpf[x]==x  表示x是质数
# lpf[x]!=x  表示lpf[x]是x最近的一个质因子

def get_factors(x):
    k = x
    factors = []
    while k > 1:
        p = lpf[k]
        k //= p
        factors.append(p)

    n = len(factors)
    res = set()
    for i in range(1, (1 << n)):
        x1 = 1
        for b in range(n):
            if i >> b & 1:
                x1 *= factors[b]
        res.add((x1, x // x1))
    return res


dp = [0 for _ in range(N)]
dp[1] = 0
dp[2] = 1

for i in range(2, N):
    dp[i] = dp[i - 1] + 1
    xys = get_factors(i)
    print(xys)
    for x, y in xys:
        dp[i] = min(dp[i], dp[x] + dp[y] + 1)

# print(dp)

import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
n = I()
a = LI()
rst = 0
for x in a:
    rst += dp[x]
print(rst)
