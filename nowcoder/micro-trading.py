# -*- coding : utf-8 -*-
# @Time: 2021/12/11 10:25
# @Author: yefei.wang
# @File: micro-trading.py
import sys
import copy

nums = []
while True:
    x = sys.stdin.readline().strip()
    if x:
        nums.append(int(x))
    else:
        break


def func(n):
    i = 1
    level = [1]
    while i <= n:
        print(' '.join([str(x) for x in level]))
        i = i + 1
        next_level = []
        if i == 2:
            next_level = [1, 1]
        else:
            next_level.append(1)
            for j in range(0, len(level) - 1):
                next_level.append(level[j] + level[j + 1])
            next_level.append(1)
        level = copy.deepcopy(next_level)


for n in nums:
    func(n)