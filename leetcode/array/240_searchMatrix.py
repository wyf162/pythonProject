# _*_ coding: utf-8 _*_
# @Time : 10/24/21 7:46 PM 
# @Author : wangyefei
# @File : 240_searchMatrix.py
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        tag = False
        while i < m and j > -1:
            print(i, j)
            if matrix[i][j] == target:
                tag = True
                break
            elif matrix[i][j] > target:
                j = j - 1
            else:
                i = i + 1
        return tag


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = -8
    print(sol.searchMatrix(matrix, target))
