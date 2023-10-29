# -*- coding : utf-8 -*-
# @Time: 2023/10/18 20:26
# @Author: yefei.wang
# @File: make_input.py


import sys
import random

sys.stdout = open('./../codeforces/input.txt', 'w')
# sys.stdout = open('./../nowcoder/input.txt', 'w')

E5 = 10 ** 5
E9 = 10 ** 9

tcn = 1
print(tcn)
for _tcn_ in range(tcn):
    print(E5)
    print(E9, end=' ')
    for i in range(1, E5):
        print(E5-i, end=' ')
    print()
# for _tcn_ in range(tcn):
#     print(1000)
#     for i in range(1000):
#         num = random.randint(1, 1000)
#         print(num, end=' ')
#     print()
