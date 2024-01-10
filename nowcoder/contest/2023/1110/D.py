# -*- coding : utf-8 -*-
# @Time: 2023/11/10 20:07
# @Author: yefei.wang
# @File: D.py

import sys
from heapq import heappop, heappush

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
s = input()
ss = []
a = LI()
h = []

for i in range(n):
    if s[i] == '0':
        heappush(h, [-a[i], i])
    elif s[i] == '1':
        heappush(h, [a[i], i])
    ss.append(int(s[i]))
res = []

while True:
    sm = 0
    ixs = []
    for _ in range(m):
        x, i = heappop(h)
        sm += -x
        ixs.append(i)

    if sm > 0:
        rs = [0] * n
        for j in ixs:
            rs[j] = 1
            ss[j] ^= 1
            if ss[j] == 1:
                heappush(h, [a[j], j])
            else:
                heappush(h, [-a[j], j])
        res.append(rs)
    else:
        break

# print(''.join(map(str, ss)))
ans = 0
for i in range(n):
    if ss[i] == 1:
        ans += a[i]

p = len(res)
print(f"{ans} {p}")
for i in range(p):
    print(''.join(map(str, res[i])))
