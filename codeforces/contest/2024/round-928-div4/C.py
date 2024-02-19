# -*- coding : utf-8 -*-
# @Time: 2024/2/19 22:45
# @Author: yefei.wang
# @File: C.py

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

N = 2 * 10 ** 5 + 5
nums = [0] * N
for i in range(1, N):
    nums[i] = nums[i-1] + sum(int(x) for x in str(i))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    print(nums[n])