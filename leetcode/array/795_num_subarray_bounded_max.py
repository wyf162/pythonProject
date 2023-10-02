# _*_ coding: utf-8 _*_
# @Time : 2022/11/24 9:18 PM 
# @Author : yefe
# @File : 795_num_subarray_bounded_max

from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ret = 0
        left_idx = None
        valid_idx = None

        for i, num in enumerate(nums):
            if left <= num <= right:
                ret += 1
                if left_idx is None:
                    left_idx = i
                valid_idx = i
                ret += i - left_idx
            elif num < left:
                if valid_idx is not None and left_idx is not None:
                    ret += valid_idx - left_idx + 1
                if left_idx is None:
                    left_idx = i

            elif num > right:
                left_idx = None
                valid_idx = None

        return ret


if __name__ == '__main__':
    sol = Solution()
    # nums = [2, 1, 4, 3]
    # left = 2
    # right = 3
    nums = [876, 880, 482, 260, 132, 421, 732, 703, 795, 420, 871, 445, 400, 291, 358, 589, 617, 202, 755, 810, 227,
            813, 549, 791, 418, 528, 835, 401, 526, 584, 873, 662, 13, 314, 988, 101, 299, 816, 833, 224, 160, 852, 179,
            769, 646, 558, 661, 808, 651, 982, 878, 918, 406, 551, 467, 87, 139, 387, 16, 531, 307, 389, 939, 551, 613,
            36, 528, 460, 404, 314, 66, 111, 458, 531, 944, 461, 951, 419, 82, 896, 467, 353, 704, 905, 705, 760, 61,
            422, 395, 298, 127, 516, 153, 299, 801, 341, 668, 598, 98, 241]
    left = 658
    right = 719
    ret = sol.numSubarrayBoundedMax(nums, left, right)
    print(ret)
