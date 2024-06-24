# -*- coding: utf-8 -*-
# @Time: 2024/6/24 11:15
# @Author: yfwang
# @File: 3193.py

from typing import List
from functools import lru_cache

mod = 10 ** 9 + 7


class Solution:
    def numberOfPermutations2(self, n: int, requirements: List[List[int]]) -> int:
        hst = dict()
        for end, cnt in requirements:
            hst[end] = cnt

        @lru_cache(None)
        def dfs(i, j):
            if j < 0:
                return 0
            if i == 0:
                return int(j == 0)

            if i in hst:
                if j == hst[i]:
                    tot = 0
                    for k in range(i + 1):
                        tot += dfs(i - 1, j - k)
                        tot %= mod
                    return tot
                else:
                    return 0
            else:
                tot = 0
                for k in range(i + 1):
                    tot += dfs(i - 1, j - k)
                    tot %= mod
                return tot

        if n - 1 not in hst:
            hst[n - 1] = n * (n - 1) // 2

        ans = dfs(n - 1, hst[n - 1])
        return ans

    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 1_000_000_007
        req = [-1] * n
        req[0] = 0
        for end, cnt in requirements:
            req[end] = cnt
        if req[0]:
            return 0

        m = max(req)
        f = [[0] * (m + 1) for _ in range(n)]
        f[0][0] = 1
        for i in range(1, n):
            mx = m if req[i] < 0 else req[i]
            r = req[i - 1]
            if r >= 0:
                for j in range(r, min(i + r, mx) + 1):
                    f[i][j] = f[i - 1][r]
            else:
                for j in range(mx + 1):
                    f[i][j] = sum(f[i - 1][j - k] for k in range(min(i, j) + 1)) % MOD
        return f[-1][req[-1]]



if __name__ == '__main__':
    sol = Solution()
    # n = 3
    # requirements = [[2, 2], [0, 0]]
    n = 11
    requirements = [[6,10],[10,22]]

    ret = sol.numberOfPermutations(n, requirements)
    print(ret)
