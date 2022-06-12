# _*_ coding: utf-8 _*_
# @Time : 2022/05/22 10:30 AM 
# @Author : yefe
# @File : week-294-20220522
import bisect
from math import gcd
from typing import List


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        cnt = 0
        for a in s:
            if a == letter:
                cnt += 1
        ret = int(100 * cnt / n)
        return ret

    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        reminders = [0] * n
        for i in range(n):
            reminders[i] = capacity[i] - rocks[i]
        reminders.sort()
        i = 0
        cnt = 0
        while i < n and additionalRocks > 0:
            additionalRocks -= reminders[i]
            i += 1
            if additionalRocks >= 0:
                cnt += 1
        return cnt

    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n <= 2:
            return 1
        stockPrices.sort()
        k = self.compute_slope(stockPrices[0], stockPrices[1])
        cnt = 1
        for i in range(2, n):
            tk = self.compute_slope(stockPrices[i - 1], stockPrices[i])
            if tk == k:
                continue
            else:
                cnt += 1
                k = tk
        return cnt

    @staticmethod
    def compute_slope(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        dt = gcd(dy, dx)
        dy = int(dy / dt)
        dx = int(dx / dt)
        return dy, dx

    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(strength)
        left, st = [-1] * n, []  # left[i] 为左侧严格小于 strength[i] 的最近元素位置（不存在时为 -1）
        for i, v in enumerate(strength):
            while st and strength[st[-1]] >= v: st.pop()
            if st: left[i] = st[-1]
            st.append(i)

        right, st = [n] * n, []  # right[i] 为右侧小于等于 strength[i] 的最近元素位置（不存在时为 n）
        for i in range(n - 1, -1, -1):
            while st and strength[st[-1]] > strength[i]: st.pop()
            if st: right[i] = st[-1]
            st.append(i)

        s = [0] * (n + 1)  # 前缀和
        for i, v in enumerate(strength):
            s[i + 1] = (s[i] + v) % MOD
        ss = [0] * (n + 2)  # 前缀和的前缀和
        for i, v in enumerate(s):
            ss[i + 1] = (ss[i] + v) % MOD

        ans = 0
        for i, v in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1  # [l, r]  左闭右闭
            res = ((i - l + 1) * (ss[r + 2] - ss[i + 1]) - (r - i + 1) * (ss[i + 1] - ss[l])) % MOD
            ans = (ans + res * v) % MOD  # 累加贡献
        return ans


if __name__ == '__main__':
    strength = [1, 3, 1, 2]
    ret = Solution().totalStrength(strength)
    print(ret)





    # stockPrices = [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]
    # # stockPrices = [[3, 4], [1, 2], [7, 8], [2, 3]]
    # ret = Solution().minimumLines(stockPrices)
    # print(ret)

    # capacity = [10, 2, 2]
    # rocks = [2, 0, 0]
    # additionalRocks = 188
    # ret = Solution().maximumBags(capacity, rocks, additionalRocks)
    # print(ret)
