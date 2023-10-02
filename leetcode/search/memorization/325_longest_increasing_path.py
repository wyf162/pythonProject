# _*_ coding: utf-8 _*_
# @Time : 2022/2/19 下午7:02 
# @Author : wangyefei
# @File : 325_longest_increasing_path.py
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        def backtrack(i, j):
            if dp[i][j]:
                return dp[i][j]
            res = 1
            for d_i, d_j in dir:
                n_i, n_j = i + d_i, j + d_j
                if 0 <= n_i < m and 0 <= n_j < n:
                    if matrix[n_i][n_j] > matrix[i][j]:
                        res = max(res, backtrack(n_i, n_j) + 1)
            dp[i][j] = res
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                backtrack(i, j)
                print(dp)
        ret = 1
        for i in range(m):
            for j in range(n):
                ret = max(ret, dp[i][j])
        return ret


if __name__ == '__main__':
    sol = Solution()
    # matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    matrix = [[4, 2], [3, 1]]
    # matrix = [[1]]
    ret = sol.longestIncreasingPath(matrix)
    print(ret)
