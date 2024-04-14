# -*- coding : utf-8 -*-
# @Time: 2024/4/14 17:17
# @Author: yefei.wang
# @File: 1956D.py
# mex

import sys
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


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

n = I()
nums = LI()

dp = [0] * n
for i in range(n):
    dp[i] = nums[i]

mxdp = [0] * (n + 1)
md = [0] * (n + 1)

if dp[0] < 1:
    dp[0] = 1
    md[1] |= 1 << 0

mxdp[1] = dp[0]
for i in range(1, n):
    for c in range(i + 2):
        if c == 0:
            if nums[i] == 0:
                md[i + 1] = md[i - c] | (1 << i)
                mxdp[i + 1] = mxdp[i - c] + 1
                dp[i] = 1
            elif mxdp[i + 1 - c] + nums[i] > mxdp[i + 1]:
                md[i + 1] = md[i - c]
                mxdp[i + 1] = mxdp[i - c] + nums[i]

        else:
            if mxdp[i + 1 - c] + c * c > mxdp[i + 1]:
                mxdp[i + 1] = mxdp[i + 1 - c] + c * c
                dp[i + 1 - c:i + 1] = [c] * c
                md[i + 1] = md[i + 1 - c] | ((1 << (i + 1)) - (1 << (i - c + 1)))

# print(dp)
# print(mxdp)

ops = []


@bootstrap
def f1(start, end):
    if end - start + 1 == 1:
        ops.append((start, start))
        yield

    yield f1(start, end - 1)
    for i in range(end - 2, start - 1, -1):
        ops.append((start, i))
        yield f1(start, i)
    ops.append((start, end))
    yield


# print(md)
# for x in md[1:]:
#     state = list(bin(x)[2:])
#     state.reverse()
#     print(state)

i = 0
state = list(bin(md[-1])[2:])
state.reverse()
# print(state)
n = len(state)
while i < n:
    while i < n and state[i] == '0':
        i += 1
    j = i
    while j < n and state[j] == '1':
        j += 1
    if i < n:
        for i1 in range(i, j):
            if nums[i1] != 0:
                nums[i1] = 0
                ops.append((i1, i1))
        f1(i, j - 1)
    i = j

print(sum(dp), len(ops))
for op in ops:
    print(op[0] + 1, op[1] + 1)
