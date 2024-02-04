# -*- coding : utf-8 -*-
# @Time: 2024/2/4 11:06
# @Author: yefei.wang
# @File: C2.py

from typing import List


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        Tot = [[0 for _ in range(n)] for _ in range(m)]
        Cnt = [[0 for _ in range(n)] for _ in range(m)]

        def compute(ni, nj):
            tot = 0
            tmp = []
            for dii in (-1, 0, 1):
                for djj in (-1, 0, 1):
                    nii, njj = ni + dii, nj + djj
                    if 0 <= nii < m and 0 <= njj < n:
                        tmp.append(image[nii][njj])
            if len(tmp) == 9:
                diff = [tmp[0] - tmp[1], tmp[0] - tmp[3],
                        tmp[1] - tmp[2], tmp[1] - tmp[4],
                        tmp[2] - tmp[5],
                        tmp[3] - tmp[6], tmp[3] - tmp[4],
                        tmp[4] - tmp[5], tmp[4] - tmp[7],
                        tmp[5] - tmp[8],
                        tmp[6] - tmp[7],
                        tmp[7] - tmp[8]]
                mi = min(diff)
                mx = max(diff)
                if -threshold <= mi and mx <= threshold:
                    tot = sum(tmp) // 9
                    for dii in (-1, 0, 1):
                        for djj in (-1, 0, 1):
                            nii, njj = ni + dii, nj + djj
                            Tot[nii][njj] += tot
                            Cnt[nii][njj] += 1

        res = [[image[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                compute(i, j)
        for i in range(m):
            for j in range(n):
                if Cnt[i][j]:
                    res[i][j] = Tot[i][j] // Cnt[i][j]
        return res


if __name__ == '__main__':
    sol = Solution()
    image = [[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]]
    threshold = 3
    ret = sol.resultGrid(image, threshold)
    print(ret)
