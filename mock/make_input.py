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


tcn = 1
print(tcn)
for _tcn_ in range(tcn):
    N = 10000
    M = 100
    print(N, M)
    # nums = [random.randint(-1, 1) for _ in range(N)]
    # nums = [x if x > 0 else 0 for x in nums]
    nums = [0] * N
    print(*nums)



