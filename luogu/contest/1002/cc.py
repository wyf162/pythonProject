# -*- coding : utf-8 -*-
# @Time: 2023/10/2 15:27
# @Author: yefei.wang
# @File: cc.py


import sys

sys.stdin = open('../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
a = LI()
b = LI()

colors = list(set(a))

unedges = set()

for i in range(n):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            unedges.add((a[j], a[i]))
            unedges.add((a[i], a[j]))

g = {k: set() for k in colors}
for u in colors:
    for v in colors:
        if (u, v) not in unedges:
            g[u].add(v)
            g[v].add(u)


class Tarjan:
    def __init__(self, graph):
        self.graph = graph
        self.id = 0
        self.disc = dict.fromkeys(self.graph, -1)
        self.low = dict.fromkeys(self.graph, -1)
        self.visited = set()
        self.stack = []
        self.res = []

    def connect(self, u):
        self.disc[u] = self.id
        self.low[u] = self.id
        self.id += 1

        self.visited.add(u)
        self.stack.append(u)

        for v in self.graph[u]:
            if self.disc[v] == -1:
                self.connect(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif u in self.visited:
                self.low[u] = min(self.low[u], self.disc[v])

        w = -1
        if self.low[u] == self.disc[u]:
            temp = []
            while w != u:
                w = self.stack.pop()
                temp.append(w)
                self.visited.remove(w)

            self.res.append(temp)

    def scc(self):
        for u in self.graph:
            if self.disc[u] == -1:
                self.connect(u)

        return self.res


def tarjan(graph):
    t = Tarjan(graph)
    return t.scc()


scc = tarjan(g)
print(scc)

ans = -1
for sc in scc:
    if len(sc) >= k:
        canditates = []
        for v in sc:
            canditates.append(b[v - 1])
        canditates.sort()
        ans = max(ans, sum(canditates[-k:]))

print(ans)
