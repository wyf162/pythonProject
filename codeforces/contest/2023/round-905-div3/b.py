# -*- coding : utf-8 -*-
# @Time: 2023/10/22 19:12
# @Author: yefei.wang
# @File: b.py

import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    s = input()
    cnt = [0]*26
    for c in s:
        i = ord(c) - ord('a')
        cnt[i] += 1
    odd = 0
    for i in range(26):
        if cnt[i]%2:
            odd += 1
    ans = False
    if k >= odd - 1:
        ans = True
    YN(ans)
