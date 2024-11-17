
from typing import List
import bisect


class SegmentTree:
    def __init__(self, nums: List[int], func):
        n = len(nums)
        self.n = n
        self.seg = [0] * (n * 4)
        self.func = func
        self.build(nums, 0, 0, n - 1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = self.func(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def update(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.update(index, val, node * 2 + 1, s, m)
        else:
            self.update(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = self.func(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def query(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.query(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.query(left, right, node * 2 + 2, m + 1, e)
        return self.func(self.query(left, m, node * 2 + 1, s, m), self.query(m + 1, right, node * 2 + 2, m + 1, e))


class Solution:
    def maxArea(self, height: List[int]) -> int:
        hi = [(h, i) for i, h in enumerate(height)]
        hi.sort()
        hghs = []
        idxs = []
        for h, i in hi:
            hghs.append(h)
            idxs.append(i)
        n = len(height)
        segmin = SegmentTree(idxs, min)
        segmax = SegmentTree(idxs, max)
        ans = 0
        for i, h in enumerate(height):
            i1 = bisect.bisect_left(hghs, h)
            mi = segmin.query(i1, n-1, 0, 0, n-1)
            mx = segmax.query(i1, n-1, 0, 0, n-1)
            tmp = h * max(abs(mi - i), abs(mx - i))
            ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ret = sol.maxArea(height)
    print(ret)
