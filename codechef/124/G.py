# -*- coding : utf-8 -*-
# @Time: 2024/3/6 23:14
# @Author: yefei.wang
# @File: G.py


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


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def divisors(M):
    d = []
    i = 1
    while M >= i ** 2:
        if M % i == 0:
            d.append(i)
            if i ** 2 != M:
                d.append(M // i)
        i = i + 1
    return d


tcn = I()
for _tcn_ in range(tcn):
    n, x = MI()
    nums = divisors(x)
    nums.sort()
    v2i = {v: i for i, v in enumerate(nums)}

    m = len(nums)
    ii = dict()
    for i1 in range(m):
        for i2 in range(m):
            ii[(i1, i2)] = v2i[lcm(nums[i1], nums[i2])]

    dp = [[0] * m for _ in range(n)]
    for j in range(m):
        dp[0][j] = 1
    for i in range(1, n):
        for cj in range(m):
            for xj in range(m):
                nj = ii[(cj, xj)]
                dp[i][nj] += dp[i - 1][cj]
                dp[i][nj] %= mod2
    rst = 0
    for i in range(n):
        rst += dp[i][-1]
        rst %= mod2
    print(rst)
