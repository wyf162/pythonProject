# -*- coding : utf-8 -*-
# @Time: 2022/1/29 21:00
# @Author: yefei.wang
# @File: 1765_highest_peak.py
import collections
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        m, n = len(isWater), len(isWater[0])
        visited = [[False for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append([i, j])
                    visited[i][j]=True
                    isWater[i][j]=0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                if x - 1 >= 0 and not visited[x-1][y]:
                    q.append([x - 1, y])
                    isWater[x - 1][y] = isWater[x][y] + 1
                    visited[x - 1][y]=True
                if x + 1 < m and not visited[x+1][y]:
                    q.append([x + 1, y])
                    isWater[x + 1][y] = isWater[x][y] + 1
                    visited[x + 1][y] = True
                if y - 1 >= 0 and not visited[x][y-1]:
                    q.append([x, y - 1])
                    isWater[x][y - 1] = isWater[x][y] + 1
                    visited[x][y - 1] = True
                if y + 1 < n and not visited[x][y+1]:
                    q.append([x, y + 1])
                    isWater[x][y + 1] = isWater[x][y] + 1
                    visited[x][y + 1] = True
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == -1:
                    isWater[i][j] = 0
        return isWater


if __name__ == '__main__':
    sol = Solution()
    isWater = [[0,0,1],[1,0,0],[0,0,0]]
    data = sol.highestPeak(isWater)
    print(data)
