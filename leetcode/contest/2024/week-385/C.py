# -*- coding : utf-8 -*-
# @Time: 2024/2/18 10:28
# @Author: yefei.wang
# @File: C.py

from typing import List
from collections import Counter

N = 10 ** 7
lpf = list(range(N + 1))
for x in range(2, int(N ** .5) + 1):
    if lpf[x] == x:
        for y in range(x * x, N + 1, x):
            lpf[y] = x


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        hst = Counter()
        for ci in range(m):
            for cj in range(n):

                i, j = ci, cj
                v = mat[i][j]
                while j + 1 < n:
                    v *= 10
                    v += mat[i][j + 1]
                    hst[v] += 1
                    j += 1

                i, j = ci, cj
                v = mat[i][j]
                while j - 1 >= 0:
                    v *= 10
                    v += mat[i][j - 1]
                    hst[v] += 1
                    j -= 1

                i, j = ci, cj
                v = mat[i][j]
                while i + 1 < m:
                    v *= 10
                    v += mat[i + 1][j]
                    hst[v] += 1
                    i += 1

                i, j = ci, cj
                v = mat[i][j]
                while i - 1 >= 0:
                    v *= 10
                    v += mat[i - 1][j]
                    hst[v] += 1
                    i -= 1

                i, j = ci, cj
                v = mat[i][j]
                while j + 1 < n and i + 1 < m:
                    v *= 10
                    v += mat[i + 1][j + 1]
                    hst[v] += 1
                    j += 1
                    i += 1

                i, j = ci, cj
                v = mat[i][j]
                while j + 1 < n and i - 1 >= 0:
                    v *= 10
                    v += mat[i - 1][j + 1]
                    hst[v] += 1
                    j += 1
                    i -= 1

                i, j = ci, cj
                v = mat[i][j]
                while j - 1 >= 0 and i + 1 < m:
                    v *= 10
                    v += mat[i + 1][j - 1]
                    hst[v] += 1
                    j -= 1
                    i += 1

                i, j = ci, cj
                v = mat[i][j]
                while j - 1 >= 0 and i - 1 >= 0:
                    v *= 10
                    v += mat[i - 1][j - 1]
                    hst[v] += 1
                    j -= 1
                    i -= 1

        print(hst)
        mx = 0
        ans = -1
        for k, v in hst.items():
            if lpf[k] == k:
                if v > mx:
                    ans = k
                    mx = v
                elif v == mx:
                    ans = max(ans, k)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # mat = [[1, 1], [9, 9], [1, 1]]
    mat = [[8, 9, 3], [3, 5, 6], [1, 2, 5]]

    ret = sol.mostFrequentPrime(mat)
    print(ret)
