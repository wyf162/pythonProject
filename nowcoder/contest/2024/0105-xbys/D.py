# -*- coding : utf-8 -*-
# @Time: 2024/1/5 19:28
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

n, m = MI()
A = LI()
B = [0]
for i in range(n):
    if A[i] == 0:
        if B[-1] == 0:
            continue
        B.append(0)
    else:
        if B[-1]:
            B[-1] += A[i]
        else:
            B.append(A[i])
if max(B) >= m:
    print('NO')
    exit()
print(B)
x = 0
for i in range(len(B) - 1, -1, -1):
    if x + B[i] < m:
        x += B[i]
    else:
        break
rst = sum(B) - x + n-1
print(rst)

