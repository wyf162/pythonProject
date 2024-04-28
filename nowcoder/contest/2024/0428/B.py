# -*- coding : utf-8 -*-
# @Time: 2024/4/28 19:02
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, h = MI()
s2 = input()
s1 = input()

x = 0
y = 0
for i in range(n):
    if s1[i] == '*' and s2[i] == '*':
        x += 2
    elif s1[i] == '*' and s2[i] == '#':
        x += 1
    elif s1[i] == '#' and s2[i] == '*':
        y += 1

input()
s1 = input()
s2 = input()

for i in range(n):
    if s1[i] == '*' and s2[i] == '*':
        x += 2
    elif s1[i] == '*' and s2[i] == '#':
        x += 1
    elif s1[i] == '#' and s2[i] == '*':
        y += 1

if h <= x:
    ans = h
else:
    ans = x
    h -= x
    if y * 2 <= h:
        ans += y
    else:
        ans += h // 2
print(ans)
