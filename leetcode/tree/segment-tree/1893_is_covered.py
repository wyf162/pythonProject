# _*_ coding: utf-8 _*_
# @Time : 2022/05/15 9:39 PM 
# @Author : yefe
# @File : 1893_is_covered
from typing import List


class Node:
    def __init__(self, l, r, cnt):
        self.l = l
        self.r = r
        self.cnt = cnt


class Solution:
    def isCovered(self, ranges: List[List[int]], l: int, r: int) -> bool:
        def pushup(u):
            tr[u].cnt = tr[u << 1].cnt + tr[u << 1 | 1].cnt

        def build(u, l, r):
            tr[u] = Node(l, r, 0)
            if l != r:
                tr[u] = Node(l, r, 0)
                mid = l + r >> 1
                build(u << 1, l, mid)
                build(u << 1 | 1, mid + 1, r)
                pushup(u)

        # 从 tr 数组的下标 u 开始，在数值 x 的位置进行标记
        def update(u, x):
            if tr[u].l == x and tr[u].r == x:
                tr[u].cnt = 1
            else:
                mid = tr[u].l + tr[u].r >> 1
                if x <= mid:
                    update(u << 1, x)
                else:
                    update(u << 1 | 1, x)
                pushup(u)

        # 从 tr 数组的下标 u 开始，查询 [l,r] 范围内有多少个数值被标记
        def query(u, l, r):
            if l <= tr[u].l and tr[u].r <= r:
                return tr[u].cnt
            mid = tr[u].l + tr[u].r >> 1
            ans = 0
            if l <= mid:
                ans += query(u << 1, l, r)
            if r > mid:
                ans += query(u << 1 | 1, l, r)
            return ans

        N = 55
        tr = [None] * N * 4
        build(1, 1, N)
        for a, b in ranges:
            for i in range(a, b + 1):
                update(1, i)
        tot = r - l + 1
        cnt = query(1, l, r)
        return tot == cnt



