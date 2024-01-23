# -*- coding : utf-8 -*-
# @Time: 2024/1/23 22:40
# @Author: yefei.wang
# @File: 1511D.py
from typing import List
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


class DirectedEulerPath:
    def __init__(self, n, pairs: List[List[int]]):
        self.n = n
        # directed edge
        self.pairs = pairs
        # edges order on euler path
        self.paths = list()
        # nodes order on euler path
        self.nodes = list()
        self.exist = False
        self.get_euler_path()
        return

    def get_euler_path(self):
        # in and out degree sum of node
        degree = [0] * self.n
        edge = [[] for _ in range(self.n)]
        for i, j in self.pairs:
            degree[i] += 1
            degree[j] -= 1
            edge[i].append(j)

        # visited by lexicographical order
        for i in range(self.n):
            edge[i].sort(reverse=True)  # which can be adjusted

        # find the start point and end point of euler path
        starts = []
        ends = []
        zero = 0
        for i in range(self.n):
            if degree[i] == 1:
                starts.append(i)  # start node which out_degree - in_degree = 1
            elif degree[i] == -1:
                ends.append(i)  # start node which out_degree - in_degree = -1
            else:
                zero += 1  # other nodes have out_degree - in_degree = 0
        del degree

        if not len(starts) == len(ends) == 1:
            if zero != self.n:
                return
            starts = [0]

        # Hierholzer algorithm with iterative implementation
        stack = [starts[0]]
        while stack:
            current = stack[-1]
            if edge[current]:
                next_node = edge[current].pop()
                stack.append(next_node)
            else:
                self.nodes.append(current)
                if len(stack) > 1:
                    self.paths.append([stack[-2], current])
                stack.pop()
        self.paths.reverse()
        self.nodes.reverse()

        # Pay attention to determining which edge passes through before calculating the Euler path
        if len(self.nodes) == len(self.pairs) + 1:
            self.exist = True
        return


n, m = MI()
pairs = []
for i in range(m):
    for j in range(m):
        pairs.append([i, j])


dep = DirectedEulerPath(m, pairs)
paths = dep.paths
s = "abcdefghijklmnopqrstuvwxyz"
t = ''
for p in paths:
    t += s[p[1]]
# print(t)
rst = t * (n // len(t)) + t[:n % len(t)]
print(rst)

