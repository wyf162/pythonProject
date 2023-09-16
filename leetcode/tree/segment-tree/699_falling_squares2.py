# _*_ coding: utf-8 _*_
# @Time : 2022/05/26 10:28 PM 
# @Author : yefe
# @File : 699_falling_squares2
from typing import List


class SegNode:
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.max_ = 0
        self.lazy_max = 0
        self.left = None
        self.right = None


class Solution:
    def get_left(self, rt: SegNode) -> SegNode:
        if rt.left == None:
            rt.left = SegNode(rt.l, (rt.l + rt.r) // 2)
        return rt.left

    def get_right(self, rt: SegNode) -> SegNode:
        if rt.right == None:
            rt.right = SegNode((rt.l + rt.r) // 2 + 1, rt.r)
        return rt.right

    def push_up(self, rt: SegNode) -> None:
        ll = self.get_left(rt)
        rr = self.get_right(rt)
        rt.max_ = max(ll.max_, rr.max_)

    def push_down(self, rt: SegNode) -> None:
        if rt.lazy_max != 0:
            v = rt.lazy_max
            ll = self.get_left(rt)
            rr = self.get_right(rt)

            ll.lazy_max = v
            rr.lazy_max = v
            ll.max_ = max(ll.max_, v)
            rr.max_ = max(rr.max_, v)

            self.push_up(rt)
            rt.lazy_max = 0

    def update(self, rt: SegNode, ul: int, ur: int, val: int) -> None:
        if ul <= rt.l and rt.r <= ur:
            rt.max_ = val
            rt.lazy_max = val
            return
        mid = (rt.l + rt.r) // 2
        ll = self.get_left(rt)
        rr = self.get_right(rt)

        self.push_down(rt)
        if ur <= mid:
            self.update(ll, ul, ur, val)
        elif mid + 1 <= ul:
            self.update(rr, ul, ur, val)
        else:
            self.update(ll, ul, ur, val)
            self.update(rr, ul, ur, val)
        self.push_up(rt)

    def query(self, rt: SegNode, ql: int, qr: int) -> int:
        if ql <= rt.l and rt.r <= qr:
            return rt.max_

        mid = (rt.l + rt.r) // 2
        ll = self.get_left(rt)
        rr = self.get_right(rt)
        self.push_down(rt)

        if qr <= mid:
            return self.query(ll, ql, qr)
        elif mid + 1 <= ql:
            return self.query(rr, ql, qr)
        return max(self.query(ll, ql, qr), self.query(rr, ql, qr))

    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        INF = 10 ** 9
        root = SegNode(0, INF)

        res = []
        for l, Len in positions:
            r = l + Len - 1
            cur_h = self.query(root, l, r)
            self.update(root, l, r, cur_h + Len)

            cur = root.max_
            res.append(cur)

        return res


if __name__ == '__main__':
    sol = Solution()
    # positions = [[1, 2], [2, 3], [6, 1]]
    positions = [[9, 7], [1, 9], [3, 1]]
    ret = sol.fallingSquares(positions)
    print(ret)
