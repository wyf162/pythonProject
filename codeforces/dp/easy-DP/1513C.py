# -*- coding : utf-8 -*-
# @Time: 2024/1/23 19:46
# @Author: yefei.wang
# @File: 1513C.py

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

M = 2 * 10 ** 5 + 5

f = [[0] * 10 for _ in range(M)]
for i in range(10):
    cnt = [0] * 10
    cnt[i] = 1
    for j in range(M):
        f[j][i] = sum(cnt) % mod
        ncnt = [0] * 10
        for k in range(9):
            ncnt[k + 1] = cnt[k]
        ncnt[0] += cnt[9]
        ncnt[1] += cnt[9]
        ncnt[1] %= mod
        cnt = ncnt

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    cnt = [0] * 10
    x = n
    while x:
        d = x % 10
        cnt[d] += 1
        x = x // 10
    rst = 0
    for i in range(10):
        rst += f[m][i] * cnt[i]
        rst %= mod
    print(rst)
