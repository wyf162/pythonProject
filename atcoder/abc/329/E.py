# -*- coding : utf-8 -*-
# @Time: 2023/11/18 20:17
# @Author: yefei.wang
# @File: E.py

import sys
from collections import deque

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


def check(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(m):
        if s1[i] == '#' or s1[i] == s2[i]:
            continue
        else:
            return False
    return True


n, m = MI()
s = list(input())
t = list(input())

q = deque()
unvis = [True] * n

for i in range(n):
    if check(s[i:i + m], t):
        q.append(i)

while q:
    x = q.popleft()
    unvis[x] = False
    for j in range(x, x + m):
        s[j] = '#'
    for y in range(max(x - 5, 0), min(x + 5, n), 1):
        if unvis[y] and check(s[y:y + m], t):
            q.append(y)

if all(c == '#' for c in s):
    print('Yes')
else:
    print('No')
