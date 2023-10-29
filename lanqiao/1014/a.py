# -*- coding : utf-8 -*-
# @Time: 2023/10/14 19:03
# @Author: yefei.wang
# @File: c.py

import os
import sys

# 请在此输入您的代码
from collections import Counter

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    cnt = Counter(s)
    if len(cnt) == 2:
        k = list(cnt.keys())[0]
        if cnt[k] in [1, 3]:
            print('Yes')
            continue
    print('No')
