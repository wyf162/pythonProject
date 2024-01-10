# -*- coding : utf-8 -*-
# @Time: 2024/1/5 19:08
# @Author: yefei.wang
# @File: B.py

import sys

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

x = I()
if x % 2 == 0:
    print(x * 2)
else:
    print(x * 2 + 1)

# pre_sum = 0
# for i in range(1, 100):
#     pre_sum += i
#     if pre_sum % 2 ==0:
#         print(i)
