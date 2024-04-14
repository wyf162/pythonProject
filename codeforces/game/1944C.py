# -*- coding : utf-8 -*-
# @Time: 2024/4/14 23:28
# @Author: yefei.wang
# @File: 1944c.py
# https://codeforces.com/contest/1944/problem/C
# mex

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    cnt = [0] * n
    for num in nums:
        cnt[num] += 1

    one = True
    for i in range(n):
        if cnt[i] >= 2:
            continue
        else:
            if cnt[i] == 1:
                if one:
                    one = False
                else:
                    print(i)
                    break
            else:
                print(i)
                break
    else:
        print(n)
