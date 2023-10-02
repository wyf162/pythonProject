# _*_ coding: utf-8 _*_
# @Time : 2022/3/27 上午10:19 
# @Author : wangyefei
# @File : week-286-20220327.py
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ret = list()
        for num in nums:
            if len(ret) % 2 == 0:
                ret.append(num)
            else:
                if num == ret[-1]:
                    continue
                else:
                    ret.append(num)
        if len(ret) % 2 == 0:
            return len(nums) - len(ret)
        else:
            return len(nums) - len(ret) + 1

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        if intLength == 1:
            return [query if query < 10 else -1 for query in queries]
        n = intLength
        ret = list()
        if n % 2 == 0:
            m = n // 2
            start = 10 ** (m - 1)
            end = sum([9 * 10 ** i for i in range(m)])
            for query in queries:
                if query > (end - start) + 1:
                    ret.append(-1)
                else:
                    cur = start + query - 1
                    ret.append(int(str(cur) + str(cur)[::-1]))
        else:
            m = n // 2
            start = 10 ** (m - 1)
            end = sum([9 * 10 ** i for i in range(m)])
            print(start, end)
            for query in queries:
                if query > (end - start + 1) * 10:
                    ret.append(-1)
                else:
                    mid = ((query - 1) % 10)
                    cur = ((query - 1) // 10) + 1
                    cur = start + cur - 1
                    print(cur, mid)
                    ret.append(int(str(cur) + str(mid) + str(cur)[::-1]))
        return ret

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        dp = [[0 for j in range(k+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1,k+1):
                dp[i][j] = dp[i-1][j]
                cur = 0
                for t in range(1, min(j, len(piles[i-1]))+1):
                    cur += piles[i-1][t-1]
                    dp[i][j] = max(dp[i-1][j-t]+cur, dp[i][j])
        return dp[n][k]


if __name__ == '__main__':
    sol = Solution()
    piles = [[1, 100, 3], [7, 8, 9]]
    k = 3
    ret = sol.maxValueOfCoins(piles, k)
    print(ret)

    # queries = [9]
    # intLength = 5
    # queries = [449229674, 501930675, 40059525, 908875541, 9, 672504016]
    # intLength = 5
    # ret = sol.kthPalindrome(queries, intLength)
    # print(ret)
    # nums = [1,1,2,2,3,3]
    # nums = [1, 1, 2, 3, 5]
    # ret = sol.minDeletion(nums)
    # print(ret)
