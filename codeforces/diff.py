# -*- coding : utf-8 -*-
# @Time: 2024/5/1 14:13
# @Author: yefei.wang
# @File: diff.py

import sys

with open('./output.txt', 'r') as f:
    answer = f.readlines()

with open('./jury.txt', 'r') as f:
    jury = f.readlines()

n = len(jury)
for i in range(n):
    if jury[i] != answer[i]:
        print(f'first diff in {i + 1}')
        print(jury[i])
        print(answer[i])
        break
