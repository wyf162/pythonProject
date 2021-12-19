# -*- coding : utf-8 -*-
# @Time: 2021/12/15 22:33
# @Author: yefei.wang
# @File: 851_loud_and_rich.py
import collections
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        hst = collections.defaultdict(list)
        adj = collections.defaultdict(list)
        deg = [0] * n
        for edge in richer:
            x, y = edge
            hst[y].append(x)
            adj[x].append(y)
            deg[y] += 1

        zeros = list()
        for i in range(n):
            if deg[i] == 0:
                zeros.append(i)

        ans = [quiet[i] for i in range(n)]
        m = {v:k for k,v in zip(range(n),quiet)}
        while zeros:
            cur = zeros.pop(0)
            if hst.get(cur):
                ans[cur] = min(quiet[cur],min([ans[x] for x in hst.get(cur)]))
            for x in adj.get(cur,[]):
                deg[x] = deg[x] - 1
                if deg[x] == 0:
                    zeros.append(x)
        ans_new = [m[x] for x in ans]
        return ans_new

if __name__ == "__main__":
    sol = Solution()
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    richer = []
    quiet = [0]
    print(sol.loudAndRich(richer,quiet))
