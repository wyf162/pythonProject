# -*- coding : utf-8 -*-
# @Time: 2024/6/15 14:30
# @Author: yefei.wang
# @File: 1186D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
def I(): return int(input())
def MI(): return map(int, input().split())
def GMI(): return map(lambda x: int(x) - 1, input().split())
def LI(): return list(MI())
def TI(): return tuple(MI())
def LGMI(): return list(GMI())
def YN(x): return print('YES' if x else 'NO')


mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    nums = []
    x = 1
    i1s = []
    i2s = []
    for i in range(n):
        s = input()
        s1, s2 = s.split('.')
        if s2 == '00000':
            nums.append(int(s1))
        else:
            if x == 1:
                if s1.startswith('-'):
                    nums.append(int(s1))
                else:
                    nums.append(int(s1) + 1)
                i1s.append(i)
            else:
                if s1.startswith('-'):
                    nums.append(int(s1) - 1)
                else:
                    nums.append(int(s1))
                i2s.append(i)
            x = -x
    tot = sum(nums)
    while tot > 0:
        tot -= 1
        i1 = i1s.pop()
        nums[i1] -= 1

    while tot < 0:
        tot += 1
        i2 = i2s.pop()
        nums[i2] += 1

    print('\n'.join(str(x) for x in nums))
