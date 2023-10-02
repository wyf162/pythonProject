# _*_ coding: utf-8 _*_
# @Time : 2022/12/04 3:40 PM 
# @Author : yefe
# @File : 6256_magnificent_sets

from collections import deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            x -= 1
            y -= 1
            g[x].append(y)
            g[y].append(x)

        time = [0] * n
        clock = 0

        def bfs(start: int) -> int:
            mx = 0
            nonlocal clock
            clock += 1
            time[start] = clock
            q = deque()
            q.append((start, base))
            while q:
                x, i = q.popleft()
                mx = max(mx, i)
                for y in g[x]:
                    if time[y] != clock:
                        time[y] = clock
                        q.append((y, i + 1))
            return mx

        color = [0] * n

        def dfs(x: int, c: int) -> bool:
            nodes.append(x)
            color[x] = c
            for y in g[x]:
                if color[y] == c or color[y] == 0 and not dfs(y, -c):
                    return False
            return True

        ans = 0
        for i, c in enumerate(color):
            if c:
                continue
            nodes = []
            if not dfs(i, 1):
                return -1
            base = ans + 1
            for x in nodes:
                ans = max(ans, bfs(x))
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]

    ret = sol.magnificentSets(n, edges)
    print(ret)
