# -*- coding : utf-8 -*-
# @Time: 2024/6/9 10:32
# @Author: yefei.wang
# @File: B.py

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        nums = [1] * n
        for _ in range(k):
            for i in range(1, n):
                nums[i] += nums[i - 1]
                nums[i] %= mod
        return nums[-1]


if __name__ == '__main__':
    n = 4
    k = 5
    ret = Solution().valueAfterKSeconds(n, k)
    print(ret)
