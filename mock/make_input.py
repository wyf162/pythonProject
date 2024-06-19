# -*- coding : utf-8 -*-
# @Time: 2023/10/18 20:26
# @Author: yefei.wang
# @File: make_input.py


import sys
import random
import itertools

# sys.stdout = open('./../codeforces/input.txt', 'w')
# sys.stdout = open('./../nowcoder/input.txt', 'w')
sys.stdout = open('./../codechef/input.txt', 'w')

E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

# N = 7
# for perm in itertools.permutations(list(range(1, 8))):
#     print(7)
#     print(*perm)

print(120)
P = [1, 2, 3, 4, 5]
perms = itertools.permutations(P)
for perm in perms:
    print(5)
    print(*perm)

# tcn = 1
# # print(tcn)
# for _tcn_ in range(tcn):
#     n = 10000
#     print(n)
#     nums = [random.randint(1, 100) for _ in range(n)]
#     print(*nums)
#     m = 1000
#     print(m)
#     for i in range(m):
#         print(random.randint(1, 100), random.randint(1, 100), random.randint(1, n))
