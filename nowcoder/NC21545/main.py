# _*_ coding: utf-8 _*_
# @Time : 2022/4/20 下午10:38 
# @Author : wangyefei
# @File : main.py
import sys


def minimum_distance(nums, x):
    n = len(nums)
    nums.sort()
    ret = abs(nums[-1] - nums[0])
    for i in range(0, n - 1):
        ret = min(ret, max(nums[i] + x, nums[-1] - x) - min(nums[0] + x, nums[i + 1] - x))
    return ret


if __name__ == '__main__':
    sys.stdin = open('input.txt')
    n = int(input())
    nums = list(map(int, input().split(" ")))
    x = int(input())
    print(nums, x)
    print(minimum_distance(nums, x))
