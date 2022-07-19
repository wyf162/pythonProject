# -*- coding : utf-8 -*-
# @Time: 2022/7/18 20:22
# @Author: yefei.wang
# @File: 749_contain_virus.py

from typing import List
from collections import deque


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        while True:
            neighbors, firewalls = list(), list()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        q = deque([(i, j)])
                        neighbor = set()
                        firewall, idx = 0, len(neighbors) + 1
                        isInfected[i][j] = -idx

                        while q:
                            x, y = q.popleft()
                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 1:
                                        q.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                                    elif isInfected[nx][ny] == 0:
                                        firewall += 1
                                        neighbor.add((nx, ny))

                        neighbors.append(neighbor)
                        firewalls.append(firewall)

            if not neighbors:
                break

            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            ans += firewalls[idx]

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2

            for i, neighbor in enumerate(neighbors):
                if i!=idx:
                    for x,y in neighbor:
                        isInfected[x][y]=1

            if len(neighbors) == 1:
                break
        return ans


if __name__ == '__main__':
    sol = Solution()
    isInfected = [[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0]]
    ret = sol.containVirus(isInfected)
    print(ret)
