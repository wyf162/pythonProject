# -*- coding : utf-8 -*-
# @Time: 2022/1/9 14:28
# @Author: yefei.wang
# @File: 304_num_matrix.py
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i-1][j-1] + matrix[i - 1][j - 1]

        self.dp = dp
        for i in range(m):
            print(dp[i])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
        return ans


if __name__ == '__main__':
    mtx = [[3, 0, 1, 4, 2],
           [5, 6, 3, 2, 1],
           [1, 2, 0, 1, 5],
           [4, 1, 0, 1, 7],
           [1, 0, 3, 0, 5]]

    num_matrix = NumMatrix(mtx)
    for arg in [[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]:
        ans = num_matrix.sumRegion(*arg)
        print(ans)
