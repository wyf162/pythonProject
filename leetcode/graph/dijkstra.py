# _*_ coding: utf-8 _*_
# @Time : 2021/11/7 下午7:30 
# @Author : wangyefei
# @File : dijkstra.py
import math

MAX_PATH = math.inf


class Solution(object):

    def dijkstra(self, n, edges):
        hst = {}
        for edge in edges:
            hst[(edge[0], edge[1])] = edge[2]
            hst[(edge[1], edge[0])] = edge[2]
        adj_tbl = {}
        for u, v, w in edges:
            adj_tbl[u] = adj_tbl.get(u, [])
            adj_tbl[u].append(v)
            adj_tbl[v] = adj_tbl.get(v, [])
            adj_tbl[v].append(u)

        dis = [0] + [MAX_PATH] * n
        pre = [0] + [0]*n
        vis = [True] + [False] * n

        for i in range(1, n + 1):
            if hst.get((0, i)):
                dis[i] = hst.get((0, i))
        while not all(vis):
            u, d = 0, MAX_PATH
            for i in range(1, n + 1):
                if not vis[i] and dis[i] <= d:
                    u, d = i, dis[i]
            vis[u] = True

            for i in range(1, n + 1):
                if hst.get((i, u)) and dis[i] + hst[(i, u)] < dis[u]:
                    dis[u] = dis[i] + hst[(i, u)]
                    pre[u] = i
        self.show_path(n,pre)
        return dis, pre

    def show_path(self, n, pre):
        for i in range(1,n+1):
            path = []
            p = i
            path.insert(0, p)
            while p:
                p = pre[p]
                path.insert(0, p)
            for i,p in enumerate(path):
                if i:
                    print(f"->{p}", end="")
                else:
                    print(p, end="")
            print("")


if __name__ == "__main__":
    n = 4
    edges = [[0, 1, 3], [0, 2, 2], [1, 2, 5], [2, 3, 1], [1, 3, 4], [1, 4, 6]]
    sol = Solution()
    dis, pre = sol.dijkstra(n,edges)
    print(dis)
    print(pre)