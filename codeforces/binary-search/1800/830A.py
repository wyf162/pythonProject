# -*- coding : utf-8 -*-
# @Time: 2024/6/18 22:01
# @Author: yefei.wang
# @File: 830A.py

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

n, m, p = MI()
A = LI()
B = LI()
A.sort()
B.sort()


def check(mid):
    segments = []
    for i, b in enumerate(B):
        if b <= p:
            left = max(p - mid, 1)
            right = min(10 ** 9, p + (mid - (p - b) * 2))
            segments.append((left, right))
        else:
            left = max(p - (mid - (b - p) * 2), 1)
            right = min(p + mid, 10 ** 9)
            segments.append((left, right))
    segments.sort(key=lambda x: (x[1], x[0]))
    i = 0
    j = 0
    while j < len(segments):
        if segments[j][0] <= A[i] <= segments[j][1]:
            i += 1
        j += 1
        if i == n:
            break

    return i == n


L = 0
R = 2 * 10 ** 9 + 5
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
print(ans)
