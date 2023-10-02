# _*_ coding: utf-8 _*_
# @Time : 2022/12/11 2:35 PM 
# @Author : yefe
# @File : 6264_minimum_total_cost

from typing import List


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ans = swap_cnt = mode_cnt = mode = 0
        cnt = [0] * (len(nums1) + 1)
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if x == y:
                ans += i
                swap_cnt += 1
                cnt[x] += 1
                if cnt[x] > mode_cnt:
                    mode_cnt, mode = cnt[x], x
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if mode_cnt * 2 <= swap_cnt:
                break
            if x != y and x != mode and y != mode:
                ans += i
                swap_cnt += 1
        return ans if mode_cnt * 2 <= swap_cnt else -1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 2, 3, 4, 5]
    ret = sol.minimumTotalCost(nums1, nums2)
    print(ret)
