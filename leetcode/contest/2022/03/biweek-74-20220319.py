# _*_ coding: utf-8 _*_
# @Time : 2022/3/19 下午10:30 
# @Author : wangyefei
# @File : biweek-74-20220319.py
import collections
import heapq
import random
from typing import List
from tools.decorators import print_run_time

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hst = dict(collections.Counter(nums))
        for k, v in hst.items():
            if v % 2 == 1:
                return False
        return True

    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        if pattern[0] == pattern[1]:
            target = pattern[0]
            cnt = 0
            for alpha in text:
                if alpha == target:
                    cnt += 1
            return (cnt + 1) * cnt // 2
        else:
            a, b = pattern
            n = len(text)
            cnt_a, cnt = 0, 0
            for i in range(n):
                if text[i] == a:
                    cnt_a += 1
                elif text[i] == b:
                    cnt += cnt_a
            a_nums = [0] * (n + 1)
            for i in range(n):
                if text[i] == a:
                    a_nums[i + 1] = a_nums[i] + 1
                else:
                    a_nums[i + 1] = a_nums[i]
            b_nums = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if text[j] == b:
                    b_nums[j] = b_nums[j + 1] + 1
                else:
                    b_nums[j] = b_nums[j + 1]
            ret = cnt + max(max(a_nums), max(b_nums))

            return ret

    @print_run_time
    def halveArray(self, nums: List[int]) -> int:
        nums = [-1 * num for num in nums]
        target = sum(nums) / 2
        heapq.heapify(nums)
        cnt = 0
        ret = 0
        while cnt > target:
            num = heapq.heappop(nums)
            cnt += num / 2
            heapq.heappush(nums, num / 2)
            ret += 1
        return ret

    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = numCarpets
        m = len(floor)
        f = [[0] * m for _ in range(n + 1)]
        f[0][0] = ord(floor[0]) % 2
        for i in range(m):
            f[0][i] = f[0][i - 1] + ord(floor[i]) % 2
        for i in range(1, n + 1):
            # j < carpetLen 的 f[i][j] 均为 0
            for j in range(carpetLen, m):
                f[i][j] = min(f[i][j - 1] + ord(floor[j]) % 2, f[i - 1][j - carpetLen])
        return f[n][m - 1]


if __name__ == '__main__':
    sol = Solution()
    # nums = [random.randint(1, 10000000) for i in range(100000)]
    nums = [1]
    ret = sol.halveArray(nums)
    print(ret)

    # text = "abdcdbc"
    # pattern = "ac"
    # text = "aabb"
    # pattern = "ab"
    # text = "iekbksdsmuuzwxbpmcngsfkjvpzuknqguzvzik"  # 5
    # pattern = "mp"
    # ret = sol.maximumSubsequenceCount(text, pattern)
    # print(ret)

    # nums = [18, 19, 5, 5, 18, 19, 5, 6, 12, 19, 13, 4, 16, 11, 4, 16, 10, 8, 12, 8, 2, 1, 8, 17, 4, 18, 3, 5, 16, 2, 16,
    #         12, 17, 16, 7, 16, 2, 17, 19, 9, 1, 20, 17, 17, 4, 6]
    # ret = sol.divideArray(nums)
    # print(ret)
