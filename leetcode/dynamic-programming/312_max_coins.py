# _*_ coding: utf-8 _*_
# @Time : 2022/06/04 10:03 PM 
# @Author : yefe
# @File : 312_max_coins
from typing import List
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1]+nums+[1]

        @lru_cache(None)
        def solve(left: int, right: int):
            if left>=right-1:
                return 0

            best = 0
            for i in range(left+1, right):
                total = val[left]*val[i]*val[right]
                total += solve(left, i)+solve(i, right)
                best = max(total, best)
            return best

        return solve(0, n+1)

    def max_coins(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0]*(n+2) for _ in range(n+2)]
        val = [1] + nums + [1]

        for i in range(n-1, -1, -1):
            for j in range(i+2, n+2):
                for k in range(i+1, j):
                    total = val[i]*val[k]*val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)
        return rec[0][n+1]


if __name__ == '__main__':
    sol = Solution()
    nums = [3,1,5,8]
    ret = sol.maxCoins(nums)
    print(ret)