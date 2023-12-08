# -*- coding : utf-8 -*-
# @Time: 2023/12/2 19:00
# @Author: yefei.wang
# @File: Q2.py

import sys

sys.stdin = open('./input.txt')

n = 100
ans = 0
for i in range(100):
    s = input().replace(' ', '')
    s2 = s.split(':')[1]

    r, g, b = 0, 0, 0

    for ss in s2.split(';'):
        for c in ss.split(','):
            if 'red' in c:
                c = int(c.replace('red', ''))
                r = max(r, c)
            elif 'green' in c:
                c = int(c.replace('green', ''))
                g = max(g, c)
            elif 'blue' in c:
                c = int(c.replace('blue', ''))
                b = max(b, c)
    print(r, g, b)
    ans += r * g * b
print(ans)
