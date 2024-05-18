# -*- coding : utf-8 -*-
# @Time: 2024/5/18 20:06
# @Author: yefei.wang
# @File: C.py

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
cards = [LI() + [i] for i in range(n)]

cards.sort(key=lambda x: (x[0], -x[1]))

rets = []
mi = 10**9+1
for i in range(n - 1, -1, -1):
    if cards[i][1] < mi:
        rets.append(cards[i][2]+1)
        mi = cards[i][1]
    else:
        continue

print(len(rets))
rets.sort()
print(*rets)
