# -*- coding : utf-8 -*-
# @Time: 2023/10/7 12:52
# @Author: yefei.wang
# @File: P2345.py
import sys

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = [LI() for _ in range(n)]
a.sort()
# v, x
ans = 0
c = [[0] * 2 for _ in range(n)]


def merge_sort(b, e):
    # begin end
    if b >= e:
        return
    mid = (b + e) // 2
    merge_sort(b, mid)
    merge_sort(mid + 1, e)
    s1, s2 = 0, 0
    for i in range(b, mid + 1):
        s1 += a[i][1]

    i, k = b, b
    for j in range(mid + 1, e + 1, 1):
        while j <= e and i <= mid and a[i][1] <= a[j][1]:
            s1 -= a[i][1]
            s2 += a[i][1]
            i += 1

        global ans
        ans += a[j][0] * ((a[j][1] * (i - b) - s2) + s1 - (a[j][1] * (mid + 1 - i)))

    i, j = b, mid + 1
    k = b
    while i <= mid and j <= e:
        if a[i][1] <= a[j][1]:
            c[k][0], c[k][1] = a[i]
            k += 1
            i += 1
        else:
            c[k][0], c[k][1] = a[j]
            k += 1
            j += 1
    while i <= mid:
        c[k][0], c[k][1] = a[i]
        k += 1
        i += 1
    while j <= e:
        c[k][0], c[k][1] = a[j]
        k += 1
        j += 1
    for i in range(b, e + 1):
        a[i][0], a[i][1] = c[i]


merge_sort(0, n - 1)

print(ans)
