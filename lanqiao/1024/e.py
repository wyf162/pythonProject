# -*- coding : utf-8 -*-
# @Time: 2023/10/24 21:08
# @Author: yefei.wang
# @File: e.py
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


# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
g = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, w = MI()
    u -= 1
    v -= 1
    g[u].append([v, w])
    g[v].append([u, w])




