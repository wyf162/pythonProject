# -*- coding : utf-8 -*-
# @Time: 2022/1/23 11:04
# @Author: yefei.wang
# @File: 20220123.py
from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        def check(i: int) -> int:
            cnt = 0  # i 中好人个数
            for j, row in enumerate(statements):  # 枚举 i 中的好人 j
                if (i >> j) & 1:
                    if any(st < 2 and st != (i >> k) & 1 for k, st in enumerate(row)):
                        return 0  # 好人 j 的某个陈述 st 与实际情况矛盾
                    cnt += 1
            return cnt

        return max(check(i) for i in range(1, 1 << len(statements)))

