# -*- coding : utf-8 -*-
# @Time: 2023/10/1 19:06
# @Author: yefei.wang
# @File: 1857_largestPathValue.py
from string import ascii_lowercase
from typing import List
from collections import deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        rg = [[] for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            rg[v].append(u)
            deg[u] += 1

        q = deque(i for i, d in enumerate(deg) if d == 0)

        while q:
            x = q.popleft()
            for y in rg[x]:
                deg[y] -= 1
                if deg[y] == 0:
                    q.append(y)
        if any(deg):
            return -1

        def solve(a):
            deg = [0] * n
            for u, v in edges:
                deg[u] += 1
            dp = [0] * n
            q = deque(i for i, d in enumerate(deg) if d == 0)
            for i, d in enumerate(deg):
                if d == 0:
                    dp[i] = int(colors[i] == a)

            while q:
                x = q.popleft()
                for y in rg[x]:
                    deg[y] -= 1
                    if deg[y] == 0:
                        q.append(y)
                    dp[y] = max(dp[y], dp[x] + int(colors[y] == a))

            return max(dp)

        ans = 0
        for c in ascii_lowercase:
            ans = max(ans, solve(c))
        return ans


if __name__ == '__main__':
    sol = Solution()
    # colors = "a"
    # edges = [[0, 0]]
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    ret = sol.largestPathValue(colors, edges)
    print(ret)
