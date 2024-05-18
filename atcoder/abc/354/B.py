# -*- coding : utf-8 -*-
# @Time: 2024/5/18 20:02
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
users = []
tot = 0
for i in range(n):
    s, c = input().split()
    c = int(c)
    users.append((s, c))
    tot += c

idx = tot % n
users.sort()
print(users[idx][0])
