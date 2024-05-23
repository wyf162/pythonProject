# -*- coding: utf-8 -*-
# @Time: 2024/5/23 9:41
# @Author: yfwang
# @File: 2929.py

import math


def comb(a, b):
    if a < 0:
        return 0
    else:
        return math.comb(a, b)


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        c0 = comb(n + 2, 2)

        # 至少有一个大于
        c1 = comb(n - limit + 1, 2)
        # 至少有两个大于
        c2 = comb(n - limit * 2, 2)
        # 至少有三个大于
        c3 = comb(n - limit * 3 - 1, 2)
        ans = c0 - c1 * 3 + c2 * 3 - c3
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 5
    limit = 2
    ret = sol.distributeCandies(n, limit)
    print(ret)
