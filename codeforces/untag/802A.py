# -*- coding: utf-8 -*-
# @Time: 2024/7/3 17:55
# @Author: yfwang
# @File: 802A.py

import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 3
for _tcn_ in range(tcn):
    n, k = MI()
    books = LI()
    nex = [n] * n
    hst = dict()
    for i in range(n - 1, -1, -1):
        book = books[i]
        if book in hst:
            nex[i] = hst[book]
        hst[book] = i

    h = []
    tot = 0
    st = set()
    for i, book in enumerate(books):
        if book in st:
            print()
            print(st)
            continue
        tot += 1
        heappush(h, (-nex[i], book))
        st.add(book)
        if len(h) > k:
            _, book = heappop(h)
            st.remove(book)
        print(f"book:{book}, {tot}")
        print(st)
    print(tot)
