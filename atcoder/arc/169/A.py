# -*- coding : utf-8 -*-
# @Time: 2023/12/9 20:01
# @Author: yefei.wang
# @File: A.py

import copy
import sys

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N = I()
A = LI()
P = LI()

a = copy.deepcopy(A)

for _ in range(30):
    for i in range(N - 1):
        a[P[i] - 1] += a[i + 1]
    # print(a)

# print(A)
# print(a)

if a[0] == A[0]:
    if a[0] == 0:
        print('0')
    elif a[0] > 0:
        print('+')
    elif a[0] < 0:
        print('-')
elif a[0] < A[0]:
    print('-')
elif a[0] > A[0]:
    print('+')
