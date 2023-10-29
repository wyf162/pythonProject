# -*- coding : utf-8 -*-
# @Time: 2023/10/12 21:28
# @Author: yefei.wang
# @File: 1731D.py
import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    grid = [LI() for _ in range(n)]


    def check(mid):
        pre_sum = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + int(grid[i][j] >= mid)

                if i+1 >= mid and j+1 >= mid:
                    sum = pre_sum[i + 1][j + 1] - pre_sum[i + 1 - mid][j + 1] - pre_sum[i + 1][j + 1 - mid] + \
                          pre_sum[i + 1 - mid][j + 1 - mid]
                    if sum == mid * mid:
                        return True
        return False


    l, r = 1, min(m, n)
    ans = l
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)
