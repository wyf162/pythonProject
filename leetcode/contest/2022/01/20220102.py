# -*- coding : utf-8 -*-
# @Time: 2022/1/2 10:51
# @Author: yefei.wang
# @File: 20220102.py
from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, g: List[int]) -> int:
        n = len(g)
        rg = [[] for _ in range(n)]  # g的反图
        deg = [0] * n  # g 上每个节点的入度
        for v, w in enumerate(g):
            rg[w].append(v)
            deg[w] += 1

        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            v = q.popleft()
            w = g[v]
            deg[w] -= 1
            if deg[w] == 0:
                q.append(w)

        print(deg)

        def rdfs(v: int) -> int:
            max_depth = 1
            for w in rg[v]:
                if deg[w] == 0:
                    max_depth = max(max_depth, rdfs(w) + 1)
            return max_depth

        max_ring_size, sum_chain_size = 0, 0
        for i, d in enumerate(deg):
            if d <= 0:
                continue
            deg[i] = -1
            ring_size = 1
            v = g[i]
            while v != i:
                deg[v] = -1
                ring_size += 1
                v = g[v]
            if ring_size == 2:
                sum_chain_size += rdfs(i) + rdfs(g[i])
            else:
                max_ring_size = max(max_ring_size, ring_size)

        return max(max_ring_size, sum_chain_size)


if __name__ == "__main__":
    sol = Solution()
    g = [1, 2, 3, 1, 3, 4, 5]
    data = sol.maximumInvitations(g)
    print(data)
