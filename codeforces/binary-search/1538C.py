# -*- coding: utf-8 -*-
# @Time: 2024/4/1 9:13
# @Author: yfwang
# @File: 1538C.py

import sys
import bisect

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
    n, l, r = MI()
    nums = LI()
    nums.sort()
    ans = 0
    for i in range(n):
        i1 = bisect.bisect_left(nums, l - nums[i], i + 1)
        i2 = bisect.bisect_right(nums, r - nums[i], i + 1)
        # print(i, i1, i2)
        ans += i2 - i1

    print(ans)
