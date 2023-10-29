# -*- coding : utf-8 -*-
# @Time: 2023/10/28 15:36
# @Author: yefei.wang
# @File: f.py

import sys
from collections import Counter

sys.stdin = open('./../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, k = MI()
a = LI()
b = LI()
a = [x ^ k for x in a]

cnt_a = Counter(a)
cnt_b = Counter(b)

in_b = 0
not_in_b = 0
for k, v in a:
    if k in cnt_b:
        in_b += v
    else:
        not_in_b += v

in_a = 0
not_in_a = 0
for k, v in cnt_b.items():
    if k in cnt_a:
        in_a += 1
        not_in_a += v - 1
    else:
        not_in_a += v

if in_b > 1 and not_in_a + in_a > not_in_b + 1:
    print('Bob')
else:
    print('Alice')
