# _*_ coding: utf-8 _*_
# @Time : 2022/3/27 下午9:34 
# @Author : wangyefei
# @File : 17023_find_square.py
from typing import List


class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0:
            return list()
        if n == 1:
            if matrix[0][0] == 0:
                return [0, 0, 1]
            else:
                return list()
        ans = [0, 0, 0]
        cnt = [[[0, 0] for j in range(n)] for i in range(n)]
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if matrix[r][c] == 1:
                    cnt[r][c][0] = 0
                    cnt[r][c][1] = 0
                else:
                    if r < n - 1:
                        cnt[r][c][0] = cnt[r + 1][c][0]+1
                    else:
                        cnt[r][c][0] = 1
                    if c < n - 1:
                        cnt[r][c][1] = cnt[r][c + 1][1]+1
                    else:
                        cnt[r][c][1] = 1

                    l = min(cnt[r][c][0], cnt[r][c][1])
                    while l >= ans[2]:
                        if cnt[r][c+l-1][0] >= l and cnt[r+l-1][c][1] >= l:
                            ans = [r, c, l]
                            break
                        l = l - 1
        print(cnt)
        return ans


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ]
    ret = sol.findSquare(matrix)
    print(ret)