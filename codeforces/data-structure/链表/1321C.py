# -*- coding: utf-8 -*-
# @Time: 2024/6/28 13:36
# @Author: yfwang
# @File: 1321C.py

import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
sys.stdout = open('../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


class ListNode:

    def __init__(self, val=None, idx=None):
        self.val = val
        self.idx = idx
        self.pre = None
        self.nex = None


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = input()
    cur = ListNode(26)
    dummy = cur
    h = []
    vis = [0] * n
    for i, c in enumerate(s):
        x = ord(c) - ord('a')
        node = ListNode(x, i)
        cur.nex = node
        node.pre = cur
        cur = node

    node = ListNode(26)
    cur.nex = node
    node.pre = cur

    cur = dummy.nex
    for i in range(n):
        if cur.pre.val == cur.val - 1 or cur.nex.val == cur.val - 1:
            heappush(h, (-cur.val, cur.idx, cur))
            vis[i] = 1
        cur = cur.nex

    ans = 0
    while h:
        c, _, node = heappop(h)
        if node.pre.val == node.val - 1 or node.nex.val == node.val - 1:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            cur = node.pre
            if cur.idx is not None and vis[cur.idx] == 0:
                if cur.pre.val == cur.val - 1 or cur.nex.val == cur.val - 1:
                    heappush(h, (-cur.val, cur.idx, cur))
                    vis[cur.idx] = 1
            cur = node.nex
            if cur.idx is not None and vis[cur.idx] == 0:
                if cur.pre.val == cur.val - 1 or cur.nex.val == cur.val - 1:
                    heappush(h, (-cur.val, cur.idx, cur))
                    vis[cur.idx] = 1

            ans += 1
    print(ans)
