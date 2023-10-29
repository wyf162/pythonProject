# -*- coding : utf-8 -*-
# @Time: 2023/10/21 12:15
# @Author: yefei.wang
# @File: a-bf.py

def solve(n):
    a1, a2 = 0, 0
    nums = list(range(1, n + 1))
    while nums:
        a1 += 1
        # print(' '.join(map(str, nums)))
        tmp = []
        for i, num in enumerate(nums):
            if i % 3 == 0:
                continue
            tmp.append(num)
        nums = tmp
        if a2 == 0 and (not nums or nums[-1] != n):
            a2 = a1
    print(a1, a2)


if __name__ == '__main__':
    solve(200)
