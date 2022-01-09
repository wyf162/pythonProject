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
        s, t = min(m, n), max(m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    upper = i
                    down = m - i - 1
                    left = j
                    right = n - j - 1
                    for k in [upper, down, left, right]:
                        if k == 0:
                            continue
                        if t > k > s:
                            t = k
                        elif s > k:
                            t = s
                            s = k
        h, w = min(stampHeight, stampHeight), max(stampHeight, stampHeight)
        if h <= s and w <= t:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    # grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
    # stampHeight = 2
    # stampWidth = 1
    grid = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    stampHeight = 4
    stampWidth = 3
    ans = sol.possibleToStamp(grid, stampWidth, stampHeight)
    print(ans)

    # words = ["lc", "cl", "gg"]
    # ans = sol.longestPalindrome(words)
    # print(ans)

    # title = "capiTalIze tHe titLe"
    # print(sol.capitalizeTitle(title))
