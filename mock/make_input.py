# -*- coding : utf-8 -*-
# @Time: 2023/10/18 20:26
# @Author: yefei.wang
# @File: make_input.py


import sys
import random
import itertools

# sys.stdout = open('./../codeforces/input.txt', 'w')
sys.stdout = open('./../nowcoder/input.txt', 'w')

E5 = 10 ** 5
E9 = 10 ** 9

# N = 7
# for perm in itertools.permutations(list(range(1, 8))):
#     print(7)
#     print(*perm)


tcn = 1000
print(tcn)
for _tcn_ in range(tcn):
    n = 1000
    print(n)
    print(*[random.randint(1, 3) for _ in range(n)])
    # n, m, k = random.randint(1, E5), random.randint(1, E5), random.randint(1, E5)
    # print(n, m, k)

# for _tcn_ in range(tcn):
#     print(E5)
#     print(E9, end=' ')
#     for i in range(1, E5):
#         print(E5-i, end=' ')
#     print()

# for _tcn_ in range(tcn):
#     print(1000)
#     for i in range(1000):
#         num = random.randint(1, 1000)
#         print(num, end=' ')
#     print()
