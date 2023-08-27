# _*_ coding: utf-8 _*_
# @Time : 2022/12/04 1:29 PM 
# @Author : yefe
# @File : 1774_closest_cost

from typing import List

MAX = 0x3f3f3f3f


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = MAX
        n = len(toppingCosts)

        def dfs(cost, i):
            nonlocal ans
            if abs(cost - target) < abs(ans - target):
                ans = cost
            elif abs(cost - target) == abs(ans - target) and cost < ans:
                ans = cost
            if i == n:
                return
            else:
                dfs(cost, i + 1)
                dfs(cost + toppingCosts[i], i + 1)
                dfs(cost + toppingCosts[i] * 2, i + 1)

        for base_cost in baseCosts:
            dfs(base_cost, 0)

        return ans


if __name__ == '__main__':
    sol = Solution()
    baseCosts = [2, 3]
    toppingCosts = [4, 5, 100]
    target = 18
    ret = sol.closestCost(baseCosts, toppingCosts, target)
    print(ret)
