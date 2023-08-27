# _*_ coding: utf-8 _*_
# @Time : 2022/10/16 3:52 PM 
# @Author : yefe
# @File : 886_possible_bipartition

from typing import List


class Solution:
    def possibleBipartition2(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n + 1)]

        for x, y in dislikes:
            g[x].append(y)
            g[y].append(x)

        tags = [None] * (n + 1)
        ret = True

        def dfs(x, tag):
            if tags[x] is None:
                tags[x] = tag
                for y in g[x]:
                    dfs(y, tag ^ 1)
            else:
                if tags[x] != tag:
                    nonlocal ret
                    ret = False

        for i in range(n):
            if tags[i] is None:
                dfs(i, 0)

        return ret

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n  # color[x] = 0 表示未访问节点 x

        def dfs(x: int, c: int) -> bool:
            color[x] = c
            return all(color[y] != c and (color[y] or dfs(y, -c)) for y in g[x])

        return all(c or dfs(i, 1) for i, c in enumerate(color))


if __name__ == '__main__':
    sol = Solution()
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    ret = sol.possibleBipartition(n, dislikes)
    print(ret)
