# -*- coding : utf-8 -*-
# @Time: 2024/6/9 10:29
# @Author: yefei.wang
# @File: A.py

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        nums = [i for i in range(n)]
        pos = -1
        i = 0
        for _ in range(k):
            if i == 0 or i == n - 1:
                pos = -pos
            i += pos
        return i
