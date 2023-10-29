# -*- coding : utf-8 -*-
# @Time: 2023/10/13 21:48
# @Author: yefei.wang
# @File: 1013_oneMoreGridTask.py

import sys

# sys.stdin = open('./../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
grid = [LI() for _ in range(n)]
nums = []
pre_sum = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(n):
    for j in range(m):
        pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + grid[i][j]
        nums.append(grid[i][j])

nums = list(sorted(set(nums)))
ans = 0
pre_sum2 = [[0 for j in range(m + 1)] for i in range(n + 1)]
for num in nums:
    for i in range(n):
        for j in range(m):
            pre_sum2[i + 1][j + 1] = pre_sum2[i + 1][j] + pre_sum2[i][j + 1] - pre_sum2[i][j] + int(grid[i][j] >= num)

            for pi in range(i+1):
                for pj in range(j+1):
                    cnt = pre_sum2[i + 1][j + 1] - pre_sum2[i + 1][pj] - pre_sum2[pi][j + 1] + pre_sum2[pi][pj]
                    if cnt == (i + 1 - pi) * (j + 1 - pj):
                        sum = pre_sum[i + 1][j + 1] - pre_sum[i + 1][pj] - pre_sum[pi][j + 1] + pre_sum[pi][pj]
                        val = num * sum
                        ans = max(ans, val)

print(ans)
