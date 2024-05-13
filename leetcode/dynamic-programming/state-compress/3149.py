# -*- coding: utf-8 -*-
# @Time: 2024/5/13 14:25
# @Author: yfwang
# @File: 3149.py

from functools import cache
from typing import List

inf = 0x3f3f3f3f


class Solution:
    def findPermutation(self, a: List[int]) -> List[int]:
        n = len(a)

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(s: int, j: int) -> int:
            if s == (1 << n) - 1:
                # 所有位置都填完了，最后一个位置是下标 j
                return abs(j - a[0])
            res = inf
            # 枚举当前位置填下标 k
            for k in range(1, n):
                if s >> k & 1 == 0:  # k 之前没填过
                    res = min(res, dfs(s | 1 << k, k) + abs(j - a[k]))
            return res

        ans = []

        # 原理见上面贴的题解链接
        def make_ans(s: int, j: int) -> None:
            ans.append(j)
            if s == (1 << n) - 1:
                return
            final_res = dfs(s, j)
            for k in range(1, n):
                if s >> k & 1 == 0 and dfs(s | 1 << k, k) + abs(j - a[k]) == final_res:
                    make_ans(s | 1 << k, k)
                    break

        make_ans(1, 0)
        return ans
