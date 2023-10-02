# -*- coding : utf-8 -*-
# @Time: 2022/6/9 20:58
# @Author: yefei.wang
# @File: 497_Pick.py
from typing import List
import random
import bisect


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.nums = [0]
        for rect in rects:
            num = (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            self.nums.append(self.nums[-1]+num)

    def pick(self) -> List[int]:
        num = random.randint(0, self.nums[-1]-1)
        idx = bisect.bisect_right(self.nums, num)
        rect = self.rects[idx]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]


if __name__ == '__main__':
    for i in range(10):
        print(random.randrange(0, 1))
