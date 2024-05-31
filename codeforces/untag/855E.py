# -*- coding: utf-8 -*-
# @Time: 2024/5/31 16:53
# @Author: yfwang
# @File: 855E.py

import sys
from functools import cache

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def convert_to_base(base, x):
    rets = []
    while x > 0:
        rets.append(x % b)
        x //= b
    return rets[::-1]


tcn = I()
for _tcn_ in range(tcn):
    b, L, R = MI()

    cc = []
    for x in [L - 1, R]:
        nums = convert_to_base(b, x)
        print(nums)


        @cache
        def dfs(i, is_num, is_limit, state):
            if i == len(nums):
                return int(state == 0)
            if is_limit:
                up = nums[i]
            else:
                up = b
            ret = 0
            if not is_num:
                ret += dfs(i + 1, False, False, state)
                down = 1
            else:
                down = 0

            for d in range(down, up):
                ret += dfs(i + 1, True, d == nums[i] and is_limit, state ^ (1 << d))
            return ret

        c = dfs(0, False, True, 0)
        cc.append(c)
        dfs.cache_clear()
    print(cc)
    ans = cc[1] - cc[0]
    print(ans)
