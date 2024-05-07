# -*- coding: utf-8 -*-
# @Time: 2024/5/7 9:32
# @Author: yfwang
# @File: 1550C.py

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


def check(nums):
    n = len(nums)
    ret = False
    if n == 3:
        a, b, c = nums
        if a > b < c or a < b > c:
            ret = True
    elif n == 4:
        a, b, c, d = nums
        if b > a > c and b > c and c < d < b:
            ret = True
        if b < a < c and b < c and b < d < c:
            ret = True
    # print(*nums, ret)
    return ret


tcn = I()
for _tcn_ in range(tcn):
    N = I()
    A = LI()
    ans = N + N - 1
    for i in range(3, N + 1):
        ans += int(check(A[i - 3:i]))
    for i in range(4, N + 1):
        ans += int(check(A[i - 4:i]))
    print(ans)
