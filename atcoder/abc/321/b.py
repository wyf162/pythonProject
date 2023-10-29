# -*- coding : utf-8 -*-
# @Time: 2023/9/23 20:28
# @Author: yefei.wang
# @File: c.py
import sys
sys.stdin = open('../../input.txt', 'r')
n, x = map(int, input().split())
a = list(map(int, input().split()))

for score in range(0, 101):
    b = a + [score]
    b.sort()
    if sum(b[1:-1]) >= x:
        print(score)
        exit(0)
print(-1)
exit(0)
