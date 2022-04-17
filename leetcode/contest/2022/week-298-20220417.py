# _*_ coding: utf-8 _*_
# @Time : 2022/4/17 上午10:28 
# @Author : wangyefei
# @File : week-298-20220417.py
from typing import List
from collections import defaultdict


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        while n > k:
            t = ""
            for i in range(0, n, k):
                print(s[i:i + k])
                t += str(sum([int(x) for x in s[i:i + k]]))
            print(t)
            s = t
            n = len(s)
        return s

    def minimumRounds(self, tasks: List[int]) -> int:
        hst = dict()
        for task in tasks:
            hst[task] = hst.get(task, 0) + 1
        ret = 0
        for k, v in hst.items():
            if v < 2:
                return -1
            n = v // 3
            m = v % 3
            if m == 0:
                ret += n
            else:
                ret += n + 1
        return ret

    def maxTrailingZeros2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0

        dp = [[[0, 0] for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j][0] = self.compute(grid[i][j], 2)
                    dp[i][j][1] = self.compute(grid[i][j], 5)
                elif i == 0:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i][j - 1][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i][j - 1][1]
                elif j == 0:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i - 1][j][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i - 1][j][1]
                else:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i - 1][j - 1][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i - 1][j - 1][1]
        for i in range(m):
            for j in range(n):
                ret = max(ret, min(dp[i][j]))

        dp = [[[0, 0] for i in range(n)] for j in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i == m - 1 and j == 0:
                    dp[i][j][0] = self.compute(grid[i][j], 2)
                    dp[i][j][1] = self.compute(grid[i][j], 5)
                elif i == m - 1:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i][j - 1][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i][j - 1][1]
                elif j == 0:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i + 1][j][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i + 1][j][1]
                else:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i + 1][j - 1][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i + 1][j - 1][1]
        for i in range(m - 1, -1, -1):
            for j in range(n):
                ret = max(ret, min(dp[i][j]))

        dp = [[[0, 0] for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i == 0 and j == n - 1:
                    dp[i][j][0] = self.compute(grid[i][j], 2)
                    dp[i][j][1] = self.compute(grid[i][j], 5)
                elif i == 0:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i][j + 1][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i][j + 1][1]
                elif j == n - 1:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i - 1][j][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i - 1][j][1]
                else:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i - 1][j + 1][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i - 1][j + 1][1]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                ret = max(ret, min(dp[i][j]))

        dp = [[[0, 0] for i in range(n)] for j in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j][0] = self.compute(grid[i][j], 2)
                    dp[i][j][1] = self.compute(grid[i][j], 5)
                elif i == m - 1:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i][j + 1][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i][j + 1][1]
                elif j == n - 1:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i + 1][j][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i + 1][j][1]
                else:
                    dp[i][j][0] = self.compute(grid[i][j], 2) + dp[i + 1][j + 1][0]
                    dp[i][j][1] = self.compute(grid[i][j], 5) + dp[i + 1][j + 1][1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ret = max(ret, min(dp[i][j]))
        return ret

    def compute(self, num, k):
        ret = 0
        while num:
            if num % k == 0:
                ret += 1
                num = num // k
            else:
                break
        return ret

    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0

        gd = [[[0, 0] for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                gd[i][j][0] = self.compute(grid[i][j], 2)
                gd[i][j][1] = self.compute(grid[i][j], 5)

        dp = [[[0, 0] for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j][0] = gd[i][j][0]
                    dp[i][j][1] = gd[i][j][1]
                else:
                    dp[i][j][0] = gd[i][j][0] + dp[i][j - 1][0]
                    dp[i][j][1] = gd[i][j][1] + dp[i][j - 1][1]

        dp2 = [[[0, 0] for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp2[i][j][0] = gd[i][j][0]
                    dp2[i][j][1] = gd[i][j][1]
                else:
                    dp2[i][j][0] = gd[i][j][0] + dp2[i - 1][j][0]
                    dp2[i][j][1] = gd[i][j][1] + dp2[i - 1][j][1]

        for i in range(m):
            for j in range(n):
                l_2 = dp[i][j][0]
                r_2 = dp[i][-1][0] - dp[i][j][0]

                l_5 = dp[i][j][1]
                r_5 = dp[i][-1][1] - dp[i][j][1]

                ll_2 = dp2[i][j][0]
                rr_2 = dp2[-1][j][0] - dp2[i][j][0]

                ll_5 = dp2[i][j][1]
                rr_5 = dp2[-1][j][1] - dp2[i][j][1]

                ret = max(ret,
                          min(l_2 + ll_2 - gd[i][j][0], l_5 + ll_5 - gd[i][j][1]),
                          min(r_2 + ll_2, r_5 + ll_5),
                          min(r_2 + rr_2 + gd[i][j][0], r_5 + rr_5 + gd[i][j][1]),
                          min(l_2 + rr_2, l_5 + rr_5))

        return ret

    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        ans = 0

        def dfs(x: int) -> int:
            nonlocal ans
            max_len = 0
            for y in g[x]:
                l = dfs(y) + 1
                if s[y] != s[x]:
                    ans = max(ans, max_len + l)
                    max_len = max(max_len, l)
            return max_len

        dfs(0)
        return ans + 1


if __name__ == '__main__':
    sol = Solution()
    parent = [-1, 0, 0, 1, 1, 2]
    s = "abacbe"
    ret = sol.longestPath(parent, s)
    print(ret)

    # grid = [[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]]
    # grid = [[899, 727, 165, 249, 531, 300, 542, 890],
    #         [981, 587, 565, 943, 875, 498, 582, 672],
    #         [106, 902, 524, 725, 699, 778, 365, 220]]  # 5
    # grid = [
    #     [824, 709, 193, 413, 701, 836, 727],
    #     [135, 844, 599, 211, 140, 933, 205],
    #     [329, 68, 285, 282, 301, 387, 231],
    #     [293, 210, 478, 352, 946, 902, 137],
    #     [806, 900, 290, 636, 589, 522, 611],
    #     [450, 568, 990, 592, 992, 128, 92],
    #     [780, 653, 795, 457, 980, 942, 927],
    #     [849, 901, 604, 906, 912, 866, 688]]  # 6
    # ret = sol.maxTrailingZeros(grid)
    # print(ret)

    # print(sol.compute(8,2))
    # print(sol.compute(9,3))
    # print(sol.compute(6,2))
    # print(sol.compute(6,3))

    # tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    # tasks = [2, 3, 3]
    # ret = sol.minimumRounds(tasks)
    # print(ret)

    # s = "11111222223"
    # k = 3
    # s = "00"
    # k = 3
    # ret = sol.digitSum(s, k)
    # print(ret)
