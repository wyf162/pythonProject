# -*- coding : utf-8 -*-
# @Time: 2023/10/1 15:44
# @Author: yefei.wang
# @File: 2127_maximumInvitations.py

from typing import List
from collections import deque


class Solution:
    def maximumInvitations(self, g: List[int]) -> int:  # favorite 就是内向基环森林 g
        n = len(g)
        rg = [[] for _ in range(n)]  # g 的反图
        deg = [0] * n  # g 上每个节点的入度
        for v, w in enumerate(g):
            rg[w].append(v)
            deg[w] += 1

        # 拓扑排序，剪掉 g 上的所有树枝
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            v = q.popleft()
            w = g[v]  # v 只有一条出边
            deg[w] -= 1
            if deg[w] == 0:
                q.append(w)

        # 通过反图 rg 寻找树枝上最深的链
        def rdfs(v: int) -> int:
            max_depth = 1
            for w in rg[v]:
                if deg[w] == 0:  # 树枝上的点在拓扑排序后，入度均为 0
                    max_depth = max(max_depth, rdfs(w) + 1)
            return max_depth

        max_ring_size = sum_chain_size = 0
        for i, d in enumerate(deg):
            if d <= 0:
                continue
            # 遍历基环上的点（拓扑排序后入度大于 0）
            deg[i] = -1
            ring_size = 1
            v = g[i]
            while v != i:
                deg[v] = -1  # 将基环上的点的入度标记为 -1，避免重复访问
                ring_size += 1
                v = g[v]
            if ring_size == 2:  # 基环大小为 2
                sum_chain_size += rdfs(i) + rdfs(g[i])  # 累加两条最长链的长度
            else:
                max_ring_size = max(max_ring_size, ring_size)  # 取所有基环的最大值
        return max(max_ring_size, sum_chain_size)


if __name__ == '__main__':
    sol = Solution()
    favorite = [3, 0, 1, 4, 1]
    ret = sol.maximumInvitations(favorite)
    print(ret)
