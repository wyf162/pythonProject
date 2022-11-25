# _*_ coding: utf-8 _*_
# @Time : 2022/11/13 7:15 PM 
# @Author : yefe
# @File : 6240_most_profitable_path

from typing import List
from collections import deque, defaultdict


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # 进行建图，建立成以 0 节点为根的树，并记录一个点所有子节点
        path = defaultdict(list)
        for u, v in edges:
            path[u].append(v)
            path[v].append(u)
        father = [-1] * (len(edges) + 1)
        note = [[] for _ in range(len(edges) + 1)]
        q = deque([0])
        while q:
            p = q.popleft()
            for newp in path[p]:
                if father[newp] == -1 and newp != 0:
                    father[newp] = p
                    q.append(newp)
                    note[p].append(newp)

        # 找到 bob 位置往根节点的路径
        bob_path = [bob]
        while father[bob_path[-1]] >= 0:
            bob_path.append(father[bob_path[-1]])

        # 对于数值调整
        for i in bob_path[:len(bob_path) // 2]:
            amount[i] = 0
        if len(bob_path) % 2:
            amount[bob_path[len(bob_path) // 2]] //= 2

        # 树状 DP
        def getRes(idx):
            if len(note[idx]) == 0:
                return amount[idx]
            return max(getRes(i) for i in note[idx]) + amount[idx]

        return getRes(0)
