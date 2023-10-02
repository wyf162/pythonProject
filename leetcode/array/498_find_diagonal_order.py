# -*- coding : utf-8 -*-
# @Time: 2022/6/14 23:00
# @Author: yefei.wang
# @File: 498_find_diagonal_order.py
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ret = []
        for s in range(0, m + n - 1):
            tmp = []
            for i in range(s + 1):
                j = s - i
                if i >= m or j >= n:
                    continue
                else:
                    tmp.append(mat[i][j])
            if s%2==0:
                ret.extend(reversed(tmp))
            else:
                ret.extend(reversed(tmp))

        return ret


if __name__ == '__main__':
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ret = sol.findDiagonalOrder(mat)
    print(ret)
