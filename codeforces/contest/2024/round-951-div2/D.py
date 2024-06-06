# -*- coding : utf-8 -*-
# @Time: 2024/6/6 23:06
# @Author: yefei.wang
# @File: D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    ans = -1
    s = input()
    if s[0] == '1':
        s = '1' * k + '0' * k + s
    else:
        s = '0' * k + '1' * k + s
    n += 2 * k
    suf = s[-1]
    for i in range(n - 2, -1, -1):
        if s[i] == suf[-1]:
            suf += s[i]
        else:
            break
    if len(suf) == k:
        suf1 = '0' * (k * 2)
        i1 = s.find(suf1) + k
        if i1 >= k:
            t = s[i1:] + s[:i1][::-1]
            ans = i1 - 2 * k
            # print(t)
        else:
            suf2 = '1' * (k * 2)
            i2 = s.find(suf2) + k
            if i2 >= k:
                t = s[i2:] + s[:i2][::-1]
                ans = i2 - 2 * k
                # print(t)
            else:
                ans = 1
                t = s
                # print(t)
    else:
        plc = '0' if s[-1] == '1' else '1'
        suf1 = plc + s[-1] * (k - len(suf)) + plc
        i1 = s.find(suf1) + k - len(suf) + 1
        if i1 >= k - len(suf) + 1:
            t = s[i1:] + s[:i1][::-1]
            ans = i1 - 2 * k
            # print(t)
        else:
            suf2 = plc + s[-1] * (k + k - len(suf)) + plc
            i2 = s.find(suf2) + k - len(suf) + 1
            if i2 >= k - len(suf) + 1:
                t = s[i2:] + s[:i2][::-1]
                # print(t)
                ans = i2 - 2 * k
            else:
                t = '#'

    cnt = len(s) // k
    c1 = cnt // 2
    c2 = cnt % 2
    if t[0] == '0':
        tt = ('0' * k + '1' * k) * c1 + ('0' * k) * c2
        if tt == t:
            print(ans)
        else:
            print(-1)
    else:
        tt = ('1' * k + '0' * k) * c1 + ('1' * k) * c2
        if tt == t:
            print(ans)
        else:
            print(-1)
