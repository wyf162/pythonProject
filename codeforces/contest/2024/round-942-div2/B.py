# -*- coding : utf-8 -*-
# @Time: 2024/4/30 22:43
# @Author: yefei.wang
# @File: B.py

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
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

hst = dict()


@bootstrap
def dfs(ss):
    if ss in ['U', 'UD', 'DU']:
        yield True
    elif ss in ['D', 'UU', 'DD']:
        yield False
    for i in range(len(ss)):
        tt = ss[i:] + ss[:i]
        if tt in hst:
            yield hst[tt]

    ans = False
    for i, c in enumerate(ss):
        if c == 'U':
            t = ss[i + 1:] + ss[:i]
            tt = ''
            if t[0] == 'U':
                tt += 'D'
            else:
                tt += 'U'
            tt += t[1:-1]
            if t[-1] == 'U':
                tt += 'D'
            else:
                tt += 'U'
            ans = ans or (not next(dfs(t)))
    hst[ss] = ans
    yield ans


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = input()
    ret = dfs(nums)
    YN(ret)
