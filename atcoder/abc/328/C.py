# -*- coding : utf-8 -*-
# @Time: 2023/11/11 20:14
# @Author: yefei.wang
# @File: C.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
s = input()
pre_sum = [0, 0]
for i in range(1, n):
    if s[i] == s[i-1]:
        pre_sum.append(pre_sum[-1] + 1)
    else:
        pre_sum.append(pre_sum[-1])


for _ in range(q):
    l, r = MI()
    rst = pre_sum[r] - pre_sum[l]
    print(rst)
