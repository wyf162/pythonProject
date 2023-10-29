# -*- coding : utf-8 -*-
# @Time: 2023/10/6 20:44
# @Author: yefei.wang
# @File: P1816.py

import sys

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

m, n = MI()
a = LI()
a.insert(0, 0)
queries = [LI() for _ in range(n)]

d = [0] * (4 * m + 4)


def build(s, t, p):
    # 对 [s,t] 区间建立线段树,当前根的编号为 p
    if s == t:
        d[p] = a[s]
        return
    m = s + ((t - s) >> 1)
    # 移位运算符的优先级小于加减法，所以加上括号
    # 如果写成 (s + t) >> 1 可能会超出 int 范围
    build(s, m, p * 2)
    build(m + 1, t, p * 2 + 1)
    # 递归对左右区间建树
    d[p] = min(d[p * 2], d[(p * 2) + 1])


def get_min(l, r, s, t, p):
    # [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p 为当前节点的编号
    if l <= s and t <= r:
        return d[p]  # 当前区间为询问区间的子集时直接返回当前区间的和
    m = s + ((t - s) >> 1)
    mi = 0x3f3f3f3f
    if l <= m:
        mi = min(mi, get_min(l, r, s, m, p * 2))
    # 如果左儿子代表的区间 [s, m] 与询问区间有交集, 则递归查询左儿子
    if r > m:
        mi = min(mi, get_min(l, r, m + 1, t, p * 2 + 1))
    # 如果右儿子代表的区间 [m + 1, t] 与询问区间有交集, 则递归查询右儿子
    return mi


build(1, m, 1)

for l, r in queries:
    rst = get_min(l, r, 1, m, 1)
    print(rst, end=' ')
print()
