# -*- coding : utf-8 -*-
# @Time: 2023/11/26 10:31
# @Author: yefei.wang
# @File: B.py
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n, m = len(mat), len(mat[0])
        for i in range(n):
            if i % 2 == 1:
                for j in range(m):
                    if mat[i][j] == mat[i][(j + k) % m]:
                        continue
                    else:
                        return False
            else:
                for j in range(m):
                    if mat[i][j] == mat[i][(j - k) % m]:
                        continue
                    else:
                        return False

        return True
