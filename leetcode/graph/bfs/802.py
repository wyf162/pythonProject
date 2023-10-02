# -*- coding : utf-8 -*-
# @Time: 2023/10/1 20:32
# @Author: yefei.wang
# @File: 802.py

from typing import List
from collections import deque


class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        n = len(g)
        rg = [[] for i in range(n)]
        q = deque()
        deg = [0] * n
        for x in range(n):
            for y in g[x]:
                rg[y].append(x)
            deg[x] = len(g[x])
            if len(g[x]) == 0:
                q.append(x)

        ans = []
        while q:
            x = q.popleft()
            ans.append(x)
            for y in rg[x]:
                deg[y] -= 1
                if deg[y] == 0:
                    q.append(y)
        ans.sort()
        return ans


if __name__ == '__main__':
    sol = Solution()
    # g = [[1, 2], [2, 3], [5], [0], [5], [], []]
    g = [[], [0, 2, 3, 4], [3], [4], []]
    ret = sol.eventualSafeNodes(g)
    print(ret)
