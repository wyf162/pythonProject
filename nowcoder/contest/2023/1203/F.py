# -*- coding : utf-8 -*-
# @Time: 2023/12/3 14:54
# @Author: yefei.wang
# @File: F.py
import copy
import math
import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

n, q = LI()
a = LI()
ops = LI()
b = copy.deepcopy(a)

for op in ops:
    if op > 0:
        b[op - 1] = 0

v = 0
for i in range(n):
    v = math.gcd(v, b[i])

rst = 0
for op in ops[::-1]:
    if op > 0:
        v = math.gcd(v, a[op - 1])
    else:
        rst += v
        rst %= mod

print(rst)
