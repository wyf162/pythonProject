# -*- coding : utf-8 -*-
# @Time: 2023/10/10 23:41
# @Author: yefei.wang
# @File: 1037D.py

import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
edges = [LI() for _ in range(n - 1)]
seq = LI()

g = [[] for _ in range(n + 1)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)

ans = True
vis = [False] * (n + 1)
q = deque()
q.append(1)
vis[1] = True
i = 1
if seq[0] != 1:
    print('No')
    exit(0)


def check(nums1, nums2):
    nums1.sort()
    nums2.sort()
    return nums1 == nums2


while q:
    for _ in range(len(q)):
        x = q.popleft()
        tmp = []
        for y in g[x]:
            if not vis[y]:
                q.append(y)
                vis[y] = True
                tmp.append(y)
        if not check(tmp, seq[i:i + len(tmp)]):
            ans = False
            break
        for j in range(len(tmp)):
            q.pop()
        for j in range(len(tmp)):
            q.append(seq[i + j])
        i += len(tmp)

    if not ans:
        break


print(['No', 'Yes'][int(ans)])
