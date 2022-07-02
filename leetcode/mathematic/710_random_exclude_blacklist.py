# -*- coding : utf-8 -*-
# @Time: 2022/6/27 20:49
# @Author: yefei.wang
# @File: 710_random_exclude_blacklist.py
from typing import List
import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        self.bound = w = n - m
        black = {b for b in blacklist if b >= self.bound}
        self.b2w = {}
        for b in blacklist:
            if b < self.bound:
                while w in black:
                    w += 1
                self.b2w[b] = w
                w += 1

    def pick(self) -> int:
        x = random.randrange(self.bound)
        return self.b2w.get(x, x)


