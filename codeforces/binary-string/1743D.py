# -*- coding: utf-8 -*-
# @Time: 2024/3/18 16:12
# @Author: yfwang
# @File: 1743D.py
# https://codeforces.com/problemset/problem/1743/D

n = int(input())
S = input()
if "1" not in S:
    exit(print("0"))
x = S.index("1")
S = S[x:]
n -= x
ans = list(S)
for i in range(1, n):
    if S[i - 1] == "0":
        break
    T = list(S)
    ok = False
    for j in range(i, n):
        if S[j - i] == "1":
            T[j] = "1"
            if ans[j] == "0":
                ok = True
        elif not ok and ans[j] == "1" and T[j] == "0":
            break
    if ok:
        ans = T
print(*ans, sep="")
