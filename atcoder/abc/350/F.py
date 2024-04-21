# -*- coding : utf-8 -*-
# @Time: 2024/4/20 20:51
# @Author: yefei.wang
# @File: F.py


import sys

sys.setrecursionlimit(10 ** 6)

S = input() + ")"
n = len(S) - 1
p = [-1] * n
t = []
for i in range(n):
    if S[i] == "(":
        t.append(i)
    elif S[i] == ")":
        x = t.pop()
        p[x] = i
        p[i] = x
ans = []


def f(i, mode):
    if mode == "R":
        if S[i] == ")":
            return
        elif S[i] == "(":
            f(p[i] - 1, "L")
            f(p[i] + 1, "R")
        else:
            print(S[i], end="")
            f(i + 1, "R")
    else:
        if S[i] == "(":
            return
        elif S[i] == ")":
            f(p[i] + 1, "R")
            f(p[i] - 1, "L")
        else:
            print(chr(ord(S[i]) ^ 32), end="")
            f(i - 1, "L")


f(0, "R")
