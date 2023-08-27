# _*_ coding: utf-8 _*_
# @Time : 2022/08/21 11:38 PM 
# @Author : yefe
# @File : 1766_get_coprimes

from math import gcd
from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        parent = [-1]*n
        for u, v in edges:
            parent[v] = u

        ans = [-1]*n
        for i in range(n):
            x = parent[i]
            while x > -1:
                if gcd(nums[i], nums[x]) == 1:
                    ans[i] = x
                    break
                x = parent[x]
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, 3, 2]
    edges = [[0, 1], [1, 2], [1, 3]]
    ret = sol.getCoprimes(nums, edges)
    print(ret)
