# -*- coding : utf-8 -*-
# @Time: 2023/12/3 10:28
# @Author: yefei.wang
# @File: B.py
from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        f = [0] * (target + 1)
        coins.sort()

