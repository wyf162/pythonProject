# -*- coding : utf-8 -*-
# @Time: 2024/2/17 20:07
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

h, w, n = MI()
t = input()
grid = [list(input()) for _ in range(h)]


def check(i, j):
    ci, cj = i, j
    if grid[ci][cj] == '#':
        return False
    for c in t:
        if c == 'L':
            cj -= 1
        if c == 'R':
            cj += 1
        if c == 'U':
            ci -= 1
        if c == 'D':
            ci += 1
        if grid[ci][cj] == '#':
            return False
    return True


ans = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if check(i, j):
            ans += 1

print(ans)
