# -*- coding : utf-8 -*-
# @Time: 2023/10/18 20:26
# @Author: yefei.wang
# @File: make_input.py


import sys
import random
import itertools

# sys.stdout = open('./../codeforces/input.txt', 'w')
sys.stdout = open('./../nowcoder/input.txt', 'w')
# sys.stdout = open('./../codechef/input.txt', 'w')

E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

# N = 7
# for perm in itertools.permutations(list(range(1, 8))):
#     print(7)
#     print(*perm)


tcn = 1
# print(tcn)
for _tcn_ in range(tcn):
    N = 100
    print(N)
    for _ in range(N):
        print(random.randint(0, E5), random.randint(0, E5))



