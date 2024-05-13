# -*- coding: utf-8 -*-
# @Time: 2024/5/13 15:53
# @Author: yfwang
# @File: 1356.py

from functools import cmp_to_key
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def cmp(a: int, b: int):
            if a.bit_count() > b.bit_count():
                return 1
            elif a.bit_count() < b.bit_count():
                return -1
            else:
                if a>b:
                    return 1
                elif a<b:
                    return -1
                else:
                    return 0
        arr.sort(key=cmp_to_key(cmp))
        return arr
