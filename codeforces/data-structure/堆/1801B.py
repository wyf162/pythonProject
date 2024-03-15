# -*- coding: utf-8 -*-
# @Time: 2024/3/15 11:09
# @Author: yfwang
# @File: 1801B.py
# https://codeforces.com/problemset/problem/1801/B

import sys
import sys
import heapq

sys.stdin = open('../../input.txt', 'r')

input = sys.stdin.buffer.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort(key=lambda x: x[0])
    suf = [arr[-1][1]]
    for i in range(n - 2, -1, -1):
        suf.append(max(suf[-1], arr[i][1]))
    suf.reverse()
    suf.append(0)
    mx, mn = [float('inf')], [float('inf')]
    diff = float('inf')

    for i in range(n):
        if i > 0:
            if arr[i - 1][-1] < arr[i][0]:
                heapq.heappush(mx, -arr[i - 1][-1])
            else:
                heapq.heappush(mn, arr[i - 1][-1])
        x = heapq.heappop(mn)
        while x < arr[i][0]:
            heapq.heappush(mx, -x)
            x = heapq.heappop(mn)
        heapq.heappush(mn, x)
        if abs(mx[0]) >= suf[i + 1]:
            diff = min(diff, abs(arr[i][0] - abs(mx[0])))
        if abs(mn[0]) >= suf[i + 1]:
            diff = min(diff, abs(arr[i][0] - abs(mn[0])))
        if i == n - 1:
            suf[i + 1] = float('inf')
        diff = min(diff, abs(arr[i][0] - suf[i + 1]))
    print(diff)
