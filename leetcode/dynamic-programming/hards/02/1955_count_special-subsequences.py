# _*_ coding: utf-8 _*_
# @Time : 2022/08/29 11:07 PM 
# @Author : yefe
# @File : 1955_count_special-subsequences

from typing import List


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        f = [[0] * 3 for _ in range(n + 1)]

        for i in range(n):
            f[i + 1][0] = f[i][0] + (f[i][0] + 1 if nums[i] == 0 else 0)
            f[i + 1][1] = f[i][1] + (f[i][1] + f[i][0] if nums[i] == 1 else 0)
            f[i + 1][2] = f[i][2] + (f[i][2] + f[i][1] if nums[i] == 2 else 0)

            for j in range(3):
                f[i][j] %= MOD

        return f[n][2]


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 2, 2]
    ret = sol.countSpecialSubsequences(nums)
    print(ret)
