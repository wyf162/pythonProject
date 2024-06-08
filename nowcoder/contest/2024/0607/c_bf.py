# -*- coding : utf-8 -*-
# @Time: 2024/6/7 20:11
# @Author: yefei.wang
# @File: c_bf.py
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
sys.stdout = open('../../../jury.txt', 'w')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353

n = I()
A = LI()
m = I()
queries = [LI() for i in range(m)]

for val, mi, mx in queries:
    ans = False
    for i in range(n - mi + 1):
        if min(A[i:i + mi]) >= val:
            ans = True
            break
    YN(ans)
