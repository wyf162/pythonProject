# -*- coding : utf-8 -*-
# @Time: 2024/5/26 22:38
# @Author: yefei.wang
# @File: B.py

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
    x = I()
    bits = []
    while x > 0:
        bits.append(x % 2)
        x //= 2
    # print(bits)
    ans = []

    i = 0
    while i < len(bits):
        if bits[i] == 1:
            j = i + 1
            while j < len(bits):
                if bits[j] == 1:
                    j += 1
                else:
                    break
            if j - i > 1:
                ans.append(-1)
                for i1 in range(i + 1, j):
                    ans.append(0)
                if j < len(bits):
                    bits[j] = 1
                else:
                    ans.append(1)
            else:
                ans.append(bits[i])
            i = j
        else:
            ans.append(bits[i])
            i += 1
    print(len(ans))
    print(*ans)
