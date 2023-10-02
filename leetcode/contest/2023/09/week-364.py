# -*- coding : utf-8 -*-
# @Time: 2023/9/24 10:29
# @Author: yefei.wang
# @File: week-364.py

from typing import List

N = 10000
# latest prime factor
lpf = list(range(N + 1))
# 最小质因数 埃式筛法 初始化过程
for x in range(2, int(N ** .5) + 1):
    if lpf[x] == x:
        for y in range(x * x, N + 1, x):
            lpf[y] = x


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ss = list(s)
        ss.sort(reverse=True)
        ss.append(ss.pop(0))
        ans = ''.join(ss)
        return ans

    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        stk = [-1]
        pre = [0]
        for i in range(n):
            while len(stk) > 1 and maxHeights[stk[-1]] > maxHeights[i]:
                stk.pop()
            pre.append(pre[stk[-1] + 1] + (i - stk[-1]) * maxHeights[i])
            stk.append(i)
        print(pre)

        stk = [n]
        suf = [0 for _ in range(n+1)]
        for i in range(n - 1, -1, -1):
            while len(stk) > 1 and maxHeights[stk[-1]] > maxHeights[i]:
                stk.pop()
            suf[i] = suf[stk[-1]] + (stk[-1] - i) * maxHeights[i]
            stk.append(i)
        print(suf)

        ans = n
        for i in range(n):
            ans = max(ans, pre[i] + suf[i])
        return ans




    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        lr = [0 for _ in range(n + 1)]

        def dfs(x, fa):
            child = 1
            for y in g[x]:
                if y != fa:
                    child += dfs(y, x)
            nonlocal lr
            lr[x] = child
            return lr[x]

        dfs(1, 0)
        print(lr)

        ans = 0

        def dfs2(x, fa):
            if lpf[x] == x:
                nonlocal ans
                for y in g[x]:
                    if y != fa:
                        ans += lr[y] * (lr[x] - lr[y] - 1)
            for y in g[x]:
                if y != fa:
                    dfs(y, x)

        dfs2(1, -1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    maxHeights = [3, 2, 5, 5, 2, 3]
    ret = sol.maximumSumOfHeights(maxHeights)
    print(ret)
    # sol = Solution()
    # n = 5
    # edges = [[1,2],[1,3],[2,4],[2,5]]
    # ret = sol.countPaths(n, edges)
    # print(ret)
