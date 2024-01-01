# -*- coding : utf-8 -*-
# @Time: 2023/12/16 20:54
# @Author: yefei.wang
# @File: F.py

import sys
from collections import Counter

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N = I()