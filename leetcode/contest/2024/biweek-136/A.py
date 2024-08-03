# -*- coding : utf-8 -*-
# @Time: 2024/8/3 22:29
# @Author: yefei.wang
# @File: A.py

from collections import Counter
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        f = [[0] * 11 for i in range(n)]
        for i, c in pick:
            f[i][c] += 1

        ans = 0
        for i in range(n):
            if max(f[i]) > i:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 4
    pick = [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]
    ret = sol.winningPlayerCount(n, pick)
    print(ret)
