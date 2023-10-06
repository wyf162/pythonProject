# -*- coding : utf-8 -*-
# @Time: 2023/10/4 15:05
# @Author: yefei.wang
# @File: c.py

import sys

sys.stdin = open('./../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
mod = 10 ** 9 + 7
ans = 0
cnt = 0
for i in range(n):
    if a[i] == 5:
        cnt += 1
        if i - cnt + 1 > 0:
            ans += cnt * (i - cnt + 1)
        ans += cnt * (cnt + 1) // 2
        ans %= mod
    else:
        cnt = 0
print(ans)
