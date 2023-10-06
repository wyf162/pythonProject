# -*- coding : utf-8 -*-
# @Time: 2023/10/4 18:23
# @Author: yefei.wang
# @File: P1083.py


import sys

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()
dd = [0]*m
ss = [0]*m
tt = [0]*m
for i in range(m):
    d, s, t = MI()
    dd[i] = d
    ss[i] = s
    tt[i] = t
diff = [0] * (n + 5)


def check(mid):
    for i in range(n + 5):
        diff[i] = 0
    for i in range(mid):
        d, s, t = dd[i], ss[i], tt[i]
        diff[s - 1] += d
        diff[t] -= d
    x0 = 0
    for i in range(n):
        x1 = x0 + diff[i]
        if x1 > a[i]:
            return False
        x0 = x1
    return True


ans = 0
l, r = 1, m
while l <= r:
    mid = (l + r) >> 1
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

if ans + 1 <= m:
    print(-1)
    print(ans + 1)
else:
    print(0)
