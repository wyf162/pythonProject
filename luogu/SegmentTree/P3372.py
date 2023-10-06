# -*- coding : utf-8 -*-
# @Time: 2023/10/4 21:58
# @Author: yefei.wang
# @File: P3372.py

import sys

sys.stdin = open('./../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()
a.insert(0, 0)
ops = [LI() for _ in range(m)]

d = [0] * (4 * n + 4)
b = [0] * (4 * n + 4)


def build(s, t, p):
    # 对[s, t] 区间建立线段树，当前根的编号为p
    if s == t:
        d[p] = a[s]
        return
    m = s + ((t - s) >> 1)
    build(s, m, p * 2)
    build(m + 1, t, p * 2 + 1)
    d[p] = d[p * 2] + d[p * 2 + 1]


def getsum(l, r, s, t, p):
    # [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p为当前节点的编号
    if l <= s and t <= r:
        return d[p]
    # 当前区间为询问区间的子集时直接返回当前区间的和
    m = s + ((t - s) >> 1)
    if b[p]:
        # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值
        d[p * 2] = d[p * 2] + b[p] * (m - s + 1)
        d[p * 2 + 1] = d[p * 2 + 1] + b[p] * (t - m)
        # 将标记下传给子节点
        b[p * 2] = b[p * 2] + b[p]
        b[p * 2 + 1] = b[p * 2 + 1] + b[p]
        # 清空当前节点的标记
        b[p] = 0
    sum = 0
    if l <= m:
        sum = getsum(l, r, s, m, p * 2)
    if r > m:
        sum = sum + getsum(l, r, m + 1, t, p * 2 + 1)
    return sum


def update(l, r, c, s, t, p):
    # [l, r] 为修改区间, c 为被修改的元素的变化量, [s, t] 为当前节点包含的区间, p
    # 为当前节点的编号
    if l <= s and t <= r:
        d[p] = d[p] + (t - s + 1) * c
        b[p] = b[p] + c
        return
    # 当前区间为修改区间的子集时直接修改当前节点的值, 然后打标记, 结束修改
    m = s + ((t - s) >> 1)
    if b[p] and s != t:
        # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值
        d[p * 2] = d[p * 2] + b[p] * (m - s + 1)
        d[p * 2 + 1] = d[p * 2 + 1] + b[p] * (t - m)
        # 将标记下传给子节点
        b[p * 2] = b[p * 2] + b[p]
        b[p * 2 + 1] = b[p * 2 + 1] + b[p]
        # 清空当前节点的标记
        b[p] = 0
    if l <= m:
        update(l, r, c, s, m, p * 2)
    if r > m:
        update(l, r, c, m + 1, t, p * 2 + 1)
    d[p] = d[p * 2] + d[p * 2 + 1]


build(1, n, 1)
for op in ops:
    if op[0] == 1:
        _, x, y, k = op
        update(x, y, k, 1, n, 1)
    else:
        _, x, y = op
        rst = getsum(x, y, 1, n, 1)
        print(rst)
