# -*- coding : utf-8 -*-
# @Time: 2023/10/21 19:40
# @Author: yefei.wang
# @File: c.py

import sys

sys.stdin = open('./../input.txt')
input = lambda: sys.stdin.readline().rstrip('\r\n')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

q = I()
queries = [LI() for _ in range(q)]

s0 = "DKER EPH VOS GOLNJ ER RKH HNG OI RKH UOPMGB CPH VOS FSQVB DLMM VOS QETH SQB"
s1 = "DKER EPH VOS GOLNJ UKLMH QHNGLNJ A"
s2 = "AB CPH VOS FSQVB DLMM VOS QHNG A"
s3 = "AB"

x0 = len(s0)
x1 = len(s1)
x2 = len(s2)
x3 = len(s3)

N = 10 ** 5 + 1
x = len(s0)
f = [0] * N
f[0] = x
MN = 10 ** 20
for i in range(1, N):
    f[i] = x1 + f[i - 1] + x2 + f[i - 1] + 2
    f[i] = min(f[i], MN)

rst = ''
for n, k in queries:
    ans = '.'
    if k > f[n]:
        rst += ans
        continue
    while n >= 1:
        if k <= x1:
            ans = s1[k - 1]
            break
        elif x1 + f[n - 1] < k <= x1 + f[n - 1] + x2:
            ans = s2[k - x1 - f[n - 1] - 1]
            break
        elif x1 + f[n - 1] + x2 + f[n - 1] < k <= x1 + f[n - 1] + x2 + f[n - 1] + 2:
            ans = s3[k - x1 - f[n - 1] - x2 - f[n - 1] - 1]
            break
        elif x1 < k <= x1 + f[n - 1]:
            k -= x1
            n -= 1
        elif x1 + f[n - 1] + x2 < k <= x1 + f[n - 1] + x2 + f[n - 1]:
            k -= x1 + f[n - 1] + x2
            n -= 1

    if n == 0:
        ans = s0[k - 1]
    rst += ans
print(rst)
