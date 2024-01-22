# -*- coding : utf-8 -*-
# @Time: 2024/1/19 19:50
# @Author: yefei.wang
# @File: D.py

import sys
from collections import deque

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

n, m = MI()
mtx = [[0] * m for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == '*':
            mtx[i][j] = 1

rst = 0
for i in range(n):
    for j in range(m):
        if mtx[i][j] == 1:
            continue
        dots = []
        q = deque()
        q.append((i, j))
        mtx[i][j] = 1
        while q:
            x, y = q.popleft()
            dots.append((x, y))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and mtx[nx][ny] == 0:
                    q.append((nx, ny))
                    mtx[nx][ny] = 1
        ans = True
        dots.sort()
        left, down = dots[0]
        right, up = dots[-1]
        for x, y in dots:
            if left <= x <= right and down <= y <= up:
                continue
            else:
                ans = False
                break
        if ans and (right-left+1) * (up-down+1) == len(dots):
            rst += 1
print(rst)

