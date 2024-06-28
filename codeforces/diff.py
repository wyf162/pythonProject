# -*- coding : utf-8 -*-
# @Time: 2024/5/1 14:13
# @Author: yefei.wang
# @File: diff.py

import sys

with open('./output.txt', 'r') as f:
    out = f.readlines()

with open('./jury.txt', 'r') as f:
    jury = f.readlines()

n = len(out)
for i in range(n):
    if jury[i] != out[i]:
        print(f"differ in {i + 1} row")
        print(f"expect {jury[i]} but find {out[i]}")
        break
