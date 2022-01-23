# -*- coding : utf-8 -*-
# @Time: 2022/1/16 22:46
# @Author: yefei.wang
# @File: test.py
import functools
import sys
import logging

# print(sys.argv)
from typing import List


def my_compare(nums1, nums2):
    nums1 = str(nums1)
    nums2 = str(nums2)
    m, n = len(nums1), len(nums2)
    i = 0
    while i < m and i < n:
        if nums1[i] < nums2[i]:
            return 1
        elif nums1[i] > nums2[i]:
            return -1
        i = i + 1
    if i == m and i == n:
        return 0
    elif i == m:
        return -1 if nums2[i] != '0' else 1
    else:
        return -1 if nums1[i] == '0' else 1


def minNumber(nums: List[int]) -> str:
    nums = sorted(nums, key=functools.cmp_to_key(my_compare))
    print(nums)
    return "".join([str(x) for x in nums])


if __name__ == '__main__':
    data = my_compare(30, 3)
    print(data)

    data = my_compare(34, 3)
    print(data)

    nums = [3, 30, 3]
    data = minNumber(nums)
    print(data)
