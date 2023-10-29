# -*- coding : utf-8 -*-
# @Time: 2023/10/23 19:31
# @Author: yefei.wang
# @File: 2023-csps-04.py

import sys
import time
from functools import lru_cache
from types import GeneratorType

sys.setrecursionlimit(10 ** 6)


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


E5 = 10 ** 5
E9 = 10 ** 9

# sys.stdin = open('./../input.txt', 'r')
sys.stdin = open('./ins/tree1.in', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
abc = [LI() for _ in range(n)]

g = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = MI()
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

father = [0 for i in range(n)]
children = []


@bootstrap
def dfs(x, fa):
    father[x] = fa
    child = []
    for y in g[x]:
        if y != fa:
            yield dfs(y, x)
            child.append(y)
    if child:
        children.append(child)
    yield


# t1 = time.time()
dfs(0, -1)


# t2 = time.time()
# print(f"dfs cost {t2 - t1}s")


# print(father)
# print(children)

@lru_cache(None)
def get_late_start_date(mx, a, b, c):
    start, end = 1, mx
    ok = 1
    while start <= end:
        test = (start + end) // 2
        # print(test)
        if c >= 0:
            h = (2 * b + (test + mx) * c) * (mx - test + 1) // 2
        else:
            x1 = (1 - b) // c if c != 0 else -1
            if x1 < test:
                h = mx - test + 1
            elif test <= x1 < mx:
                s = b + test * c
                e = b + x1 * c
                h = mx - x1 + (s + e) * (x1 - test + 1) // 2
            else:
                h = (2 * b + (test + mx) * c) * (mx - test + 1) // 2

        if h >= a:
            ok = test
            start = test + 1
        else:
            end = test - 1
    return ok


@lru_cache(None)
def get_late_start_date_v2(mx, a, b, c):
    pass


ddl = [0] * n
l, r = n, E9
ans = E9
while l <= r:
    # t3 = time.time()
    mid = (l + r) // 2
    imp = False
    for child in children:
        fa = father[child[0]]
        ddl[fa] = get_late_start_date(mid, *abc[fa])
        if ddl[fa] < 1: imp = True; break
        ts = []
        for x in child:
            lsd = get_late_start_date(mid, *abc[x])
            if lsd < 1: imp = True; break
            ddl[x] = lsd
            ts.append(lsd)
        if imp: break
        ts.sort()
        for i, t in enumerate(ts):
            ddl[fa] = min(ddl[fa], t - i - 1)
            if ddl[fa] < 1: imp = True; break

    # t4 = time.time()
    # print(f"calculate ddl cost {t4 - t3}s")

    if imp:
        l = mid + 1
    else:
        ans = mid
        r = mid - 1

print(ans)
