# -*- coding : utf-8 -*-
# @Time: 2022/2/13 10:23
# @Author: yefei.wang
# @File: 20220213.py
from typing import List
import bisect


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        n = len(nums)
        hst_0 = dict()
        for i in range(0, n, 2):
            k = nums[i]
            hst_0[k] = hst_0.get(k, 0) + 1
        hst_1 = dict()
        for i in range(1, n, 2):
            k = nums[i]
            hst_1[k] = hst_1.get(k, 0) + 1
        keys_0 = [(k, v) for k, v in hst_0.items()]
        keys_0 = sorted(keys_0, key=lambda keys: keys[1])
        keys_0 = [k[0] for k in keys_0]
        keys_1 = [(k, v) for k, v in hst_1.items()]
        keys_1 = sorted(keys_1, key=lambda keys: keys[1])
        keys_1 = [k[0] for k in keys_1]

        if keys_0[-1] != keys_1[-1]:
            ans = n - hst_0.get(keys_0[-1]) - hst_1.get(keys_1[-1])
        else:
            if len(keys_1) > 1:
                ans = n - hst_0.get(keys_0[-1]) - hst_1.get(keys_1[-2])
            else:
                ans = n - hst_0.get(keys_0[-1])
            if len(keys_0) > 1:
                ans = min(ans, n - hst_0.get(keys_0[-2]) - hst_1.get(keys_1[-1]))
            else:
                ans = min(ans, n - hst_1.get(keys_1[-1]))
        return ans

    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        prefix_sum = [0]
        for bean in beans:
            prefix_sum.append(prefix_sum[-1] + bean)
        keys = set(beans)
        n = len(beans)
        ans = prefix_sum[-1]
        for k in keys:
            left = bisect.bisect_left(beans, k)
            right = bisect.bisect_right(beans, k)
            tmp = prefix_sum[left] + prefix_sum[-1] - prefix_sum[right] - (n - right) * k
            ans = min(ans, tmp)
        return ans

    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        ans = 0
        f = [0] * (1 << (numSlots * 2))
        for i, fi in enumerate(f):
            c = i.bit_count()
            if c >= len(nums):
                continue
            for j in range(numSlots * 2):
                if (i & (1 << j)) == 0:  # 枚举空篮子 j
                    s = i | (1 << j)
                    f[s] = max(f[s], fi + ((j // 2 + 1) & nums[c]))
                    ans = max(ans, f[s])
        return ans

    def maximum_and_sum(self, nums: List[int], num_slots: int) -> int:
        n = len(nums)
        f = [0] * (1 << (num_slots * 2))
        for i, fi in enumerate(f):
            c = i.bit_count()
            if c >= n:
                continue
            for j in range(num_slots * 2):
                if (i & (1 << j)) == 0:
                    s = i | (1 << j)
                    f[s] = max(f[s], fi + (j // 2 + 1) & nums[c])
        return max(f)


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    numSlots = 3
    ans = sol.maximum_and_sum(nums, numSlots)
    print(ans)

    # beans = [4,1,6,5]
    # beans = [2,10,3,2]
    # nums = sol.minimumRemoval(beans)
    # print(nums)
    # nums = [1, 1]
    # ans = sol.minimumOperations(nums)
    # print(ans)
