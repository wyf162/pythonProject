# -*- coding : utf-8 -*-
# @Time: 2024/3/9 20:42
# @Author: yefei.wang
# @File: E.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


class Node:
    __slots__ = ['val', 'pre', 'nex']

    def __init__(self, x):
        self.val = x
        self.pre = None
        self.nex = None


n = I()
nums = LI()
q = I()
ops = [LI() for _ in range(q)]

hst = dict()
dummy = Node(0)
hst[0] = dummy
cur = dummy
for x in nums:
    node = Node(x)
    hst[x] = node
    cur.nex = node
    node.pre = cur
    cur = cur.nex

for op in ops:
    if op[0] == 1:
        _, x, y = op
        node = Node(y)
        hst[y] = node
        cur = hst[x]
        if cur.nex:
            cur.nex.pre = node
        node.nex = cur.nex
        node.pre = cur
        cur.nex = node
    elif op[0] == 2:
        _, x = op
        cur = hst[x]
        if cur.nex:
            cur.nex.pre = cur.pre
        cur.pre.nex = cur.nex
        del hst[x]

rst = []
cur = dummy.nex
while cur:
    rst.append(cur.val)
    cur = cur.nex
print(*rst)
