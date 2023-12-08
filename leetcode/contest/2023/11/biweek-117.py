# -*- coding : utf-8 -*-
# @Time: 2023/11/11 22:30
# @Author: yefei.wang
# @File: biweek-117.py
import math


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        N = max(n, limit) + 15

        dp1 = [0] * (N + 5)
        for i in range(min(limit + 1, n + 1)):
            dp1[i] = 1

        pre_dp1 = [0] * (N + 5)
        for i in range(0, n + 2):
            pre_dp1[i + 1] = pre_dp1[i] + dp1[i]

        for i in range(0, min(limit * 2 + 1, n + 1)):
            dp1[i] = pre_dp1[i + 1] - pre_dp1[max(0, i - limit)]

        for i in range(0, n + 2):
            pre_dp1[i + 1] = pre_dp1[i] + dp1[i]

        for i in range(0, min(limit * 3 + 1, n + 1)):
            dp1[i] = pre_dp1[i + 1] - pre_dp1[max(0, i - limit)]

        return dp1[n]

        # for i in range(limit + 1):
        #     f[i][1] = 1
        #
        # for i in range(0, min(limit * 2 + 1, n + 1)):
        #     for j in range(max(0, i - limit), i + 1):
        #         f[i][2] += f[j][1]
        #
        # for i in range(0, min(limit * 3 + 1, n + 1)):
        #     for j in range(max(0, i - limit), i + 1):
        #         f[i][3] += f[j][2]
        #
        # return f[n][3]

    def stringCount(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n < 4:
            return 0
        if n == 4:
            return 12
        x1 = pow(26, n)
        x2 = pow(23, n-3) * math.comb(n, 3) * 12
        x3 = pow(23, n-2) * math.comb(n, 2) * 7
        x4 = pow(23, n-1) * math.comb(n, 1) * 3
        rst = x1 - x2 - x3 - x4
        rst %= mod
        return rst


if __name__ == '__main__':
    sol = Solution()
    n = 10
    ret = sol.stringCount(n)
    print(ret)

    # n = 19
    # limit = 17
    # ret = sol.distributeCandies(n, limit)
    # print(ret)
