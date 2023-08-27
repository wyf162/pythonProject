# _*_ coding: utf-8 _*_
# @Time : 2022/11/16 9:15 PM 
# @Author : yefe
# @File : 51_reverse_pairs

from typing import List


class Solution:

    def merge_sort(self, nums: List[int], tmp: List[int], l: int, r: int) -> int:
        if l >= r:
            return 0
        mid = (l + r) // 2
        inv_count = self.merge_sort(nums, tmp, l, mid) + self.merge_sort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1

        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.merge_sort(nums, tmp, 0, n - 1)


if __name__ == '__main__':
    sol = Solution()
    nums = [7, 5, 6, 1]
    ret = sol.reversePairs(nums)
    print(ret)
