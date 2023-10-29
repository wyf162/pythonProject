# -*- coding : utf-8 -*-
# @Time: 2023/10/15 10:31
# @Author: yefei.wang
# @File: week-367.py

from collections import deque
from typing import List


class Solution:
    def findIndices2(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    ans = [i, j]
                    return ans
        return ans

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ''
        for i in range(n):
            for j in range(i + k, n + 1):
                if s[i:j].count('1') == k:
                    if not ans:
                        ans = s[i:j]
                    elif len(ans) > len(s[i:j]):
                        ans = s[i:j]
                    elif len(ans) == len(s[i:j]) and ans > s[i:j]:
                        ans = s[i:j]
        return ans

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        k = indexDifference
        if k == 0:
            if valueDifference == 0:
                return [0, 0]
            else:
                return [-1, -1]

        mx = []
        qmax = deque()
        for i in range(k):
            while qmax and nums[qmax[-1]] < nums[i]:
                qmax.pop()
            qmax.append(i)
        mx.append(qmax[0])

        for i in range(k, len(nums)):
            while qmax and qmax[0] <= i - k:
                qmax.popleft()
            while qmax and nums[qmax[-1]] < nums[i]:
                qmax.pop()
            qmax.append(i)
            mx.append(qmax[0])

        mi = []
        qmin = deque()
        for i in range(k):
            while qmin and nums[qmin[-1]] > nums[i]:
                qmin.pop()
            qmin.append(i)
        mi.append(qmin[0])

        for i in range(k, len(nums)):
            while qmin and qmin[0] >= i - k:
                qmin.popleft()
            while qmin and nums[qmin[-1]] < nums[i]:
                qmin.pop()
            qmin.append(i)
            mi.append(qmin[0])
        n = len(nums)
        for i in range(n - k):
            if nums[mx[i]] - nums[mi[i]] >= valueDifference:
                return [mx[i], mi[i]]
        return [-1, -1]

    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        n, m = len(grid), len(grid[0])
        multi = 1

        for i in range(n):
            for j in range(m):
                multi *= grid[i][j]
                multi %= mod

        p = [[1 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                p[i][j] = (multi // grid[i][j]) % mod

        return p

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        if n == 1:
            if indexDifference > 0 or valueDifference > 0:
                return [-1, -1]
            else:
                return [0, 0]

        mx = [0] * n
        k = indexDifference
        for i in range(1, n):
            if nums[i] > nums[mx[i - 1]]:
                mx[i] = i
            else:
                mx[i] = mx[i-1]

            if i >= indexDifference:
                if nums[mx[i - k]] - nums[i] >= valueDifference:
                    return [mx[i - k], i]

        mi = [0] * n
        for i in range(1, n):
            if nums[i] < nums[mi[i - 1]]:
                mi[i] = i
            else:
                mi[i] = mi[i-1]

            if i >= indexDifference:
                if nums[i] - nums[mi[i - k]] >= valueDifference:
                    return [mi[i - k], i]
        return [-1, -1]


if __name__ == '__main__':
    sol = Solution()
    # grid = [[1, 2], [3, 4]]
    # # grid = [[12345], [2], [1]]
    # ret = sol.constructProductMatrix(grid)
    # print(ret)
    # s = "1100100101011001001"
    # k = 7
    # ret = sol.shortestBeautifulSubstring(s, k)
    # print(ret)
    # nums = [2, 1]
    # indexDifference = 0
    # valueDifference = 0
    # nums = [5, 1, 4, 1]
    # indexDifference = 2
    # valueDifference = 4
    # nums = [1, 2, 3]
    # indexDifference = 2
    # valueDifference = 4
    nums = [3, 12, 40]
    indexDifference = 0
    valueDifference = 9
    ret = sol.findIndices(nums, indexDifference, valueDifference)
    print(ret)
