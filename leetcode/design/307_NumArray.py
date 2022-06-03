# _*_ coding: utf-8 _*_
# @Time : 2022/05/29 11:52 PM 
# @Author : yefe
# @File : 307_NumArray
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.seg = [0] * (n * 4)
        self.build(nums, 0, 0, n - 1)

    def build(self, nums: List[int], o: int, l: int, r: int):
        if l == r:
            self.seg[o] = nums[l]
            return
        m = l + (r - l) // 2
        self.build(nums, o * 2 + 1, l, m)
        self.build(nums, o * 2 + 2, m + 1, r)
        self.seg[o] = self.seg[o * 2 + 1] + self.seg[o * 2 + 2]

    def change(self, index: int, val: int, o: int, l: int, r: int):
        if l == r:
            self.seg[o] = val
            return
        m = l + (r - l) // 2
        if index <= m:
            self.change(index, val, o * 2 + 1, l, m)
        else:
            self.change(index, val, o * 2 + 2, m + 1, r)
        self.seg[o] = self.seg[o * 2 + 1] + self.seg[o * 2 + 2]

    def range(self, L: int, R: int, o: int, l: int, r: int) -> int:
        if L <= l and r <= R:
            return self.seg[o]
        m = l + (r - l) // 2
        if L <= m:
            return self.range(L, R, o * 2 + 1, l, m)
        if R > m:
            return self.range(L, R, o * 2 + 2, m + 1, r)
        return self.range(L, R, o * 2 + 1, l, m) + self.range(L, R, o * 2 + 2, m + 1, r)

    def update(self, index: int, val: int) -> None:
        self.change(index, val, 0, 0, self.n - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.range(left, right, 0, 0, self.n - 1)


if __name__ == '__main__':
    # cmds = ["NumArray", "sumRange", "update", "sumRange"]
    # parms = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]

    # cmds = ["NumArray", "update", "sumRange", "sumRange", "update", "sumRange"]
    # parms = [[[9, -8]], [0, 3], [1, 1], [0, 1], [1, -3], [0, 1]]

    cmds = ["NumArray", "sumRange", "sumRange", "sumRange", "update", "update", "update", "sumRange", "update",
            "sumRange",
            "update"]
    parms = [[[0, 9, 5, 7, 3]], [4, 4], [2, 4], [3, 3], [4, 5], [1, 7], [0, 8], [1, 2], [1, 9], [4, 4], [3, 4]]

    num_array = NumArray(*parms[0])
    for cmd, parm in zip(cmds[1:], parms[1:]):
        ret = getattr(num_array, cmd)(*parm)
        print(ret)
