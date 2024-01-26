# -*- coding : utf-8 -*-
# @Time: 2024/1/26 19:38
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


def lcm(a, b):
    return a * b // gcd(a, b)


tcn = I()
for _tcn_ in range(tcn):
    a, b = MI()
    st = [a, b]
    x = gcd(a, b)
    y = lcm(a, b)
    if y in st:
        print(0)
        continue

    ops = [[1, a, b], [1, a, b]]
    st.append(x)
    st.append(x)
    fib = [x, x]
    while fib[-1] + fib[-2] <= y:
        ops.append([2, fib[-1], fib[-2]])
        fib.append(fib[-1] + fib[-2])

    i = len(fib) - 1
    tot = fib[i]
    while tot < y:
        # print(tot, y)
        if tot + fib[i] <= y:
            ops.append([2, tot, fib[i]])
            tot += fib[i]
        else:
            i -= 1
    # print(len(ops))
    # for op in ops:
    #     print(*op)

    print(y, tot, ops[-1][-1] + ops[-1][-2], y == tot)
