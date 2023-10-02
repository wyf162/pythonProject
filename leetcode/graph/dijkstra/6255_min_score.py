# _*_ coding: utf-8 _*_
# @Time : 2022/12/04 4:09 PM 
# @Author : yefe
# @File : 6255_min_score
from collections import deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in roads:
            x -= 1
            y -= 1
            g[x].append([y, w])
            g[y].append([x, w])

        vis = [False]*n
        q = deque([0])
        ans = 100001
        while q:
            x = q.popleft()
            for y, w in g[x]:
                ans = min(ans, w)
                if not vis[y]:
                    q.append(y)
                    vis[y]=True
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 4
    roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    ret = sol.minScore(n, roads)
    print(ret)
