# -*- coding: utf-8 -*-
# @Time: 2024/5/20 16:56
# @Author: yfwang
# @File: 1542.py
import random
import time


class Solution:
    def longestAwesome(self, s: str) -> int:
        D = 10  # s 中的字符种类数
        n = len(s)
        pos = [n] * (1 << D)  # n 表示没有找到异或前缀和
        pos[0] = -1  # pre[-1] = 0
        ans = pre = 0
        for i, x in enumerate(map(int, s)):
            pre ^= 1 << x
            ans = max(ans, i - pos[pre],  # 偶数
                      max(i - pos[pre ^ (1 << d)] for d in range(D)))  # 奇数
            if pos[pre] == n:  # 首次遇到值为 pre 的前缀异或和，记录其下标 i
                pos[pre] = i
        return ans


if __name__ == '__main__':
    sol = Solution()
    # s = "3242415"
    nums = [random.randint(0, 9) for _ in range(10 ** 6)]
    s = "".join(str(x) for x in nums)
    print(s)
    t1 = time.time()
    ret = sol.longestAwesome(s)
    print(ret)
    t2 = time.time()
    print(t2 - t1)
