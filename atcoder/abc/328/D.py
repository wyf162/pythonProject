# -*- coding : utf-8 -*-
# @Time: 2023/11/11 20:22
# @Author: yefei.wang
# @File: D.py

import sys

sys.stdin = open('../../input.txt', 'r')


s = input()
stk = []
n = len(s)
for i in range(n):
    if s[i] == 'A':
        stk.append(s[i])
    elif s[i] == 'B':
        stk.append(s[i])
    else:
        if len(stk) >= 2 and stk[-1] == 'B' and stk[-2] == 'A':
            stk.pop()
            stk.pop()
        else:
            stk.append(s[i])

print(''.join(stk))
