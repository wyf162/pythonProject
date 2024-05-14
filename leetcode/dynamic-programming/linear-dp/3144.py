# -*- coding: utf-8 -*-
# @Time: 2024/5/14 13:25
# @Author: yfwang
# @File: 3144.py
from collections import Counter


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        f = [[0 for _ in range(26)] for _ in range(n + 1)]
        for i, c in enumerate(s):
            for j in range(26):
                f[i + 1][j] = f[i][j] + int(ord(c) - ord('a') == j)

        def check(i1, i2):
            mx = 0
            mi = 1001
            for j in range(26):
                d = f[i2][j] - f[i1][j]
                if d > 0:
                    if d > mx:
                        mx = d
                    if d < mi:
                        mi = d
                    if mx != mi:
                        return False
            return True

        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                if check(j, i):
                    if dp[j] + 1 < dp[i]:
                        dp[i] = dp[j] + 1
        return dp[-1]

