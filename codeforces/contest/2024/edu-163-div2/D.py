# -*- coding : utf-8 -*-
# @Time: 2024/3/15 23:28
# @Author: yefei.wang
# @File: D.py


import sys

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

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    ans = 0
    for d in range(n // 2, 0, -1):
        cnt = 0
        for i in range(n-d):
            if s[i] == s[i + d] or s[i] == '?' or s[i+d] == '?':
                cnt += 1
            else:
                cnt = 0
            if cnt == d:
                ans = d * 2
                break
        if ans:
            break
    print(ans)


