# -*- coding: utf-8 -*-
# @Time: 2024/5/28 11:18
# @Author: yfwang
# @File: 1168B.py

import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def check(one, zero):
    for i, j, k in combinations(one, 3):
        if j + j == i + k:
            return True
    for i, j, k in combinations(zero, 3):
        if j + j == i + k:
            return True
    return False


tcn = 2
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        one = []
        zero = []
        if s[i] == '1':
            one.append(i)
        else:
            zero.append(i)
        j = i
        while j + 1 < n and not check(one, zero):
            j += 1
            if s[j] == '1':
                one.append(j)
            else:
                zero.append(j)
        if check(one, zero):
            ans += n - j
    print(ans)
