# -*- coding : utf-8 -*-
# @Time: 2022/1/1 18:36
# @Author: yefei.wang
# @File: is_N_straight_hand.py
from collections import Counter
from typing import List
import heapq
from sortedcontainers import SortedDict
from tools.decorators import print_run_time


def is_n_straight_hand(hand: List[int], group_size: int) -> bool:
    sorted_dict = SortedDict(dict(Counter(hand)))
    while sorted_dict:
        start_node = sorted_dict.peekitem(index=0)[0]
        for i in range(group_size):
            if sorted_dict.get(start_node + i, 0) > 0:
                sorted_dict[start_node + i] -= 1
                if sorted_dict[start_node + i] == 0:
                    sorted_dict.pop(start_node + i)
            else:
                return False
    return True


class Solution(object):
    @print_run_time
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i for i in range(1, n + 1)]
        level = 1
        while len(nums) > 1:
            new_nums = []
            if level % 2 == 1:
                for j in range(1, len(nums), 2):
                    new_nums.append(nums[j])
            else:
                for j in range(len(nums) - 2, -1, -2):
                    new_nums.insert(0, nums[j])
            nums = new_nums
            level += 1
            # print(nums)
        return nums[0]

    @print_run_time
    def last_remaining(self, n):
        a1, an = 1, n
        k, cnt, step = 0, n, 1
        while cnt > 1:
            if k % 2 == 0:  # 正向
                a1 += step
                if cnt % 2:
                    an -= step
            else:  # 反向
                if cnt % 2:
                    a1 += step
                an -= step
            k += 1
            cnt >>= 1
            step <<= 1
        return a1


if __name__ == "__main__":
    sol = Solution()
    print(sol.last_remaining(100000000))
    # hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    # group_size = 2
    # ans = is_n_straight_hand(hand, group_size)
    # print(ans)
