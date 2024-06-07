# -*- coding: utf-8 -*-
# @Time: 2024/6/7 13:03
# @Author: yfwang
# @File: 1979D.py
# kmp

import sys

sys.stdin = open('../../input.txt', 'r')
sys.stdout = open('../../jury.txt', 'w')


def check(ANS):
    T = S[ANS:] + S[:ANS][::-1]

    A = [0]
    for i in range(len(T)):
        if i == 0 or T[i] == T[i - 1]:
            A[-1] += 1
        else:
            A.append(1)

    if set(A) == {k}:
        return True
    else:
        return False


t = int(input())
for tests in range(t):
    n, k = map(int, input().split())
    S = list(input().strip())
    one = S.count("1")
    zero = S.count("0")

    ANS = n
    A = [0]
    for i in range(len(S)):
        if i == 0 or S[i] == S[i - 1]:
            A[-1] += 1
        else:
            A.append(1)

    for i in range(len(A)):
        if A[i] != k:
            if A[i] < k:
                ANS = sum(A[:i + 1])
                break
            else:
                ANS = k * i + (A[i] - k)
                break

    if check(ANS) == True:
        print(ANS)
    else:
        print(-1)
