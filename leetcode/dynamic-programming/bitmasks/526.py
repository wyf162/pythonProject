# -*- coding: utf-8 -*-
# @Time: 2024/5/24 9:37
# @Author: yfwang
# @File: 526.py

from collections import deque


class Solution:
    def countArrangement(self, n: int) -> int:
        f = [0] * (1 << n)
        f[0] = 1
        for s in range(1, 1 << n):
            i = s.bit_count()
            for j in range(1, n + 1):
                if s >> (j - 1) & 1 and (i % j == 0 or j % i == 0):
                    f[s] += f[s ^ (1 << (j - 1))]
        return f[-1]


if __name__ == '__main__':
    sol = Solution()
    n = 1
    ret = sol.countArrangement(n)
    print(ret)
