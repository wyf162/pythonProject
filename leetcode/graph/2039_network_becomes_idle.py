# _*_ coding: utf-8 _*_
# @Time : 2022/3/20 下午12:51 
# @Author : wangyefei
# @File : 2039_network_becomes_idle.py
import collections
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [False] * n
        vis[0] = True
        q = collections.deque([0])
        ans, dist = 0, 1
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if vis[v]:
                        continue
                    vis[v] = True
                    q.append(v)
                    ans = max(ans, (dist * 2 - 1) // patience[v] * patience[v] + dist * 2 + 1)
            dist += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    edges = [[0, 1], [1, 2]]
    patience = [0, 2, 1]
    ret = sol.networkBecomesIdle(edges, patience)
    print(ret)
