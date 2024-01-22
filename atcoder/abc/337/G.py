# -*- coding : utf-8 -*-
# @Time: 2024/1/20 20:32
# @Author: yefei.wang
# @File: E.py

class BIT:
    def __init__(self, n):
        self.BIT = [0] * (n + 1)
        self.num = n

    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    # Ai += x O(logN)
    def update(self, idx, x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx & (-idx)
        return


import sys

input = sys.stdin.readline

N = int(input())
edge = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

vertex = []
stack = []
pos = 0
start = [-1 for i in range(N)]
end = [-1 for i in range(N)]
new_edge = [[] for i in range(N)]

while True:
    if start[pos] == -1:
        start[pos] = len(vertex) + 1
        vertex.append(pos)
        stack.append(pos)

    if edge[stack[-1]]:
        tmp = edge[stack[-1]].pop()
        if start[tmp] != -1:
            continue
        else:
            new_edge[pos].append(tmp)
            pos = tmp
    else:
        vertex.append(stack.pop())
        end[vertex[-1]] = len(vertex)
        if stack:
            pos = stack[-1]
        else:
            break

n = len(vertex)
bit = BIT(n)
add = [v for v in range(N)]
all = 0
for v in range(N):
    for nv in new_edge[v]:
        tmp = bit.query(end[nv]) - bit.query(start[nv] - 1)
        add[nv] -= tmp
        add[v] -= tmp
        all += tmp
    bit.update(start[v], 1)

res = [all] * N
S = 0
visit = [False] * N
for v in vertex:
    if not visit[v]:
        visit[v] = True
        S += add[v]
        res[v] += S
    else:
        S -= add[v]

print(*res)
