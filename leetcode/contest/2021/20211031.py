# _*_ coding: utf-8 _*_
# @Time : 10/31/21 10:27 AM 
# @Author : wangyefei
# @File : 20211031.py
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        dq = [start]
        old = [True] * 1001
        old[start] = False
        level = 1
        while dq:
            print(level, dq)
            for i in range(len(dq)):
                x = dq.pop()
                for num in nums:
                    y = x + num
                    if y == goal:
                        return level
                    elif 0 <= y <= 1000 and old[y]:
                        dq.insert(0, y)
                        old[y] = False

                    y = x - num
                    if y == goal:
                        return level
                    elif 0 <= y <= 1000 and old[y]:
                        dq.insert(0, y)
                        old[y] = False

                    y = x ^ num
                    if y == goal:
                        return level
                    elif 0 <= y <= 1000 and old[y]:
                        dq.insert(0, y)
                        old[y] = False
            level = level + 1
        return -1

    def possiblyEquals(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        dp = [[set() for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0].add(0)
        for i in range(m+1):
            for j in range(n+1):
                for delta in dp[i][j]:
                    num = 0
                    for k in range(i, min(i + 3, m)):
                        if '1' <= s1[k] <= '9':
                            num = 10 * num + int(s1[k])
                            dp[k + 1][j].add(delta + num)
                        else:
                            break
                    num = 0
                    for k in range(j, min(j + 3, n)):
                        if '1' <= s2[k] <= '9':
                            num = 10 * num + int(s2[k])
                            dp[i][k + 1].add(delta - num)
                        else:
                            break
                    if i < m and delta < 0 and not ('1' <= s1[i] <= '9'):
                        dp[i + 1][j].add(delta + 1)
                    if j < n and delta > 0 and not ('1' <= s2[j] <= '9'):
                        dp[i][j + 1].add(delta - 1)
                    if i < m and j < n and delta == 0 and s1[i] == s2[j]:
                        dp[i + 1][j + 1].add(0)
        for i in range(m+1):
            print(dp[i])
        return 0 in dp[m][n]


if __name__ == "__main__":
    s1 = "l123e"
    s2 = "44"
    sol = Solution()
    print(sol.possiblyEquals(s1, s2))
