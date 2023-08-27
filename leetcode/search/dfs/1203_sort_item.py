# _*_ coding: utf-8 _*_
# @Time : 2022/08/20 1:22 PM 
# @Author : yefe
# @File : 1203_sort_item

from typing import List
from collections import deque


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_item = [[] for _ in range(n + m)]

        group_graph = [[] for _ in range(n + m)]
        item_graph = [[] for _ in range(n)]

        group_degree = [0] * (n + m)
        item_degree = [0] * n

        idxs = [_ for _ in range(n + m)]

        left_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = left_id
                left_id += 1
            group_item[group[i]].append(i)

        for i in range(n):
            cur_group_id = group[i]
            for item in beforeItems[i]:
                before_group_id = group[item]
                if before_group_id == cur_group_id:
                    item_degree[i] += 1
                    item_graph[item].append(i)
                else:
                    group_degree[cur_group_id] += 1
                    group_graph[before_group_id].append(cur_group_id)

        group_top_sort = self.topoSort(group_degree, group_graph, idxs)
        if not group_top_sort:
            return group_top_sort

        ans = []
        for cur_group_id in group_top_sort:
            size = len(group_item[cur_group_id])
            if size == 0:
                continue
            res = self.topoSort(item_degree, item_graph, group_item[cur_group_id])
            if not res:
                return res
            for item in res:
                ans.append(item)
        return ans

    def topoSort(self, deg: List[int], graph: List[List[int]], items: List[int]):
        q = deque()
        for item in items:
            if deg[item] == 0:
                q.append(item)
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

        return res if len(res) == len(items) else []


if __name__ == '__main__':
    sol = Solution()
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    rets = sol.sortItems(n, m, group, beforeItems)
    print(rets)
