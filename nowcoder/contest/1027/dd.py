# -*- coding : utf-8 -*-
# @Time: 2023/10/28 14:06
# @Author: yefei.wang
# @File: dd.py
import bisect
import sys

sys.stdin = open('./../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, k = MI()
a = LI()
nums = [0] * m
for x in a:
    nums[x - 1] += 1

snums = list(sorted(nums))

pre_sum = [0]
for num in snums:
    pre_sum.append(pre_sum[-1] + num)

ans = [0] * m

for i, num in enumerate(nums):
    if n - num < k:
        ans[i] = -1
        continue

    l, r = 0, n
    while l <= r:
        mid = (l + r) // 2
        j = bisect.bisect_right(snums, mid)

        # print(i)
        if num <= mid:
            s = pre_sum[-1] - pre_sum[j] - mid * (m - j)
        else:
            s = pre_sum[-1] - pre_sum[j] - mid * (m - j) - (num - mid)
        if s <= k:
            ans[i] = mid
            r = mid - 1
        else:
            l = mid + 1

print(' '.join(map(str, ans)))
