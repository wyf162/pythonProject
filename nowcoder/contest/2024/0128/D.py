# -*- coding : utf-8 -*-
# @Time: 2024/1/28 19:30
# @Author: yefei.wang
# @File: D.py
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


x, y, l, r = MI()
d = gcd(x, y)
x //= d
y //= d

a1, a2 = (l + x - 1) // x, r // x
a3, a4 = (l + y - 1) // y, r // y
left, right = max(a1, a3), min(a4, a2)
rst = right - left + 1

print(rst)
