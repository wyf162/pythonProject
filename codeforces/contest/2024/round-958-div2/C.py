# -*- coding : utf-8 -*-
# @Time: 2024/7/15 22:44
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    n = I()
    s = list(bin(n)[2:])
    nums = [n]
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            s[i] = '0'
            nums.append(int(''.join(s), 2))
            s[i] = '1'
    if nums[-1] == 0:
        nums.pop()
    nums.reverse()
    print(len(nums))
    print(*nums)
