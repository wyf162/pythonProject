# _*_ coding: utf-8 _*_
# @Time : 2022/08/28 7:06 PM 
# @Author : yefe
# @File : 1388_max_size_slices

from typing import List


class Solution2:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        slices = slices + slices

        dp = [[0] * (n + n + 1) for _ in range(n + n + 1)]
        for i in range(n + n - 3 + 1):
            k = 3
            dp[i][i + k] = slices[i + 1]
            print(i, i + k, dp[i][i + k])

        for k in range(6, n + n + 1 - 3, 3):
            for i in range(n + n - k + 1):
                dp[i][i + k] = max(dp[i][i + k], dp[i][i + k - 3] + slices[i + k - 3 + 1])
                dp[i][i + k] = max(dp[i][i + k], dp[i + 1][i + 1 + k - 3] + slices[i + k - 3 + 1])
                dp[i][i + k] = max(dp[i][i + k], dp[i + 2][i + 2 + k - 3] + slices[i + 1])
                dp[i][i + k] = max(dp[i][i + k], dp[i + 3][i + 3 + k - 3] + slices[i + 1])
        return max([dp[i][i + n] for i in range(n + 1)])


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def calculate(s):
            n = len(s)
            choose = (n + 1) // 3
            dp = [[0] * (choose + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, choose + 1):
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i - 2 >= 0 else 0) + s[i - 1])
            return dp[n][choose]

        ans1 = calculate(slices[1:])
        ans2 = calculate(slices[:-1])
        return max(ans1, ans2)


if __name__ == '__main__':
    sol = Solution()
    # slices = [1, 2, 3, 4, 5, 6]
    # slices = [8, 9, 8, 6, 1, 1]
    slices = [3, 95, 6, 53, 77, 76, 22, 47, 20, 42, 32, 79, 6, 41, 76, 73, 72, 17, 65, 91, 57, 67, 61, 35, 94, 47, 48,
              70, 63, 33, 96, 20, 16, 47, 38, 48, 64, 48, 5, 95, 43, 45, 48, 63, 70, 92, 58, 77, 89, 78, 94, 33, 29, 2,
              40, 29, 81, 99, 72, 86, 7, 41, 99, 22, 25, 89, 15, 58, 27, 17, 10, 95, 54, 30, 36, 41, 44, 64, 45, 26, 94,
              38, 93, 99, 57, 62, 44, 25, 76, 75, 97, 77, 55, 22, 15, 49]
    # slices = [1, 2, 3, 2, 3, 2]
    ret = sol.maxSizeSlices(slices)
    print(ret)
