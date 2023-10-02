# _*_ coding: utf-8 _*_
# @Time : 2022/12/11 4:13 PM 
# @Author : yefe
# @File : 6260_max_points
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        mn = m * n

        # 并查集模板
        fa = list(range(mn))
        size = [1] * mn

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def merge(from_: int, to: int) -> None:
            from_ = find(from_)
            to = find(to)
            if from_ != to:
                fa[from_] = to
                size[to] += size[from_]

        # 矩阵元素从小到大排序，方便离线
        a = sorted((x, i, j) for i, row in enumerate(grid) for j, x in enumerate(row))

        ans, j = [0] * len(queries), 0
        # 查询的下标按照查询值从小到大排序，方便离线
        for i, q in sorted(enumerate(queries), key=lambda p: p[1]):
            while j < mn and a[j][0] < q:
                _, x, y = a[j]
                # 枚举周围四个格子，值小于 q 才可以合并
                for x2, y2 in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                    if 0 <= x2 < m and 0 <= y2 < n and grid[x2][y2] < q:
                        merge(x * n + y, x2 * n + y2)  # 把坐标压缩成一维的编号
                j += 1
            if grid[0][0] < q:
                ans[i] = size[find(0)]  # 左上角的连通块的大小
        return ans


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
    queries = [5, 6, 2]
    ret = sol.maxPoints(grid, queries)
    print(ret)