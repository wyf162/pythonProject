# -*- coding: utf-8 -*-
# @Time: 2024/2/22 15:44
# @Author: yfwang
# @File: 1907F.py
# https://codeforces.com/problemset/problem/1907/F


import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = float('inf')

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()


    def solve1(nums):
        group = [[]]
        asc = None
        for num in nums:
            if asc is None:
                if not group[-1]:
                    group[-1].append(num)
                else:
                    if group[-1][-1] < num:
                        asc = True
                    elif group[-1][-1] > num:
                        asc = False
                    group[-1].append(num)

            elif asc is True:
                if num >= group[-1][-1]:
                    group[-1].append(num)
                else:
                    group.append([num])
                    asc = None
            elif asc is False:
                if num <= group[-1][-1]:
                    group[-1].append(num)
                else:
                    group.append([num])
                    asc = None
        # print(len(group))
        dirs = []
        for x in group:
            if x[0] < x[-1]:
                dirs.append('asc')
            elif x[0] > x[-1]:
                dirs.append('desc')
            else:
                dirs.append('equal')
        # print(dirs)
        ans = inf
        if len(group) == 1:
            ans = 1 if dirs[0] == 'desc' else 0
        elif len(group) == 2:
            x1, x2 = group
            s1, s2 = dirs
            if s1 == 'asc' and s2 != 'desc':
                if x2[-1] <= x1[0]:
                    ans = min(len(x2), len(x1) + 2)
            if s1 == 'desc' and s2 != 'asc':
                if x2[-1] >= x1[0]:
                    ans = min(len(x2) + 1, len(x1) + 1)
        return ans


    def solve2(nums):
        group = [[]]
        asc = None
        for num in nums[::-1]:
            if asc is None:
                if not group[-1]:
                    group[-1].append(num)
                else:
                    if group[-1][-1] < num:
                        asc = True
                    elif group[-1][-1] > num:
                        asc = False
                    group[-1].append(num)

            elif asc is True:
                if num >= group[-1][-1]:
                    group[-1].append(num)
                else:
                    group.append([num])
                    asc = None
            elif asc is False:
                if num <= group[-1][-1]:
                    group[-1].append(num)
                else:
                    group.append([num])
                    asc = None
        group.reverse()
        for x in group:
            x.reverse()
        # print(len(group))
        dirs = []
        for x in group:
            if x[0] < x[-1]:
                dirs.append('asc')
            elif x[0] > x[-1]:
                dirs.append('desc')
            else:
                dirs.append('equal')
        # print(dirs)
        ans = inf
        if len(group) == 1:
            ans = 1 if dirs[0] == 'desc' else 0
        elif len(group) == 2:
            x1, x2 = group
            s1, s2 = dirs
            if s1 != 'asc' and s2 == 'desc':
                if x2[-1] >= x1[0]:
                    ans = min(len(x1) + 1, len(x2) + 1)
            if s1 != 'desc' and s2 == 'asc':
                if x2[-1] <= x1[0]:
                    ans = min(len(x1) + 2, len(x2))
        return ans


    ans1 = solve1(nums)
    ans2 = solve2(nums)
    ans = min(ans1, ans2)
    if ans == inf:
        print(-1)
    else:
        print(ans)
