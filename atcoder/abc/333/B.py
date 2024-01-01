# -*- coding : utf-8 -*-
# @Time: 2023/12/16 20:01
# @Author: yefei.wang
# @File: B.py

import sys

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

s1 = input()
s2 = input()


def get_len(s):
    c1, c2 = s[0], s[1]
    k = abs(ord(c1) - ord(c2))
    if k <= 2:
        return k
    else:
        return 5 - k


k1 = get_len(s1)
k2 = get_len(s2)
if k1 == k2:
    print('Yes')
else:
    print('No')
