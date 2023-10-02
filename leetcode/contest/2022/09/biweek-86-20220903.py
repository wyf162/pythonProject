# _*_ coding: utf-8 _*_
# @Time : 2022/09/03 10:20 PM 
# @Author : yefe
# @File : biweek-86-20220903
import bisect
from typing import List
from bisect import bisect_left


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        ss = set()
        for i in range(n - 1):
            s = nums[i] + nums[i + 1]
            if s in ss:
                return True
            else:
                ss.add(s)
        return False

    def isStrictlyPalindromic(self, n: int) -> bool:

        for k in range(2, n - 1):
            t = []
            m = n
            while m > 0:
                t.append(m % k)
                m = m // k
            if t == t[::-1]:
                continue
            else:
                return False
        return True

    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m = len(mat)
        n = len(mat[0])
        cs = []

        def dfs(i, k, c):
            if bin(c).count('1') == k:
                cs.append(c)
            elif i < n:
                dfs(i + 1, k, c)
                dfs(i + 1, k, c | (1 << i))

        dfs(0, cols, 0)
        # print(cs)

        mats = []
        for i in range(m):
            tmp = 0
            for j in range(n):
                if mat[i][j] == 1:
                    tmp |= (1 << j)
            mats.append(tmp)
        ans = 0
        for c in cs:
            cnt = 0
            for m in mats:
                if m & c == m:
                    cnt += 1
            ans = max(ans, cnt)
        return ans

    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

        n = len(chargeTimes)

        pres = [0]*(n+1)
        for i in range(n):
            pres[i+1] = pres[i] + runningCosts[i]

        def my_max(nums):
            pass

        def check(k):
            if k == 0:
                return False
            for i in range(0, n - k + 1):
                c = max(chargeTimes[i:i + k])
                s = pres[i+k]-pres[i]
                if c + k * s <= budget:
                    return True
            return False

        l = 0
        r = n

        while l < r:
            # print(l, r)
            m = (r-l+1)//2 + l
            if check(m):
                l = m
            else:
                r = m - 1
        return l


if __name__ == '__main__':
    sol = Solution()
    # chargeTimes = [3, 6, 1, 3, 4]
    # runningCosts = [2, 1, 3, 4, 5]
    # budget = 25

    # chargeTimes = [11, 12, 19]
    # runningCosts = [10, 8, 7]
    # budget = 19
    chargeTimes = [8, 76, 74, 9, 75, 71, 71, 42, 15, 58, 88, 38, 56, 59, 10, 11]
    runningCosts = [1, 92, 41, 63, 22, 37, 37, 8, 68, 97, 39, 59, 45, 50, 29, 37]
    budget = 412
    ret = sol.maximumRobots(chargeTimes, runningCosts, budget)
    print(ret)
    # mat = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]]
    # cols = 2
    # ret = sol.maximumRows(mat, cols)
    # print(ret)

    # n = 9
    # ret = sol.isStrictlyPalindromic(n)
    # print(ret)
