# -*- coding : utf-8 -*-
# @Time: 2022/6/26 10:27
# @Author: yefei.wang
# @File: week-299-20220626.py
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        x = set()
        for i in range(n):
            x.add((i, i))
            x.add((n - 1 - i, i))
        tag = True
        for i in range(n):
            for j in range(n):
                if (i, j) in x:
                    if grid[i][j]:
                        continue
                    else:
                        tag = False
                else:
                    if grid[i][j]:
                        tag = False
                    else:
                        continue
        return tag

    def countHousePlacements(self, n: int) -> int:
        dp = [[0] * 4 for _ in range(n)]
        dp[0] = [1] * 4

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
            dp[i][2] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][3] = dp[i - 1][0]
        return sum(dp[-1])

    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        diff = [y-x for x, y in zip(nums1, nums2)]
        pre = 0
        ans1 = diff[0]
        for d in diff:
            pre = max(pre+d, d)
            ans1 = max(ans1, pre)
        ret1 = ans1+sum(nums1)

        diff2 = [x-y for x, y in zip(nums1, nums2)]
        pre = 0
        ans2 = diff2[0]
        for d in diff2:
            pre = max(pre+d, d)
            ans2 = max(ans2, pre)
        ret2 = ans2+sum(nums2)

        return max(ret1, ret2)


if __name__ == '__main__':
    sol = Solution()
    # nums1 = [60, 60, 60]
    # nums2 = [10, 90, 10]
    # nums1 = [20, 40, 20, 70, 30]
    # nums2 = [50, 20, 50, 40, 20]
    # nums1 = [7, 11, 13]
    # nums2 = [1, 1, 1]
    # nums2 = [7, 11, 13]
    # nums1 = [1, 1, 1]
    nums1 = [10, 20, 50, 15, 30, 10]  # 230
    nums2 = [40, 20, 10, 100, 10, 10]
    ret = sol.maximumsSplicedArray(nums1, nums2)
    print(ret)

    # n = 9468
    # ret = sol.countHousePlacements(n)
    # print(ret)

    # grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]
    # ret = sol.checkXMatrix(grid)
    # print(ret)
