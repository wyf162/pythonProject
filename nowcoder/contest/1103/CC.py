# -*- coding : utf-8 -*-
# @Time: 2023/11/5 22:20
# @Author: yefei.wang
# @File: CC.py

import sys

sys.stdin = open('./../../input.txt', 'r')
sys.stdout = open('./../../jury.txt', 'w')

t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    if k % 2 == 0:
        a = (n + m * 2) // k
    else:
        a = min(n, (n + m * 2) // k)
    b = n + 2 * m - a * k
    girl = min(m, b // 2)
    print(girl + (b - girl * 2))
