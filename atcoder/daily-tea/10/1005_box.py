# -*- coding : utf-8 -*-
# @Time: 2023/10/5 23:28
# @Author: yefei.wang
# @File: 1005_box.py

import sys

sys.stdin = open('./../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
queries = [LI() for _ in range(q)]

box = [i for i in range(n + 1)]
ball = [i for i in range(n + 1)]
fa = [i for i in range(n + 1)]


def find(x: int) -> int:
    cur = x
    while x != fa[x]:
        x = fa[x]
    while fa[cur] != x:
        fa[cur], cur = x, fa[cur]
    return x


for qry in queries:
    if qry[0] == 1:
        x, y = box[qry[1]], box[qry[2]]
        if y == -1:
            continue
        if x == -1:
            box[qry[1]] = y
            ball[y] = qry[1]
        else:
            fa[y] = x
        box[qry[2]] = -1
    elif qry[0] == 2:
        n += 1
        fa.append(n)
        ball.append(n)
        x = box[qry[1]]
        if x == -1:
            ball[-1] = qry[1]
            box[qry[1]] = n
        else:
            fa[-1] = x
    else:
        print(ball[find(qry[1])])
