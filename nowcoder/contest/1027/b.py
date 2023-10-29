# -*- coding : utf-8 -*-
# @Time: 2023/10/27 19:33
# @Author: yefei.wang
# @File: b.py

from collections import Counter

# sys.stdin = open('./../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, k = MI()
a = LI()
cnt = Counter(a)

mx = 0

for _, v in cnt.items():
    mx = max(mx, v - max(0, k - n + v))
print(mx)
