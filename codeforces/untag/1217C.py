# -*- coding: utf-8 -*-
# @Time: 2024/5/30 10:35
# @Author: yfwang
# @File: 1217C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
sys.stdout = open('../output.txt', 'w')
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
    s = input()
    n = len(s)
    # for i in range(1, 30):
    #     t = bin(i)[2:].zfill(i)
    #     print(t)
    ans = s.count('1') + s.count('10')
    left_zero = 0
    for i in range(n):
        if s[i] == '0':
            left_zero += 1
        elif left_zero:
            x = 0
            for j in range(i, n):
                x *= 2
                x += int(s[j])
                if left_zero >= x - (j - i + 1):
                    if x - (j - i + 1) > 0:
                        ans += 1
                else:
                    break
            left_zero = 0
    print(ans)
    # ans = 0
    # for i in range(1, n+1):
    #     t = bin(i)[2:].zfill(i)
    #     ans += s.count(t)
    # print(ans)
