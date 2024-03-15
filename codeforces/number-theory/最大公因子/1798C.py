# https://codeforces.com/problemset/problem/1798/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = [LI() for _ in range(n)]

    cnt = 1
    x, y = 0, 1
    for i in range(n):
        a, b = nums[i]
        x = gcd(a * b, x)
        y = lcm(b, y)
        if x % y == 0:
            continue
        else:
            cnt += 1
            x = a * b
            y = b
    print(cnt)
