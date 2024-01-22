# -*- coding : utf-8 -*-
# @Time: 2024/1/21 10:30
# @Author: yefei.wang
# @File: B.py

from itertools import accumulate
from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        # 调整 x, y 的大小关系
        if x > y: x, y = y, x
        ans = [0] * (n + 1)
        x -= 1
        y -= 1
        for i in range(n):
            # 不需要中介的情况
            if abs(i - x) + 1 > abs(i - y):
                ans[1] += 1
                ans[n - i] -= 1
            # 需要中介的情况
            else:
                # 找到分界点
                d = abs(i - x) + 1
                sep = i + d + (y - i - d) // 2
                # 分界点左侧是直接走，距离从 1 到 sep - i
                ans[1] += 1
                ans[sep - i + 1] -= 1
                # 分界点及其右侧与 y 左侧，通过中介，距离从 d + 1 到 d + y - (sep + 1)
                ans[d + 1] += 1
                ans[d + y - sep] -= 1
                # y 及其右侧，距离从 d 到 d + (n - 1) - y
                ans[d] += 1
                ans[d + n - y] -= 1
        ans = list(accumulate(ans))
        return [x * 2 for x in ans[1:]]
