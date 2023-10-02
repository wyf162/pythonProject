# -*- coding : utf-8 -*-
# @Time: 2023/9/21 22:53
# @Author: yefei.wang
# @File: a.py


ss = 'abc'
tcn = int(input())
for _ in range(tcn):
    s = input()
    cnt = 0
    for i in range(3):
        cnt += int(ss[i] == s[i])
    if cnt == 1 or cnt == 3:
        print('YES')
    else:
        print('NO')
