# -*- coding: utf-8 -*-
# @Time: 2024/4/29 13:21
# @Author: yfwang
# @File: F.py
# scanline

import sys
from heapq import heapify, heappop

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m = MI()
W = LI()
V = LI()
X = LI()

h = []
s = 0
p = 0
for w, v in zip(W, V):
    for x in X:
        h.append([s-x, v-p])
    p = v
    s += w

for x in X:
    h.append([s-x, 0-p])

heapify(h)
st = set()
st.add(0)
cur = 0
while h:
    t = h[0][0]
    while h and h[0][0] == t:
        cur += h[0][1]
        heappop(h)
    st.add(cur)
print(len(st))


