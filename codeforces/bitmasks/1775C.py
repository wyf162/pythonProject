# -*- coding : utf-8 -*-
# @Time: 2023/12/30 19:36
# @Author: yefei.wang
# @File: 1775C.py
from sys import stdin

input = lambda: stdin.readline()[:-1]


def solve():
    n, x = map(int, input().split())
    if n == x:
        print(n)
        return
    res = n
    now = n
    for i in range(62):
        if (now >> i) & 1:
            now += (1 << i)
        res &= now
        if res == x:
            print(now)
            return
    print(-1)


for _ in range(int(input())):
    solve()
