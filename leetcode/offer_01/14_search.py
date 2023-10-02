# -*- coding : utf-8 -*-
# @Time: 2022/1/16 15:19
# @Author: yefei.wang
# @File: 14_search.py
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, path):
            print(path)
            if len(path) >= len(word):
                return True
            locations_list = self.next_locations(i, j, m, n)
            ans = False
            for x, y in locations_list:
                if board[x][y] == word[len(path)] and (x, y) not in path:
                    path.add((x, y))
                    ans = ans or dfs(x, y, path)
                    path.remove((x, y))
            return ans

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    s = set()
                    s.add((i, j))
                    ans = dfs(i, j, s)
                    if ans:
                        return True
        return False

    @staticmethod
    def next_locations(i, j, m, n):
        return [(x, y) for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if 0 <= x < m and 0 <= y < n]

    def movingCount(self, m: int, n: int, k: int) -> int:
        ans = 0
        q = list()
        q.append((0, 0))
        dp = [[1 for j in range(n)] for i in range(m)]
        dp[0][0] = 0
        while q:
            i, j = q.pop(0)
            ans += 1
            locations = self.next_locations(i, j, m, n)
            for x, y in locations:
                if self.cnt(x, y) <= k and dp[x][y]:
                    q.append((x, y))
                    dp[x][y]=0
        return ans

    @staticmethod
    def cnt(i, j):
        s = 0
        while i > 0:
            m = i % 10
            s = s + m
            i = i // 10
        while j > 0:
            m = j % 10
            s = s + m
            j = j // 10
        return s


if __name__ == '__main__':
    sol = Solution()
    res = sol.movingCount(2, 3, 1)
    print(res)
    # res = sol.cnt(15, 19)
    # print(res)
    # # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # # word = "ABCCED"
    # board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    # word = "AAB"
    # sol = Solution()
    # res = sol.exist(board, word)
    # print(res)
