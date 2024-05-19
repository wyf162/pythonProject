# -*- coding : utf-8 -*-
# @Time: 2024/5/19 10:47
# @Author: yefei.wang
# @File: D.py
from functools import lru_cache


class Solution:
    def waysToReachStair(self, k: int) -> int:

        @lru_cache(None)
        def dfs(cur, jump, minus):
            ret = 0
            if cur - 2 > k:
                return ret
            if cur == k:
                ret += 1
            if cur > 0 and minus:
                ret += dfs(cur - 1, jump, False)
            ret += dfs(cur + 2 ** jump, jump + 1, True)
            return ret

        ans = dfs(1, 0, True)
        return ans


if __name__ == '__main__':
    sol = Solution()
    k = 524285
    ret = sol.waysToReachStair(k)
    print(ret)
