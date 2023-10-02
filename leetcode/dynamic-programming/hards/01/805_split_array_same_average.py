# _*_ coding: utf-8 _*_
# @Time : 2022/08/27 5:00 PM
# @Author : yefe
# @File : 805_split_array_same_average


from typing import List
from collections import defaultdict


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        s = sum(nums)
        k = len(nums)

        def helper(array):
            n = len(array)
            hst = defaultdict(set)
            hst[0].add(0)
            dp = [0] * (1 << n)
            for i in range(1, 1 << n):
                for j in range(n-1, -1, -1):
                    if (1 << j) & i:
                        dp[i] = dp[i - (1 << j)] + array[j]
                        break
                cnt = bin(i).count('1')
                hst[cnt].add(dp[i])
            return hst

        hst1 = helper(nums[:k // 2])
        hst2 = helper(nums[k // 2:])
        print(hst1)
        print(hst2)

        for i in range(k // 2 + 1):
            for j in range(k - k // 2 + 1):
                for x in hst1[i]:
                    y = ((i + j) * s / k)-x
                    if abs(y - int(y)) < 1e-6:
                        y = int(y)
                        if 0<i+j<k and y in hst2[j]:
                            print(i, j)
                            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 3, 4, 5, 6, 7, 8]
    nums = [1, 3]
    ret = sol.splitArraySameAverage(nums)
    print(ret)
