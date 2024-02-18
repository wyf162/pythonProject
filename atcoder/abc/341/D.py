# -*- coding : utf-8 -*-
# @Time: 2024/2/17 20:17
# @Author: yefei.wang
# @File: D.py
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

sys.stdin = open('./../../input.txt', 'r')
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


def lcm(a, b):
    return a * b // gcd(a, b)


n, m, k = MI()


def check(v):
    a1 = v // n
    b1 = v // (lcm(n, m))
    a2 = v // m
    return a1 + a2 - b1 * 2


L, R = 1, n * m * k * k
rst = L
while L <= R:
    mid = (L + R) // 2
    c = check(mid)
    if c == k:
        rst = mid
    if c < k:
        L = mid + 1
    elif c >= k:
        R = mid - 1

print(rst)
