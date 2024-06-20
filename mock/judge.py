# -*- coding : utf-8 -*-
# @Time: 2023/11/5 22:49
# @Author: yefei.wang
# @File: judge.py

with open('./../codechef/output.txt', 'r') as f:
    rds1 = f.readlines()

with open('./../codechef/jury.txt', 'r') as f:
    rds2 = f.readlines()

n = len(rds1)
for i in range(n):
    if rds1[i] != rds2[i]:
        print(f"differ in {i+1} row")
        print(f"expect {rds2[i]} but find {rds1[i]}")
        break
