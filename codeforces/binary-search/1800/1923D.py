# -*- coding: utf-8 -*-
# @Time: 2024/3/15 15:21
# @Author: yfwang
# @File: 1923D.py
# https://codeforces.com/problemset/problem/1923/D


from sys import stdin, stdout

input = stdin.readline


def bin_search(L, R, func, x):
    while R - L > 0:
        mid = (L + R + x) // 2
        if func(mid):
            L = mid + (1 - x)
        else:
            R = mid - x
    return L * x - (1 - x) if func(L) else L * (1 - x) - x


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)

    psum = [0]
    e = [0]
    for i in range(1, n + 1):
        psum.append(psum[-1] + a[i])
    for i in range(1, n + 1):
        e.append(e[-1] + (a[i - 1] != a[i]))

    for i in range(1, n + 1):
        m1 = bin_search(L=1, R=i, func=lambda mid: (psum[i - 1] - psum[mid - 1]) > a[i], x=1)
        if -1 != m1 != i - 1 and e[m1] == e[i - 1]:
            m1 = bin_search(L=1, R=m1, func=lambda mid: e[mid] < e[m1], x=1)

        m2 = bin_search(L=i, R=n, func=lambda mid: (psum[mid] - psum[i]) <= a[i], x=0)
        if -1 != m2 != i + 1 and e[m2] == e[i + 1]:
            m2 = bin_search(L=m2, R=n, func=lambda mid: e[mid] <= e[m2], x=0)

        if m1 != -1 != m2:
            stdout.write(str(min(i - m1, m2 - i)))
        else:
            stdout.write(str(-1 if m1 == m2 == -1 else abs(i - max(m1, m2))))
        stdout.write(' ')
    stdout.write('\n')
