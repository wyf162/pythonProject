# -*- coding: utf-8 -*-
# @Time: 2024/7/8 11:02
# @Author: yfwang
# @File: 1585D.py
# 逆序对

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    c = [0] * n


    def merge_sort(b, e):
        ret = 0
        if b == e:
            return ret
        mid = (b + e) // 2
        ret += merge_sort(b, mid)
        ret += merge_sort(mid + 1, e)
        i, j = b, mid + 1
        k = b
        while i <= mid and j <= e:
            if a[i] < a[j]:
                c[k] = a[i]
                k += 1
                i += 1
            elif a[i] > a[j]:
                c[k] = a[j]
                k += 1
                j += 1
                ret += mid - i + 1
            else:
                c[k] = a[i]
                k += 1
                j += 1

        while i <= mid:
            c[k] = a[i]
            k += 1
            i += 1
        while j <= e:
            c[k] = a[j]
            k += 1
            j += 1
        for i in range(b, e + 1):
            a[i] = c[i]
        return ret


    ans = merge_sort(0, n - 1)
    ans = True if ans % 2 == 0 else False
    for i in range(n):
        if c[i] == c[i - 1]:
            ans = True
    YN(ans)
