from bisect import bisect_left
from functools import cache


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count(num: int) -> int:
            @cache
            def dfs(i: int, cnt1: int, is_limit: bool) -> int:
                if i == 0:
                    return cnt1
                res = 0
                up = num >> (i - 1) & 1 if is_limit else 1
                for d in range(up + 1):  # 枚举要填入的数字 d
                    res += dfs(i - 1, cnt1 + (d == 1 and i % x == 0), is_limit and d == up)
                return res
            return dfs(num.bit_length(), 0, True)

        # <= k 转换成 >= k+1 的数再减一
        # 原理见 https://www.bilibili.com/video/BV1AP41137w7/
        return bisect_left(range((k + 1) << x), k + 1, key=count) - 1
