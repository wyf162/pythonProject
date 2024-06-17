# -*- coding : utf-8 -*-
# @Time: 2024/6/16 22:07
# @Author: yefei.wang
# @File: 1978C.py

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
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    k = m
    tot = 0
    for i in range(0, n, 2):
        tot += (n - i - 1) * 2
    if k % 2 == 1 or k > tot:
        print("NO")
        continue
    print('YES')

    rets = [_ for _ in range(n)]
    i = 0
    j = n - 1
    while k > 0:
        if k >= (j - i) * 2:
            k -= (j - i) * 2
            rets[i] = j
            rets[j] = i
            i += 1
            j -= 1
        else:
            rets[j] = j
            j -= 1
    print(' '.join(str(x + 1) for x in rets))
    # dis = 0
    # for i in range(n):
    #     dis += abs(rets[i] - i)
    # print(dis, dis == m)
