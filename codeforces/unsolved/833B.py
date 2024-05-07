# -*- coding : utf-8 -*-
# @Time: 2024/5/6 23:10
# @Author: yefei.wang
# @File: 833B.py

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
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, K = MI()
A = LI()
cache = dict()


@bootstrap
def dfs(i, k):
    if (i, k) in cache:
        yield cache[(i, k)]
    if k == 1:
        yield len(set(A[:i + 1]))
    rst = 0
    s = set()
    s.add(A[i])
    for j in range(i - 1, k - 2, -1):
        rst = max(rst, next(dfs(j, k - 1)) + len(s))
        s.add(A[j])
    cache[(i, k)] = rst
    yield rst


ans = dfs(N - 1, K)
print(ans)
