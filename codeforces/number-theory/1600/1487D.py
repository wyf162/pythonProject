# -*- coding : utf-8 -*-
# @Time: 2024/4/20 14:40
# @Author: yefei.wang
# @File: 1487D.py
import bisect
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

nums = []
for a in range(3, 44724, 2):
    b = (a * a - 1) // 2
    c = b + 1
    nums.append(c)

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    idx = bisect.bisect_right(nums, n)
    print(idx)
