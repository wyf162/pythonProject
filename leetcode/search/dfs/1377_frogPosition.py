# _*_ coding: utf-8 _*_
# @Time : 2022/08/21 5:11 PM 
# @Author : yefe
# @File : 1377_frogPosition

import copy
from typing import List
from collections import defaultdict


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        if target==1 and t>1:
            return 0

        hst = defaultdict(list)
        for u, v in edges:
            hst[u].append(v)
            hst[v].append(u)

        ps = []

        def dfs(x: int, paths: List[int]):
            nonlocal ps
            # print(paths)
            for y in hst[x]:
                if y in paths:
                    continue
                elif y == target:
                    ps = copy.deepcopy(paths)
                else:
                    dfs(y, paths + [y])

        dfs(1, [1])
        print(ps)

        if t < len(ps) or t > len(ps) and len(hst[target]) > 1:
            return 0
        else:
            ret = 1
            for i, p in enumerate(ps):
                ret *= len(hst[p]) - (1 if i else 0)
        return float(1 / ret)


if __name__ == '__main__':
    sol = Solution()
    # n = 7
    # edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
    # t = 2
    # target = 4
    n = 9
    edges = [[2, 1], [3, 2], [4, 3], [5, 3], [6, 5], [7, 3], [8, 4], [9, 5]]
    t = 9
    target = 1
    ret = sol.frogPosition(n, edges, t, target)
    print(ret)
