# -*- coding : utf-8 -*-
# @Time: 2023/12/9 22:45
# @Author: yefei.wang
# @File: D.py

from typing import List

MX = 0x3f3f3f3f


class Floyd:
    def __init__(self):
        return

    @staticmethod
    def shortest_path(n, dp):
        # Calculate the shortest path between all point pairs using the Floyd algorithm
        for k in range(n):  # mid point
            for i in range(n):  # start point
                for j in range(n):  # end point
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        return dp


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        mtx = [[MX for _ in range(n)] for _ in range(n)]
        for u, v, w in roads:
            mtx[u][v] = min(mtx[u][v], w)
            mtx[v][u] = min(mtx[v][u], w)
        ans = 1
        for s in range(1, 1 << n, 1):
            dp = [[MX for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if (s >> i) & 1 and (s >> j) & 1:
                        dp[i][j] = mtx[i][j]
                        dp[j][i] = mtx[i][j]

            Floyd.shortest_path(n, dp)
            tag = True
            for i in range(n):
                for j in range(i + 1, n):
                    if (s >> i) & 1 and (s >> j) & 1:
                        if dp[i][j] > maxDistance:
                            tag = False
                            break
                if tag is False:
                    break
            # print(bin(s)[2:].zfill(3), tag)
            if tag:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 3
    maxDistance = 5
    # roads = [[0, 1, 2], [1, 2, 10], [0, 2, 10]]
    roads = [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]
    ret = sol.numberOfSets(n, maxDistance, roads)
    print(ret)
