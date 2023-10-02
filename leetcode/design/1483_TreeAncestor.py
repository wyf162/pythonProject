# _*_ coding: utf-8 _*_
# @Time : 2022/08/21 6:49 PM 
# @Author : yefe
# @File : 1483_TreeAncestor
from math import ceil, log, floor
from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.M = 16
        self.dp = [[-1] * self.M for _ in range(n)]

        for i in range(n):
            self.dp[i][0] = parent[i]

        for i in range(n):
            for j in range(1, self.M):
                if self.dp[i][j - 1] == -1:
                    continue
                self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.M):
            if k & 1 << i:
                node = self.dp[node][i]
            if node == -1:
                break
        return node


if __name__ == '__main__':
    n = 7
    parent = [-1, 0, 0, 1, 1, 2, 2]
    tree_ancestor = TreeAncestor(n, parent)
    ret = tree_ancestor.getKthAncestor(6, 1)
    print(ret)
