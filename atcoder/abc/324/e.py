# -*- coding : utf-8 -*-
# @Time: 2023/10/14 20:48
# @Author: yefei.wang
# @File: e.py
import sys
import bisect

sys.stdin = open('../../input.txt', 'r')

n, t = input().split()
n = int(n)
m = len(t)

ss = [input() for i in range(n)]
prefix = []
suffix = []


def calculate(s):
    i, j = 0, 0
    while j < len(s) and i < m:
        if t[i] == s[j]:
            i += 1
        j += 1
    pre = i

    i, j = m - 1, len(s) - 1
    while j >= 0 and i >= 0:
        if t[i] == s[j]:
            i -= 1
        j -= 1
    suf = m - i - 1
    return pre, suf


for s in ss:
    pre, suf = calculate(s)
    prefix.append(pre)
    suffix.append(suf)

prefix.sort()
suffix.sort()

ans = 0
for pre in prefix:
    i = bisect.bisect_left(suffix, m-pre)
    ans += n - i
print(ans)
