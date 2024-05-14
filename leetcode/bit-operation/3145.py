# -*- coding: utf-8 -*-
# @Time: 2024/5/14 14:49
# @Author: yfwang
# @File: 3145.py

from typing import List


# big nums
# 1 2 1 2 4 1 4 2 4 1 2 4 8
# 0
# 1 0 1
# 2 0 2 1 2 0 1 2
# 3 0 3 1 3 0 1 3 2 3 0 2 3 1 2 3 0 1 2 3
# 4 0 4 1 4 0 1 4 2 4 0 2 4 1 2 4 0 1 2 4 3 4 0 3 4 1 3 4 0 1 3 4
class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def sum_e(k: int) -> int:
            res = n = cnt1 = sum_i = 0
            for i in range((k + 1).bit_length() - 1, 0, -1):
                c = (cnt1 << i) + (i << (i - 1))  # 新增的幂次个数
                if c <= k:
                    k -= c
                    res += (sum_i << i) + ((i * (i - 1) // 2) << (i - 1))
                    sum_i += i  # 之前填的 1 的幂次之和
                    cnt1 += 1  # 之前填的 1 的个数
                    n |= 1 << i  # 填 1
            # 最低位单独计算
            if cnt1 <= k:
                k -= cnt1
                res += sum_i
                n += 1  # 填 1
            # 剩余的 k 个幂次，由 n 的低 k 个 1 补充
            for _ in range(k):
                lb = n & -n
                res += lb.bit_length() - 1
                n ^= lb
            return res
        return [pow(2, sum_e(r + 1) - sum_e(l), mod) for l, r, mod in queries]




