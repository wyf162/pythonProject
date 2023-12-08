# -*- coding : utf-8 -*-
# @Time: 2023/12/2 18:48
# @Author: yefei.wang
# @File: Q1.py

import sys
sys.stdin = open('./input.txt')


n = 100
ans = 0
for i in range(100):
    s = input().replace(' ', '')
    s2 = s.split(':')[1]
    tag = True
    for ss in s2.split(';'):
        for c in ss.split(','):
            if 'red' in c:
                c = int(c.replace('red', ''))
                if c <= 12:
                    continue
                else:
                    tag = False
                    break
            elif 'green' in c:
                c = int(c.replace('green', ''))
                if c <= 13:
                    continue
                else:
                    tag = False
                    break
            elif 'blue' in c:
                c = int(c.replace('blue', ''))
                if c <= 14:
                    continue
                else:
                    tag = False
                    break
        if tag is False:
            break
    if tag:
        ans += i + 1
        print(i+1)
print(ans)
