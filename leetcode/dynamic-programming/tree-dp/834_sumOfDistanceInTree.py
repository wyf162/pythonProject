# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 10:08 PM 
# @Author : yefe
# @File : 834_sumOfDistanceInTree
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * n
        sz = [0] * n
        dp = [0] * n
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, f):
            sz[u] = 1
            dp[u] = 0
            for v in g[u]:
                if v == f:
                    continue
                dfs(v, u)
                dp[u] += dp[v] + sz[v]
                sz[u] += sz[v]

        def dfs2(u, f):
            ans[u] = dp[u]
            for v in g[u]:
                if v == f:
                    continue
                pu, pv = dp[u], dp[v]
                su, sv = sz[u], sz[v]
                dp[u] -= dp[v] + sz[v]
                sz[u] -= sz[v]
                dp[v] += dp[u] + sz[u]
                sz[v] += sz[u]

                dfs2(v, u)
                dp[u], dp[v] = pu, pv
                sz[u], sz[v] = su, sv

        dfs(0, -1)
        dfs2(0, -1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    ret = sol.sumOfDistancesInTree(n, edges)
    print(ret)
