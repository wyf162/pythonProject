# -*- coding : utf-8 -*-
# @Time: 2022/1/8 22:28
# @Author: yefei.wang
# @File: 20220108.py

"""
rank 648 / 3360

"""
from typing import List


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ss = title.split(' ')
        sss = list()
        for s in ss:
            if len(s) < 3:
                sss.append(s.lower())
            else:
                sss.append(s.capitalize())
        return " ".join(sss)

    def longestPalindrome(self, words: List[str]) -> int:
        offset = ord('a')
        dp = [[0 for j in range(26)] for i in range(26)]
        for word in words:
            i, j = word
            i, j = ord(i) - offset, ord(j) - offset
            dp[i][j] += 1

        ans = 0
        for i in range(26):
            for j in range(i + 1, 26):
                ans += min(dp[i][j], dp[j][i]) * 4
        tag = False
        for i in range(26):
            if dp[i][i] > 1:
                ans += (dp[i][i] >> 1) * 4
            if tag == False and dp[i][i] % 2 == 1:
                tag = True
        if tag:
            ans += 2
        return ans

    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        sum = [[0] * (n + 1) for _ in range(m + 1)]
        diff = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):  # grid 的二维前缀和
                sum[i + 1][j + 1] = sum[i + 1][j] + sum[i][j + 1] - sum[i][j] + v

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0:
                    x, y = i + stampHeight, j + stampWidth  # 注意这是矩形右下角横纵坐标都 +1 后的位置
                    if x <= m and y <= n and sum[x][y] - sum[x][j] - sum[i][y] + sum[i][j] == 0:
                        diff[i][j] += 1
                        diff[i][y] -= 1
                        diff[x][j] -= 1
                        diff[x][y] += 1  # 更新二维差分

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                dp[i + 1][j + 1] = dp[i+1][j] + dp[i][j + 1] - dp[i][j] + diff[i][j]
                if dp[i + 1][j + 1] == 0 and v == 0:
                    return False
        for i in range(n+1):
            print(dp[i])
        return True


if __name__ == '__main__':
    sol = Solution()
    # grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
    # stampHeight = 2
    # stampWidth = 1
    grid = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    stampHeight = 4
    stampWidth = 3
    ans = sol.possibleToStamp(grid, stampHeight, stampWidth)
    print(ans)

    # words = ["lc", "cl", "gg"]
    # ans = sol.longestPalindrome(words)
    # print(ans)

    # title = "capiTalIze tHe titLe"
    # print(sol.capitalizeTitle(title))
