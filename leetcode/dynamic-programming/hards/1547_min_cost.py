# _*_ coding: utf-8 _*_
# @Time : 2022/08/24 9:53 PM 
# @Author : yefe
# @File : 1547_min_cost
from typing import List
from functools import cache


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @cache
        def dfs(s, t):
            can_cut = False
            ret = float("inf")
            for cut in cuts:
                if s < cut < t:
                    can_cut = True
                    tmp = t - s + dfs(s, cut) + dfs(cut, t)
                    ret = min(ret, tmp)

            if not can_cut:
                return 0
            else:
                return ret

        res = dfs(0, n)
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 7
    cuts = [1, 3, 4, 5]
    ans = sol.minCost(n, cuts)
    print(ans)
