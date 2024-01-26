# -*- coding : utf-8 -*-
# @Time: 2024/1/26 19:14
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

tcn = I()
for _tcn_ in range(tcn):
    n, p = MI()
    a = LI()
    p -= 1
    if a[p] + 1 < 10:
        print(0, 0)
        continue
    left_pos, right_pos = p - 1, p + 1
    left_val, right_val = 1, 1
    while (left_pos >= 0 and left_val) or (right_pos < n and right_val):

        while left_pos >= 0 and left_val:
            if a[left_pos] + left_val >= 10:
                right_val += 1
                left_val -= 10 - a[left_pos]
                left_val += 1
                left_pos -= 1
            else:
                a[left_pos] += left_val
                left_val = 0

        while right_pos < n and right_val:
            if a[right_pos] + right_val >= 10:
                left_val += 1
                right_val -= 10 - a[right_pos]
                right_val += 1
                right_pos += 1
            else:
                a[right_pos] += right_val
                right_val = 0

    print(left_val, right_val)
