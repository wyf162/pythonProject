# _*_ coding: utf-8 _*_
# @Time : 2021/11/3 下午10:24 
# @Author : wangyefei
# @File : 407_trapRainWater.
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        water = 0
        unvisited = [[True for j in range(n)] for i in range(m)]
        for i in range(m):
            unvisited[i][0] = False
            unvisited[i][m - 1] = False
        for j in range(n):
            unvisited[0][j] = False
            unvisited[m - 1][j] = False

        while coord := self.find(unvisited):
            while coord := self.find(unvisited):
                q = []
                border_val = 20001
                border_map = []
                insider_map = []
                insider_val = -1
                q.append(coord)
                print(q)
                while q:
                    x, y = cur = q.pop()
                    unvisited[x][y] = False
                    insider_map.append(heightMap[x][y])
                    insider_val = max(insider_val, heightMap[x][y])
                    s, t = x + 1, y + 1
                    if unvisited[s][t]:
                        q.insert(0, (s, t))
                    elif heightMap[s][t] > insider_val:
                        border_map.append((s, t))
                        border_val = min(border_val, heightMap[s][t])
                    s, t = x + 1, y - 1
                    if unvisited[s][t]:
                        q.insert(0, (s, t))
                    elif heightMap[s][t] > insider_val:
                        border_map.append((s, t))
                        border_val = min(border_val, heightMap[s][t])
                    s, t = x - 1, y + 1
                    if unvisited[s][t]:
                        q.insert(0, (s, t))
                    elif heightMap[s][t] > insider_val:
                        border_map.append((s, t))
                        border_val = min(border_val, heightMap[s][t])
                    s, t = x - 1, y - 1
                    if unvisited[s][t]:
                        q.insert(0, (s, t))
                    elif heightMap[s][t] > insider_val:
                        border_map.append((s, t))
                        border_val = min(border_val, heightMap[s][t])
                print("border val",border_val)
                print("insider map ",insider_map)
                water += border_val * len(insider_map) - sum(insider_map)
        print(water)
        return water

    @staticmethod
    def find(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]:
                    return i, j
        return None


if __name__ == "__main__":
    sol = Solution()
    heightMap = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]
    sol.trapRainWater(heightMap)
