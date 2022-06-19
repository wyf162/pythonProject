# -*- coding : utf-8 -*-
# @Time: 2022/6/12 10:26
# @Author: yefei.wang
# @File: week-297-20220612.py
from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        fee = 0
        for idx, bracket in enumerate(brackets):
            if idx == 0:
                upper, percent = bracket
                if income <= upper:
                    fee += income * percent
                    break
                else:
                    fee += upper * percent
            else:
                upper, percent = bracket
                if income <= upper:
                    fee += (income - brackets[idx - 1][0]) * percent
                    break
                else:
                    fee += (brackets[idx][0] - brackets[idx - 1][0]) * percent

        return fee / 100

    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[5050 for j in range(n)] for i in range(m)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(m - 1):
            for j in range(n):
                for k in range(n):
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + moveCost[grid[i][k]][j] + grid[i + 1][j])

        return min(dp[-1])

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)
        if k == 7:
            cookies.sort()
            return max(cookies[0] + cookies[1], cookies[-1])
        if k == 6:
            cookies.sort()
            ret = max(cookies[0]+cookies[2], cookies[1]+cookies[3], cookies[-1])
            ret = min(ret, max(cookies[0]+cookies[3], cookies[1]+cookies[2], cookies[-1]))
            return ret
        n = len(cookies)
        k2 = k ** n
        ret = sum(cookies)
        for i in range(k2):
            t = i
            dp = [0] * k
            for j in range(n):
                idx = t % k
                t = t // k
                dp[idx] += cookies[j]
            ret = min(ret, max(dp))

        return ret

    def distinctNames(self, ideas: List[str]) -> int:
        d = defaultdict(set)
        for name in ideas:
            d[name[0]].add(name[1:])
        return sum((len(d[a]) - len(d[a] & d[b])) * (len(d[b]) - len(d[a] & d[b])) * 2 for a, b in product(d, repeat=2) if ord(a) < ord(b))


if __name__ == '__main__':
    sol = Solution()
    # cookies = [8, 15, 10, 20, 8]
    # k = 2
    # cookies = [6, 1, 3, 2, 2, 4, 1, 2]
    # k = 6
    cookies = [2, 13, 5, 12, 4, 12, 10, 4]
    k = 3
    ret = sol.distributeCookies(cookies, k)
    print(ret)

    # grid = [[5, 3], [4, 0], [2, 1]]
    # moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
    # ret = sol.minPathCost(grid, moveCost)
    # print(ret)
