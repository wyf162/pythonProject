# -*- coding : utf-8 -*-
# @Time: 2024/4/13 22:44
# @Author: yefei.wang
# @File: B.py

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    cnt = Counter(nums)
    two = 0
    for k, v in cnt.items():
        if v == 2:
            two += 1
    print(two)
