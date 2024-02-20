# -*- coding: utf-8 -*-
# @Time: 2024/2/20 14:06
# @Author: yfwang
# @File: 1922E.py
# https://codeforces.com/problemset/problem/1922/E

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
    x = I()
    i = 64
    nums = list(range(200))
    ret = []
    ans = []
    while (1 << i) > x:
        i -= 1

    ret.append(i)
    ans.extend(nums[-i:])
    nums = nums[:-i]

    x -= (1 << i)

    while x:
        if 2 ** i <= x:
            ans.insert(len(ans) - i, nums.pop())
            x -= 2 ** i
        else:
            i -= 1
    print(len(ans))
    print(*ans)
    # print(ret)
    # print(sum(ret))
