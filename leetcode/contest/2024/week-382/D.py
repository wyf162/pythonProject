# -*- coding : utf-8 -*-
# @Time: 2024/1/28 11:03
# @Author: yefei.wang
# @File: D.py

from typing import List


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        tempn = [[] for _ in range(30)]
        for i in range(30):
            for n in nums:
                if n & (1 << i):
                    tempn[i].append(1)
                else:
                    tempn[i].append(0)
        # print(tempn)
        to_ret = []
        for i in range(29, -1, -1):
            sumt = sum(tempn[i])
            if sumt == 0:
                to_ret.append(0)
                continue

            mask = (1 << 30) - 1  # 30个1
            for j in range(len(to_ret)):
                if to_ret[j] == 1:
                    mask -= 1 << (29 - j)
            if i > 0:
                mask -= (1 << i) - 1
            # print(bin(mask))

            tk = 0
            base = (1 << 30) - 1
            for n in nums:
                base = base & n
                if base & mask:
                    tk += 1
                else:
                    base = (1 << 30) - 1
            if tk <= k:
                to_ret.append(0)
            else:
                to_ret.append(1)
        temp = 0
        for t in to_ret:
            temp = temp * 2 + t
        return temp


if __name__ == '__main__':
    sol = Solution()
    nums = [7, 3, 15, 14, 2, 8]
    k = 4
    ret = sol.minOrAfterOperations(nums, k)
    print(ret)
