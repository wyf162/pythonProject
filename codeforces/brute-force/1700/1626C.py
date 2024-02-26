# -*- coding : utf-8 -*-
# @Time: 2023/10/17 22:32
# @Author: yefei.wang
# @File: 1626C.py

import sys

# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    k = LI()
    h = LI()
    st = []
    for i in range(n):
        st.append([k[i] - h[i], k[i]])
    st.sort()
    l, r = -1, -1
    ans = 0
    for it in st:
        if it[0] >= r:
            ans += (r - l) * (r - l + 1) // 2
            l, r = it
        else:
            r = max(r, it[1])
    ans += (r - l) * (r - l + 1) // 2
    print(ans)
