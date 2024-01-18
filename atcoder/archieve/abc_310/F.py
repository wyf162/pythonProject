import sys
from math import gcd

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353


def sim(numerator, denominator):
    k = gcd(numerator, denominator)
    return numerator // k, denominator // k


def add(x1, y1, x2, y2):
    x = x1 * y2 + x2 * y1
    y = y1 * y2
    return sim(x, y)


def mul(x1, y1, x2, y2):
    x = x1 * x2
    y = y1 * y2
    return sim(x, y)


n = I()
a = LI()

N = 10
dp = [(0, 1)] * (1 << N)
ans = (0, 1)

for i in range(n):
    ndp = [(0, 1)] * (1 << N)
    for x in range(1, a[i] + 1):
        if x > 10:
            break
        elif x == 10:
            ans = add(*ans, 1, a[i])
        else:
            for s in range(1 << N):
                if s >> (10 - x):
                    ans = add(*ans, 1, a[i])

