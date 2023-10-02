# -*- coding : utf-8 -*-
# @Time: 2023/9/30 19:59
# @Author: yefei.wang
# @File: a.py
import sys
sys.stdin = open('./../../../input.txt', 'r')

n = int(input())
s = input()

for i in range(1, n-1):
    if s[i-1:i+2] == 'ABC':
        print(i)
        exit(0)
print('-1')
