# -*- coding : utf-8 -*-
# @Time: 2023/9/23 21:09
# @Author: yefei.wang
# @File: d.py
import bisect
import sys
sys.stdin = open('../../input.txt', 'r')

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
pa = [0]
for i in range(n):
    pa.append(pa[-1] + a[i])

pb = [0]
for i in range(m):
    pb.append(pb[-1] + b[i])

s = 0
for i in range(n):
    x = a[i]
    y = p - a[i]
    idx = bisect.bisect_left(b, y)
    s += x * idx + pb[idx] + p * (m - idx)

print(s)

