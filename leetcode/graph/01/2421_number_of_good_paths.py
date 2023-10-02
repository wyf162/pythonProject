# _*_ coding: utf-8 _*_
# @Time : 2022/12/03 2:44 PM 
# @Author : yefe
# @File : 2421_number_of_good_paths

from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        fa = [_ for _ in range(n)]
        size = [1] * n

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans = n
        for vx, x in sorted(zip(vals, range(n))):
            fx = find(x)
            for y in g[x]:
                y = find(y)
                if y == fx or vals[y] > vx:
                    continue
                if vals[y] == vx:
                    ans += size[fx] * size[y]
                    size[fx] += size[y]
                fa[y] = fx
        return ans


if __name__ == '__main__':
    sol = Solution()
    vals = [1, 3, 2, 1, 3]
    edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
    ret = sol.numberOfGoodPaths(vals, edges)
    print(ret)
