# -*- coding : utf-8 -*-
# @Time: 2024/6/8 23:01
# @Author: yefei.wang
# @File: C.py


from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        f = [[0] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n):
            f[i][0] = 1
            for i1 in range(i):
                for j in range(k+1):
                    if nums[i] == nums[i1]:
                        f[i][j] = max(f[i][j], f[i1][j] + 1)
                    else:
                        if j + 1 <= k:
                            f[i][j + 1] = max(f[i][j + 1], f[i1][j] + 1)

        ret = max(max(f[i]) for i in range(n))
        return ret


if __name__ == '__main__':
    nums = [89, 89, 90, 88, 88, 88, 88, 90, 90]
    k = 2
    nums = [29, 30, 30]
    k = 0
    ret = Solution().maximumLength(nums, k)
    print(ret)
