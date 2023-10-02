# -*- coding : utf-8 -*-
# @Time: 2023/8/27 10:42
# @Author: yefei.wang
# @File: minimumOperations.py
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:

        if sum(nums) < target:
            return -1

        # 统计每种2的幂出现的次数
        cnt = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    cnt[i] += 1
                    break

        # target 转成二进制保存在数组中
        tar = [0] * 32
        k = target
        for i in range(32):
            tar[i] = k % 2
            k = k // 2

        s = 0
        op = 0
        for i in range(32):
            if tar[i]:
                if s >= (1 << i):
                    s -= (1 << i)
                elif cnt[i]:
                    cnt[i] -= 1
                else:
                    j = i
                    while True:
                        if cnt[j]:
                            cnt[j] -= 1
                            break
                        j += 1
                    for x in range(i, j):
                        cnt[x] += 1
                        op += 1
            s += cnt[i] * (1 << i)

        return op


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 8]
    # target = 7
    nums = [1, 32, 1, 2]
    target = 12
    ret = sol.minOperations(nums, target)
    print(ret)
