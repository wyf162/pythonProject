# -*- coding : utf-8 -*-
# @Time: 2023/10/10 21:17
# @Author: yefei.wang
# @File: 1365D.py

import sys
from collections import Counter, deque

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    maze = [list(input()) for _ in range(n)]
    ans = True
    for i in range(n):
        for j in range(m):
            if maze[i][j] != 'B':
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maze[nx][ny] == '.':
                    maze[nx][ny] = 'W'
                elif maze[nx][ny] == 'G':
                    ans = False
                    break
    if ans is False:
        print('No')
        continue

    good_count = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'G':
                good_count += 1
    if maze[n - 1][m - 1] == 'W':
        if good_count == 0:
            print('Yes')
            continue
        else:
            print('No')
            continue

    vis = [[False for j in range(m)] for i in range(n)]
    q = deque()
    q.append((n - 1, m - 1))
    vis[n - 1][m - 1] = True
    while q:
        i, j = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maze[nx][ny] == '.' and not vis[nx][ny]:
                q.append((nx, ny))
                vis[nx][ny] = True
            if maze[nx][ny] == 'G' and not vis[nx][ny]:
                good_count -= 1
                q.append((nx, ny))
                vis[nx][ny] = True
    if good_count:
        ans = False

    if ans is False:
        print('No')
    else:
        print('Yes')
