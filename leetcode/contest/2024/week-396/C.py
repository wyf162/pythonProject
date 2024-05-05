# -*- coding : utf-8 -*-
# @Time: 2024/5/5 10:37
# @Author: yefei.wang
# @File: C.py
from collections import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        ans = n
        for div in divisors:
            c1 = Counter(s[:div])
            for i in range(div, n, div):
                if c1 == Counter(s[i:i+div]):
                    continue
                else:
                    break
            else:
                ans = div
                break
        return ans

