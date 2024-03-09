# -*- coding : utf-8 -*-
# @Time: 2024/3/9 20:03
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

nums = []
while True:
    try:
        x = input()
        if x:
            nums.append(input())
        else:
            break
    except:
        break
nums.reverse()
for x in nums:
    print(x)
