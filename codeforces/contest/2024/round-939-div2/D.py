# -*- coding : utf-8 -*-
# @Time: 2024/4/13 23:20
# @Author: yefei.wang
# @File: C2.py

import sys
from itertools import accumulate
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
sys.stdin = open('../../../input.txt', 'r')
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
acc = list(accumulate(nums, initial=0))
ops = []


@bootstrap
def f(i, j):
    if j - i < 1:
        yield
    tot = acc[j] - acc[i]
    c = j - i
    if tot >= c * c:
        mx = max(nums[i:j])
        i0 = nums[i:j].index(mx)
        yield f(i, i + i0)
        yield f(i + i0 + 1, j)
    else:
        for i1 in range(i, j):
            ops.append((i, i1 + 1))
            nums[i1] = c
    yield


f(0, n)

ret1 = sum(nums)
ret2 = len(ops)
print(ret1, ret2)
for op in ops:
    print(op[0] + 1, op[1])
