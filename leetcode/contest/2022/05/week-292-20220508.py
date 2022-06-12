# _*_ coding: utf-8 _*_
# @Time : 2022/05/08 10:30 AM 
# @Author : yefe
# @File : week-292-20220508
from functools import cache
from typing import List


class Solution:
    def largestGoodInteger(self, num: str) -> str:

        for i in range(9, -1, -1):
            if str(i) * 3 in num:
                return str(i) * 3
        return ""

    def countTexts(self, pressedKeys: str) -> int:
        mod = 1000000007

        n = len(pressedKeys)
        f = [1, 1, 2, 4] + [0] * (n - 4)
        g = [1, 1, 2, 4] + [0] * (n - 4)
        for i in range(4, n):
            f[i] = (f[i - 1] + f[i - 2] + f[i - 3]) % mod
            g[i] = (g[i - 1] + g[i - 2] + g[i - 3] + g[i - 4]) % mod

        i = 0
        ret = 1
        while i < n:
            cnt = 1
            while i + 1 < n and pressedKeys[i] == pressedKeys[i + 1]:
                cnt += 1
                i += 1
            if pressedKeys[i] in '79':
                ret = ret * g[cnt] % mod
            else:
                ret = ret * f[cnt] % mod
            i += 1
        return ret

    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        vis = set()

        @cache
        def dfs(x, y, c):
            if x == m - 1 and y == n - 1:
                return c == 1

            c += 1 if grid[x][y] == '(' else -1
            return c >= 0 and (x < m - 1 and dfs(x + 1, y, c) and dfs(x, y + 1, c))


if __name__ == '__main__':
    sol = Solution()
    pressed_keys = "22233"
    ret = sol.countTexts(pressed_keys)
    print(ret)
