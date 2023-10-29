# -*- coding : utf-8 -*-
# @Time: 2023/10/14 20:14
# @Author: yefei.wang
# @File: c.py
import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


def check(s):
    if len(s) == m:
        d = 0
        for i in range(m):
            d += (s[i] != t[i])
        return d <= 1
    elif len(s) == m - 1:
        i = 0
        j = 0
        d = 0
        while i < len(s) and j < m:
            if s[i] != t[j]:
                d += 1
                j += 1
            else:
                i += 1
                j += 1

        return d <= 1
    elif len(s) == m + 1:
        i = 0
        j = 0
        d = 0
        while i < len(s) and j < m:
            if s[i] != t[j]:
                d += 1
                i += 1
            else:
                i += 1
                j += 1

        return d <= 1
    else:
        return False


n, t = input().split()
n = int(n)
ss = [input() for _ in range(n)]
m = len(t)
ans = []
for i in range(n):
    if check(ss[i]):
        ans.append(i + 1)

print(len(ans))
print(' '.join(map(str, ans)))
