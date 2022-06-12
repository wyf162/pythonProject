# _*_ coding: utf-8 _*_
# @Time : 2022/3/6 上午10:27 
# @Author : wangyefei
# @File : 20220306.py
from typing import List
import collections
from sortedcontainers import sortedset


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alpha_offset = ord('A')
        start_alpha = ord(s[0]) - alpha_offset
        end_alpha = ord(s[3]) - alpha_offset
        start_num = int(s[1])
        end_num = int(s[4])
        ret = list()
        for alpha in range(start_alpha, end_alpha + 1):
            for num in range(start_num, end_num + 1):
                ret.append(chr(alpha + alpha_offset) + str(num))
        return ret

    def minimalKSum(self, nums: List[int], k: int) -> int:
        upper = max(nums)
        n = len(set(nums))
        print(n)
        if upper <= n + k:
            print(upper, n + k)
            adds = set(list(range(1, upper))) - set(nums)
            adds = list(adds)
            adds.sort()

            return sum(adds[:k])
        else:
            nums.sort()
            print(nums)
            for idx, num in enumerate(nums):
                if num - idx - 1 >= k:
                    cur = idx
                    break

            adds = set(list(range(1, nums[cur] + 1))) - set(nums[:cur + 1])
            adds = list(adds)
            adds.sort()

            return sum(adds[:k])

    def minimal_k_sum(self, nums, k):
        upper = max(nums)
        n = len(set(nums))
        if upper <= n + k:
            adds = set(list(range(1, n+k+1))) - set(nums)

            return sum(adds)
        nums = set(nums)
        i = 1
        ret = 0
        while k > 0:
            if i not in nums:
                ret += i
                k -= 1
            i += 1

        return ret


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 4, 25, 10, 25]
    # k = 2
    # nums = [5,6]
    # k = 6
    # nums = [96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40,
    #         84]
    # k = 35
    # nums = [93, 44, 49, 45, 93, 52, 6, 7, 88, 70, 86, 15, 38, 86, 86, 95, 8, 62, 13, 84, 26, 16, 33, 85, 7, 62, 55, 50, 77, 10,
    #  76, 10, 35, 67, 19, 12, 24, 39, 76, 37]
    # k = 17
    # nums = [95, 45, 87, 65, 21, 64, 19, 24, 38, 71, 6, 68, 45, 90, 49, 72, 73, 87, 51, 61, 53, 39, 27, 99, 35, 27, 35,
    #         91, 43,
    #         11, 30, 56, 76, 61, 52, 54, 54, 64, 18, 47, 57, 95]
    # k = 57
    nums = [7, 2, 94, 5, 9, 8, 18, 80, 48, 1, 6, 75, 28, 100, 43, 3, 59, 48, 4, 98, 88, 82]
    k = 80
    ret = sol.minimal_k_sum(nums, k)
    print(ret)
    # s = "K1:L2"
    # ret = sol.cellsInRange(s)
    # print(ret)
