# -*- coding : utf-8 -*-
# @Time: 2024/1/28 11:34
# @Author: yefei.wang
# @File: D2.py


from typing import List


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        ans = (1 << 30) - 1
        tmp = ans
        for i in range(29, -1, -1):
            cur = ans - (1 << i)
            val = tmp
            cnt = 0
            for v in nums:
                x = v - (v & cur)
                val &= x
                if val: cnt += 1
                else: val = tmp
            if cnt <= k: ans = cur
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 5, 3, 2, 7]
    k = 3
    ret = sol.minOrAfterOperations(nums, k)
    print(ret)
